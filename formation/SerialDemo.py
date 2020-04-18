import serial

sock = serial.Serial("COM5")
while(True):
    s = sock.readline()
    print(s)