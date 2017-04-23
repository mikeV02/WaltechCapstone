

class Counter():
    def __init__(self, name):
        self.name = name
        self.prevInput = 45
        self.currentValue = 0
        self.preset = 0
        self.done = 0
    
    def setLocationType(self, x, y,type):
        self.x = x
        self.y = y
        self.type = type
        
    def setPrevElement(self, x, y, element):
        self.Prevelement = element
        self.Prevx = x
        self.Prevy = y
    
class Timer():
    def __init__(self, name):
        self.name = name
        self.prevInput = 45
        self.currentValue = 0
        self.preset = 0
        self.done = 0
        
    def setLocationType(self, x, y,type):
        self.x = x
        self.y = y
        self.type = type
        
    def setPrevElement(self, x, y, element):
        self.Prevelement = element
        self.Prevx = x
        self.Prevy = y
		
class Internal():
    def __init__(self, name):
        self.name = name
        self.done = 0
        
    def setLocationType(self, x, y,type):
        self.x = x
        self.y = y
        self.type = type
        
    def setDoneBit(self, x, y, name):
        self.Prevname = name
        self.Prevx = x
        self.Prevy = y
		