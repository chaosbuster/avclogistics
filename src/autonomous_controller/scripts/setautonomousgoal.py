#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Joy
from autonomous_controller.srv import *
from autonomous_controller.msg import *

ERROR_NONE = 0
ERROR_NOTINAUTONOMOUS = 1
ERROR_NOTVALIDGOAL = 2

GOAL_AUTOSTART = 'autostart'
GOAL_PICKUPMATERIAL = 'pickupmaterial'
GOAL_DROPOFFMATERIAL = 'dropoffmaterial'

# Create our variable to hold the current state
curAutonomousGoal = AutonomousState()
 
def handle_setautonomousgoal(req):
    global curAutonomousGoal, pubGoal

    print "Attempting to set Autonomous Goal to: %s"%(req.goal)
    # All the individual autonomous tasks will not switch to their task unless the main Autonomous mode is True
    if curAutonomousGoal.inAutonomous:
         print "In Autonomous so setting Autonomous Goal to: %s"%(req.goal)
         if req.goal <> GOAL_AUTOSTART and req.goal <> GOAL_PICKUPMATERIAL and req.goal <> GOAL_DROPOFFMATERIAL:
              print "Not a valid goal for our current autonomous capabilities"
              return SetAutonomousGoalResponse(ERROR_NOTVALIDGOAL)
         elif req.goal == GOAL_AUTOSTART:
              curAutonomousGoal.autoStart = True
              curAutonomousGoal.pickupMaterial = False
              curAutonomousGoal.dropoffMaterial = False
              print "Set Autonomous Goal to:  %s"%(GOAL_AUTOSTART)
         elif req.goal == GOAL_PICKUPMATERIAL:
              curAutonomousGoal.autoStart = False
              curAutonomousGoal.pickupMaterial = True
              curAutonomousGoal.dropoffMaterial = False
              print "Set Autonomous Goal to:  %s"%(GOAL_PICKUPMATERIAL)
         elif req.goal == GOAL_DROPOFFMATERIAL:
              curAutonomousGoal.autoStart = False
              curAutonomousGoal.pickupMaterial = False
              curAutonomousGoal.dropoffMaterial = True
              print "Set Autonomous Goal to:  %s"%(GOAL_DROPOFFMATERIAL)

         # Let other services know we have changed Autonomous Goal
         pubGoal.publish(curAutonomousGoal) 
    else:
         print "Not in autonomous mode. Please set robot into autonomous mode before setting a goal."
         return SetAutonomousGoalResponse(ERROR_NOTINAUTONOMOUS)

    return SetAutonomousGoalResponse(ERROR_NONE)

def callback_resetCurrentAutonomousState(curState):
    global curAutonomousGoal
    print "Setting Autonomous goal in our Goal services to keep current. "
    # Set main Autonomous state to passed setting
    curAutonomousGoal.inAutonomous = curState.inAutonomous
    curAutonomousGoal.autoStart = curState.autoStart
    curAutonomousGoal.pickupMaterial = curState.pickupMaterial
    curAutonomousGoal.transportToProduction = curState.transportToProduction
    curAutonomousGoal.dropoffMaterial = curState.dropoffMaterial 
    curAutonomousGoal.transportToWarehouse = curState.transportToWarehouse

 
def setautonomousgoal():
    global curAutonomousGoal, pubGoal

    rospy.init_node('setautonomousgoal')

    # Set default values to our autonomous options
    curAutonomousGoal.inAutonomous = False
    curAutonomousGoal.autoStart = False
    curAutonomousGoal.pickupMaterial = False
    curAutonomousGoal.transportToProduction = False
    curAutonomousGoal.dropoffMaterial = False
    curAutonomousGoal.transportToWarehouse = False

    # Need to subscribe to AutonomousState msgs to make sure we are current whether we are in Autonomous mode
    rospy.Subscriber('autonomousstate', AutonomousState, callback_resetCurrentAutonomousState)

    # defining a publisher to advertise the new goal
    pubGoal = rospy.Publisher('autonomousstate', AutonomousState, queue_size=1)

    s = rospy.Service('setautonomousgoal', SetAutonomousGoal, handle_setautonomousgoal)
    print "Reading to set autonomous goal"
    rospy.spin()

if __name__ == "__main__":
     setautonomousgoal()



