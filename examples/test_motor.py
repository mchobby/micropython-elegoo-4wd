""" test_motors.py - Example for the Elegoo 4WD rover MicroPython library

	Show how control the motors of the Elegoo.

* Author(s):  Meurisse D. from MCHobby (shop.mchobby.be).

See project source @ https://github.com/mchobby/micropython-elegoo-4wd

See adapter board: Elegoo-4WD-Pico @ shop.mchobby.be
"""

from rover import Rover
import time

r = Rover()

# Move at speed between 0 and 100
r.motors.forward( 50, 50 ) # No parameter = full speed
time.sleep( 2 )
r.motors.backward( 100, 100 ) # No parameter = full speed
time.sleep( 2 )
r.motors.stop()
time.sleep( 2 )
r.motors.right( 80, 80 ) # No parameter= full speed
time.sleep( 2 )
r.motors.left( 80, 80 ) # No parameter= full speed
r.motors.stop()
