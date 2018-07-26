Header header
# Following model of Open Software Robot Foundation for their car demo with a Prius

# Range 0 to 1, 1 is max speed
float64 chassis_speed

# Speed direction of our chassis
#     FORWARD=1
#     NOSPEED=0
#     REVERSE=-1
int32 chassis_speeddirection

# Range -1 to +1, +1 is maximum left turn
float64 chassis_steering

uint8 NO_COMMAND=0

# Values 0 or 1, 1 means stop all motor actions
uint8 STOPMOTORS=0



