#!/usr/bin/env python
import rospy
import time
from std_msgs.msg import String
from detect_field.msg import Clockstart

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.hasClockStarted)
    
def listen_forClockStart():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # node are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('listen_forClockStart', anonymous=True)

    rospy.Subscriber("clockstart", Clockstart, callback)
 
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listen_forClockStart()
