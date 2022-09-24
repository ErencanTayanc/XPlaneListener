import struct,socket

class XPlaneListener:
    def __init__(self,xPlaneIP,xPlaneRecievePort,udpBufferSize):
        self.xPlaneIP = xPlaneIP
        self.xPlaneRecievePort = xPlaneRecievePort
        self.udpBufferSize = udpBufferSize
        self.xPlaneMessageList = list()

    def startListener(self):
        xPlaneSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)  # Create a datagram socket
        xPlaneSocket.bind((self.xPlaneIP, self.xPlaneRecievePort))  # Bind to address and ip        
        print("UDP server up and listening")
        return xPlaneSocket


        
    def readMessage(self,message):
        message = message[5:]   # Remove "DATA*" prefix from message
        
        messageCount = len(message)//36     # Devide and cast to int
        xPlaneMessage = list()              # Create empty list
        
        for row in range(messageCount):
            params = list()
            packet=message[row*36:row*36+36]
            dataIndex = struct.unpack("i",packet[0:4])[0]
            params.append(dataIndex)
            packet = packet[4:]
            for col in range(8):
                params.append(struct.unpack("f",packet[col*4:(col*4)+4])[0])            
            xPlaneMessage.append(params)
        self.xPlaneMessageList = xPlaneMessage
        return (xPlaneMessage)


    def temp(self):
        for xPlaneMessage in self.xPlaneMessageList:
            print(xPlaneMessage[0])
        



dataIndex =	{
  0: 	"Frame Rate",
  1: 	"Times",
  2: 	"Sim stats",
  3: 	"Speeds",
  4: 	"Mach,VVI,g-load",
  5: 	"Weather",
  6: 	"Aircraft atmosphere",
  7: 	"System pressures",
  8: 	"Joystick aileron/elevator/rudder",
  9: 	"Other flight controls",
  10: 	"Artificial Stability aileron/elevator/rudder",
  11: 	"Flight controls aileron/elevator/rudder",
  12: 	"Wing sweep & thrust vectoring",
  13:   "Trim,flap,stats, & speedbreaks",
  14:   "Gear & brakes"
}
