#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Joy
from i2cpwm_board.msg import Servo, ServoArray


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
#   1. Direction and velocity commands for Planning (geometry 
#      and chaosbot hardward specific).
#   2. Button commands for actions like Emergency stop
#      and gripper movements
#   3. Button commands for poses or autonomous motions
# 
# Direction and velocity geometry will be provided by
# the following joystick axes. 
# NOTE: Using MODE where the MODE button light is ON
# axis 3 aka right stick vertical controls linear speed
# axis 2 aka right stick horizontal controls angular speed

# Speed directions of our chassis
GOFORWARD=1
NOSPEED=0
GOREVERSE=-1
ZERO_HIGH = 0.01
ZERO_LOW = -0.01

    
joystick = Twist()
chaosbot_cmds = [ Servo() for i in range(4)]

def callback_allcurrentinputs(data):
    rospy.loginfo('Received a joystick input')

    joystick.linear.x = data.axes[3]
    joystick.angular.z = data.axes[2]

    # Set the steering (negative's are right, positive's are left)
    chaosbot_cmds[0].servo = 2
    chaosbot_cmds[0].value = data.axes[2]

    # Set the speed for the chassis (negative's are reverse, positive's are forward)
    chaosbot_cmds[1].servo = 1
    chaosbot_cmds[1].value = data.axes[3]

    # Set the speed for the shoulder (negative's are reverse, positive's are forward)
    chaosbot_cmds[2].servo = 5
    chaosbot_cmds[2].value = data.axes[1]

    # Set the speed for the shoulder (negative's are reverse, positive's are forward)
    chaosbot_cmds[3].servo = 6
    chaosbot_cmds[3].value = data.axes[0]

    #pubPlanned.publish(joystick)
    pubControl.publish(chaosbot_cmds)


# Initializes everything
def joystick_translator():
    global pubPlanned, pubControl

    # Starting the node
    rospy.init_node('joystick_translator')

    # publishing a geometry cmd_vel Twist to control ChaosBot in Planning Simulations
    # pubPlanned = rospy.Publisher('cmd_vel', Twist, queue_size=10)
    # publishing to chaosbot Control msg to control ChaosBot
    pubControl = rospy.Publisher('servos_proportional', ServoArray, queue_size=5)

    # Need to subscribe to joystick inputs on topic 'joy'
    rospy.Subscriber('joy', Joy, callback_allcurrentinputs)

    rospy.spin()

if __name__ == '__main__':
    try:
        joystick_translator()
    except rospy.ROSInterruptException:
        pass

 

