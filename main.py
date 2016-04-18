#!/usr/bin/env python
import time
import os

from plugins import *
import CustomHandlers

# Light switch
#try:
#    CapSwitch.CapSwitch(SerialEnumeration.find("capbutton1"))
#except:
#    pass

try:
    # Telephony services
    rotdial = RotaryDial.RotaryDial(SerialEnumeration.find("rotarydial"))

    # Handle telephony requests and connect calls
    CustomHandlers.RotaryHandler(rotdial.ser)
except:
    pass

# Interface with a light production mechanism
print(" * Connecting lightbulbs...")
test = Lightbulb.connect(1, 71, 151, Lightbulb.GattQueue("44:A6:E5:03:27:F9", "hci0"))
test2 = Lightbulb.connect(2, 89, 119, Lightbulb.GattQueue("44:A6:E5:03:27:DF", "hci1"))
print(" * Lightbulbs connected!")

# Various telemetry and electromagnetic relay control
#srb = SensorRelayBoard.SensorRelayBoard(SerialEnumeration.find("sensorrelay"))
#SensorRelayBoard.Relay(3, 1, srb.ser)

# Allow control over a Highly Terrific but Troublesome Protocol
HTTP_API.HTTP_API()

# Test temporal quantification mechanism
#CustomHandlers.Timer().start()

#test.setStatus(0)
#test2.setStatus(0)
#time.sleep(2)
#test.setParameter("color", 1)
#test.setParameter("temp", 144)
#time.sleep(5)
#test.setStatus(1)
#test2.setStatus(1)

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
