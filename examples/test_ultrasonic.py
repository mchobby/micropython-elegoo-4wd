""" test_ultrasonic.py - Example for the Elegoo 4WD rover MicroPython library

	Read the object distance in the front of the HC-SR04 ultrasonic sensor.

* Author(s):  Meurisse D. from MCHobby (shop.mchobby.be).

See project source @ https://github.com/mchobby/micropython-elegoo-4wd

See adapter board: Elegoo-4WD-Pico @ shop.mchobby.be
"""
from rover import Rover
from time import sleep

rover=Rover()
counter = 0
while True:
	counter += 1
	dist = rover.distance.distance_in_cm()
	print( "iteration %i : %s cm" % (counter,dist) )
	sleep( 1 )
