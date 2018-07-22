#!/usr/bin/env python
import rospy
import cv2
import time
import numpy as np
from std_msgs.msg import String
from std_msgs.msg import Bool
from detect_field.msg import Clockstart
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

# Initialize a StartLooking structure and initialize
startLooking = True

# Initialize a Clockstart structure
startClock = Clockstart()
startClock.durationSinceStart = 0
startClock.hasClockStarted = False

count = 0
t0 = 0

bridge = CvBridge()
numHoughCirclesRequired = 30

# Initialize our publisher of clockstart topic with Clockstart msg
pubClockStart = rospy.Publisher('clockstart', Clockstart, queue_size=5)

def detect_GreenCircle(image):

    # convert raw image to an OpenCV BGR image
    cvimage_bgr = bridge.imgmsg_to_cv2(image, "bgr8")

    cv2.imwrite("~/catkin_ws/img/" + str(time.time()) + "_Clockstart_OriginalInput" + ".jpg" , cvimage_bgr)

    (rows,cols,channels) = cvimage_bgr.shape
    orig_image = cvimage_bgr.copy()

    # blur the BGR image
    # ***  blurred_bgr = cv2.medianBlur(cvimage_bgr, 3)

    # convert to HSV 
    cvimage_hsv = cv2.cvtColor(cvimage_bgr, cv2.COLOR_BGR2HSV)

    # define lower and upper limit of hue range for red color
    lowerRedHueRange = cv2.inRange(cvimage_hsv, np.array([0,100,100]),np.array([10,255,255]))
    upperRedHueRange = cv2.inRange(cvimage_hsv, np.array([160,100,100]),np.array([179,255,255]))

    # define lower and upper limit of hue range for green color
    lowerGreenHue = np.array([50,50,120])
    upperGreenHue = np.array([70,255,255])

    # Threshold the HSV image, keep only the green pixels
    greenMask = cv2.inRange(cvimage_hsv, lowerGreenHue, upperGreenHue)
  
    # Calculates the weighted sum of two arrays
    redHueThresholdedImage = cv2.addWeighted(lowerRedHueRange, 1.0, upperRedHueRange, 1.0, 0.0)

    # Blur the images using a Gaussian blur
    redHueThresholdedImage = cv2.GaussianBlur(redHueThresholdedImage, (9, 9), 2, 2)
    greenHueThresholdedImage = cv2.GaussianBlur(greenMask, (9, 9), 2, 2)

    cv2.imwrite("/home/chaos/catkin_ws/img/" + str(time.time()) + "_Clockstart_OriginalInput" + ".jpg" , cvimage_bgr)

    cv2.imwrite("/home/chaos/catkin_ws/img/" + str(time.time()) + "_Clockstart_redHueThresholdedImage" + ".jpg" ,redHueThresholdedImage)

    cv2.imwrite("/home/chaos/catkin_ws/img/" + str(time.time()) + "_Clockstart_greenHueThresholdedImage" + ".jpg" ,greenHueThresholdedImage)

    #find contours in the red hue image formed after weighted adding of lower and upper ranges of red
    redContours = cv2.findContours(redHueThresholdedImage.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]

    #find contours in the green hue image formed 
    greenContours = cv2.findContours(greenHueThresholdedImage.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]

    rospy.loginfo('{:30} {: d}'.format('Number of RED Contours found:', len(redContours)))
    rospy.loginfo('{:30} {: d}'.format('Number of GREEN Contours found:', len(greenContours)))

    if len(greenContours) > 0:

      greenCnt = greenContours[0]
      maxGreenContour = max(greenContours, key=cv2.contourArea)
      mGreen = cv2.moments(maxGreenContour)
      mGreenArea = cv2.contourArea(greenCnt)
      mGreenPerimeter = cv2.arcLength(greenCnt, True)

      rospy.loginfo('{} {:.2f}'.format('Max GREEN Contour Moment Area:', mGreenArea))
      rospy.loginfo('{} {:.2f}'.format('Max GREEN Contour Moment Perimeter:', mGreenPerimeter))

      if len(redContours) > 0:

        redCnt = redContours[0]
        maxRedContour = max(redContours, key=cv2.contourArea)
        mRed = cv2.moments(maxRedContour)
        mRedArea = cv2.contourArea(redCnt)
        mRedPerimeter = cv2.arcLength(redCnt, True)

        rospy.loginfo('{} {:.2f}'.format('Max RED Contour Moment Area:', mRedArea))
        rospy.loginfo('{} {:.2f}'.format('Max RED Contour Moment Perimeter:', mRedPerimeter))

      else:
        mRedArea = 0
        mRedPerimeter = 0

      # Compare the size of the red with the green contour 
      if mRedArea > mGreenArea:
        # More Red than Green so return False
        return False
      # More Green than Red but let's check for a minimum area of Green
      elif mGreenArea < 100:
        # Did not find a minimum amount of Green so not the Green Signal
        return False
      else:
        return True
    else:
      return False

 
def callback_processimage(rawimage):
    global startClock, sawStartSignal, count, t0, startLooking

    count = count + 1

    if startClock.hasClockStarted:
      #Clock has started
      #Updating duration to indicate time passed since the clock started          
      startClock.durationSinceStart = time.time() - t0
                   
    else:
      #Forcing to start looking for start signal
      startLooking = True
      if startLooking:

        #Use camera to detect start signal
        if detect_GreenCircle(rawimage):
          startClock.hasClockStarted = True
          t0 = time.time()
          startClock.durationSinceStart = 0

def callback_setIfLooking(looking):
    global startLooking

    if looking.data:
      #Start looking for start signal      
      startLooking= True             
      rospy.loginfo("Start looking for start signal")
    else:
      #Not ready to look for start signal
      startLooking = False                             
      rospy.loginfo("DON'T Start looking for start signal")

    #Will force to start looking for signal
    startLooking= True             
    rospy.loginfo("Start looking for start signal")



def detect_clockstart():
    global startClock, pubClockStart, sawStartSignal, pubSawStartSignal

    rospy.init_node('detect_clockstart', anonymous=True)

    rate = rospy.Rate(10) # 10hz

    rospy.Subscriber('cam_startsignal/image_raw', Image, callback_processimage)
    rospy.Subscriber('startlooking', Bool, callback_setIfLooking)


    while not rospy.is_shutdown():
        rospy.loginfo(startClock)
        pubClockStart.publish(startClock)
        rate.sleep()


if __name__ == '__main__':
    try:
        detect_clockstart()
    except rospy.ROSInterruptException:
        pass

 

