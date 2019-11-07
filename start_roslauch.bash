#!/bin/bash
source /opt/ros/kinetic/setup.bash
source /home/ubuntu/catkin_ws/devel/setup.bash

export ROS_IP=$(ip route get 1.2.3.4 | awk '{print $7}')
export ROS_MASTER_URI=http://192.168.3.3:11311/ 
echo y|rosclean purge
roslaunch hypharos_minibot HyphaROS_MiniBot_Nav.launch

