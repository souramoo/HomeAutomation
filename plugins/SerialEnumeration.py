import glob
import serial
import threading

Arduinos = []
processing = []

class testDevice(threading.Thread):
    def __init__(self, file):
        threading.Thread.__init__(self)
        self.f = file
    def run(self):
        print("   -> Asking %s..." % self.f)
        ser = serial.Serial(self.f)
        #ser.open()
        #ser.isOpen()

        serid = ser.readline()
        if serid.startswith("S:"):
            Arduinos.append([self.f, serid[2:].strip()])

        ser.close()
        processing.remove(self.f)

def init():
    for f in glob.glob("/dev/ttyUSB*"):
        processing.append(f)
        testDevice(f).start()

def find(name):
    for a in Arduinos:
        if a[1] == name:
            return a[0]
    raise Exception("No "+name+" arduino device found")

print(" * Enumerating serial interfaces...")
init()
while len(processing) > 0:
    pass
print(" * Serial ports enumerated!")

if __name__ == "__main__":
    for a in Arduinos:
        print a
