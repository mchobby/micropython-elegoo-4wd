""" test_spi.py - Example for the Elegoo 4WD rover MicroPython library

	Show how to grab a reference to the SPI bus available on RFM connector
	and UEXT connector. It also shows how to gain access to the various
	chip select line as well as the reset line required for RFM69 module

* Author(s):  Meurisse D. from MCHobby (shop.mchobby.be).

See project source @ https://github.com/mchobby/micropython-elegoo-4wd

See adapter board: Elegoo-4WD-Pico @ shop.mchobby.be
"""
from rover import Rover
from time import sleep

rover=Rover()
# Get SPI bus and the two select lines and also the rfm reset line
spi = rover.spi
rfm_cs = rover.rfm_cs
rfm_rst = rover.rfm_reset
uext_cs = rover.uext_cs
