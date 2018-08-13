#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Joy
from autonomous_controller.srv import *
from autonomous_controller.msg import *
from i2cpwm_board.msg import Servo, ServoArray
from i2cpwm_board.srv import *

GOAL_AUTOSTART = 'autostart'
GOAL_PICKUPMATERIAL = 'pickupmaterial'
GOAL_DROPOFFMATERIAL = 'dropoffmaterial'

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

ARMMOTORS_IN_CONTROL = 4
    
joystick = Twist()
chaosbot_cmds = [ Servo() for i in range(ARMMOTORS_IN_CONTROL)]

# Initialize a inAutonomous variable and initialize [Toggled with Button 10]
inAutonomous = False

global pos_wrist, pos_hand

def callback_allcurrentinputs(data):
    rospy.loginfo('Received a joystick input')
    # Initialize the wrist and hand to neutral (middle) position
    global pos_wrist, pos_hand

    # Stop all motors and don't send servo positions if Button 10
    if data.buttons[9] <> 0:
         toggleAutonomous()

    elif inAutonomous and data.buttons[0] <> 0:
         setGoal(GOAL_AUTOSTART)

    elif not inAutonomous:
         # Set chassis direction and speed          
	 joystick.linear.x = data.axes[3]
    	 joystick.angular.z = data.axes[2]

         # Publish chassis direction and speed
         pubChassis.publish(joystick)

         # Set the speed for the shoulder 
         # Negative's are reverse towards the back
         # Positive's are forward towards the front
         chaosbot_cmds[0].servo = 5
         chaosbot_cmds[0].value = data.axes[1]

         # Set the speed for the elbow
         # Negative's are reverse towards the back
         # Positive's are forward towards the front
         chaosbot_cmds[1].servo = 6
         chaosbot_cmds[1].value = data.axes[0]

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

         # Make sure in range
         if pos_wrist < -1.0:  
              pos_wrist = -1.0
         elif pos_wrist > 1.0:  
              pos_wrist = 1.0

         # The wrist 
         # Channel 6 Base-Zero
         # Base-One for i2c software interface below
         chaosbot_cmds[2].servo = 7
         chaosbot_cmds[2].value = pos_wrist
 
         if data.buttons[6] <> 0:
         # If Button 7 then Positive to open
              pos_hand = pos_hand + 0.2
 
         elif data.buttons[4] <> 0:
         # If Button 5 then Negative to close
              pos_hand = pos_hand - 0.2

         else:
         # If No Button 6 or 8 then no change
              pos_hand = pos_hand

         # Make sure in range
         if pos_hand > 1.0: 
              pos_hand = 1.0
         elif pos_hand < -1.0: 
              pos_hand = -1.0

         # The hand 
         # Channel 7 Base-Zero
         # Channel 8 Base-One for i2c software interface below
         chaosbot_cmds[3].servo = 8  
         chaosbot_cmds[3].value = pos_hand

         pubArm.publish(chaosbot_cmds)

def toggleAutonomous():
    global inAutonomous

    # Toggle the whether we are in autonomous
    inAutonomous = not inAutonomous

    # Stop any non-servo motors and let next mode take over
    stopmotors()

    # Set the autonomous mode for our autonomous controller
    rospy.wait_for_service('setautonomousmode')
    try:
         setMode = rospy.ServiceProxy('setautonomousmode', SetAutonomousMode)
         resp1 = setMode(inAutonomous)
    except rospy.ServiceException, e:
         print "Service call failed: %s"%e
 
def setGoal(goal):
    # Stop any non-servo motors and let next mode and goal take over
    stopmotors()

    # Set the autonomous mode for our autonomous controller
    rospy.wait_for_service('setautonomousgoal')
    try:
         setGoalService = rospy.ServiceProxy('setautonomousgoal', SetAutonomousGoal)
         resp1 = setGoalService(goal)
         print "Service call failed: %s"%resp1
    except rospy.ServiceException, e:
         print "Service call failed: %s"%e
 

def stopmotors():

    # Set chassis direction and speed to zero          
    joystick.linear.x = 0
    joystick.angular.z = 0

    # Publish chassis direction and speed
    pubChassis.publish(joystick)

    # Set the speed for the shoulder to zero
    chaosbot_cmds[0].servo = 5
    chaosbot_cmds[0].value = 0

    # Set the speed for the elbow to zero
    chaosbot_cmds[1].servo = 6
    chaosbot_cmds[1].value = 0

    pubArm.publish(chaosbot_cmds)

# Initializes everything
def joystick_translator():
    global pubChassis, pubArm
    global pos_wrist, pos_hand

    # Starting the node
    rospy.init_node('joystick_translator')
    pos_wrist = 0
    pos_hand = 0

    # publishing a geometry servos_drive Twist to control ChaosBot chassis in mecanum mode
    pubChassis = rospy.Publisher('servos_drive', Twist, queue_size=1)

    # publishing to chaosbot Control msg to control ChaosBot
    pubArm = rospy.Publisher('servos_proportional', ServoArray, queue_size=1)

    # Need to subscribe to joystick inputs on topic 'joy'
    rospy.Subscriber('joy', Joy, callback_allcurrentinputs)

    rospy.spin()

if __name__ == '__main__':
    try:
         joystick_translator()
    except rospy.ROSInterruptException:
         pass

 

