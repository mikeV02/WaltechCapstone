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
        #self.PN = PortNumber

        #needed to finish the setup
        time.sleep(1)
        #self.ser.write("ready")
       
       
    #gets the state of the arduino        
    def getArduinoState(self):
        #self.ser.write("ready")

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
                
        self.ser.write("ready")
        received = ''

        #self.ser.reset_input_buffer()    #when put together it flushes everything

        received = self.ser.readline()     #but the read size
        #time.sleep(.1)

        if self.HW == "ArduinoNano" or self.HW == "ArduinoUno":
            return received
                
        if self.HW == "ArduinoMega":
            return received
        
# se = SerialCommunicator("/dev/ttyACM0", "ArduinoMega")

# #while 1:#se.ser.inWaiting() > 0:
# #    if (se.getArduinoState() != None):
# while 1:
#     rvd = se.getArduinoState()

#     if (rvd is not None):
#         print "{0:08b}".format(ord(rvd[0])) + "{0:08b}".format(ord(rvd[1])) + "{0:06b}".format(ord(rvd[2]))[0:6]\
#             + "{0:08b}".format(ord(rvd[3]))  + "{0:08b}".format(ord(rvd[4]))  + "{0:08b}".format(ord(rvd[5]))[0:6]
#         #print rvd