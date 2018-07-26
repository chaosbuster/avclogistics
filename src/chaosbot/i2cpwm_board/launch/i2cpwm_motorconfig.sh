
rosservice call /config_servos "servos: [{servo: 1, center: 310, range: 80, direction: 1},{servo: 2, center: 300, range: 100, direction: -1}]"

rosservice call /config_drive_mode "{mode: ackerman, rpm: 56.0, radius: 0.0325, track: 0.22, scale: 1.0, servos: [{servo: 2, position: 1}]}"
rosservice call /config_servos "servos: [{servo: 5, center: 330, range: 90, direction: 1}]"

rostopic pub -1 /servos_absolute i2cpwm_board/ServoArray "{servos:[{servo: 2, value: 425}]}"

rostopic pub -1 /servos_proportional i2cpwm_board/ServoArray "{servos:[{servo: 1, value: 0.50}]}"

rosservice call /stop_servos

