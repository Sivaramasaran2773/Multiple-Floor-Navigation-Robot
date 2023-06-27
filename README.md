# Multiple-Floor-Navigation-Robot
A comprehensive repository with programs, tools, and documentation for autonomous navigation in multi-floor environments. Includes floor mapping, localization, path planning, obstacle avoidance, Camera Sensing, and more. Enhance robots' seamless multi-floor navigation by automatically updating floor maps. Ideal for buildings, hospitals, and more.


### multi_nav
```
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
