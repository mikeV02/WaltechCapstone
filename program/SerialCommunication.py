import serial
import sys
import time
import tester
import datetime
import time
import subprocess

from subprocess import PIPE
#purpose of this class is to Communicate with the Arduino serially 

class SerialCommunicator():

    def __init__(self,PortNumber, HW):
        #setup for serial communication
        self.ser = serial.Serial(
            port=PortNumber,
            baudrate=9600,
            stopbits=1,
            bytesize=serial.EIGHTBITS,
            timeout=1)
            
        self.HW = HW

        #needed to finish the setup
        time.sleep(1)
        #self.ser.write("ready")
       
       
    #gets the state of the arduino        
    def getArduinoState(self):
        self.ser.write("ready")

        # global last_received
        # buffer_string = ''

        # buffer_string = buffer_string + self.ser.read(self.ser.inWaiting())
        # if '\n' in buffer_string:
        #     lines = buffer_string.split('\n') # Guaranteed to have at least 2 entries
        #     last_received = lines[-2]
        #     #If the Arduino sends lots of empty lines, you'll lose the
        #     #last filled line, so you could make the above statement conditional
        #     #like so: if lines[-2]: last_received = lines[-2]
        #     buffer_string = lines[-1]

        #     return last_received
                
        #self.ser.write("ready")
        received = ""

        self.ser.reset_input_buffer()    #when put together it flushes everything
        received = self.ser.readline()     #but the read size
        
        if self.HW == "ArduinoNano" or self.HW == "ArduinoUno":
            if len(received) == 14:
                return received
                
        if self.HW == "ArduinoMega":
            if len(received) == 46:
                return received
        
#se = SerialCommunicator("/dev/ttyACM1", "ArduinoMega", fdk)

#while 1:#se.ser.inWaiting() > 0:
#    if (se.getArduinoState() != None):
#se.getArduinoState()
