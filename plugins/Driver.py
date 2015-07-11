Drivers = []

class Driver(object):
    def __init__(self, id):
        self.id = id
        Drivers.append([id, self])
    def getParameters(self):
        return []
    def setParameters(self, param, value):
        return
