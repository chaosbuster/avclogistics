cmake_minimum_required(VERSION 2.8.3)
project(autonomous_start)

find_package(catkin REQUIRED COMPONENTS rospy message_generation std_msgs sensor_msgs geometry_msgs usb_cam cv_bridge autonomous_controller )

add_message_files( FILES Clockstart.msg )

generate_messages( DEPENDENCIES std_msgs sensor_msgs geometry_msgs usb_cam cv_bridge autonomous_controller )

catkin_package( CATKIN_DEPENDS rospy message_runtime std_msgs sensor_msgs geometry_msgs cv_bridge usb_cam autonomous_controller )



