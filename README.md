# Absolute coordinate
## 1.make sure that you have installed pubmoos and Weiyu's pre obstacle
 https://github.com/CT-Hung/ntu_vrx
 
 https://github.com/weiyutp6/ros_point_cloud
## 2.install absolute obstacle
     ~/ntu_vrx/catkin_ws/src
     git clone  https://github.com/CLKaoB05/test.git


## 3.run 
### open 6 terminals
    cd ~/ntu_vrx/catkin_ws
    catkin make
    source ~/ntu_vrx/catkin_ws/devel/setup.bash
    roslaunch vrx_gazebo navigation_task.launch
    roslaunch transform_gazebo_msg gazeboToMoos.launch
    roslaunch wamv_gazebo localization_example.launch
    roslaunch ros_point_cloud lidar_detect.launch
    rosrun abs_obstacle obstacle_position.py
    rostopic echo /abs_obstacle
    
