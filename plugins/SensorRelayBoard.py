import Sensor
from Driver import Driver
import Lightbulb
import serial
import threading
import subprocess
import sys, string
import os.path
import pickle

class SensorRelayBoard(object):
    def __init__(self, port):
        self.ser = serial.Serial(port, 9600)
        self.ser.open()
        SensorReader(self.ser).start()

class SensorReader(threading.Thread):
    def __init__(self, ser):
        threading.Thread.__init__(self)
        self.ser = ser

    def run(self):
        while True:
            data = self.ser.readline().strip()
            if not data.startswith("S:"):
                Sensor.EventQueue.put(["sensorsboard", data])


class Relay(Driver):
    def __init__(self, id, num, ser):
        Driver.__init__(self, id)
        self.ser = ser
        self.num = num

        if os.path.isfile("persist/"+str(self.id)):
            f = open("persist/"+str(self.id), "rb")
            self.setParameters(pickle.load(f))
            f.close()
        else: 
            self.status = 0
            self.setStatus(self.status)

    def getStatus(self):
        return self.status

    def setStatus(self, status):
        self.status = status
        if status == 0:
            self.ser.write("n"+str(self.num)+"\r\n")
        else:
            self.ser.write("y"+str(self.num)+"\r\n")
        Sensor.EventQueue.put(["relay", self.id, self.num, self.status])

    def getParameters(self):
        # [[name, value, conditional on other objectid
        return [ ["status", self.status, [], "switch"] ]

    def setParameter(self, param, value):
        if param == "status":
            self.setStatus(int(value))
        f = open( "persist/"+str(self.id), "wb" )
        pickle.dump(self.getParameters(), f)
        f.close()

    def setParameters(self, list):
        for a in list:
            self.setParameter(a[0], a[1])
