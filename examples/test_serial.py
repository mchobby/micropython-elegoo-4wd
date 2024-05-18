""" test_serial.py - Example for the Elegoo 4WD rover MicroPython library

	Show how to grab a reference to the UART

* Author(s):  Meurisse D. from MCHobby (shop.mchobby.be).

See project source @ https://github.com/mchobby/micropython-elegoo-4wd

See adapter board: Elegoo-4WD-Pico @ shop.mchobby.be
"""
from rover import Rover
from time import sleep

rover=Rover()
# Get Serial/uart line
# Use the ser.init() to change the default settings (8N1 9600 bauds)
ser = rover.uart
