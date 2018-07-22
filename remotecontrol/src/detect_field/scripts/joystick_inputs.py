#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Joy

# Author: Jeanette Breton (aka Chaos Buster)
# This ROS Node converts Joystick inputs from
# the joy node into commands for AVCChaos, our 
# robot for SparkFun AVC Logistics Class category
#
# Kudos, Thanks and Credit to Andrew Dai for his node  
# creation for his xbox controller.  More information at:
# https://andrewdai.co/xbox-controller-ros.html#rosjoy
#
# Receives joystick messages (subscribed to Joy topic)
# then converts the joystick inputs into Geometry commands
# to provide commands for our AVCChaos robot. 
# 
# Releases: 
#   1. Direction and velocity geometry commands  
#   2. Button commands for actions like Emergency stop
#      and gripper movements
#   3. Button commands for poses or autonomous motions
# 
# Direction and velocity geometry will be provided by
# the following joystick axis
# axis 1 aka left stick vertical controls linear speed
# axis 0 aka left stick horizontal controls angular speed
    
chaoscmds = Twist()

def callback_allcurrentinputs(data):
    rospy.loginfo('Received a joystick input')

    chaoscmds.linear.x = 4*data.axes[1]
    chaoscmds.angular.z = 4*data.axes[0]
    pub.publish(chaoscmds)

# Initializes everything
def joystick_inputs():
    global pub
    # publishing to avcchaos/cmd_vel to control AVCChaos
    pub = rospy.Publisher('avcchaos/cmd_vel', Twist, queue_size=10)

    # Need to subscribe to joystick inputs on topic 'joy'
    rospy.Subscriber('joy', Joy, callback_allcurrentinputs)

    # Starting the node
    rospy.init_node('joystick_inputs')
    rospy.spin()

if __name__ == '__main__':
    try:
        joystick_inputs()
    except rospy.ROSInterruptException:
        pass

