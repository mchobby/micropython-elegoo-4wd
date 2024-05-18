""" test_line.py - Example for the Elegoo 4WD rover MicroPython library

	Show how to grab a read the line sensors available under the rover.

* Author(s):  Meurisse D. from MCHobby (shop.mchobby.be).

See project source @ https://github.com/mchobby/micropython-elegoo-4wd

See adapter board: Elegoo-4WD-Pico @ shop.mchobby.be
"""
from rover import Rover
from time import sleep

rover=Rover()
while True:
	# returns a list of 3 values [0,0,0] corresponding to the [left,middle,right]
	# line sensors.
	values = rover.read_line()
	print( "Line value [left,middle,right] : %s" % (values) )
	sleep( 1 )
