import Sensor
import Driver
import Lightbulb
import serial
import threading

class RotaryDial(object):
    def __init__(self, port):
        self.ser = serial.Serial(port, 9600)
#        self.ser.open()
        RotaryReader(self.ser).start()

class RotaryReader(threading.Thread):
    def __init__(self, ser):
        threading.Thread.__init__(self)
        self.ser = ser

    def run(self):
        while True:
            data = self.ser.readline().strip()
#            print(data)
            if not data.startswith("S:"):
                Sensor.EventQueue.put(["rotary", data])
