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
       
       
    #gets the state of the arduino        
    def getArduinoState(self):
        
        self.ser.write("ready")
        received = ""

        self.ser.reset_input_buffer()    #when put together it flushes everything
        received = self.ser.readline()     #but the read size
        
        if self.HW == "ArduinoNano" or self.HW == "ArduinoUno":
            if len(received) == 14:
                return received
                
        if self.HW == "ArduinoMega":
            if len(received) == 46:
                return received
        
        
#se = SerialCommunicator("/dev/ttyACM0", "ArduinoMega")

#while 1:#se.ser.inWaiting() > 0:
#    if (se.getArduinoState() != None):
#        print se.getArduinoState()
