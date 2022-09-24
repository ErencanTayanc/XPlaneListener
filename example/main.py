from XPlaneListener import XPlaneListener


XPlaneListener = XPlaneListener("127.0.0.1",49041,4096)
xPlaneSocket = XPlaneListener.startListener()

while(True):

    bytesAddressPair = xPlaneSocket.recvfrom(4096)
    message = bytesAddressPair[0]
    address = bytesAddressPair[1]         
    XPlaneListener.readMessage(message)
    XPlaneListener.temp()
    clientIP  = "Client IP Address:{}".format(address)


