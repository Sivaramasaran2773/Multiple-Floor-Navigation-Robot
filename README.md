# Multiple-Floor-Navigation-Robot
A comprehensive repository with programs, tools, and documentation for autonomous navigation in multi-floor environments. Includes floor mapping, localization, path planning, obstacle avoidance, Camera Sensing, and more. Enhance robots' seamless multi-floor navigation by automatically updating floor maps. Ideal for buildings, hospitals, and more.

## Table of Contents
* [Robot in Multiple Floor Environment](###robot-in-multiple-floor-environment)
* [Required Tools](###RequiredTools)
* [Folders and Files in multi_nav](###FoldersandFilesinmulti_nav)
* [Solution Architecture](###Solution_Architecture)
* [Prerequisite Commands to load turtlebot3_waffle](###PrerequisiteCommandstoloadturtlebot3_waffle)
* [Commands to Run the Simulation](###CommandstoRuntheSimulation)
* [Python script Explanation](###PythonscriptExplanation)
* [Simulation Video](###SimulationVideo)
* [Applications](###Applications)
  
### Robot in Multiple Floor Environment:-
![image](https://github.com/Sivaramasaran2773/Multiple-Floor-Navigation-Robot/assets/96780921/887e9158-5fa2-447f-899d-71ccbfe0fbc8)

### Required Tools
* Gazebo 
* RViz
* SLAM Toolbox
* Nav2

### Folders and Files in multi_nav
```
┣ 📂multi_nav
   ┣ 📂launch
   ┃ ┗ 📜bringup_launch.py
   ┃ ┗ 📜gz_respawner_stage1.py
   ┃ ┗ 📜gz_respawner_stage2.py
   ┃ ┗ 📜gz_respawner_stage3.py
   ┃ ┗ 📜multi_floor_navigation_launch.py
   ┃ ┗ 📜online_async_launch.py
   ┃ ┗ 📜rviz_launch.py
   ┃ ┗ 📜slam_launch.py
   ┃ ┗ 📜tb3_gazebo_stage1.py
   ┣ 📂maps
   ┃ ┗ 📜stage1.pgm                 
   ┃ ┗ 📜stage1.yaml
   ┃ ┗ 📜stage2.pgm  
   ┃ ┗ 📜stage2.yaml
   ┃ ┗ 📜stage3.pgm  
   ┃ ┗ 📜stage3.yaml                           
   ┣ 📂params
   ┃ ┗ 📜mapper_params_online_async.yaml      
   ┃ ┗ 📜nav2_params.yaml        
   ┣ 📂rviz                                
   ┃ ┣ 📜nav2_default_view.rviz
   ┃ ┣ 📜nav2_namespaced_view.rviz
   ┣ 📂scripts                                    
   ┃ ┣ 📜floor1_2.py
   ┃ ┣ 📜floor1_2_3.py
   ┃ ┣ 📜floor1_3.py
   ┃ ┗ 📜floor1_3_2.py
   ┣ 📂urdf
   ┃ ┗ 📜turtlebot3_waffle.urdf
   ┣ 📂world
   ┃ ┗ 📜finalfloors.world  
   ┃ ┗ 📜floor2.world  
   ┃ ┗ 📜floor3.world                            
   ┣ 📜CmakeLists.txt
   ┣ 📜package.xml
```
### Solution Architecture:
![image](https://github.com/Sivaramasaran2773/Multiple-Floor-Navigation-Robot/assets/96780921/5817f82c-44ec-402e-b543-33685d09f6e1)


### Prerequisite Commands to load turtlebot3_waffle:-

<code> echo "export TURTLEBOT3_MODEL=waffle" >> ~/.bashrc </code>


<code> echo "export GAZEBO_MODEL_PATH=$GAZEBO_MODEL_PATH:/opt/ros/humble/share/turtlebot3_gazebo/models:$HOME/sun_ws/src/multi_nav/worlds" >> ~/.bashrc </code>

### Commands to Run the Simulation:-
1. To Launch the turtlebot3_waffle in our multiple floor world.

<code> ros2 launch multi_nav tb3_gazebo_stage1.py headless:=False </code> 

2. To Load our created maps using slam toolbox into RViz.

<code> ros2 launch multi_nav multi_floor_navigation.py </code> 

4. To Navigate the simulation of our robot between multiple floors.
   In the directory of the scripts folder:

<code> python3 floor1_2_3 </code> 

### Python Script Explanation:
![image](https://github.com/Sivaramasaran2773/Multiple-Floor-Navigation-Robot/assets/96780921/3d52f172-cc7f-4c33-beda-3c1c435fca18)

### Simulation Video:
[![YouTube Video](http://img.youtube.com/vi/NpObE61ZL6o/0.jpg)](https://youtu.be/NpObE61ZL6o)

### Applications:
![image](https://github.com/Sivaramasaran2773/Multiple-Floor-Navigation-Robot/assets/96780921/d56f7b50-3ebd-4b3e-ae3a-512b3065a312)

