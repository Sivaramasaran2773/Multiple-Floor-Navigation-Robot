# Copyright (c) 2018 Intel Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""This is all-in-one launch script intended for use by nav2 developers."""

import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, ExecuteProcess, IncludeLaunchDescription
from launch.conditions import IfCondition
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration, PythonExpression
from launch_ros.actions import Node


def generate_launch_description():
    # Get the launch directory
    bringup_dir = get_package_share_directory('multi_nav')
    launch_dir = os.path.join(bringup_dir, 'launch')

    # Create the launch configuration variables
    namespace = LaunchConfiguration('namespace')
    use_sim_time = LaunchConfiguration('use_sim_time')

    # Launch configuration variables specific to simulation
    use_simulator = LaunchConfiguration('use_simulator')
    use_robot_state_pub = LaunchConfiguration('use_robot_state_pub')
    headless = LaunchConfiguration('headless')
    world = LaunchConfiguration('world')
    pose = {'x': LaunchConfiguration('x_pose', default='-2.00'),
            'y': LaunchConfiguration('y_pose', default='-0.5'),
            'z': LaunchConfiguration('z_pose', default='0.01'),
            'R': LaunchConfiguration('roll', default='0.00'),
            'P': LaunchConfiguration('pitch', default='0.00'),
            'Y': LaunchConfiguration('yaw', default='0.00')}
    robot_name = LaunchConfiguration('robot_name')
    robot_sdf = LaunchConfiguration('robot_sdf')
    timeout = '3000.0'

    # Map fully qualified names to relative ones so the node's namespace can be prepended.
    # In case of the transforms (tf), currently, there doesn't seem to be a better alternative
    # https://github.com/ros/geometry2/issues/32
    # https://github.com/ros/robot_state_publisher/pull/30
    # TODO(orduno) Substitute with `PushNodeRemapping`
    #              https://github.com/ros2/launch_ros/issues/56
    remappings = [('/tf', 'tf'),
                  ('/tf_static', 'tf_static')]

    # Declare the launch arguments
    declare_namespace_cmd = DeclareLaunchArgument(
        'namespace',
        default_value='',
        description='Top-level namespace')

    declare_use_namespace_cmd = DeclareLaunchArgument(
        'use_namespace',
        default_value='false',
        description='Whether to apply a namespace to the navigation stack')

    declare_use_sim_time_cmd = DeclareLaunchArgument(
        'use_sim_time',
        default_value='true',
        description='Use simulation (Gazebo) clock if true')

    declare_use_respawn_cmd = DeclareLaunchArgument(
        'use_respawn', default_value='False',
        description='Whether to respawn if a node crashes. Applied when composition is disabled.')

    declare_use_simulator_cmd = DeclareLaunchArgument(
        'use_simulator',
        default_value='True',
        description='Whether to start the simulator')

    declare_use_robot_state_pub_cmd = DeclareLaunchArgument(
        'use_robot_state_pub',
        default_value='True',
        description='Whether to start the robot state publisher')

    declare_simulator_cmd = DeclareLaunchArgument(
        'headless',
        default_value='True',
        description='Whether to execute gzclient)')

    declare_world_cmd = DeclareLaunchArgument(
        'world',
        # TODO(orduno) Switch back once ROS argument passing has been fixed upstream
        #              https://github.com/ROBOTIS-GIT/turtlebot3_simulations/issues/91
        # default_value=os.path.join(get_package_share_directory('turtlebot3_gazebo'),
        # worlds/turtlebot3_worlds/waffle.model')
        default_value=os.path.join(bringup_dir, 'worlds', 'floor2.world'),
        description='Full path to world model file to load')

    declare_robot_name_cmd = DeclareLaunchArgument(
        'robot_name',
        default_value='turtlebot3_waffle',
        description='name of the robot')

    declare_robot_sdf_cmd = DeclareLaunchArgument(
        'robot_sdf',
        default_value=os.path.join(bringup_dir, 'worlds', 'waffle.model'),
        description='Full path to robot sdf file to spawn the robot in gazebo')

    # Specify the actions
    start_gazebo_server_cmd = ExecuteProcess(
        condition=IfCondition(use_simulator),
        cmd=['gzserver', '-s', 'libgazebo_ros_init.so',
             '-s', 'libgazebo_ros_factory.so', world],
        cwd=[launch_dir], output='screen')
    
    start_gazebo_client_cmd = ExecuteProcess(
        condition=IfCondition(PythonExpression(
            [use_simulator, ' and not ', headless])),
        cmd=['gzclient'],
        cwd=[launch_dir], output='screen')

    urdf = os.path.join(bringup_dir, 'urdf', 'turtlebot3_waffle.urdf')
    with open(urdf, 'r') as infp:
        robot_description = infp.read()

    declare_robot_name_cmd = DeclareLaunchArgument(
        'robot_name',
        default_value='turtlebot3_waffle',
        description='name of the robot')

    start_robot_state_publisher_cmd = Node(
        condition=IfCondition(use_robot_state_pub),
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='robot_state_publisher',
        namespace=namespace,
        output='screen',
        parameters=[{'use_sim_time': use_sim_time,
                     'robot_description': robot_description}],
        remappings=remappings)

    start_gazebo_spawner_cmd = Node(
        package='gazebo_ros',
        executable='spawn_entity.py',
        output='screen',
        arguments=[
            '-entity', robot_name,
            '-file', robot_sdf,
            '-robot_namespace', namespace,
            '-timeout', timeout,
            '-x', pose['x'], '-y', pose['y'], '-z', pose['z'],
            '-R', pose['R'], '-P', pose['P'], '-Y', pose['Y']])

    
    # Create the launch description and populate
    ld = LaunchDescription()
    ld.add_action(declare_namespace_cmd)
    ld.add_action(declare_use_namespace_cmd)
    ld.add_action(declare_use_sim_time_cmd)

    ld.add_action(declare_use_simulator_cmd)
    ld.add_action(declare_use_robot_state_pub_cmd)

    ld.add_action(declare_simulator_cmd)
    ld.add_action(declare_world_cmd)
    ld.add_action(declare_robot_name_cmd)
    ld.add_action(declare_robot_sdf_cmd)
    ld.add_action(declare_use_respawn_cmd)
    
    
    # Declare the launch options
    ld.add_action(start_gazebo_spawner_cmd)

    return ld
