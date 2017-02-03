import serial

ser = serial.Serial(
            port='com3',
            baudrate=9600,
            stopbits=1,
            bytesize=serial.EIGHTBITS)
            
while True:
    bytesToRead = ser.inWaiting()
    if bytesToRead > 0:
        print ser.read(bytesToRead)