#!/usr/bin/env python
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import rospy
import os
import cv2
import sys
import time
import numpy as np
from std_msgs.msg import String
from std_msgs.msg import Bool
from autonomous_controller.msg import AutonomousState
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
from autonomous_start.msg import Clockstart 

import tensorflow as tf


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

def load_graph(model_file):
    global graph, graph_def

    graph = tf.Graph()
    graph_def = tf.GraphDef()

    with open(model_file, "rb") as f:
         graph_def.ParseFromString(f.read())
    with graph.as_default():
         tf.import_graph_def(graph_def)

    return graph

def load_labels(label_file):
    label = []
    proto_as_ascii_lines = tf.gfile.GFile(label_file).readlines()
    for l in proto_as_ascii_lines:
         label.append(l.rstrip())

    return label

def read_tensor_from_image_file(rawimage, input_height=299, input_width=299,
				input_mean=0, input_std=255):
    global graph

    try:
         cv_image = bridge.imgmsg_to_cv2(rawimage, "bgr8")
    except CvBridgeError as e:
         print(e)

    image_cv = cv2.cvtColor(cv_image, cv2.COLOR_BGR2RGB)
    # the array based representation of the image will be used later 
    # in order to prepare the result image with boxes and labels on it.
    image_tf = np.asarray(image_cv)
    # Expand dimensions since the model expects images to have shape: [1, None, None, 3]
    image_tf_expanded = np.expand_dims(image_tf, axis=0)

    resized = tf.image.resize_bilinear(image_tf_expanded, [input_height, input_width])
    normalized = tf.divide(tf.subtract(resized, [input_mean]), [input_std])
    sess = tf.Session()
    result = sess.run(normalized)

    return result

 
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
              if detect_StartSignal(rawimage):
                   rospy.loginfo(rospy.get_caller_id() + "Detected start signal")
                   startClock.hasClockStarted = True
                   t0 = time.time()
                   startClock.durationSinceStart = 0
                   # Move ChaosBot past the startline
                   moveChaosBot()


def detect_StartSignal(rawimage):
    global graph, labels

    input_height = 224
    input_width = 224
    input_mean = 128
    input_std = 128
    input_layer = "input"
    output_layer = "final_result"

    t = read_tensor_from_image_file(rawimage, 
                                    input_height=input_height,
                                    input_width=input_width,
                                    input_mean=input_mean,
                                    input_std=input_std)

    input_name = "import/" + input_layer
    output_name = "import/" + output_layer
    input_operation = graph.get_operation_by_name(input_name);
    output_operation = graph.get_operation_by_name(output_name);

    with tf.Session(graph=graph) as sess:
         start = time.time()
         results = sess.run(output_operation.outputs[0],
                            {input_operation.outputs[0]: t})
         end=time.time()
    
    results = np.squeeze(results)

    top_k = results.argsort()[-5:][::-1]

    print('\nEvaluation time (1-image): {:.3f}s\n'.format(end-start))
    template = "{} (score={:0.5f})"
    for i in top_k:
         print(template.format(labels[i], results[i]))

    if labels[0] == 'go' and results[0] > 0.75:
         # Save the image that triggered the start signal
         try:
              cv_image = bridge.imgmsg_to_cv2(rawimage, "bgr8")
         except CvBridgeError as e:
              print(e)
         image_cv = cv2.cvtColor(cv_image, cv2.COLOR_BGR2RGB)
         PATH_TO_IMAGE = os.path.join(os.path.dirname(sys.path[0]),'tf_files','saved_go',str(time.time())+"_RAWIMAGE" + ".jpg")
         print(PATH_TO_IMAGE)
         cv2.imwrite(PATH_TO_IMAGE , image_cv)
         return True
    else:
         return False

    
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
    global pubChassis, graph, labels

    model_file = "/home/chaos/avclogistics/src/autonomous_start/tf_files/trainedsigns_graph.pb"
    label_file = "/home/chaos/avclogistics/src/autonomous_start/tf_files/trainedsigns_labels.txt"

    graph = load_graph(model_file)
    labels = load_labels(label_file)

    rospy.init_node('autostart')

    rospy.Subscriber('cam_startsignal/image_raw', Image, callback_processimage, queue_size=5, buff_size=2**12)
    rospy.Subscriber('autonomousstate', AutonomousState, callback_setIfRequested)

    # publishing a geometry servos_drive Twist to control ChaosBot chassis when we see the start signal
    pubChassis = rospy.Publisher('servos_drive', Twist, queue_size=1)

    rospy.spin()

if __name__ == "__main__":
     autostart()

 

