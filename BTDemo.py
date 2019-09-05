import bluetooth

sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
sock.connect(("00:0E:EA:CF:58:B8", 1))

def readline(sock):
    s = ""
    data = ""
    while(data != '\n'):
        data = sock.recv(1).decode()
        s += data
    return s

while(True):
    s = readline(sock)
    print(float(s))