#!/usr/bin/env python

from autonomous_controller.srv import *
from autonomous_controller.msg import *
import rospy

ERROR_NONE = 0

# Create our variable to hold the current state
curAutonomousMode = AutonomousState()

def handle_setautonomousmode(req):
    global pubMode

    print "In Set Autonomous Mode service, toggling mode"
    # Clear all to False 
    # All the individual autonomous tasks will not switch to their task unless the main Autonomous mode is True
    curAutonomousMode.inAutonomous = False
    curAutonomousMode.autoStart = False
    curAutonomousMode.pickupMaterial = False
    curAutonomousMode.transportToProduction = False
    curAutonomousMode.dropoffMaterial = False
    curAutonomousMode.transportToWarehouse = False

    # Set main Autonomous Mode to passed setting
    curAutonomousMode.inAutonomous = req.inAutonomous

    # Let other services know we are changing Autonomous Mode
    pubMode.publish(curAutonomousMode) 

    return SetAutonomousModeResponse(ERROR_NONE)

def setautonomousmode():
    global pubMode

    rospy.init_node('setautonomousmode')

    # Set default values to our autonomous options
    curAutonomousMode.inAutonomous = False
    curAutonomousMode.autoStart = False
    curAutonomousMode.pickupMaterial = False
    curAutonomousMode.transportToProduction = False
    curAutonomousMode.dropoffMaterial = False
    curAutonomousMode.transportToWarehouse = False

    # publishing to autonomousstate msg to control ChaosBot
    pubMode = rospy.Publisher('autonomousstate', AutonomousState, queue_size=1)

    s = rospy.Service('setautonomousmode', SetAutonomousMode, handle_setautonomousmode)
    print "Reading to set autonomous mode"
    rospy.spin()

if __name__ == "__main__":
     setautonomousmode()






