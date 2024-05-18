""" test_i2c.py - Example for the Elegoo 4WD rover MicroPython library

	Show how to grab a reference to the I2C bus available on Qwiic connector
	and UEXT connector.

* Author(s):  Meurisse D. from MCHobby (shop.mchobby.be).

See project source @ https://github.com/mchobby/micropython-elegoo-4wd

See adapter board: Elegoo-4WD-Pico @ shop.mchobby.be
"""
from rover import Rover
from time import sleep

rover=Rover()
# Get I2C bus
i2c = rover.i2c
# Scan items on the bus
print( i2c.scan() )
