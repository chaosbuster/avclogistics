cmake_minimum_required(VERSION 2.8.12)
project(chaosbot_mininputs)

find_package(catkin REQUIRED COMPONENTS
  rospy
  std_msgs
  geometry_msgs

)

catkin_package(
  CATKIN_DEPENDS message_runtime roscpp rospy std_msgs geometry_msgs
)

