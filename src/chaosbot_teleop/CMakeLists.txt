cmake_minimum_required(VERSION 2.8.12)
project(chaosbot_teleop)

find_package(catkin REQUIRED COMPONENTS
  rospy
  std_msgs
  geometry_msgs
  i2cpwm_board
)

catkin_package(
  CATKIN_DEPENDS message_runtime roscpp rospy std_msgs geometry_msgs  i2cpwm_board
)

