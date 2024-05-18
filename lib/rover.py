""" rover.py - Library for the Elegoo 4WD rover running under MicroPython on
               Raspberry-Pi Pico board

* Author(s):  Meurisse D. from MCHobby (shop.mchobby.be).

See project source @ https://github.com/mchobby/micropython-elegoo-4wd
See adapter board: Elegoo-4WD-Pico @ shop.mchobby.be

See examples in the project source
"""
#
# The MIT License (MIT)
#
# Copyright (c) 224 Meurisse D. for MC Hobby
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

__version__ = "0.0.1"
__repo__ = "https://github.com/mchobby/micropython-elegoo-4wd"

from machine import Pin, PWM, I2C, SPI, UART
from ultrasonic import Ultrasonic
from servo import Servo
from micropython import const

I2C_DEFAULT_FREQ = const( 400000 ) # 400 KBits/sec
SPI_DEFAULT_SPI  = const( 2000000 ) # 2Mbits/sec
UART_DEFAULT_BAUDRATE = const( 9600 ) # Standard 9600 bauds

class Motors:
	def __init__(self):
		self.in1 = Pin( Pin.board.GP18, Pin.OUT )
		self.in2 = Pin( Pin.board.GP19, Pin.OUT )
		self.in3 = Pin( Pin.board.GP20, Pin.OUT )
		self.in4 = Pin( Pin.board.GP21, Pin.OUT )
		self.ena = PWM( Pin.board.GP17, freq=500 )
		self.enb = PWM( Pin.board.GP22, freq=500 )
		self.ena.duty_u16( 0 )
		self.enb.duty_u16( 0 )

	def speed_to_duty( self, speed ):
		assert 0<=speed<=100
		assert type(speed) is int

		return int(65535.0*speed/100)

	def forward( self, speed_left=100, speed_right=100 ):
		self.in1.value( 1 )
		self.in2.value( 0 )
		self.in3.value( 0 )
		self.in4.value( 1 )
		self.ena.duty_u16( self.speed_to_duty(speed_right) )
		self.enb.duty_u16( self.speed_to_duty(speed_left) )

	def backward( self, speed_left=100, speed_right=100 ):
		self.in1.value( 0 )
		self.in2.value( 1 )
		self.in3.value( 1 )
		self.in4.value( 0 )
		self.ena.duty_u16( self.speed_to_duty(speed_right) )
		self.enb.duty_u16( self.speed_to_duty(speed_left) )

	def left( self, speed_left=100, speed_right=100 ):
		self.in1.value( 0 )
		self.in2.value( 1 )
		self.in3.value( 0 )
		self.in4.value( 1 )
		self.ena.duty_u16( self.speed_to_duty(speed_right) )
		self.enb.duty_u16( self.speed_to_duty(speed_left) )

	def right( self, speed_left=100, speed_right=100 ):
		self.in1.value( 1 )
		self.in2.value( 0 )
		self.in3.value( 1 )
		self.in4.value( 0 )
		self.ena.duty_u16( self.speed_to_duty(speed_right) )
		self.enb.duty_u16( self.speed_to_duty(speed_left) )

	def stop( self, speed_left=100, speed_right=100 ):
		self.ena.duty_u16( 0 )
		self.enb.duty_u16( 0 )
		self.in1.value( 0 )
		self.in2.value( 0 )
		self.in3.value( 0 )
		self.in4.value( 0 )

class Rover:
	def __init__(self):
		# Protected object ref of vrious buses
		self._i2c = None
		self._spi = None
		self._uart= None
		self._cs_rfm = None  # Chip Select for RFM69 module
		self._cs_uext = None # Chip Select for UEXT module
		self._rst_rfm = None # Reset for RFM69 module

		# Public object ref
		self.motors = Motors()
		self.motors.stop()
		self.distance = Ultrasonic( Pin.board.GP28, Pin.board.GP2 ) # Trigger_pin, Echo_pin
		self.servo = Servo( Pin.board.GP16 )
		self.servo.calibration( 0.7, 2.0, 1.3, 0, 180 )
		# List of input Pins
		self.line_sensors = []
		for pin in (Pin.board.GP12,Pin.board.GP13,Pin.board.GP14):
			self.line_sensors.append( Pin(pin, pin.IN) )

	def read_line( self ):
		return [self.line_sensors[0].value(), self.line_sensors[1].value(), self.line_sensors[2].value() ]

	@property
	def i2c( self ):
		""" Get access to I2C bus """
		if self._i2c:
			return self._i2c
		self._i2c = I2C( 1, sda=Pin.board.GP26, scl=Pin.board.GP27, freq=I2C_DEFAULT_FREQ )
		return self._i2c

	@property
	def spi( self ):
		""" Get access to SPI bus """
		if self._spi:
			return self._spi
		self._spi = SPI( 0, mosi=Pin.board.GP7, miso=Pin.board.GP4, sck=Pin.board.GP6, baudrate=SPI_DEFAULT_SPI )
		return self._spi

	@property
	def uext_cs( self ):
		""" Get Chip Select line for UEXT connector """
		if self._cs_uext:
			return self._cs_uext
		self._cs_uext = Pin( Pin.board.GP9, Pin.OUT, value=1 )
		return self._cs_uext

	@property
	def rfm_cs( self ):
		""" Get Chip Select line for RFM69 connector """
		if self._cs_rfm:
			return self._cs_rfm
		self._cs_rfm = Pin( Pin.board.GP5, Pin.OUT, value=1 )
		return self._cs_rfm

	@property
	def rfm_reset( self ):
		""" Get Reset line for RFM69 connector """
		if self._rst_rfm:
			return self._rst_rfm
		self._rst_rfm = Pin( Pin.board.GP8, Pin.OUT, value=1 )
		return self._rst_rfm

	@property
	def uart( self ):
		""" Access the UART """
		if self._uart:
			return self._uart
		self._uart = UART( 0, rx=Pin.board.GP1, tx=Pin.board.GP0, bits=8, parity=None, stop=1, baudrate=UART_DEFAULT_BAUDRATE )
		return self._uart
