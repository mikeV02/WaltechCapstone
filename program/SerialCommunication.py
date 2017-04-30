import serial
import sys
import time
import tester
import datetime
import time
import subprocess

from subprocess import PIPE
#purpose of this class is to Communicate with the Arduino serially


''' ORIGINALLY CREATED BY CHRIS, THIS FUNCTION USES THE serial LIBRARY GIVEN BY PySerial TO GET THE INFORMATION
    SENT BY THE ARDUINO. MIGUEL MODIFIED THE CODE TO USE THE SERIAL FUNCTION readline() TO HAVE AN ACCURATE
    VALUE RECEIVED, AS THE BUFFER TENDED TO FLUCTUATE.
'''
# MIGUEL 32

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
                
        self.ser.write("ready") #ALWAS SENT TO THE ARDUINO TO KEEP IT AWAKE
        received = ''

        received = self.ser.readline()

        if self.HW == "ArduinoNano" or self.HW == "ArduinoUno":
            return received
                
        if self.HW == "ArduinoMega":
            return received

''' CODE TO THEST THE MODULE INDIVIDUALLY '''        
# se = SerialCommunicator("/dev/ttyACM0", "ArduinoMega")

# #while 1:#se.ser.inWaiting() > 0:
# #    if (se.getArduinoState() != None):
# while 1:
#     rvd = se.getArduinoState()

#     if (rvd is not None):
#         print "{0:08b}".format(ord(rvd[0])) + "{0:08b}".format(ord(rvd[1])) + "{0:06b}".format(ord(rvd[2]))[0:6]\
#             + "{0:08b}".format(ord(rvd[3]))  + "{0:08b}".format(ord(rvd[4]))  + "{0:08b}".format(ord(rvd[5]))[0:6]
#         #print rvd