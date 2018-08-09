#!/usr/bin/env python
import rospy
import cv2
import time
import numpy as np
from std_msgs.msg import String
from std_msgs.msg import Bool
from autonomous_controller.msg import AutonomousState
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
from autonomous_start.msg import Clockstart 

# Initialize a stillAutonomous variable and initialize
stillAutonomous = False
# Initialize a variable that let's us know if an AutoStart goal has been set
goal_StartLooking = False

# Initialize a Clockstart structure
startClock = Clockstart()
startClock.durationSinceStart = 0
startClock.hasClockStarted = False

count = 0
t0 = 0

bridge = CvBridge()
numHoughCirclesRequired = 30

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
    global startClock, count, t0, stillAutonomous, goal_StartLooking

    count = count + 1

    if startClock.hasClockStarted:
         #Clock has started
         #Updating duration to indicate time passed since the clock started          
         startClock.durationSinceStart = time.time() - t0
                   
    else:
         if stillAutonomous and goal_StartLooking:
              #Use camera to detect start signal
              if detect_GreenCircle(rawimage):
                   rospy.loginfo(rospy.get_caller_id() + "Detected green circle")
                   startClock.hasClockStarted = True
                   t0 = time.time()
                   startClock.durationSinceStart = 0
                   # Move ChaosBot past the startline
                   moveChaosBot()
    
# If the clock has started, then we need to move chaosbot past the start line (Assuming straight)
def moveChaosBot():
    startlineDirection = Twist()

    rospy.loginfo(rospy.get_caller_id() + "Moving past start line")
    if stillAutonomous and goal_StartLooking:
         # Set chassis direction and speed          
	 startlineDirection.linear.x = 0.25
    	 startlineDirection.angular.z = 0

         # Publish chassis direction and speed
         pubChassis.publish(startlineDirection)
    
def callback_setIfRequested(autonomousState):
    global stillAutonomous, goal_StartLooking

    if autonomousState.inAutonomous and autonomousState.autoStart:
         #Start looking for start signal      
         stillAutonomous = True      
         goal_StartLooking = True       
         rospy.loginfo("Start in autonomous state and autonomous start goal has been set.")
    elif autonomousState.inAutonomous:
         #Start looking for start signal      
         stillAutonomous = True      
         goal_StartLooking = False       
         rospy.loginfo("Start in autonomous state. Can look for start signal if set as goal")
    else:
         #Not ready to look for start signal
         stillAutonomous = False 
         goal_StartLooking = False                            
         rospy.loginfo("DON'T Start looking for start signal")


def autostart():
    global pubChassis

    rospy.init_node('autostart')

    rospy.Subscriber('cam_startsignal/image_raw', Image, callback_processimage, queue_size=5, buff_size=2**12)
    rospy.Subscriber('autonomousstate', AutonomousState, callback_setIfRequested)

    # publishing a geometry servos_drive Twist to control ChaosBot chassis when we see the start signal
    pubChassis = rospy.Publisher('servos_drive', Twist, queue_size=1)

    rospy.spin()

if __name__ == "__main__":
     autostart()

 

