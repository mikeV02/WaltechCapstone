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

    def __init__(self):
        #setup for serial communication
        self.ser = serial.Serial(
            port="com4",
            baudrate=9600,
            stopbits=1,
            bytesize=serial.EIGHTBITS)
            
        #needed to finish the setup
        time.sleep(1)
       
       
    #gets the state of the arduino        
    def getArduinoState(self):
        
        self.ser.write("ready")
        
        bytes = self.ser.inWaiting();        #checks how many bytes are in input buffer
        
        while bytes < 13:                    #waits till there is more than 12 bytes
            
            self.ser.reset_input_buffer()    #when put together it flushes everything
            received = self.ser.read(13)     #but the read size
            
            return received
            
    def findPort(self):
        plat = sys.platform.lower();
        
        
        USBserialPort = None
        
        for i in range(9):
            
            maybePort = "com"+str(i)    
            commandAvrDude = r"..\\WinAVR\\bin\\avrdude.exe -p m328p -P " + maybePort + " -c arduino"
            start = datetime.datetime.now()
            process = subprocess.Popen(commandAvrDude,stdout = subprocess.PIPE, stderr= subprocess.PIPE,shell=True)
            working = False
            while process.poll() is None:
                time.sleep(0.1)
                now = datetime.datetime.now()
                if (now - start).seconds > 2 and working == False:
                    displayOutputPlace.append("Working...")
                    working = True
                    QApplication.processEvents()#this makes the UI update before going on.
                if (now - start).seconds > 10:
                    subprocess.call(['taskkill', '/F', '/T', '/PID', str(process.pid)])
                    #os.kill(process.pid, signal.SIGKILL) #use SIGKILL for not windows
                    #os.waitpid(-1, os.WNOHANG)              #use WHOHANG for not windows
                    print "timed out"
                    output = process.stdout.read()
                    error = process.stderr.read()
                    print "error:", error
                    print "output", output
                    if "timeout" in error:
                        USBserialPort = "timeout"
            output = process.stdout.read()
            error = process.stderr.read()
            if "avrdude.exe: AVR device initialized and ready to accept instructions" in error:
                USBserialPort = maybePort
                print" this is the port:",  USBserialPort
        if USBserialPort == None: 
            print "port greater than 9"
            return None
        else: 
            commandAvrDude = r"..\\WinAVR\\bin\\avrdude.exe -p m328p -P " + USBserialPort + " -c wiring"
            return commandAvrDude  
        
        
        
        print "hello",USBserialPort
        
        
se = SerialCommunicator()


print se.findPort();