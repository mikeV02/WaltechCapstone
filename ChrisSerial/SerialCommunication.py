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

    def __init__(self,PortNumber):
        #setup for serial communication
        self.ser = serial.Serial(
            port=PortNumber,
            baudrate=9600,
            stopbits=1,
            bytesize=serial.EIGHTBITS,
            timeout=1)

        #needed to finish the setup
        time.sleep(2)
       
       
    #gets the state of the arduino        
    def getArduinoState(self):
        
        self.ser.write("ready")

        #if bytes > 44:                  #waits till there is more than 40 bytes
    
        self.ser.reset_input_buffer()        #when put together it flushes everything
        received = self.ser.read(14)    #but the read size

#        received = ''
#        self.ser.reset_input_buffer()    #when put together it flushes everything
        
        return received
        
        
#se = SerialCommunicator("com6")
#
#while 1:#se.ser.inWaiting() > 0:
#    print se.getArduinoState()
