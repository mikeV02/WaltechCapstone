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
        time.sleep(1)
       
       
    #gets the state of the arduino        
    def getArduinoState(self):
        
        #self.ser.write("ready")
        received = ''
        #bytes = self.ser.inWaiting();        #checks how many bytes are in input bufferbytes
        #print "BYYYYTEEEESSSS   ", bytes
        #while self.ser.inWaiting() > 0:
        #    received += self.ser.read(1)
        #    #self.ser.reset_input_buffer()    #when put together it flushes everything
        
        received += self.ser.readline()
        #self.ser.close()
        return received
        
        
se = SerialCommunicator("/dev/ttyACM1")

while 1:
    print se.getArduinoState()
