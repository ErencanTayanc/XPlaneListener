from asyncio.windows_events import NULL
import struct,socket

from sqlalchemy import null

class XPlaneListener:
    def __init__(self,xPlaneIP,xPlaneRecievePort,udpBufferSize):
        self.xPlaneIP = xPlaneIP
        self.xPlaneRecievePort = xPlaneRecievePort
        self.udpBufferSize = udpBufferSize
        self.xPlaneMessageList = list()


        """         Frame Rate          """
        self.f_act_sec      = null
        self.f_sim_sec      = null
        self.frame_time     = null
        self.cpu_time       = null
        self.gpu_time       = null
        self.grnd_ratio     = null
        self.flit_ratio     = null
        
        """         Times               """
        self.real_time      = null
        self.totl_time      = null
        self.missn_time     = null
        self.timer_time     = null
        self.zulu_time      = null
        self.local_time     = null
        self.hobbs_time     = null

        """         Sim stats           """
        self.explo_DIM      = null
        self.explo_USE      = null
        self.cratr_DIM      = null
        self.cratr_USE      = null
        self.puffs_TOT      = null
        self.puffs_VIS      = null
        self.tris_vis       = null
        self.q_depth        = null

        """         Speeds              """
        self.Vind_kias      = null
        self.Vind_keas      = null
        self.Vtrue_ktas     = null
        self.Vtrue_ktgs     = null
        self.Vind_mph       = null
        self.Vtrue_mphas    = null
        self.Vtrue_mphgs    = null





        self.lat_deg        = null
        self.long_deg       = null
        self.alt_ftmsl      = null
        self.alt_ftagl      = null
        self.on_runwy       = null
        self.alt_ind        = null
        self.lat_south      = null
        self.lon_west       = null





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
            xPlaneMessageIndex = xPlaneMessage[0]
            if xPlaneMessageIndex == 20:           
                self.lat_deg = (xPlaneMessage[1])
                self.long_deg = (xPlaneMessage[2])
        


