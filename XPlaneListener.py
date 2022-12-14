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
        self.gear_0_1       = None
        self.wbrak_part     = None
        self.lbrak_part     = None
        self.rbrak_part     = None

        """      Angular moments        """
        self.L_ftlb         = None
        self.M_ftlb         = None
        self.N_ftlb         = None
        self.Q_rad_s        = None
        self.P_rad_s        = None
        self.R_rad_s        = None

        """     Pitch, roll, headings   """
        self.pitch_deg      = None
        self.roll_deg       = None
        self.hding_true     = None
        self.hding_mag      = None

        """    AoA, side-slip, paths    """
        self.alpha_deg      = None
        self.beta_deg       = None
        self.hpath_deg      = None
        self.vpath_deg      = None
        self.slip_deg       = None

        """      mag compass            """
        self.mag_comp       = None
        self.mavar_deg      = None

        """     lat, lon, altitude      """
        self.lat_deg        = None
        self.long_deg       = None
        self.alt_ftmsl      = None
        self.alt_ftagl      = None
        self.on_runwy       = None
        self.alt_ind        = None
        self.lat_south      = None
        self.lon_west       = None

        """  loc, vel, dist traveled    """
        self.X_m            = None
        self.Y_m            = None
        self.Z_m            = None
        self.vX_m_s         = None
        self.vY_m_s         = None
        self.vZ_m_s         = None
        self.dist_ft        = None
        self.dist_nm        = None

        """     all planes: lat         """
        self.lat_n_deg      = None

        """     all planes: lon         """
        self.lon_n_deg      = None

        """     all planes: alt         """
        self.alt_n_ftmsl    = None

        """     throttle actual         """
        self.thro_n_part     = None

        """   feather-norm-beta-revers  """
        self.mode_n_0123     = None

        """         prop setting        """
        self.prop_n_set      = None

        """     Mixture setting         """
        self.mixt_n_ratio    = None

        """     carb heat setting       """
        self.heat_n_ratio    = None

        """     Cowl flap setting       """
        self.cowl_n_set      = None

        """     Magneto settings        """
        self.magn_n_set      = None

        """     Starter timeout         """
        self.star_n_sec      = None

        """     Engine power            """
        self.power_n_hp     = None

        """     Engine thrust           """
        self.thrst_n_lb     = None

        """     Engine torque           """
        self.trq_n_ftlb     = None

        """     Engine RPM              """
        self.rpm_n_engin    = None

        """     prop RPM                """
        self.rpm_n_prop     = None

        """     prop pitch              """
        self.ptch_n_deg     = None

        """     propwash/jetwasg        """
        self.pwash_kt       = None

        """         N1                  """
        self.N1_n_pcnt      = None

        """         N2                  """
        self.N2_n_pcnt      = None

        """         MP                  """
        self.MP_n_inhg      = None

        """         EPR                 """
        self.EPR_n_aprt     = None

        """         FF                  """
        self.FF_n_lb_h      = None

        """         ITT                 """
        self.ITT_n_deg      = None

        """         EGT                 """
        self.EGT_n_deg      = None

        """         CHT                 """
        self.CHT_n_deg      = None        

        """       Oil pressure          """
        self.OILP_n_psi     = None        

        """       Oil temp              """
        self.OILT_n_deg     = None 

        """     Fuel pressure           """
        self.FUEP_n_psi     = None

        """     Generator amperage      """
        self.genr_n_amp     = None

        """     Battery amperage        """
        self.batt_n_amp     = None

        """     Battery voltage         """
        self.batt_n_volt    = None

        """     Fuel pump on/off        """
        self.pump_n_0_1     = None

        """     Idle speed lo/hi        """
        self.idle_n_0_1     = None

        """     Battery on/off          """
        self.batt_n_0_1     = None

        """     Generator on/off        """
        self.genr_n_0_1     = None

        """     Inverter on/off         """
        self.invr_n_0_1     = None

        """     FADEC on/off            """
        self.fadec_0_1      = None

        """     Igniter on/off          """
        self.igni_n_0_1     = None

        """     Fuel weights            """
        self.fuel_n_lb      = None

        """     payload weights and CG  """
        self.empty_lb       = None
        self.payld_lb       = None
        self.fuel_totlb     = None
        self.jetti_lb       = None
        self.curnt_lb       = None
        self.maxim_lb       = None
        self.cg_ftref       = None

        """     aero forces             """
        self.lift_lb        = None
        self.drag_lb        = None
        self.side_lb        = None

        """     Engine forces           """
        self.norml_lb       = None
        self.axial_lb       = None
        self.side_lb        = None

        """   landing gear vert force   """
        self.gear_lb        = None

        """     Landing gear deployment """
        self.gear_rat       = None

        """     lift over drag coeffs   """
        self.L_D_ratio      = None
        self.cl_total       = None
        self.cd_total       = None
        self.L_D__etaP      = None

        """     prop efficiency         """
        self.Peff_n_ratio   = None

        """     defs: ailerons          """
        self.Lailn_n_deg    = None
        self.Railn_n_deg    = None

        """     defs: roll spoilers     """
        self.Lsplr_n_deg    = None
        self.Rsplr_n_deg    = None

        """     defs: elevators         """
        self.elev_n_deg     = None

        """     defs: rudders           """
        self.rudr_n_deg     = None

        """     defs: yaw brakes        """
        self.Lyawb_deg      = None 
        self.Ryawb_deg      = None 

        """     Control forces          """
        self.pitch_lb       = None
        self.roll_lb        = None
        self.hdng_lb        = None
        self.l_brk_lb       = None
        self.r_brk_lb       = None

        """  total vert thrust vects    """
        self.vert_n_tvect   = None
        
        """  total lat thrust vects     """
        self.latr_n_tvect   = None        
        
        """  Pitch cyclic disc tilts    """
        self.pitch_cycli    = None   

        """  Roll cyclic disc tilts     """
        self.roll_cycli     = None   

        """  Pitch cyclic flapping      """
        self.pitch_flap     = None   

        """  Roll cyclic flapping       """
        self.roll_flap      = None   

        """   grnd effect lift, wings   """
        self.wing_n_L_cl_   = None
        self.wing_n_R_cl_   = None
        
        """  grnd effect drag, wings    """
        self.wing_n_Lcdi_   = None
        self.wing_n_Rcdi_   = None

        """ grnd effect wash, wings     """
        self.wing_n_wash_   = None

        """ grnd effect lift, stabs     """
        self.hstab_L_cl_    = None
        self.hstab_R_cl_    = None
        self.vstb1_cl_      = None

        """ grnd effect drag, stabs     """
        self.hstab_Lcdi_    = None
        self.hstab_Rcd,_    = None
        self.vstb_n_cdi_    = None

        """ grnd effect wash, stabs     """
        self.hstab_wash_    = None
        self.vstb_n_wash_   = None

        """ grnd effect lift, props     """
        self.prop_n_cl_     = None

        """ grnd effect drag, props     """
        self.prop_n_cdi_    = None

        """         Wing lift           """
        self.wing_n_lift    = None

        """         Wing drag           """
        self.wing_n_drag    = None
        
        """         stab lift           """
        self.hstab_lift     = None
        self.vstb_n_lift    = None
                
        """         stab drag           """
        self.hstab_drag     = None
        self.vstb_n_drag    = None
        
        """     COM 1/2 frequency       """
        self.COM_n_freq     = None
        self.COM_n_stby     = None
        self.COM_xmt        = None
        
        """     NAV 1/2 frequency       """
        self.NAV_n_freq     = None
        self.NAV_n_stby     = None
        self.NAV_n_type     = None
        
        """     NAV 1/2 NAV 1/2 OBS     """
        self.NAV_n_OBS      = None
        self.NAV_n_s_crs    = None
        self.NAV_n_flag     = None
        
        """     NAV n deflections       """
        self.NAV_n_n_typ    = None
        self.NAV_n_to_fr    = None
        self.NAV_n_m_crs    = None
        self.NAV_n_r_brg    = None
        self.NAV_n_dme_d    = None
        self.NAV_n_h_def    = None
        self.NAV_n_v_def    = None
        
        """     ADF 1/2 status          """
        self.ADF_n_freq     = None
        self.ADF_n_card     = None
        self.ADF_n_r_brg    = None
        self.ADF_n_n_typ    = None
        
        """     DME status              """
        self.DME_nav01      = None
        self.DME_mode       = None
        self.DME_found      = None
        self.DME_dist       = None
        self.DME_speed      = None
        self.DME_time       = None
        self.DME_n_type     = None
        self.DME_3_freq     = None
        
        """     GPS status              """
        self.GPS_mode       = None
        self.GPS_index      = None
        self.dist_nm        = None
        self.OBS_mag        = None
        self.crs_mag        = None
        self.rel_brng       = None
        self.hdef_dots      = None
        self.vdef_dots      = None
        
        """     XPNDR status            """
        self.trans_mode     = None
        self.trans_sett     = None
        self.trans_ID       = None
        self.trans_inter    = None
        
        """     Marker status           """
        self.OM_morse       = None
        self.MM_morse       = None
        self.IM_morse       = None
        self.audio_activ    = None
        
        """     Switches 1: electrical  """
        self.avio_0_1       = None
        self.nav_lite       = None
        self.beacn_lite     = None
        self.strob_lite     = None
        self.land_lite      = None
        self.taxi_lite      = None
        
        """     Switches 2: EFIS        """
        self.ECAM_mode      = None
        self.EFIS_sel_n     = None
        self.HSI_sel_n      = None
        self.HSI_arc        = None
        self.map_r_sel      = None
        self.map_range      = None
        
        """  switches 3: AP/f-dir/HUD   """
        self.ap_src         = None              
        self.fdir_mode      = None     
        self.fdir_ptch      = None           
        self.fdir_roll      = None           
        self.HUD_power      = None           
        self.HUD_brite      = None
        
        """ Switches 4: anti-ice        """           
        self.deice_all      = None
        self.deice_inlet    = None
        self.deice_prop     = None
        self.deice_windo    = None
        self.deice_n_pitot  = None
        self.deice_AOA      = None
        self.deice_wing     = None
        
        """ Switches 5: anti-ice/fuel   """
        self.alt_air_n      = None
        self.auto_ignit     = None
        self.manul_ignit    = None
        self.l_eng_tank     = None
        self.r_eng_tank     = None
        
        """ switches 6: clutch/astab    """
        self.prero_engag    = None
        self.clutc_ratio    = None
        self.art_ptch       = None
        self.art_roll       = None
        self.yaw_damp       = None
        self.auto_brake     = None
        
        """     switches 7: misc        """
        self.tot_energ      = None
        self.radal_feet     = None
        self.prop_sync      = None
        self.fethr_mode     = None
        self.puffr_power    = None
        self.water_scoop    = None
        self.arrst_hook     = None
        self.chute_deply    = None
        
        """     Annunciators: general   """
        self.mast_cau       = None
        self.mast_war       = None
        self.mast_accp      = None
        self.auto_disco     = None
        self.low_vacum      = None
        self.low_volt       = None
        self.fuel_quant     = None
        self.hyd_press      = None    
        
        """     Annunciators: general   """
        self.yawda_on       = None  
        self.sbrk_on        = None  
        self.GPWS_warn      = None  
        self.ice_warn       = None  
        self.pitot_off      = None  
        self.cabin_althi    = None  
        self.afthr_arm      = None
        self.ospd_time      = None
        
        """     Annunciators: engine    """
        self.fuel_press     = None
        self.oil_press      = None
        self.oil_temp       = None
        self.inver_warn     = None
        self.gener_warn     = None
        self.chip_detec     = None
        self.engin_fire     = None
        self.ignit_0_1      = None
        
        """     autopilot arms          """
        self.nav_arm        = None
        self.alt_arm        = None
        self.app_arm        = None
        self.vnav_enab      = None
        self.vnav_arm       = None
        self.vnav_time      = None
        self.gp_enabl       = None
        self.app_typ        = None
        
        """     autopilot modes         """
        self.auto_throt     = None
        self.mode_hding     = None
        self.mode_alt       = None
        self.bac_0_1        = None
        self.app_           = None
        self.sync_butn      = None
        
        """     Autopilot values        """
        self.set_speed      = None
        self.set_hding      = None
        self.set_vvi        = None
        self.dial_alt       = None
        self.vnav_alt       = None
        self.use_alt        = None
        self.sync_roll      = None
        self.sync_pitch     = None
        
        """     Weapon status           """
        self.hdng_delta     = None
        self.pitch_delta    = None
        self.R_d_sec        = None
        self.Q_d_sec        = None
        self.rudd_ratio     = None
        self.elev_ratio     = None
        self.V_kts          = None
        self.dist_ft        = None
        
        """ Pressurization status       """
        self.alt_set        = None
        self.vvi_set        = None
        self.alt_act        = None
        self.vvi_act        = None
        self.test_time      = None
        self.diff_psi       = None
        self.dump_all       = None
        self.bleed_src      = None
        
        """     APU/GPU status          """
        self.APU_eqipd      = None
        self.APU_swtch      = None
        self.APU_runng      = None
        self.APU_N1         = None
        self.APU_genrt      = None
        self.GPU_power      = None
        
        """         Radar status        """
        self.targ_selct     = None
        
        """     Hydraulic status        """
        self.hydr_pump_n    = None
        self.hydr_qty_n     = None
        self.hydr_pres_n    = None
        
        """     elec & solar status     """
        self.bus_n_amp      = None
        self.bus_n_volt     = None
        self.engin_in_W     = None
        self.solar_out_W    = None
        self.batt_w_hr      = None
        self.Cross_tie      = None
        
        """     Icing status 1          """
        self.inlet_ice      = None
        self.prop_ice       = None
        self.pitot_ice      = None
        self.statc_ice      = None
        
        """     Icing status 1          """
        self.aoa_ice        = None
        self.lwing_ice      = None
        self.rwing_ice      = None
        self.windo_ice      = None
        
        """     Warning status          """
        self.warn_time      = None
        self.caut_time      = None
        self.warn_work      = None
        self.caut_work      = None
        self.gear_work      = None
        self.gear_warn      = None
        self.stall_warn     = None
        self.VRS_ratio      = None
        
        """     flite-plan legs         """
        self.leg__          = None
        self.leg_type       = None
        self.leg_lat        = None
        self.leg_lon        = None
        
        """     Hardware options        """
        self.pedal_nobrk    = None
        self.pedal_wibrk    = None
        self.yoke_PFC       = None
        self.pedal_PFC      = None
        self.throt_PFC      = None
        self.cecon_PFC      = None
        self.switc_PFC      = None
        self.btogg_PFC      = None
        
        """     Camera location         """
        self.camra_lon      = None
        self.camra_lat      = None
        self.camra_ele      = None
        self.camra_hdg      = None
        self.camra_pitch    = None
        self.camra_roll     = None
        self.camra_clou     = None
        
        """     Ground location         """
        self.cntr_X         = None
        self.cntr_Y         = None
        self.cntr_Z         = None
        self.slope_X        = None
        self.slope_Z        = None
        
        """     climb stats             """
        self.h_spd_kt       = None
        self.v_spd_fpm      = None
        self.mult_VxVVI     = None
        
        """     cruise stats            """
        self.ff_pph         = None
        self.ff_gph         = None
        self.speed_mph      = None
        self.eta_smpg       = None
        self.eta_nm_lb      = None
        self.range_sm       = None
        self.endur_hours    = None
        self.mult_VxMPG     = None
        
        
        


    def startListener(self):
        """
        Start UDP Listener for X-Plane

        Returns:
            _type_: socket
        """
        xPlaneSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)  # Create a datagram socket
        xPlaneSocket.bind((self.xPlaneIP, self.xPlaneRecievePort))  # Bind to address and ip        
        print("UDP server up and listening...")
        return xPlaneSocket


        
    def readMessage(self,message):
        """
        | DATA* | 4 Byte Message Index | 8 x 4 Byte Message |

        Args:
            message (_type_): UDP Data from X-Plane

        Returns:
            _type_: list
        """
        message = message[5:]                               # Remove "DATA*" prefix from message
        messageLength = 36                                  # 4 Byte Data Index + 8 x (4 Byte Data)        
        messageCount = len(message)//messageLength          # Devide and cast to int
        xPlaneMessage = list()                              # Create empty list
        
        for row in range(messageCount):
            params = list()
            packet=message[row*messageLength:row*messageLength+messageLength]               
            dataIndex = struct.unpack("i",packet[0:4])[0]   # 4 Data Index's Length
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
            if xPlaneMessageIndex == 1:
                self.__setFrameRate(xPlaneMessage)
            elif xPlaneMessageIndex == 2:
                self.__setTimes(xPlaneMessage)
            elif xPlaneMessageIndex == 3:
                self.__setSimStats(xPlaneMessage)
            
            
  
    def __setFrameRate(self,msg):
        """ Private Method. """
        self.f_act_sec  = msg[1]
        self.f_sim_sec  = msg[2]
        self.frame_time = msg[3]
        self.cpu_time   = msg[4]
        self.gpu_time   = msg[5]
        self.grnd_ratio = msg[6]
        self.flit_ratio = msg[7]
        
    def __setTimes(self,msg):
        """ Private Method. """
        self.real_time  = msg[1]
        self.totl_time  = msg[2]
        self.missn_time = msg[3]
        self.timer_time = msg[4]
        self.zulu_time  = msg[5]
        self.local_time = msg[6]
        self.hobbs_time = msg[7]
        
    def __setSimStats(self,msg):
        """ Private Method. """
        self.explo_DIM  = msg[1]
        self.explo_USE  = msg[2]
        self.cratr_DIM  = msg[3]
        self.cratr_USE  = msg[4]
        self.puffs_TOT  = msg[5]
        self.puffs_VIS  = msg[6]
        self.tris_vis   = msg[7]
        self.tris_vis   = msg[8]
        
    def __setSpeeds(self,msg):
        """ Private Method. """
        self.Vind_kias   = msg[1]
        self.Vind_keas   = msg[2]
        self.Vtrue_ktas  = msg[3]
        self.Vtrue_ktgs  = msg[4]
        self.Vind_mph    = msg[5]
        self.Vtrue_mphas = msg[6]
        self.Vtrue_mphgs = msg[7]
        
    def __setMachVVIGload(self,msg):
        """ Private Method. """
        self.Mach_ratio   = msg[1]
        self.VVI_fpm      = msg[2]
        self.Gload_norml  = msg[3]
        self.Gload_axial  = msg[4]
        self.Gload_side   = msg[5]
        
    def __setAtmosphereWeather(self,msg):
        """ Private Method. """
        self.SLprs_inHG = msg[1]
        self.SLtmp_degC = msg[2]
        self.wind_speed = msg[3]
        self.wind_dir   = msg[4]
        self.trb_locl   = msg[5]
        self.prec_locl  = msg[6]
        self.hail_locl  = msg[7]
        
    def __setAtmosphereAircraft(self,msg):
        """ Private Method. """
        self.AMprs_inHG = msg[1]
        self.AMtmp_degC = msg[2]
        self.LEtmp_degC = msg[3]
        self.dens_ratio = msg[4]
        self.A_ktas     = msg[5]
        self.Q_psf      = msg[6]
        self.gravi_fts2 = msg[7]
    
    def __setSystemPressures(self,msg):
        self.baro_inHG   = msg[1]
        self.edens_part  = msg[2]
        self.vacum_ratio = msg[3]
        self.elec_ratio  = msg[4]
        self.AHRS_ratio  = msg[5]
        
    def __setJoystickAilElvRud(self,msg):
        self.elev_yoke1   = msg[1]
        self.ailrn_yoke1  = msg[2]
        self.ruddr_yoke1  = msg[3]    
        
    
    
    def __set_frame_rate(self,msg):pass
    def __set_times(self,msg):pass
    def __set_sim_stats(self,msg):pass
    def __set_speeds(self,msg):pass
    def __set_mach_vvi_g_load(self,msg):pass
    def __set_atmosphere_weather(self,msg):pass
    def __set_atmosphere_aircraft(self,msg):pass
    def __set_system_pressures(self,msg):pass
    def __set_joystick_ail_elv_rud(self,msg):pass
    def __set_other_flight_controls(self,msg):pass
    def __set_art_stab_ail_elv_rud(self,msg):pass
    def __set_flight_con_ail_elv_rud(self,msg):pass
    def __set_wing_sweep_thrust_vect(self,msg):pass
    def __set_trim_flap_slat_s_brakes(self,msg):pass
    def __set_gear_brakes(self,msg):pass
    def __set_angular_moments(self,msg):pass
    def __set_pitch_roll_headings(self,msg):pass
    def __set_aoa_side_slip_paths(self,msg):pass
    def __set_mag_compass(self,msg):pass
    def __set_lat_lon_altitude(self,msg):pass
    def __set_loc_vel_dist_traveled(self,msg):pass
    def __set_all_planes_lat(self,msg):pass
    def __set_all_planes_lon(self,msg):pass
    def __set_all_planes_alt(self,msg):pass
    def __set_throttle_command(self,msg):pass
    def __set_throttle_actual(self,msg):pass
    def __set_feather_norm_beta_revers(self,msg):pass
    def __set_prop_setting(self,msg):pass
    def __set_mixture_setting(self,msg):pass
    def __set_carb_heat_setting(self,msg):pass
    def __set_cowl_flap_setting(self,msg):pass
    def __set_magneto_settings(self,msg):pass
    def __set_starter_timeout(self,msg):pass
    def __set_engine_power(self,msg):pass
    def __set_engine_thrust(self,msg):pass
    def __set_engine_torque(self,msg):pass
    def __set_engine_rpm(self,msg):pass
    def __set_prop_rpm(self,msg):pass
    def __set_prop_pitch(self,msg):pass
    def __set_propwash_jetwash(self,msg):pass
    def __set_n1(self,msg):pass
    def __set_n2(self,msg):pass
    def __set_mp(self,msg):pass
    def __set_epr(self,msg):pass
    def __set_ff(self,msg):pass
    def __set_itt(self,msg):pass
    def __set_egt(self,msg):pass
    def __set_cht(self,msg):pass
    def __set_oil_pressure(self,msg):pass
    def __set_oil_temp(self,msg):pass
    def __set_fuel_pressure(self,msg):pass
    def __set_generator_amperage(self,msg):pass
    def __set_battery_amperage(self,msg):pass
    def __set_battery_voltage(self,msg):pass
    def __set_fuel_pump_on_off(self,msg):pass
    def __set_idle_speed_lo_hi(self,msg):pass
    def __set_battery_on_off(self,msg):pass
    def __set_generator_on_off(self,msg):pass
    def __set_inverter_on_off(self,msg):pass
    def __set_fadec_on_off(self,msg):pass
    def __set_igniter_on_off(self,msg):pass
    def __set_fuel_weights(self,msg):pass
    def __set_payload_weights_and_cg(self,msg):pass
    def __set_aero_forces(self,msg):pass
    def __set_engine_forces(self,msg):pass
    def __set_landing_gear_vert_force(self,msg):pass
    def __set_landing_gear_deployment(self,msg):pass
    def __set_lift_over_drag_coeffs(self,msg):pass
    def __set_prop_efficiency(self,msg):pass
    def __set_defs_ailerons(self,msg):pass
    def __set_defs_roll_spoilers(self,msg):pass
    def __set_defs_elevators(self,msg):pass
    def __set_defs_rudders(self,msg):pass
    def __set_defs_yaw_brakes(self,msg):pass
    def __set_control_forces(self,msg):pass
    def __set_total_vert_thrust_vects(self,msg):pass
    def __set_total_lat_thrust_vects(self,msg):pass
    def __set_pitch_cyclic_disc_tilts(self,msg):pass
    def __set_roll_cyclic_disc_tilts(self,msg):pass
    def __set_pitch_cyclic_flapping(self,msg):pass
    def __set_roll_cyclic_flapping(self,msg):pass
    def __set_grnd_effect_lift_wings(self,msg):pass
    def __set_grnd_effect_drag_wings(self,msg):pass
    def __set_grnd_effect_wash_wings(self,msg):pass
    def __set_grnd_effect_lift_stabs(self,msg):pass
    def __set_grnd_effect_drag_stabs(self,msg):pass
    def __set_grnd_effect_wash_stabs(self,msg):pass
    def __set_grnd_effect_lift_props(self,msg):pass
    def __set_grnd_effect_drag_props(self,msg):pass
    def __set_wing_lift(self,msg):pass
    def __set_wing_drag(self,msg):pass
    def __set_stab_lift(self,msg):pass
    def __set_stab_drag(self,msg):pass
    def __set_com_1_2_frequency(self,msg):pass
    def __set_nav_1_2_frequency(self,msg):pass
    def __set_nav_1_2_obs(self,msg):pass
    def __set_adf_1_2_status(self,msg):pass
    def __set_dme_status(self,msg):pass
    def __set_gps_status(self,msg):pass
    def __set_xpndr_status(self,msg):pass
    def __set_marker_status(self,msg):pass
    def __set_switches_1_electrical(self,msg):pass
    def __set_switches_2_efis(self,msg):pass
    def __set_switches_3_ap_f_dir_hud(self,msg):pass
    def __set_switches_4_anti_ice(self,msg):pass
    def __set_switches_5_anti_ice_fuel(self,msg):pass
    def __set_switches_6_clutch_astab(self,msg):pass
    def __set_switches_7_misc(self,msg):pass
    def __set_annunciators_general(self,msg):pass
    def __set_annunciators_general(self,msg):pass
    def __set_annunciators_engine(self,msg):pass
    def __set_autopilot_arms(self,msg):pass
    def __set_autopilot_modes(self,msg):pass
    def __set_autopilot_values(self,msg):pass
    def __set_weapon_status(self,msg):pass
    def __set_pressurization_status(self,msg):pass
    def __set_apu_gpu_status(self,msg):pass
    def __set_radar_status(self,msg):pass
    def __set_hydraulic_status(self,msg):pass
    def __set_elec_amp_solar_status(self,msg):pass
    def __set_icing_status_1(self,msg):pass
    def __set_icing_status_2(self,msg):pass
    def __set_warning_status(self,msg):pass
    def __set_flite_plan_legs(self,msg):pass
    def __set_hardware_options(self,msg):pass
    def __set_camera_location(self,msg):pass
    def __set_ground_location(self,msg):pass
    def __set_climb_stats(self,msg):pass
    def __set_cruise_stats(self,msg):pass