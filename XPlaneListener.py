import struct,socket



class XPlaneListener:
    def __init__(self,xPlaneIP,xPlaneRecievePort,udpBufferSize):
        self.xPlaneIP = xPlaneIP
        self.xPlaneRecievePort = xPlaneRecievePort
        self.udpBufferSize = udpBufferSize
        self.xPlaneMessageList = list()


        """         Frame Rate          """
        self.f_act_sec      = None
        self.f_sim_sec      = None
        self.frame_time     = None
        self.cpu_time       = None
        self.gpu_time       = None
        self.grnd_ratio     = None
        self.flit_ratio     = None
        
        """         Times               """
        self.real_time      = None
        self.totl_time      = None
        self.missn_time     = None
        self.timer_time     = None
        self.zulu_time      = None
        self.local_time     = None
        self.hobbs_time     = None

        """         Sim stats           """
        self.explo_DIM      = None
        self.explo_USE      = None
        self.cratr_DIM      = None
        self.cratr_USE      = None
        self.puffs_TOT      = None
        self.puffs_VIS      = None
        self.tris_vis       = None
        self.q_depth        = None

        """         Speeds              """
        self.Vind_kias      = None
        self.Vind_keas      = None
        self.Vtrue_ktas     = None
        self.Vtrue_ktgs     = None
        self.Vind_mph       = None
        self.Vtrue_mphas    = None
        self.Vtrue_mphgs    = None

        """     mach, VVI, G-load       """
        self.Mach_ratio     = None
        self.VVI_fpm        = None
        self.Gload_norml    = None
        self.Gload_axial    = None
        self.Gload_side     = None

        """     Atmosphere: weather     """
        self.SLprs_inHG     = None
        self.SLtmp_degC     = None
        self.wind_speed     = None
        self.wind_dir       = None
        self.trb_locl       = None
        self.prec_locl      = None
        self.hail_locl      = None

        """     Atmosphere: aircraft    """
        self.AMprs_inHG     = None
        self.AMtmp_degC     = None
        self.LEtmp_degC     = None
        self.dens_ratio     = None
        self.A_ktas         = None
        self.Q_psf          = None
        self.gravi_fts2     = None

        """     System pressures        """
        self.baro_inHG      = None
        self.edens_part     = None
        self.vacum_ratio    = None
        self.elec_ratio     = None
        self.AHRS_ratio     = None

        """     joystick ail/elv/rud    """
        self.elev_yoke1     = None
        self.ailrn_yoke1    = None
        self.ruddr_yoke1    = None

        """     Other flight controls   """
        self.vect_rqst      = None
        self.sweep_rqst     = None
        self.incid_rqst     = None
        self.dihed_rqst     = None
        self.retra_rqst     = None
        self.water_jetts    = None

        """    art stab ail/elv/rud     """
        self.elev_astab     = None
        self.ailrn_astab    = None
        self.ruddr_astab    = None

        """   flight con ail/elv/rud    """
        self.elev_surf      = None
        self.ailrn_surf     = None
        self.ruddr_surf     = None
        self.nwhel_steer    = None

        """     wing sweep/thrust vect  """
        self.sweep_1_deg    = None
        self.sweep_2_deg    = None
        self.sweep_h_deg    = None
        self.vect_ratio     = None
        self.sweep_ratio    = None
        self.incid_ratio    = None
        self.dihed_ratio    = None
        self.retra_ratio    = None

        """     trim/flap/slat/s-brakes """
        self.trim_elev      = None
        self.trim_ailrn     = None
        self.trim_ruddr     = None
        self.flap_handl     = None
        self.flap_postn     = None
        self.slat_ratio     = None
        self.sbrak_handl    = None
        self.sbrak_postn    = None

        """         gear/brakes         """



        self.lat_deg        = None
        self.long_deg       = None
        self.alt_ftmsl      = None
        self.alt_ftagl      = None
        self.on_runwy       = None
        self.alt_ind        = None
        self.lat_south      = None
        self.lon_west       = None





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
        


