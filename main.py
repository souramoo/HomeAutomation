from plugins import *
from plugins import Sensor
from plugins import HTTP_API
import time
import os

test = Lightbulb.connect(1, "44:A6:E5:03:27:F9", '71', '151')
#test.setStatus(1)
#time.sleep(5)
#test.setParameter("color", 1)
#test.setParameter("temp", 144)
#time.sleep(5)
#test.setStatus(0)

#print test.getParameters()

class TestHandler(Sensor.EventHandler):
    def __init__(self):
        Sensor.EventHandler.__init__(self)
    def handle(self, data):
        print data

class TestSensor(Sensor.Sensor):
    def __init__(self):
        Sensor.Sensor.__init__(self)
    def run(self):
        Sensor.EventQueue.put("test")

#TestHandler()
#TestSensor()
HTTP_API.HTTP_API()


while True:
    try:
        time.sleep(1)
    except KeyboardInterrupt:
        print '^C received, shutting down'
        os._exit(0)
