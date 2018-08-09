#!/usr/bin/env sh

# Set calibration parameters to servos on i2c board

rosservice call /config_servos "servos: [{servo: 1, center: 310, range: 80, direction: 1},{servo: 2, center: 300, range: 100, direction: 1},{servo: 5, center: 330, range: 90, direction: 1},{servo: 6, center: 335, range: 90, direction: 1},{servo: 7, center: 240, range: 200, direction: -1},{servo: 8, center: 350, range: 400, direction: -1}]"

rosservice call /stop_servos
