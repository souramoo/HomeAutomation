from Queue import Queue
import threading
import time

Sensors = []
EventHandlers = []

EventQueue = Queue()

class Sensor:
    def __init__(self):
        Sensors.append(self)
    def run(self):
        return
    def read(self):
        return ""

class EventHandler:
    def __init__(self):
        EventHandlers.append(self)
    def handle(event):
        return

class EventProcessor(threading.Thread):
    def run(self):
        while True:
            item = EventQueue.get()
            for h in EventHandlers:
                h.handle(item)
            EventQueue.task_done()
            time.sleep(0.5)

class SensorProcessor(threading.Thread):
    def run(self):
        while True:
            for s in Sensors:
                s.run()
            time.sleep(0.5)

EventProcessor().start()
SensorProcessor().start()
