import serial
import sys
import time

ser = serial.Serial(
            port='com3',
            baudrate=9600,
            stopbits=1,
            bytesize=serial.EIGHTBITS)
            
time.sleep(1)   #needed in order to correctly setup

while True:
    ser.write("ready")

    bytes = ser.inWaiting();        #checks how many bytes are in input buffer
    
    if bytes > 40:                  #waits till there is more than 40 bytes
    
        ser.reset_input_buffer()    #when put together it flushes everything
        received = ser.read(41)     #but the read size
        
        print received , "\n"

    time.sleep(.5)                  #emulate the time I told michael 
                                    #to wait per request 