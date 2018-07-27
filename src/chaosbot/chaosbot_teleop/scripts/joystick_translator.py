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
    
joystick = Twist()
chaosbot_cmds = [ Servo() for i in range(6)]
global pos_wrist, pos_hand

def callback_allcurrentinputs(data):
    rospy.loginfo('Received a joystick input')
    # Initialize the wrist and hand to neutral (middle) position
    global pos_wrist, pos_hand

    joystick.linear.x = data.axes[3]
    joystick.angular.z = data.axes[2]

    # Set the steering 
    # Negative's are right, Positive's are left
    chaosbot_cmds[0].servo = 2
    chaosbot_cmds[0].value = data.axes[2]

    # Set the speed for the chassis
    # Negative's are reverse, Positive's are forward
    chaosbot_cmds[1].servo = 1
    chaosbot_cmds[1].value = data.axes[3]

    # Set the speed for the shoulder 
    # Negative's are reverse towards the back
    # Positive's are forward towards the front
    chaosbot_cmds[2].servo = 5
    chaosbot_cmds[2].value = data.axes[1]

    # Set the speed for the elbow
    # Negative's are reverse towards the back
    # Positive's are forward towards the front
    chaosbot_cmds[3].servo = 6
    chaosbot_cmds[3].value = data.axes[0]

    # Set the position for the wrist
    if data.buttons[7] <> 0:
         # If Button 8 then Positive to open
         # For safety doing open direction if both buttons
         pos_wrist = pos_wrist + 0.1
    elif data.buttons[5] <> 0:
         # If Button 6 then Negative to close
         pos_wrist = pos_wrist - 0.1
    else:
         # If No Button 6 or 8 then no change
         pos_wrist = pos_wrist

    # The wrist 
    # Channel 6 Base-Zero
    # Base-One for i2c software interface below
    chaosbot_cmds[4].servo = 7
    chaosbot_cmds[4].value = pos_wrist

    if data.buttons[6] <> 0:
    # If Button 7 then Positive to open
         pos_hand = pos_hand + 0.1
    elif data.buttons[4] <> 0:
    # If Button 5 then Negative to close
         pos_hand = pos_hand - 0.1
    else:
    # If No Button 6 or 8 then no change
         pos_hand = pos_hand

    # The hand 
    # Channel 7 Base-Zero
    # Channel 8 Base-One for i2c software interface below
    chaosbot_cmds[5].servo = 8  
    chaosbot_cmds[5].value = pos_hand

    #pubPlanned.publish(joystick)
    pubControl.publish(chaosbot_cmds)


# Initializes everything
def joystick_translator():
    global pubPlanned, pubControl
    global pos_wrist, pos_hand

    # Starting the node
    rospy.init_node('joystick_translator')
    pos_wrist = 0
    pos_hand = 0

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

 

