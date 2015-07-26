from plugins import *
import threading
import datetime
import time

class RotaryHandler(Sensor.EventHandler):
    def __init__(self, ser):
        Sensor.EventHandler.__init__(self)
        self.ser = ser
    def handle(self, data):
        if data[0] == "rotary":
            if data[1] == "1":
                for a in Driver.Drivers:
                    if isinstance(a[1], Lightbulb.connect):
                        a[1].setParameter("status", 0)
            elif data[1] == "2":
                for a in Driver.Drivers:
                    if isinstance(a[1], Lightbulb.connect):
                        a[1].setParameter("status", 1)
            elif data[1] == "3":
                for a in Driver.Drivers:
                    if isinstance(a[1], Lightbulb.connect):
                        a[1].setParameter("color", 1)
            elif data[1] == "4":
                for a in Driver.Drivers:
                    if isinstance(a[1], Lightbulb.connect):
                        a[1].setParameter("color", 60)
            elif data[1] == "5":
                for a in Driver.Drivers:
                    if isinstance(a[1], Lightbulb.connect):
                        a[1].setParameter("color", 150)
#            elif data[1] == "6":
#                for a in Driver.Drivers:
#                    if isinstance(a[1], Lightbulb.connect):
#                        a[1].setParameter("color", 200)
            elif data[1] == "7":
                for a in Driver.Drivers:
                    if isinstance(a[1], Lightbulb.connect):
                        a[1].setParameter("brightness", 40)
            elif data[1] == "8":
                for a in Driver.Drivers:
                    if isinstance(a[1], SensorRelayBoard.Relay):
                        a[1].setParameter("status", (1 if a[1].getParameters()[0][1] == 0 else 0))
            elif data[1] == "9":
                for a in Driver.Drivers:
                    if isinstance(a[1], Lightbulb.connect):
                        a[1].setParameter("brightness", 100)
            elif data[1] == "0":
                for a in Driver.Drivers:
                    if isinstance(a[1], Lightbulb.connect):
                        a[1].setParameter("brightness", 100)
                        a[1].setParameter("temp", 144)

#test.setParameter("temp", 144)

class Timer(threading.Thread):
    def run(self):
        pasthour = -1
        while True:
            hour = datetime.datetime.now().hour
            if hour is 6 and pasthour is not 6:
                print "six am!"
                for a in Driver.Drivers:
                    if isinstance(a[1], SensorRelayBoard.Relay):
                        a[1].setParameter("status", 1)
            if hour is 10 and pasthour is not 10:
                print "ten am!"
                for a in Driver.Drivers:
                    if isinstance(a[1], SensorRelayBoard.Relay):
                        a[1].setParameter("status", 0)
            pasthour = hour
            time.sleep(1)

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
