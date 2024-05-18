""" test_servo.py - Example for the Elegoo 4WD rover MicroPython library

	Show how to control the orientation of the ultrasonic sensor (using the Servo).

	Remark: the Rover class set the specific calibration data for the Servo
			included in the Eleego kit.
			You may need to adapt the calibration data when using another servo.
			See the rover.servo.calibration() call.

* Author(s):  Meurisse D. from MCHobby (shop.mchobby.be).

See project source @ https://github.com/mchobby/micropython-elegoo-4wd

See adapter board: Elegoo-4WD-Pico @ shop.mchobby.be
"""

from rover import Rover
import time

rover=Rover()

# Update servo calibration data
# Parameter are:
#   Min pulse time (ms)
#   Max pulse time (ms)
#   Middle position pulse time (ms)
#   Minimum angle value
#   Maximum angle value
#
# rover.servo.calibration( 0.7, 2.0, 1.3, 0, 180 )

print( "Look ahead" )
rover.servo.angle( 90 )
time.sleep( 0.1 )

print( "Look right" )
rover.servo.angle( 0 )
time.sleep( 2 )

print( "Look left" )
rover.servo.angle( 180 )
time.sleep(2)

print( "Look ahead" )
rover.servo.angle( 90 )

print( "That s all folks!" )
