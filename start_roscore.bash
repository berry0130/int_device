
#!/bin/bash

source /opt/ros/kinetic/setup.bash
source /home/ubuntu/catkin_ws/devel/setup.bash

export ROS_IP=$(ip route get 1.2.3.4 | awk '{print $7}')
export ROS_MASTER_URI=http://192.168.4.10:11311/ 
rm -rf /home/ubuntu/.ros/log 
roscore