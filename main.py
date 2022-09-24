import socket,struct
from XPlaneListener import XPlaneListener
localIP     = "127.0.0.1"
localPort   = 49041
bufferSize  = 4096

 
 

XPlaneListener = XPlaneListener("127.0.0.1",49041,4096)
xPlaneSocket = XPlaneListener.startListener()

while(True):

    bytesAddressPair = xPlaneSocket.recvfrom(bufferSize)
    message = bytesAddressPair[0]
    address = bytesAddressPair[1]         
    XPlaneListener.readMessage(message)
    XPlaneListener.temp()
    clientIP  = "Client IP Address:{}".format(address)

    

    