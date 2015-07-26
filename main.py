#!/usr/bin/env python
import time
import os

from plugins import *
import CustomHandlers

# Light switch
CapSwitch.CapSwitch(SerialEnumeration.find("capbutton1"))

# Telephony services
rotdial = RotaryDial.RotaryDial(SerialEnumeration.find("rotarydial"))

# Various telemetry and electromagnetic relay control
srb = SensorRelayBoard.SensorRelayBoard(SerialEnumeration.find("sensorrelay"))
SensorRelayBoard.Relay(3, 1, srb.ser)

# Handle telephony requests and connect calls
CustomHandlers.RotaryHandler(rotdial.ser)

# Test temporal quantification mechanism
CustomHandlers.Timer()

# Interface with a light production mechanism
test = Lightbulb.connect(1, "44:A6:E5:03:27:F9", '71', '151')
test2 = Lightbulb.connect(2, "44:A6:E5:03:27:DF", '89', '119')

# Allow control over a most curious telegraphy system
HTTP_API.HTTP_API()

#test.setStatus(1)
#time.sleep(5)
#test.setParameter("color", 1)
#test.setParameter("temp", 144)
#time.sleep(5)
#test.setStatus(0)

#print test.getParameters()

#b = 100
#while b > 1:
#    test.setParameter("brightness", b)
#    b = b-1
#    time.sleep(0.1)

#test.setParameter("color", 1)
#test.setParameter("brightness", 100)

#TestHandler()
#TestSensor()

while True:
    try:
        time.sleep(1)
    except KeyboardInterrupt:
        print '^C received, shutting down'
        os._exit(0)
