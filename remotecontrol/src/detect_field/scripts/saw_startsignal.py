#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import String
from std_msgs.msg import UInt16
from detect_field.msg import Clockstart

iSawStartSignal = UInt16()
iSawStartSignal.data = 0

# Initialize a Clockstart structure
startClock = Clockstart()
startClock.durationSinceStart = 0
startClock.hasClockStarted = False

def callback(clockstart_msg):
    global iSawStartSignal

    if clockstart_msg.hasClockStarted:
      iSawStartSignal.data = 1
    else:
      iSawStartSignal.data = 0


def sawstartsignal():
    global iSawStartSignal

    pub = rospy.Publisher('sawstartsignal', UInt16, queue_size=1)
    rospy.init_node('saw_startsignal', anonymous=True)
    rate = rospy.Rate(1) # 10hz

    rospy.Subscriber('clockstart', Clockstart, callback)

    while not rospy.is_shutdown():
        rospy.loginfo(iSawStartSignal)
        pub.publish(iSawStartSignal)
        rate.sleep()


if __name__ == '__main__':
    try:
        sawstartsignal()
    except rospy.ROSInterruptException:
        pass

 

