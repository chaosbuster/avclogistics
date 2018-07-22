# Simple demo of of the PCA9685 PWM servo/LED controller library.
# This will move channel 1 from min to max position repeatedly.
# Author: Tony DiCola
# License: Public Domain
from __future__ import division
import time

# Import the PCA9685 module.
import Adafruit_PCA9685


# Uncomment to enable debug output.
#import logging
#logging.basicConfig(level=logging.DEBUG)

# Initialise the PCA9685 using the default address (0x40).
pwm = Adafruit_PCA9685.PCA9685(address=0x40, busnum=1)

# Alternatively specify a different address and/or bus:
#pwm = Adafruit_PCA9685.PCA9685(address=0x41, busnum=2)

# Configure min and max servo pulse lengths

# For Forward and Reverse ranges of speed, Channel 1.  
# Requires the neutral to be set first before forward or reverse recognized
#servo_min = 350  # reverse
#servo_neutral = 400  # neutral
#servo_max = 450  # Forward

# Ranges for steering, Channel 0
#servo_min = 300  
#servo_neutral = 400  # Min pulse length out of 4096
#servo_max = 500  # Max pulse length out of 4096

# Ranges for camera pan. Channel 14
#servo_min = 200  # Turns camera-view right
#servo_neutral = 350
#servo_max = 500   # Turns camera-view left

# Ranges for camera tilt. Channel 15
#servo_min = 250
#servo_neutral = 350
#servo_max = 475

# Ranges for shoulder joint. Channel 4
servo_min = 200  # Turns shoulder joint
servo_neutral = 375
servo_max = 500   # Turns shoulder joint

# Ranges for elbox joint. Channel 5
#servo_min = 350  # To back of bot
#servo_neutral = 400  # neutral
#servo_max = 450  # To front of bot

# Ranges for wrist joint. Channel 6
#servo_min = 150  # Turns wrist joint
#servo_neutral = 250
#servo_max = 650  # Turns wrist joint

# Ranges for main gripper joint. Channel 7
#servo_min = 200  # Turns hand joint
#servo_neutral = 400
#servo_max = 1000   # Turns hand joint


# Helper function to make setting a servo pulse width simpler.
#def set_servo_pulse(channel, pulse):
#    pulse_length = 1000000    # 1,000,000 us per second
#    pulse_length //= 60       # 60 Hz
#    print('{0}us per period'.format(pulse_length))
#    pulse_length //= 4096     # 12 bits of resolution
#    print('{0}us per bit'.format(pulse_length))
#    pulse *= 1000
#    pulse //= pulse_length
#    pwm.set_pwm(0, channel, pulse)

# Set frequency to 60hz, good for servos.
pwm.set_pwm_freq(60)

#print('Moving servo on channel 1, press Ctrl-C to quit...')
pwm.set_pwm(4, 1, servo_neutral)
time.sleep(1)

# Set frequency to 60hz, good for servos.
pwm.set_pwm_freq(0)

#while True:
   # Move servo on a channel between extremes.
#    print('Moving servo to min...')
#    pwm.set_pwm(5, 1, servo_min)
#    time.sleep(1)
#    print('Moving servo to max...')
#    pwm.set_pwm(5, 1, servo_max)
#    time.sleep(1)
