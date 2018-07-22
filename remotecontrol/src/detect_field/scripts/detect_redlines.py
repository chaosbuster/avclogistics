#!/usr/bin/env python
import rospy
import cv2
import time
import numpy as np
from enum import Enum
from std_msgs.msg import String
from detect_field.msg import Clockstart
from detect_field.msg import RedLineSight
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

startclock = Clockstart()

# Initialize a RedLineSight message structure
eyes = RedLineSight()

eyes.sightedALine = False
eyes.durationSinceSighting = 0
eyes.lapNum = 0
eyes.sightedFinish = False

# Robot stages
class Stage (Enum):
  WAIT4START = 0
  STARTING = 1
  INLAP = 2
  ENDOFLAP = 3
  LAPLINE = 4
  FINISHED = 5

robotStage = Stage.STARTING
MAXLAPS = 2
t0 = 0

# STARTUP: Timing to get going after we see the start signal
# PASTLINES: Timing to get past red lines
# LOOKAGAIN: Timing after red lines before start looking again
# NOTE: Total time from sighting to getting close to end is 45 seconds
TIME4_STARTUP = 10000000
TIME4_PASTLINES = 5
TIME4_LOOKAGAIN = 10  

bridge = CvBridge()

# Initialize our publisher of clockstart topic with Clockstart msg
pub = rospy.Publisher('redlinesight', RedLineSight, queue_size=10)

def detect_RedLines(image):

    # convert raw image to an OpenCV BGR image
    cvimage_bgr = bridge.imgmsg_to_cv2(image, "bgr8")

    cv2.imwrite("~/catkin_ws/img/" + str(time.time()) + "_Redlines_OriginalInput" + ".jpg" , cvimage_bgr)

    # convert to HSV 
    cvimage_hsv = cv2.cvtColor(cvimage_bgr, cv2.COLOR_BGR2HSV)

    # Threshold the HSV image, keep only the red pixels
    lower_red_hue_range = cv2.inRange(cvimage_hsv, (0,100,100), (10,255,255))
    upper_red_hue_range = cv2.inRange(cvimage_hsv, (160,100,100), (179,255,255))
 
    #Combine the two red images
    red_image = cv2.addWeighted(lower_red_hue_range, 1.0, upper_red_hue_range, 1.0, 0.0)

    # Gaussian blur
    gaussian_blur = cv2.GaussianBlur(red_image, (7, 7), 0)

    #bit8_gray = cv2.cvtColor(gaussian_blur,cv2.COLOR_BGR2GRAY)

    #edges = cv2.Canny(red_image, 50, 150)

    cv2.imwrite("~/catkin_ws/img/" + str(time.time()) + "_RedLines_HLInput" + ".jpg" ,gaussian_blur)
    
    # Use Hough Lines
    lines = cv2.HoughLinesP(image=gaussian_blur,rho=30,theta=np.pi/180, threshold=300,lines=np.array([]), minLineLength=500,maxLineGap=30)
    
    rospy.loginfo("RedLines...after HoughLines")

    if lines is None:
      rospy.loginfo("RedLines...lines is empty")
      
      return False
    else:

      rospy.loginfo("RedLines...trying to overlay lines on image")

      orig_image = cvimage_bgr.copy()

      # Loop over all detected lines and outline them on the original image

      a,b,c = lines.shape
      for i in range(a):
        # draw the outer line
        rospy.loginfo(lines[i])
        cv2.line(orig_image, (lines[i][0][0], lines[i][0][1]), (lines[i][0][2], lines[i][0][3]), (0, 0, 255), 3, cv2.LINE_AA)


      cv2.imwrite("~/catkin_ws/img/" + str(time.time()) + "_RedLines_HLOutput" + ".jpg" ,orig_image)
    
      return True
 
def callback_processimage(rawimage):
    global eyes, robotStage, Stage, TIME4_STARTUP, TIME4_PASTLINES, TIME4_LOOKAGAIN, t0, MAXLAPS

    rospy.loginfo("DETECT_REDLINES: In our callback_processimage")
    rospy.logdebug(rawimage)

    if robotStage == Stage.WAIT4START:
      rospy.loginfo("Redlines: Waiting for start")

      # Do nothing and just reset eyes
      eyes.sightedALine = False
      eyes.durationSinceSighting = 0
      eyes.lapNum = 0
      eyes.sightedFinish = False

    elif robotStage == Stage.STARTING:
       
      timeInStart = time.time() - t0

      logstr = '{} {} {} {}'.format('Redlines: Stage.STARTING, timeInStart=',timeInStart,', TIME4_STARTUP=', TIME4_STARTUP)
      rospy.loginfo(logstr)

      # See if we have given robot enough time to startup and get past starting line
      if timeInStart > TIME4_STARTUP:

        # Past starting line and into our lap
        robotStage = Stage.INLAP

        # Need to restart timer of when to begin looking for redlines
        t0 = time.time()  

    elif robotStage == Stage.INLAP:
      rospy.loginfo("Redlines: In Lap")

      timeInLap = time.time() - t0

      logstr = '{} {} {} {}'.format('Redlines: Stage.INLAP, timeInLap=',timeInLap,', TIME4_LOOKAGAIN=', TIME4_LOOKAGAIN)
      rospy.loginfo(logstr)

      # See if we have given robot enough time to get close to starting line
      if timeInLap > TIME4_LOOKAGAIN:

        # Getting close to end of lap
        robotStage = Stage.ENDOFLAP
        t0 = 0
        
    elif robotStage == Stage.ENDOFLAP:
    # Near end of lap. Need to process images    
      rospy.loginfo("Redlines: Near End of Lap. Start processing images")

      if detect_RedLines(rawimage):
        rospy.loginfo("Redlines: Found lines")

        t0 = time.time()
        eyes.sightedALine = True
        robotStage = Stage.LAPLINE

        if eyes.lapNum == MAXLAPS:
          eyes.sightedFinish = True

        eyes.durationSinceSighting = time.time() - t0

    elif robotStage == Stage.LAPLINE:
      # We just got near lap line 
      # If not last lap, use timer to get past before trying to detect again
      rospy.loginfo("Redlines: At Lap Line")

      eyes.durationSinceSighting = time.time() - t0

      logstr = '{} {} {} {} {} {}'.format('Redlines: Stage.LAPLINE, durationSinceSighting=',eyes.durationSinceSighting,', TIME4_PASTLINES=', TIME4_PASTLINES, ', MAXLAPS=', MAXLAPS)
      rospy.loginfo(logstr)

      if eyes.durationSinceSighting >  TIME4_PASTLINES:

        if eyes.lapNum == MAXLAPS:
          robotStage = Stage.FINISHED
          eyes.sightedFinish = True
        else:
          robotStage = Stage.INLAP
          eyes.lapNum = eyes.lapNum + 1
          eyes.sightedALine = False
          eyes.durationSinceSighting = 0
          t0 = time.time()

    elif robotStage == Stage.FINISHED:
      rospy.loginfo("Redlines: Finished")
       
      eyes.sightedALine = True
      eyes.durationSinceSighting = time.time() - t0
      eyes.sightedFinish = True

               
def callback_clockstart(data):
    global Stage, robotStage, t0, eyes, startclock

    startclock = data

    if startclock.hasClockStarted and robotStage == Stage.WAIT4START:

      rospy.loginfo("I heard the clock has started.")

      robotStage = Stage.STARTING
      t0 = time.time()
      eyes.lapNum = 1

def detect_redlines():
    global eyes

    rospy.init_node('detect_redlines', anonymous=True)
    rate = rospy.Rate(1) # Reducing till get the startsignal found
    #rate = rospy.Rate(10) # 10hz

    rospy.Subscriber('clockstart', Clockstart, callback_clockstart)

    rospy.Subscriber('cam_forward/image_raw', Image, callback_processimage)

    while not rospy.is_shutdown():
        rospy.loginfo(eyes)
        pub.publish(eyes)
        rate.sleep()


if __name__ == '__main__':
    try:
        detect_redlines()
    except rospy.ROSInterruptException:
        pass

 

