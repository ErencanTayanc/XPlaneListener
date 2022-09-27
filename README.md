# X-Plane Connect



This research tool has been used to visualize flight paths, test control algorithms, simulate an active airspace, or generate out-the-window visuals for in-house flight simulation software. Possible applications include active control of an XPlane simulation, flight visualization, recording states during a flight, or interacting with a mission over UDP.
'''python
All special chars like [Space][*italic chars*][,][/][*][-][#] etc. change with [_] char. For example:

L/D, ratio          =>  L_D_ratio<br>
L/D, *etaP          =>  L_D__etaP<br>
wing*n*, L cl*      =>  wing_n_L_cl_<br>
'''


## For more information
[X-Plane Data Set Output Table Official Website](https://www.x-plane.com/kb/data-set-output-table/)

<details>
<summary>Click to see X-Plane Data Set Output Table</summary>

<table border="1">
            <colgroup>
            <col style="text-align: center;">
            <col style="text-align: left;"> </colgroup>
            <thead>
            <tr>
            <th style="text-align: center;">Field label</th>
            <th style="text-align: left;">Descriptions of fields available in X‑Plane 10/11/12’s data output</th>
            <th style="text-align: left;">Parameter Name in Library</th>
            </tr>
            </thead>
            <tbody>
            <tr>
            <td style="text-align: center;" colspan="3"><code>Frame rate</code></td>
            </tr>
            <tr>
            <td style="text-align: center;">f-act, /sec</td>
            <td style="text-align: left;">The actual frame rate being displayed by X-Plane. Unless your computer is bogged down, this will be the same as f-sim.</td>
            <td style="text-align: left;">f_act_sec</td>
            </tr>
            <tr>
            <td style="text-align: center;">f-sim, /sec</td>
            <td style="text-align: left;">The frame rate the simulator is “pretending” to have in order to keep the flight model from failing.</td>
            <td style="text-align: left;">f_sim_sec</td>
            </tr>
            <tr>
            <td style="text-align: center;">frame, time</td>
            <td style="text-align: left;">The time required to render one frame, in seconds.</td>
            <td style="text-align: left;">frame_time</td>
            </tr>
            <tr>
            <td style="text-align: center;">cpu, time</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">cpu_time</td>
            </tr>
            <tr>
            <td style="text-align: center;">gpu, time</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">gpu_time</td>
            </tr>
            <tr>
            <td style="text-align: center;">grnd, ratio</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">grnd_ratio</td>
            </tr>
            <tr>
            <td style="text-align: center;">flit, ratio</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">flit_ratio</td>
            </tr>
            <tr>
            <td style="text-align: center;" colspan="3"><code>Times</code></td>
            </tr>
            <tr>
            <td style="text-align: center;">real, time</td>
            <td style="text-align: left;">The number of seconds, in the real world, elapsed since the simulator was launched.</td>
            <td style="text-align: left;">real_time</td>
            </tr>
            <tr>
            <td style="text-align: center;">totl, time</td>
            <td style="text-align: left;">The number of seconds elapsed since the simulator was launched <em>minus</em> time spent in a loading screen.</td>
            <td style="text-align: left;">totl_time</td>
            </tr>
            <tr>
            <td style="text-align: center;">missn, time</td>
            <td style="text-align: left;">The time since the start of the “mission” (generally the time since the last time an aircraft or location was loaded).</td>
            <td style="text-align: left;">missn_time</td>
            </tr>
            <tr>
            <td style="text-align: center;">timer, time</td>
            <td style="text-align: left;">The time elapsed on a timer for general use.</td>
            <td style="text-align: left;">timer_time</td>
            </tr>
            <tr>
            <td style="text-align: center;">zulu, time</td>
            <td style="text-align: left;">“Zulu” time (Greenwich Mean Time, or GMT) in the simulator, in decimal hours (e.g., 3.5 for 3:30 a.m.).</td>
            <td style="text-align: left;">zulu_time</td>
            </tr>
            <tr>
            <td style="text-align: center;">local, time</td>
            <td style="text-align: left;">Local time in the simulator, in decimal hours.</td>
            <td style="text-align: left;">local_time</td>
            </tr>
            <tr>
            <td style="text-align: center;">hobbs, time</td>
            <td style="text-align: left;">The aircraft’s Hobbs time (a measurement of how long the aircraft’s systems have been run).</td>
            <td style="text-align: left;">hobbs_time</td>
            </tr>
            <tr>
            <td style="text-align: center;" colspan="3">Simulator statistics (<code>sim stats</code>)</td>
            </tr>
            <tr>
            <td style="text-align: center;">explo, DIM</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">explo_DIM</td>
            </tr>
            <tr>
            <td style="text-align: center;">explo, USE</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">explo_USE</td>
            </tr>
            <tr>
            <td style="text-align: center;">cratr, DIM</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">cratr_DIM</td>
            </tr>
            <tr>
            <td style="text-align: center;">cratr, USE</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">cratr_USE</td>
            </tr>
            <tr>
            <td style="text-align: center;">puffs, TOT</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">puffs_TOT</td>
            </tr>
            <tr>
            <td style="text-align: center;">puffs, VIS</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">puffs_VIS</td>
            </tr>
            <tr>
            <td style="text-align: center;">tris, vis</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">tris_vis</td>
            </tr>
            <tr>
            <td style="text-align: center;">q, depth</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">q_depth</td>
            </tr>
            <tr>
            <td style="text-align: center;" colspan="3"><code>Speeds</code></td>
            </tr>
            <tr>
            <td style="text-align: center;">Vind, kias</td>
            <td style="text-align: left;">The craft’s indicated airspeed, in knots indicated airspeed.</td>
            <td style="text-align: left;">Vind_kias</td>
            </tr>
            <tr>
            <td style="text-align: center;">Vind, keas</td>
            <td style="text-align: left;">The craft’s indicated airspeed, in knots equivalent airspeed (the calibrated airspeed corrected for adiabatic compressible flow at the craft’s current altitude).</td>
            <td style="text-align: left;">Vind_keas</td>
            </tr>
            <tr>
            <td style="text-align: center;">Vtrue, ktas</td>
            <td style="text-align: left;">The craft’s true airspeed (the speed of the craft relative to undisturbed air), in knots true airspeed.</td>
            <td style="text-align: left;">Vtrue_ktas</td>
            </tr>
            <tr>
            <td style="text-align: center;">Vtrue, ktgs</td>
            <td style="text-align: left;">True airspeed, in knots true ground speed.</td>
            <td style="text-align: left;">Vtrue_ktgs</td>
            </tr>
            <tr>
            <td style="text-align: center;">Vind, mph</td>
            <td style="text-align: left;">The craft’s indicated airspeed, in miles per hour.</td>
            <td style="text-align: left;">Vind_mph</td>
            </tr>
            <tr>
            <td style="text-align: center;">Vtrue, mphas</td>
            <td style="text-align: left;">The craft’s true airspeed, in miles per hour airspeed.</td>
            <td style="text-align: left;">Vtrue_mphas</td>
            </tr>
            <tr>
            <td style="text-align: center;">Vtrue, mphgs</td>
            <td style="text-align: left;">The craft’s true airspeed, in miles per hour ground speed.</td>
            <td style="text-align: left;">Vtrue_mphgs</td>
            </tr>
            <tr>
            <td style="text-align: center;" colspan="3">Aircraft Mach speeds, vertical velocity, and g-loads (<code>mach, VVI, G-load</code>)</td>
            </tr>
            <tr>
            <td style="text-align: center;">Mach, ratio</td>
            <td style="text-align: left;">The aircraft’s current speed, as a ratio to Mach 1.</td>
            <td style="text-align: left;">Mach_ratio</td>
            </tr>
            <tr>
            <td style="text-align: center;">VVI, fpm</td>
            <td style="text-align: left;">The aircraft’s current vertical velocity, in feet per minute. If everything is working as it should, this is normal to the local horizon under the aircraft.</td>
            <td style="text-align: left;">VVI_fpm</td>
            </tr>
            <tr>
            <td style="text-align: center;">Gload, norml</td>
            <td style="text-align: left;">The g-load across the aircraft, relative to the aircraft body-axis, if all is working as it should.</td>
            <td style="text-align: left;">Gload_norml</td>
            </tr>
            <tr>
            <td style="text-align: center;">Gload, axial</td>
            <td style="text-align: left;">The axial g-load on the aircraft.</td>
            <td style="text-align: left;">Gload_axial</td>
            </tr>
            <tr>
            <td style="text-align: center;">Gload, side</td>
            <td style="text-align: left;">The side g-load on the aircraft.</td>
            <td style="text-align: left;">Gload_side</td>
            </tr>
            <tr>
            <td style="text-align: center;" colspan="3"><code>Atmosphere: weather</code></td>
            </tr>
            <tr>
            <td style="text-align: center;">SLprs, inHG</td>
            <td style="text-align: left;">SL<sub>prs</sub>, in inches mercury.</td>
            <td style="text-align: left;">SLprs_inHG</td>
            </tr>
            <tr>
            <td style="text-align: center;">SLtmp, degC</td>
            <td style="text-align: left;">SL<sub>tmp</sub>, in degrees Celsius.</td>
            <td style="text-align: left;">SLtmp_degC</td>
            </tr>
            <tr>
            <td style="text-align: center;">wind, speed</td>
            <td style="text-align: left;">The wind speed around the aircraft, in knots.</td>
            <td style="text-align: left;">wind_speed</td>
            </tr>
            <tr>
            <td style="text-align: center;">wind, dir</td>
            <td style="text-align: left;">The wind direction, in degrees clockwise deviation from north. Wind blowing from north to south has direction 0.0, while wind blowing from west to east has direction 270.0.</td>
            <td style="text-align: left;">wind_dir</td>
            </tr>
            <tr>
            <td style="text-align: center;">trb, locl</td>
            <td style="text-align: left;">Amount of local turbulence.</td>
            <td style="text-align: left;">trb_locl</td>
            </tr>
            <tr>
            <td style="text-align: center;">prec, locl</td>
            <td style="text-align: left;">Amount of local precipitation.</td>
            <td style="text-align: left;">prec_locl</td>
            </tr>
            <tr>
            <td style="text-align: center;">hail, locl</td>
            <td style="text-align: left;">Amount of local hail.</td>
            <td style="text-align: left;">hail_locl</td>
            </tr>
            <tr>
            <td style="text-align: center;" colspan="3"><code>Atmosphere: aircraft</code></td>
            </tr>
            <tr>
            <td style="text-align: center;">AMprs, inHG</td>
            <td style="text-align: left;">AM<sub>prs</sub>, in inches mercury.</td>
            <td style="text-align: left;">AMprs_inHG</td>
            </tr>
            <tr>
            <td style="text-align: center;">AMtmp, degC</td>
            <td style="text-align: left;">AM<sub>tmp</sub>, in degrees Celsius.</td>
            <td style="text-align: left;">AMtmp_degC</td>
            </tr>
            <tr>
            <td style="text-align: center;">LEtmp, degC</td>
            <td style="text-align: left;">LE<sub>tmp</sub>, in degrees Celsius.</td>
            <td style="text-align: left;">LEtmp_degC</td>
            </tr>
            <tr>
            <td style="text-align: center;">dens, ratio</td>
            <td style="text-align: left;">The aircraft’s density ratio.</td>
            <td style="text-align: left;">dens_ratio</td>
            </tr>
            <tr>
            <td style="text-align: center;">A, ktas</td>
            <td style="text-align: left;"><em>A</em>, in knots true airspeed.</td>
            <td style="text-align: left;">A_ktas</td>
            </tr>
            <tr>
            <td style="text-align: center;">Q, psf</td>
            <td style="text-align: left;"><em>Q</em>, dynamic pressure or velocity pressure, in pounds per square foot.</td>
            <td style="text-align: left;">Q_psf</td>
            </tr>
            <tr>
            <td style="text-align: center;">gravi, fts2</td>
            <td style="text-align: left;">Gravitational force, in feet per second squared.</td>
            <td style="text-align: left;">gravi_fts2</td>
            </tr>
            <tr>
            <td style="text-align: center;" colspan="3"><code>System pressures</code></td>
            </tr>
            <tr>
            <td style="text-align: center;">baro, inHG</td>
            <td style="text-align: left;">Barometric pressure, in inches mercury.</td>
            <td style="text-align: left;">baro_inHG</td>
            </tr>
            <tr>
            <td style="text-align: center;">edens, part</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">edens_part</td>
            </tr>
            <tr>
            <td style="text-align: center;">vacum, ratio</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">vacum_ratio</td>
            </tr>
            <tr>
            <td style="text-align: center;">elec, ratio</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">elec_ratio</td>
            </tr>
            <tr>
            <td style="text-align: center;">AHRS, ratio</td>
            <td style="text-align: left;">Pressure in the attitude heading reference system (AHRS), as a ratio to normal.</td>
            <td style="text-align: left;">AHRS_ratio</td>
            </tr>
            <tr>
            <td style="text-align: center;" colspan="3">Joystick aileron, elevator, and rudder input (<code>joystick ail/elv/rud</code>)</td>
            </tr>
            <tr>
            <td style="text-align: center;">elev, yoke1</td>
            <td style="text-align: left;">The user’s elevator input, as a ratio to full upward deflection. For instance, a value of –1.000 indicated the user is commanding the aircraft’s nose down as fast as possible.</td>
            <td style="text-align: left;">elev_yoke1</td>
            </tr>
            <tr>
            <td style="text-align: center;">ailrn, yoke1</td>
            <td style="text-align: left;">The user’s aileron input, as a ratio to full rightward deflection. For instance, a value of –1.000 indicated the user is commanding the aircraft to roll left as fast as possible.</td>
            <td style="text-align: left;">ailrn_yoke1</td>
            </tr>
            <tr>
            <td style="text-align: center;">ruddr, yoke1</td>
            <td style="text-align: left;">The user’s rudder input, as a ratio to full rightward deflection. For instance, a value of –1.000 indicated the user is commanding the aircraft to yaw left as fast as possible.</td>
            <td style="text-align: left;">ruddr_yoke1</td>
            </tr>
            <tr>
            <td style="text-align: center;" colspan="3"><code>Other flight controls</code></td>
            </tr>
            <tr>
            <td style="text-align: center;">vect, rqst</td>
            <td style="text-align: left;">The requested thrust vectoring.</td>
            <td style="text-align: left;">vect_rqst</td>
            </tr>
            <tr>
            <td style="text-align: center;">sweep, rqst</td>
            <td style="text-align: left;">The requested wing sweep.</td>
            <td style="text-align: left;">sweep_rqst</td>
            </tr>
            <tr>
            <td style="text-align: center;">incid, rqst</td>
            <td style="text-align: left;">The requested wing incidence.</td>
            <td style="text-align: left;">incid_rqst</td>
            </tr>
            <tr>
            <td style="text-align: center;">dihed, rqst</td>
            <td style="text-align: left;">The requested wing dihedral.</td>
            <td style="text-align: left;">dihed_rqst</td>
            </tr>
            <tr>
            <td style="text-align: center;">retra, rqst</td>
            <td style="text-align: left;">The requested wing retraction.</td>
            <td style="text-align: left;">retra_rqst</td>
            </tr>
            <tr>
            <td style="text-align: center;">water, jetts</td>
            <td style="text-align: left;">Water jettisoned.</td>
            <td style="text-align: left;">water_jetts</td>
            </tr>
            <tr>
            <td style="text-align: center;" colspan="3">Artificial stability inputs for aileron, elevator, and rudder (<code>art stab ail/elv/rud</code>)</td>
            </tr>
            <tr>
            <td style="text-align: center;">elev, astab</td>
            <td style="text-align: left;">The artificial stability system’s elevator input, as a ratio to full upward deflection.</td>
            <td style="text-align: left;">elev_astab</td>
            </tr>
            <tr>
            <td style="text-align: center;">ailrn, astab</td>
            <td style="text-align: left;">The artificial stability system’s aileron input, as a ratio to full rightward deflection.</td>
            <td style="text-align: left;">ailrn_astab</td>
            </tr>
            <tr>
            <td style="text-align: center;">ruddr, astab</td>
            <td style="text-align: left;">The artificial stability system’s aileron input, as a ratio to full rightward deflection.</td>
            <td style="text-align: left;">ruddr_astab</td>
            </tr>
            <tr>
            <td style="text-align: center;" colspan="3">Flight control deflections for aileron, elevator, and rudder (<code>flight con ail/elv/rud</code>)</td>
            </tr>
            <tr>
            <td style="text-align: center;">elev, surf</td>
            <td style="text-align: left;">The proportion of the elevator deflected for upward pitch. If the elevators and flight inputs are in sync, this will match the combined yoke and artificial stability system input.</td>
            <td style="text-align: left;">elev_surf</td>
            </tr>
            <tr>
            <td style="text-align: center;">ailrn, surf</td>
            <td style="text-align: left;">The proportion of the aileron deflected for rightward roll. If the elevators and flight inputs are in sync, this will match the combined yoke and artificial stability system input.</td>
            <td style="text-align: left;">ailrn_surf</td>
            </tr>
            <tr>
            <td style="text-align: center;">ruddr, surf</td>
            <td style="text-align: left;">The proportion of the rudder deflected for rightward yaw. If the elevators and flight inputs are in sync, this will match the combined yoke and artificial stability system input.</td>
            <td style="text-align: left;">ruddr_surf</td>
            </tr>
            <tr>
            <td style="text-align: center;">nwhel, steer</td>
            <td style="text-align: left;">The nosewheel’s direction, in degrees of deviation from pointing straight ahead. For instance, a value of –31.000 indicated the wheel is pointed left 31 degrees.</td>
            <td style="text-align: left;">nwhel_steer</td>
            </tr>
            <tr>
            <td style="text-align: center;" colspan="3">Wing sweep and thrust vectoring (<code>wing sweep/thrust vect</code>)</td>
            </tr>
            <tr>
            <td style="text-align: center;">sweep, 1, deg</td>
            <td style="text-align: left;">The craft’s wing sweep, in degrees back from normal.</td>
            <td style="text-align: left;">sweep_1_deg</td>
            </tr>
            <tr>
            <td style="text-align: center;">sweep, 2, deg</td>
            <td style="text-align: left;">The craft’s wing sweep, in degrees back from normal.</td>
            <td style="text-align: left;">sweep_2_deg</td>
            </tr>
            <tr>
            <td style="text-align: center;">sweep, h, deg</td>
            <td style="text-align: left;">The craft’s wing sweep, in degrees.</td>
            <td style="text-align: left;">sweep_h_deg</td>
            </tr>
            <tr>
            <td style="text-align: center;">vect, ratio</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">vect_ratio</td>
            </tr>
            <tr>
            <td style="text-align: center;">sweep, ratio</td>
            <td style="text-align: left;">The craft’s wing sweep, as a ratio to fully forward.</td>
            <td style="text-align: left;">sweep_ratio</td>
            </tr>
            <tr>
            <td style="text-align: center;">incid, ratio</td>
            <td style="text-align: left;">The craft’s wing incidence, as a ratio to fully angled.</td>
            <td style="text-align: left;">incid_ratio</td>
            </tr>
            <tr>
            <td style="text-align: center;">dihed, ratio</td>
            <td style="text-align: left;">The craft’s wing dihedral, as a ratio to fully angled.</td>
            <td style="text-align: left;">dihed_ratio</td>
            </tr>
            <tr>
            <td style="text-align: center;">retra, ratio</td>
            <td style="text-align: left;">The craft’s wing retraction, as a ratio to fully retracted.</td>
            <td style="text-align: left;">retra_ratio</td>
            </tr>
            <tr>
            <td style="text-align: center;" colspan="3">Trim, flaps, slats, and speedbrakes (<code>trim/flap/slat/s-brakes</code>)</td>
            </tr>
            <tr>
            <td style="text-align: center;">trim, elev</td>
            <td style="text-align: left;">Elevator trim.</td>
            <td style="text-align: left;">trim_elev</td>
            </tr>
            <tr>
            <td style="text-align: center;">trim, ailrn</td>
            <td style="text-align: left;">Aileron trim.</td>
            <td style="text-align: left;">trim_ailrn</td>
            </tr>
            <tr>
            <td style="text-align: center;">trim, ruddr</td>
            <td style="text-align: left;">Rudder trim.</td>
            <td style="text-align: left;">trim_ruddr</td>
            </tr>
            <tr>
            <td style="text-align: center;">flap, handl</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">flap_handl</td>
            </tr>
            <tr>
            <td style="text-align: center;">flap, postn</td>
            <td style="text-align: left;">Flap position.</td>
            <td style="text-align: left;">flap_postn</td>
            </tr>
            <tr>
            <td style="text-align: center;">slat, ratio</td>
            <td style="text-align: left;">Slat position.</td>
            <td style="text-align: left;">slat_ratio</td>
            </tr>
            <tr>
            <td style="text-align: center;">sbrak, handl</td>
            <td style="text-align: left;"></td>
            <td style="text-align: left;">sbrak_handl</td>
            </tr>
            <tr>
            <td style="text-align: center;">sbrak, postn</td>
            <td style="text-align: left;">Speedbrake position.</td>
            <td style="text-align: left;">sbrak_postn</td>
            </tr>
            <tr>
            <td style="text-align: center;" colspan="3">Landing gear and brakes (<code>gear/brakes</code>)</td>
            </tr>
            <tr>
            <td style="text-align: center;">gear, 0/1</td>
            <td style="text-align: left;">Gear extended status.</td>
            <td style="text-align: left;">gear_0_1</td>
            </tr>
            <tr>
            <td style="text-align: center;">wbrak, part</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">wbrak_part</td>
            </tr>
            <tr>
            <td style="text-align: center;">lbrak, part</td>
            <td style="text-align: left;">Left toe brake depression.</td>
            <td style="text-align: left;">lbrak_part</td>
            </tr>
            <tr>
            <td style="text-align: center;">rbrak, part</td>
            <td style="text-align: left;">Right toe brake depression.</td>
            <td style="text-align: left;">rbrak_part</td>
            </tr>
            <tr>
            <td style="text-align: center;" colspan="3"><code>Angular moments</code></td>
            </tr>
            <tr>
            <td style="text-align: center;">L, ftlb</td>
            <td style="text-align: left;">Roll torque, in foot-pounds, about the long axis, which we call the z axis.</td>
            <td style="text-align: left;">L_ftlb</td>
            </tr>
            <tr>
            <td style="text-align: center;">M, ftlb</td>
            <td style="text-align: left;">Pitch torque, in foot-pounds, about the lateral axis, which we call the x axis.</td>
            <td style="text-align: left;">M_ftlb</td>
            </tr>
            <tr>
            <td style="text-align: center;">N, ftlb</td>
            <td style="text-align: left;">Yaw torque, in foot-pounds, about the vertical axis, which we call the y axis.</td>
            <td style="text-align: left;">N_ftlb</td>
            </tr>
            <tr>
            <td style="text-align: center;">Q, rad/s</td>
            <td style="text-align: left;">Pitch rate, measured in body-axes (when all is working as it should).</td>
            <td style="text-align: left;">Q_rad_s</td>
            </tr>
            <tr>
            <td style="text-align: center;">P, rad/s</td>
            <td style="text-align: left;">Roll rate, measured in body-axes (when all is working as it should).</td>
            <td style="text-align: left;">P_rad_s</td>
            </tr>
            <tr>
            <td style="text-align: center;">R, rad/s</td>
            <td style="text-align: left;">Yaw rate, measured in body-axes (when all is working as it should).</td>
            <td style="text-align: left;">R_rad_s</td>
            </tr>
            <tr>
            <td style="text-align: center;" colspan="3"><code>Pitch, roll, headings</code></td>
            </tr>
            <tr>
            <td style="text-align: center;">pitch, deg</td>
            <td style="text-align: left;">The aircraft’s pitch, measured in body-axis Euler angles.</td>
            <td style="text-align: left;">pitch_deg</td>
            </tr>
            <tr>
            <td style="text-align: center;">roll, deg</td>
            <td style="text-align: left;">The aircraft’s roll, measured in body-axis Euler angles.</td>
            <td style="text-align: left;">roll_deg</td>
            </tr>
            <tr>
            <td style="text-align: center;">hding, true</td>
            <td style="text-align: left;">The aircraft’s true heading, measured in body-axis Euler angles.</td>
            <td style="text-align: left;">hding_true</td>
            </tr>
            <tr>
            <td style="text-align: center;">hding, mag</td>
            <td style="text-align: left;">The aircraft’s magnetic heading, in degrees.</td>
            <td style="text-align: left;">hding_mag</td>
            </tr>
            <tr>
            <td style="text-align: center;" colspan="3">Angle of attack, sideslip, and paths (<code>AoA, side-slip, paths</code>)</td>
            </tr>
            <tr>
            <td style="text-align: center;">alpha, deg</td>
            <td style="text-align: left;">The aircraft’s angle of attack, in degrees.</td>
            <td style="text-align: left;">alpha_deg</td>
            </tr>
            <tr>
            <td style="text-align: center;">beta, deg</td>
            <td style="text-align: left;">The aircraft’s angle of sideslip, in degrees.</td>
            <td style="text-align: left;">beta_deg</td>
            </tr>
            <tr>
            <td style="text-align: center;">hpath, deg</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">hpath_deg</td>
            </tr>
            <tr>
            <td style="text-align: center;">vpath, deg</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">vpath_deg</td>
            </tr>
            <tr>
            <td style="text-align: center;">slip, deg</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">slip_deg</td>
            </tr>
            <tr>
            <td style="text-align: center;" colspan="3">Magnetic compass (<code>mag compass</code>)</td>
            </tr>
            <tr>
            <td style="text-align: center;">mag, comp</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">mag_comp</td>
            </tr>
            <tr>
            <td style="text-align: center;">mavar, deg</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">mavar_deg</td>
            </tr>
            <tr>
            <td style="text-align: center;" colspan="3">Latitude, longitude, and altitude (<code>lat, lon, altitude</code>)</td>
            </tr>
            <tr>
            <td style="text-align: center;">lat, deg</td>
            <td style="text-align: left;">The aircraft’s latitudinal location, in degrees.</td>
            <td style="text-align: left;">lat_deg</td>
            </tr>
            <tr>
            <td style="text-align: center;">lon, deg</td>
            <td style="text-align: left;">The aircraft’s longitudinal location, in degrees.</td>
            <td style="text-align: left;">long_deg</td>
            </tr>
            <tr>
            <td style="text-align: center;">alt, ftmsl</td>
            <td style="text-align: left;">The aircraft’s altitude, in feet above mean sea level.</td>
            <td style="text-align: left;">alt_ftmsl</td>
            </tr>
            <tr>
            <td style="text-align: center;">alt, ftagl</td>
            <td style="text-align: left;">The aircraft’s altitude, in feet above ground level.</td>
            <td style="text-align: left;">alt_ftagl</td>
            </tr>
            <tr>
            <td style="text-align: center;">on, runwy</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">on_runwy</td>
            </tr>
            <tr>
            <td style="text-align: center;">alt, ind</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">alt_ind</td>
            </tr>
            <tr>
            <td style="text-align: center;">lat, south</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">lat_south</td>
            </tr>
            <tr>
            <td style="text-align: center;">lon, west</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">lon_west</td>
            </tr>
            <tr>
            <td style="text-align: center;" colspan="3">Location, velocity, and distance traveled (<code>loc, vel, dist traveled</code>)</td>
            </tr>
            <tr>
            <td style="text-align: center;">X, m</td>
            <td style="text-align: left;">Relative to the inertial axes.</td>
            <td style="text-align: left;">X_m</td>
            </tr>
            <tr>
            <td style="text-align: center;">Y, m</td>
            <td style="text-align: left;">Relative to the inertial axes.</td>
            <td style="text-align: left;">Y_m</td>
            </tr>
            <tr>
            <td style="text-align: center;">Z, m</td>
            <td style="text-align: left;">Relative to the inertial axes.</td>
            <td style="text-align: left;">Z_m</td>
            </tr>
            <tr>
            <td style="text-align: center;">vX, m/s</td>
            <td style="text-align: left;">Relative to the inertial axes.</td>
            <td style="text-align: left;">vX_m_s</td>
            </tr>
            <tr>
            <td style="text-align: center;">vY, m/s</td>
            <td style="text-align: left;">Relative to the inertial axes.</td>
            <td style="text-align: left;">vY_m_s</td>
            </tr>
            <tr>
            <td style="text-align: center;">vZ, m/s</td>
            <td style="text-align: left;">Relative to the inertial axes.</td>
            <td style="text-align: left;">vZ_m_s</td>
            </tr>
            <tr>
            <td style="text-align: center;">dist, ft</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">dist_ft</td>
            </tr>
            <tr>
            <td style="text-align: center;">dist, nm</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">dist_nm</td>
            </tr>
            <tr>
            <td style="text-align: center;" colspan="3">Latitude for all aircraft (<code>all planes: lat</code>)</td>
            </tr>
            <tr>
            <td style="text-align: center;">lat <em>n</em>, deg</td>
            <td style="text-align: left;">Aircraft <em>n</em>’s latitudinal location (zero if craft <em>n</em> does not exist).</td>
            <td style="text-align: left;">lat_n_deg</td>
            </tr>
            <tr>
            <td style="text-align: center;" colspan="3">Longitude for all aircraft (<code>all planes: lon</code>)</td>
            </tr>
            <tr>
            <td style="text-align: center;">lon <em>n</em>, deg</td>
            <td style="text-align: left;">Aircraft <em>n</em>’s longitudinal location (zero if craft <em>n</em> does not exist).</td>
            <td style="text-align: left;">lon_n_deg</td>
            </tr>
            <tr>
            <td style="text-align: center;" colspan="3">Altitude for all aircraft (<code>all planes: alt</code>)</td>
            </tr>
            <tr>
            <td style="text-align: center;">alt <em>n</em>, ftmsl</td>
            <td style="text-align: left;">Aircraft <em>n</em>’s altitude location (zero if craft <em>n</em> does not exist).</td>
            <td style="text-align: left;">alt_n_ftmsl</td>
            </tr>
            <tr>
            <td style="text-align: center;" colspan="3">Commanded throttle (<code>throttle command</code>)</td>
            </tr>
            <tr>
            <td style="text-align: center;">thro<em>n</em>, part</td>
            <td style="text-align: left;">Aircraft <em>n</em>’s commanded throttle.</td>
            <td style="text-align: left;">thro_n_part</td>
            </tr>
            <tr>
            <td style="text-align: center;" colspan="3">Actual throttle (<code>throttle actual</code>)</td>
            </tr>
            <tr>
            <td style="text-align: center;">thro<em>n</em>, part</td>
            <td style="text-align: left;">Aircraft <em>n</em>’s actual throttle.</td>
            <td style="text-align: left;">thro_n_part</td>
            </tr>
            <tr>
            <td style="text-align: center;" colspan="3">Engine or propeller mode (<code>feather-norm-beta-revers</code>)</td>
            </tr>
            <tr>
            <td style="text-align: center;">mode<em>n</em>, 0123</td>
            <td style="text-align: left;">Engine <em>n</em>’s current “mode,” where 0 corresponds to feathered, 1 corresponds to normal, 2 to beta, and 3 to reverse thrust.</td>
            <td style="text-align: left;">mode_n_0123</td>
            </tr>
            <tr>
            <td style="text-align: center;" colspan="3">Propeller setting (<code>prop setting</code>)</td>
            </tr>
            <tr>
            <td style="text-align: center;">prop<em>n</em>, set</td>
            <td style="text-align: left;">Aircraft <em>n</em>’s propeller setting.</td>
            <td style="text-align: left;">prop_n_set</td>
            </tr>
            <tr>
            <td style="text-align: center;" colspan="3"><code>Mixture setting</code></td>
            </tr>
            <tr>
            <td style="text-align: center;">mixt<em>n</em>, ratio</td>
            <td style="text-align: left;">Aircraft <em>n</em>’s mixture setting.</td>
            <td style="text-align: left;">mixt_n_ratio</td>
            </tr>
            <tr>
            <td style="text-align: center;" colspan="3">Carburetor heat setting (<code>carb heat setting</code>)</td>
            </tr>
            <tr>
            <td style="text-align: center;">heat<em>n</em>, ratio</td>
            <td style="text-align: left;">Aircraft <em>n</em>’s carburetor heat setting.</td>
            <td style="text-align: left;">heat_n_ratio</td>
            </tr>
            <tr>
            <td style="text-align: center;" colspan="3"><code>Cowl flap setting</code></td>
            </tr>
            <tr>
            <td style="text-align: center;">cowl<em>n</em>, set</td>
            <td style="text-align: left;">Aircraft <em>n</em>’s cowl flap setting.</td>
            <td style="text-align: left;">cowl_n_set</td>
            </tr>
            <tr>
            <td style="text-align: center;" colspan="3"><code>Magneto settings</code></td>
            </tr>
            <tr>
            <td style="text-align: center;">magn<em>n</em>, set</td>
            <td style="text-align: left;">Aircraft <em>n</em>’s magneto setting.</td>
            <td style="text-align: left;">magn_n_set</td>
            </tr>
            <tr>
            <td style="text-align: center;" colspan="3"><code>Starter timeout</code></td>
            </tr>
            <tr>
            <td style="text-align: center;">star<em>n</em>, sec</td>
            <td style="text-align: left;">Aircraft <em>n</em>’s starter timeout.</td>
            <td style="text-align: left;">star_n_sec</td>
            </tr>
            <tr>
            <td style="text-align: center;" colspan="3"><code>Engine power</code></td>
            </tr>
            <tr>
            <td style="text-align: center;">power, <em>n</em>, hp</td>
            <td style="text-align: left;">Engine <em>n</em>’s power, in horsepower.</td>
            <td style="text-align: left;">power_n_hp</td>
            </tr>
            <tr>
            <td style="text-align: center;" colspan="3"><code>Engine thrust</code></td>
            </tr>
            <tr>
            <td style="text-align: center;">thrst, <em>n</em>, lb</td>
            <td style="text-align: left;">The thrust, in pounds, generated by engine <em>n</em>.</td>
            <td style="text-align: left;">thrst_n_lb</td>
            </tr>
            <tr>
            <td style="text-align: center;" colspan="3"><code>Engine torque</code></td>
            </tr>
            <tr>
            <td style="text-align: center;">trq <em>n</em>, ftlb</td>
            <td style="text-align: left;">The torque, in foot-pounds, generated by engine <em>n</em>.</td>
            <td style="text-align: left;">trq_n_ftlb</td>
            </tr>
            <tr>
            <td style="text-align: center;" colspan="3"><code>Engine RPM</code></td>
            </tr>
            <tr>
            <td style="text-align: center;">rpm <em>n</em>, engin</td>
            <td style="text-align: left;">The current RPM of engine <em>n</em>.</td>
            <td style="text-align: left;">rpm_n_engin</td>
            </tr>
            <tr>
            <td style="text-align: center;" colspan="3">Propeller RPM (<code>prop RPM</code>)</td>
            </tr>
            <tr>
            <td style="text-align: center;">rpm <em>n</em>, prop</td>
            <td style="text-align: left;">The current RPM of propeller <em>n</em>.</td>
            <td style="text-align: left;">rpm_n_prop</td>
            </tr>
            <tr>
            <td style="text-align: center;" colspan="3">Propeller pitch (<code>prop pitch</code>)</td>
            </tr>
            <tr>
            <td style="text-align: center;">ptch<em>n</em>, deg</td>
            <td style="text-align: left;">The current pitch of propeller <em>n</em>.</td>
            <td style="text-align: left;">ptch_n_deg</td>
            </tr>
            <tr>
            <td style="text-align: center;" colspan="3">Slipstream/propwash/jetwash (<code>propwash/jetwash</code>)</td>
            </tr>
            <tr>
            <td style="text-align: center;">pwash, kt</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">pwash_kt</td>
            </tr>
            <tr>
            <td style="text-align: center;" colspan="3"><code>N1</code></td>
            </tr>
            <tr>
            <td style="text-align: center;">N1 <em>n</em>, pcnt</td>
            <td style="text-align: left;">The current N1 for engine <em>n</em>.</td>
            <td style="text-align: left;">N1_n_pcnt</td>
            </tr>
            <tr>
            <td style="text-align: center;" colspan="3"><code>N2</code></td>
            </tr>
            <tr>
            <td style="text-align: center;">N2 <em>n</em>, pcnt</td>
            <td style="text-align: left;">The current N2 for engine <em>n</em>.</td>
            <td style="text-align: left;">N2_n_pcnt</td>
            </tr>
            <tr>
            <td style="text-align: center;" colspan="3">Manifold pressure (<code>MP</code>)</td>
            </tr>
            <tr>
            <td style="text-align: center;">MP <em>n</em>, inhg</td>
            <td style="text-align: left;">The current manifold pressure for engine <em>n</em>, in inches mercury.</td>
            <td style="text-align: left;">MP_n_inhg</td>
            </tr>
            <tr>
            <td style="text-align: center;" colspan="3">Engine pressure ratio (<code>EPR</code>)</td>
            </tr>
            <tr>
            <td style="text-align: center;">EPR <em>n</em>, part</td>
            <td style="text-align: left;">The current engine pressure ratio for engine <em>n</em>.</td>
            <td style="text-align: left;">EPR_n_aprt</td>
            </tr>
            <tr>
            <td style="text-align: center;" colspan="3">Fuel flow (<code>FF</code>)</td>
            </tr>
            <tr>
            <td style="text-align: center;">FF <em>n</em>, lb/h</td>
            <td style="text-align: left;">The current fuel flow for engine <em>n</em>, in pounds per hour.</td>
            <td style="text-align: left;">FF_n_lb_h</td>
            </tr>
            <tr>
            <td style="text-align: center;" colspan="3">Interstage turbine temperature (<code>ITT</code>)</td>
            </tr>
            <tr>
            <td style="text-align: center;">ITT <em>n</em>, deg</td>
            <td style="text-align: left;">The current interstage turbine temperature for engine <em>n</em>.</td>
            <td style="text-align: left;">ITT_n_deg</td>
            </tr>
            <tr>
            <td style="text-align: center;" colspan="3">Exhaust gas temperature (<code>EGT</code>)</td>
            </tr>
            <tr>
            <td style="text-align: center;">EGT <em>n</em>, deg</td>
            <td style="text-align: left;">The current exhaust gas temperature for engine <em>n</em>.</td>
            <td style="text-align: left;">EGT_n_deg</td>
            </tr>
            <tr>
            <td style="text-align: center;" colspan="3">Cylinder head temperature (<code>CHT</code>)</td>
            </tr>
            <tr>
            <td style="text-align: center;">CHT <em>n</em>, deg</td>
            <td style="text-align: left;">The current cylinder head temperature for engine <em>n</em>.</td>
            <td style="text-align: left;">CHT_n_deg</td>
            </tr>
            <tr>
            <td style="text-align: center;" colspan="3"><code>Oil pressure</code></td>
            </tr>
            <tr>
            <td style="text-align: center;">OILP<em>n</em>, psi</td>
            <td style="text-align: left;">The current oil pressure for engine <em>n</em>, in pounds per square inch.</td>
            <td style="text-align: left;">OILP_n_psi</td>
            </tr>
            <tr>
            <td style="text-align: center;" colspan="3">Oil temperature (<code>Oil temp</code>)</td>
            </tr>
            <tr>
            <td style="text-align: center;">OILT<em>n</em>, deg</td>
            <td style="text-align: left;">The current oil temperature for engine <em>n</em>.</td>
            <td style="text-align: left;">OILT_n_deg</td>
            </tr>
            <tr>
            <td style="text-align: center;" colspan="3"><code>Fuel pressure</code></td>
            </tr>
            <tr>
            <td style="text-align: center;">FUEP<em>n</em>, psi</td>
            <td style="text-align: left;">The current fuel pressure for engine <em>n</em>, in pounds per square inch.</td>
            <td style="text-align: left;">FUEP_n_psi</td>
            </tr>
            <tr>
            <td style="text-align: center;" colspan="3"><code>Generator amperage</code></td>
            </tr>
            <tr>
            <td style="text-align: center;">genr<em>n</em>, amp</td>
            <td style="text-align: left;">The current generator amperage for generator <em>n</em>.</td>
            <td style="text-align: left;">genr_n_amp</td>
            </tr>
            <tr>
            <td style="text-align: center;" colspan="3"><code>Battery amperage</code></td>
            </tr>
            <tr>
            <td style="text-align: center;">batt<em>n</em>, amp</td>
            <td style="text-align: left;">The current batter amperage for battery <em>n</em>.</td>
            <td style="text-align: left;">batt_n_amp</td>
            </tr>
            <tr>
            <td style="text-align: center;" colspan="3"><code>Battery voltage</code></td>
            </tr>
            <tr>
            <td style="text-align: center;">batt<em>n</em>, volt</td>
            <td style="text-align: left;">The current battery voltage for battery <em>n</em>.</td>
            <td style="text-align: left;">batt_n_volt</td>
            </tr>
            <tr>
            <td style="text-align: center;" colspan="3"><code>Fuel pump on/off</code></td>
            </tr>
            <tr>
            <td style="text-align: center;">pump<em>n</em>, 0/1</td>
            <td style="text-align: left;">Fuel pump <em>n</em>’s status.</td>
            <td style="text-align: left;">pump_n_0_1</td>
            </tr>
            <tr>
            <td style="text-align: center;" colspan="3"><code>Idle speed lo/hi</code></td>
            </tr>
            <tr>
            <td style="text-align: center;">idle<em>n</em> 0/1</td>
            <td style="text-align: left;">Engine <em>n</em>’s idle speed.</td>
            <td style="text-align: left;">idle_n_0_1</td>
            </tr>
            <tr>
            <td style="text-align: center;" colspan="3"><code>Battery on/off</code></td>
            </tr>
            <tr>
            <td style="text-align: center;">batt<em>n</em>, 0/1</td>
            <td style="text-align: left;">Battery <em>n</em>’s status.</td>
            <td style="text-align: left;">batt_n_0_1</td>
            </tr>
            <tr>
            <td style="text-align: center;" colspan="3"><code>Generator on/off</code></td>
            </tr>
            <tr>
            <td style="text-align: center;">genr<em>n</em>, 0/1</td>
            <td style="text-align: left;">Generator <em>n</em>’s status.</td>
            <td style="text-align: left;">genr_n_0_1</td>
            </tr>
            <tr>
            <td style="text-align: center;" colspan="3"><code>Inverter on/off</code></td>
            </tr>
            <tr>
            <td style="text-align: center;">invr<em>n</em>, 0/1</td>
            <td style="text-align: left;">Inverter <em>n</em>’s status.</td>
            <td style="text-align: left;">invr_n_0_1</td>
            </tr>
            <tr>
            <td style="text-align: center;" colspan="3"><code>FADEC on/off</code></td>
            </tr>
            <tr>
            <td style="text-align: center;">fadec, 0/1</td>
            <td style="text-align: left;">The FADEC’s status.</td>
            <td style="text-align: left;">fadec_0_1</td>
            </tr>
            <tr>
            <td style="text-align: center;" colspan="3"><code>Igniter on/off</code></td>
            </tr>
            <tr>
            <td style="text-align: center;">igni<em>n</em>, 0/1</td>
            <td style="text-align: left;">Igniter <em>n</em>’s status.</td>
            <td style="text-align: left;">igni_n_0_1</td>
            </tr>
            <tr>
            <td style="text-align: center;" colspan="3"><code>Fuel weights</code></td>
            </tr>
            <tr>
            <td style="text-align: center;">fuel, <em>n</em> lb</td>
            <td style="text-align: left;">Fuel tank <em>n</em>’s weight, in pounds.</td>
            <td style="text-align: left;">fuel_n_lb</td>
            </tr>
            <tr>
            <td style="text-align: center;" colspan="3">Payload weights and center of gravity (<code>payload weights and CG</code>)</td>
            </tr>
            <tr>
            <td style="text-align: center;">empty, lb</td>
            <td style="text-align: left;">The aircraft’s empty weight, in pounds.</td>
            <td style="text-align: left;">empty_lb</td>
            </tr>
            <tr>
            <td style="text-align: center;">payld, lb</td>
            <td style="text-align: left;">The aircraft’s payload weight, in pounds.</td>
            <td style="text-align: left;">payld_lb</td>
            </tr>
            <tr>
            <td style="text-align: center;">fuel, totlb</td>
            <td style="text-align: left;">The total weight of the aircraft’s fuel, in pounds.</td>
            <td style="text-align: left;">fuel_totlb</td>
            </tr>
            <tr>
            <td style="text-align: center;">jetti, lb</td>
            <td style="text-align: left;">The aircraft’s jettisonable weight, in pounds.</td>
            <td style="text-align: left;">jetti_lb</td>
            </tr>
            <tr>
            <td style="text-align: center;">curnt, lb</td>
            <td style="text-align: left;">The aircraft’s current weight, in pounds.</td>
            <td style="text-align: left;">curnt_lb</td>
            </tr>
            <tr>
            <td style="text-align: center;">maxim, lb</td>
            <td style="text-align: left;">The aircraft’s maximum weight, in pounds.</td>
            <td style="text-align: left;">maxim_lb</td>
            </tr>
            <tr>
            <td style="text-align: center;">cg, ftref</td>
            <td style="text-align: left;">The aircraft’s center of gravity, measured in feet behind the reference point.</td>
            <td style="text-align: left;">cg_ftref</td>
            </tr>
            <tr>
            <td style="text-align: center;" colspan="3">Aerodynamic forces, in wind axes (<code>aero forces</code>)</td>
            </tr>
            <tr>
            <td style="text-align: center;">lift, lb</td>
            <td style="text-align: left;">The lift acting on the aircraft, in pounds.</td>
            <td style="text-align: left;">lift_lb</td>
            </tr>
            <tr>
            <td style="text-align: center;">drag, lb</td>
            <td style="text-align: left;">The drag acting on the aircraft, in pounds.</td>
            <td style="text-align: left;">drag_lb</td>
            </tr>
            <tr>
            <td style="text-align: center;">side, lb</td>
            <td style="text-align: left;">The side forces acting on the aircraft, in pounds.</td>
            <td style="text-align: left;">side_lb</td>
            </tr>
            <tr>
            <td style="text-align: center;" colspan="3"><code>Engine forces</code></td>
            </tr>
            <tr>
            <td style="text-align: center;">norml, lb</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">norml_lb</td>
            </tr>
            <tr>
            <td style="text-align: center;">axial, lb</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">axial_lb</td>
            </tr>
            <tr>
            <td style="text-align: center;">side, lb</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">side_lb</td>
            </tr>
            <tr>
            <td style="text-align: center;" colspan="3">Landing gear vertical force (<code>landing gear vert force</code>)</td>
            </tr>
            <tr>
            <td style="text-align: center;">gear, lb</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">gear_lb</td>
            </tr>
            <tr>
            <td style="text-align: center;" colspan="3"><code>Landing gear deployment</code></td>
            </tr>
            <tr>
            <td style="text-align: center;">gear, rat</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">gear_rat</td>
            </tr>
            <tr>
            <td style="text-align: center;" colspan="3">Lift-to-drag ratio and coefficients (<code>lift over drag coeffs</code>)</td>
            </tr>
            <tr>
            <td style="text-align: center;">L/D, ratio</td>
            <td style="text-align: left;">The aircraft’s lift-to-drag ratio.</td>
            <td style="text-align: left;">L_D_ratio</td>
            </tr>
            <tr>
            <td style="text-align: center;">cl, total</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">cl_total</td>
            </tr>
            <tr>
            <td style="text-align: center;">cd, total</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">cd_total</td>
            </tr>
            <tr>
            <td style="text-align: center;">L/D, *etaP</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">L_D__etaP</td>
            </tr>
            <tr>
            <td style="text-align: center;" colspan="3">Propeller efficiency (<code>prop efficiency</code>)</td>
            </tr>
            <tr>
            <td style="text-align: center;">Peff<em>n</em>, ratio</td>
            <td style="text-align: left;">Propeller <em>n</em>’s efficiency ratio.</td>
            <td style="text-align: left;">Peff_n_ratio</td>
            </tr>
            <tr>
            <td style="text-align: center;" colspan="3">Aileron deflections (<code>defs: ailerons</code>)</td>
            </tr>
            <tr>
            <td style="text-align: center;">Lailn,<em>n</em>,deg</td>
            <td style="text-align: left;">The deflection of left aileron <em>n</em>, in degrees.</td>
            <td style="text-align: left;">Lailn_n_deg</td>
            </tr>
            <tr>
            <td style="text-align: center;">Railn, <em>n</em>, deg</td>
            <td style="text-align: left;">The deflection of right aileron <em>n</em>, in degrees.</td>
            <td style="text-align: left;">Railn_n_deg</td>
            </tr>
            <tr>
            <td style="text-align: center;" colspan="3">Roll spoiler deflection (<code>defs: roll spoilers</code>)</td>
            </tr>
            <tr>
            <td style="text-align: center;">Lsplr,<em>n</em>, deg</td>
            <td style="text-align: left;">The deflection of left spoiler <em>n</em>, in degrees.</td>
            <td style="text-align: left;">Lsplr_n_deg</td>
            </tr>
            <tr>
            <td style="text-align: center;">Rsplr, <em>n</em>, deg</td>
            <td style="text-align: left;">The deflection of right spoiler <em>n</em>, in degrees.</td>
            <td style="text-align: left;">Rsplr_n_deg</td>
            </tr>
            <tr>
            <td style="text-align: center;" colspan="3">Elevator deflections (<code>defs: elevators</code>)</td>
            </tr>
            <tr>
            <td style="text-align: center;">elev<em>n</em>, deg</td>
            <td style="text-align: left;">The deflection of elevator <em>n</em>, in degrees.</td>
            <td style="text-align: left;">elev_n_deg</td>
            </tr>
            <tr>
            <td style="text-align: center;" colspan="3">Rudder deflection (<code>defs: rudders</code>)</td>
            </tr>
            <tr>
            <td style="text-align: center;">rudr<em>n</em>, deg</td>
            <td style="text-align: left;">The deflection of rudder <em>n</em>, in degrees.</td>
            <td style="text-align: left;">rudr_n_deg</td>
            </tr>
            <tr>
            <td style="text-align: center;" colspan="3">Yaw brake deflections (<code>defs: yaw brakes</code>)</td>
            </tr>
            <tr>
            <td style="text-align: center;">Lyawb, deg</td>
            <td style="text-align: left;">The deflection of the left yaw brake, in degrees.</td>
            <td style="text-align: left;">Lyawb_deg</td>
            </tr>
            <tr>
            <td style="text-align: center;">Ryawb, deg</td>
            <td style="text-align: left;">The deflection of the right yaw brake, in degrees.</td>
            <td style="text-align: left;">Ryawb_deg</td>
            </tr>
            <tr>
            <td style="text-align: center;" colspan="3"><code>Control forces</code></td>
            </tr>
            <tr>
            <td style="text-align: center;">pitch, lb</td>
            <td style="text-align: left;">The pitch forces acting on the controls in the pilot’s hands.</td>
            <td style="text-align: left;">pitch_lb</td>
            </tr>
            <tr>
            <td style="text-align: center;">roll, lb</td>
            <td style="text-align: left;">The roll forces acting on the controls in the pilot’s hands.</td>
            <td style="text-align: left;">roll_lb</td>
            </tr>
            <tr>
            <td style="text-align: center;">hdng, lb</td>
            <td style="text-align: left;">The heading forces acting on the controls in the pilot’s hands.</td>
            <td style="text-align: left;">hdng_lb</td>
            </tr>
            <tr>
            <td style="text-align: center;">l-brk, lb</td>
            <td style="text-align: left;">The left brake forces acting on the controls at the pilot’s feet.</td>
            <td style="text-align: left;">l_brk_lb</td>
            </tr>
            <tr>
            <td style="text-align: center;">r-brk, lb</td>
            <td style="text-align: left;">The right brake forces acting on the controls at the pilot’s feet.</td>
            <td style="text-align: left;">r_brk_lb</td>
            </tr>
            <tr>
            <td style="text-align: center;" colspan="3">Total vertical thrust vectors (<code>total vert thrust vects</code>)</td>
            </tr>
            <tr>
            <td style="text-align: center;">vert<em>n</em>, tvect</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">vert_n_tvect</td>
            </tr>
            <tr>
            <td style="text-align: center;" colspan="3">Total lateral thrust vectors (<code>total lat thrust vects</code>)</td>
            </tr>
            <tr>
            <td style="text-align: center;">latr<em>n</em>, tvect</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">latr_n_tvect</td>
            </tr>
            <tr>
            <td style="text-align: center;" colspan="3"><code>Pitch cyclic disc tilts</code></td>
            </tr>
            <tr>
            <td style="text-align: center;">pitch, cycli</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">pitch_cycli</td>
            </tr>
            <tr>
            <td style="text-align: center;" colspan="3"><code>Roll cyclic disc tilts</code></td>
            </tr>
            <tr>
            <td style="text-align: center;">roll, cycli</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">roll_cycli</td>
            </tr>
            <tr>
            <td style="text-align: center;" colspan="3"><code>Pitch cyclic flapping</code></td>
            </tr>
            <tr>
            <td style="text-align: center;">pitch, flap</td>
            <td style="text-align: left;"></td>
            <td style="text-align: left;">pitch_flap</td>
            </tr>
            <tr>
            <td style="text-align: center;" colspan="3"><code>Roll cyclic flapping</code></td>
            </tr>
            <tr>
            <td style="text-align: center;">roll, flap</td>
            <td style="text-align: left;"></td>
            <td style="text-align: left;">roll_flap</td>
            </tr>
            <tr>
            <td style="text-align: center;" colspan="3">Ground effect (lift) from wings (<code>grnd effect lift, wings</code>)</td>
            </tr>
            <tr>
            <td style="text-align: center;">wing<em>n</em>, L cl*</td>
            <td style="text-align: left;"></td>
            <td style="text-align: left;">wing_n_L_cl_</td>
            </tr>
            <tr>
            <td style="text-align: center;">wing<em>n</em>, R cl*</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">wing_n_R_cl_</td>
            </tr>
            <tr>
            <td style="text-align: center;" colspan="3">Ground effect (drag) from wings (<code>grnd effect drag, wings</code>)</td>
            </tr>
            <tr>
            <td style="text-align: center;">wing<em>n</em>, Lcdi*</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">wing_n_Lcdi_</td>
            </tr>
            <tr>
            <td style="text-align: center;">wing<em>n</em>, Rcdi*</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">wing_n_Rcdi_</td>
            </tr>
            <tr>
            <td style="text-align: center;" colspan="3">Ground effect (wash) from wings (<code>grnd effect wash, wings</code>)</td>
            </tr>
            <tr>
            <td style="text-align: center;">wing<em>n</em>, wash*</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">wing_n_wash_</td>
            </tr>
            <tr>
            <td style="text-align: center;" colspan="3">Ground effect (lift) from stabilizers (<code>grnd effect lift, stabs</code>)</td>
            </tr>
            <tr>
            <td style="text-align: center;">hstab, L cl*</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">hstab_L_cl_</td>
            </tr>
            <tr>
            <td style="text-align: center;">hstab, R cl*</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">hstab_R_cl_</td>
            </tr>
            <tr>
            <td style="text-align: center;">vstb1, cl*</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">vstb1_cl_</td>
            </tr>
            <tr>
            <td style="text-align: center;" colspan="3">Ground effect (drag) from stabilizers (<code>grnd effect drag, stabs</code>)</td>
            </tr>
            <tr>
            <td style="text-align: center;">hstab, Lcdi*</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">hstab_Lcdi_</td>
            </tr>
            <tr>
            <td style="text-align: center;">hstab, Rcdi*</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">hstab_Rcd</td>
            </tr>
            <tr>
            <td style="text-align: center;">vstb<em>n</em>, cdi*</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">vstb_n_cdi_</td>
            </tr>
            <tr>
            <td style="text-align: center;" colspan="3">Ground effect (wash) from stabilizers (<code>grnd effect wash, stabs</code>)</td>
            </tr>
            <tr>
            <td style="text-align: center;">hstab, wash*</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">hstab_wash_</td>
            </tr>
            <tr>
            <td style="text-align: center;">vstb<em>n</em>, wash*</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">vstb_n_wash_</td>
            </tr>
            <tr>
            <td style="text-align: center;" colspan="3">Ground effect (lift) from propellers (<code>grnd effect lift, props</code>)</td>
            </tr>
            <tr>
            <td style="text-align: center;">prop<em>n</em>, cl*</td>
            <td style="text-align: left;"></td>
            <td style="text-align: left;">prop_n_cl_</td>
            </tr>
            <tr>
            <td style="text-align: center;" colspan="3">Ground effect (drag) from propellers (<code>grnd effect drag, props</code>)</td>
            </tr>
            <tr>
            <td style="text-align: center;">prop<em>n</em>, cdi*</td>
            <td style="text-align: left;"></td>
            <td style="text-align: left;">prop_n_cdi_</td>
            </tr>
            <tr>
            <td style="text-align: center;" colspan="3"><code>Wing lift</code></td>
            </tr>
            <tr>
            <td style="text-align: center;">wing<em>n</em>, lift</td>
            <td style="text-align: left;">The lift generated by wing <em>n</em>.</td>
            <td style="text-align: left;">wing_n_lift</td>
            </tr>
            <tr>
            <td style="text-align: center;" colspan="3"><code>Wing drag</code></td>
            </tr>
            <tr>
            <td style="text-align: center;">wing<em>n</em>, drag</td>
            <td style="text-align: left;">The drag generated by wing <em>n</em>.</td>
            <td style="text-align: left;">wing_n_drag</td>
            </tr>
            <tr>
            <td style="text-align: center;" colspan="3">Stabilizer lift (<code>stab lift</code>)</td>
            </tr>
            <tr>
            <td style="text-align: center;">hstab, lift</td>
            <td style="text-align: left;">The lift generated by the horizontal stabilizer.</td>
            <td style="text-align: left;">hstab_lift</td>
            </tr>
            <tr>
            <td style="text-align: center;">vstb<em>n</em>, lift</td>
            <td style="text-align: left;">The lift generated by the vertical stabilizer.</td>
            <td style="text-align: left;">vstb_n_lift</td>
            </tr>
            <tr>
            <td style="text-align: center;" colspan="3">Stabilizer drag (<code>stab drag</code>)</td>
            </tr>
            <tr>
            <td style="text-align: center;">hstab, drag</td>
            <td style="text-align: left;">The drag generated by the horizontal stabilizer.</td>
            <td style="text-align: left;">hstab_drag</td>
            </tr>
            <tr>
            <td style="text-align: center;">vstb<em>n</em>, drag</td>
            <td style="text-align: left;">The drag generated by the vertical stabilizer.</td>
            <td style="text-align: left;">vstb_n_drag</td>
            </tr>
            <tr>
            <td style="text-align: center;" colspan="3"><code>COM 1/2 frequency</code></td>
            </tr>
            <tr>
            <td style="text-align: center;">COM <em>n</em>, freq</td>
            <td style="text-align: left;">The current frequency of the COM <em>n</em> radio.</td>
            <td style="text-align: left;">COM_n_freq</td>
            </tr>
            <tr>
            <td style="text-align: center;">COM <em>n</em>, stby</td>
            <td style="text-align: left;">The standby frequency of the COM <em>n</em> radio.</td>
            <td style="text-align: left;">COM_n_stby</td>
            </tr>
            <tr>
            <td style="text-align: center;">COM, xmt</td>
            <td style="text-align: left;">The transmit status of the COM <em>n</em>.</td>
            <td style="text-align: left;">COM_xmt</td>
            </tr>
            <tr>
            <td style="text-align: center;" colspan="3"><code>NAV 1/2 frequency</code></td>
            </tr>
            <tr>
            <td style="text-align: center;">NAV <em>n</em>, freq</td>
            <td style="text-align: left;">The current frequency of the NAV <em>n</em> radio.</td>
            <td style="text-align: left;">NAV_n_freq</td>
            </tr>
            <tr>
            <td style="text-align: center;">NAV <em>n</em>, stby</td>
            <td style="text-align: left;">The standby frequency of the NAV <em>n</em> radio.</td>
            <td style="text-align: left;">NAV_n_stby</td>
            </tr>
            <tr>
            <td style="text-align: center;">NAV <em>n</em>, type</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">NAV_n_type</td>
            </tr>
            <tr>
            <td style="text-align: center;" colspan="3"><code>NAV 1/2 OBS</code></td>
            </tr>
            <tr>
            <td style="text-align: center;">NAV <em>n</em>, OBS</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">NAV_n_OBS</td>
            </tr>
            <tr>
            <td style="text-align: center;">NAV <em>n</em>, s-crs</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">NAV_n_s_crs</td>
            </tr>
            <tr>
            <td style="text-align: center;">NAV <em>n</em>, flag</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">NAV_n_flag</td>
            </tr>
            <tr>
            <td style="text-align: center;" colspan="3">NAV <em>n</em> deflections</td>
            </tr>
            <tr>
            <td style="text-align: center;">NAV <em>n</em>, n-typ</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">NAV_n_n_typ</td>
            </tr>
            <tr>
            <td style="text-align: center;">NAV <em>n</em>, to-fr</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">NAV_n_to_fr</td>
            </tr>
            <tr>
            <td style="text-align: center;">NAV <em>n</em>, m-crs</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">NAV_n_m_crs</td>
            </tr>
            <tr>
            <td style="text-align: center;">NAV <em>n</em>, r-brg</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">NAV_n_r_brg</td>
            </tr>
            <tr>
            <td style="text-align: center;">NAV <em>n</em>, dme-d</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">NAV_n_dme_d</td>
            </tr>
            <tr>
            <td style="text-align: center;">NAV <em>n</em>, h-def</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">NAV_n_h_def</td>
            </tr>
            <tr>
            <td style="text-align: center;">NAV <em>n</em>, v-def</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">NAV_n_v_def</td>
            </tr>
            <tr>
            <td style="text-align: center;" colspan="3"><code>ADF 1/2 status</code></td>
            </tr>
            <tr>
            <td style="text-align: center;">ADF <em>n</em>, freq</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">ADF_n_freq</td>
            </tr>
            <tr>
            <td style="text-align: center;">ADF <em>n</em>, card</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">ADF_n_card</td>
            </tr>
            <tr>
            <td style="text-align: center;">ADF <em>n</em>, r-brg</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">ADF_n_r_brg</td>
            </tr>
            <tr>
            <td style="text-align: center;">ADF <em>n</em>, n-typ</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">ADF_n_n_typ</td>
            </tr>
            <tr>
            <td style="text-align: center;" colspan="3"><code>DME status</code></td>
            </tr>
            <tr>
            <td style="text-align: center;">DME, nav01</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">DME_nav01</td>
            </tr>
            <tr>
            <td style="text-align: center;">DME, mode</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">DME_mode</td>
            </tr>
            <tr>
            <td style="text-align: center;">DME, found</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">DME_found</td>
            </tr>
            <tr>
            <td style="text-align: center;">DME, dist</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">DME_dist</td>
            </tr>
            <tr>
            <td style="text-align: center;">DME, speed</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">DME_speed</td>
            </tr>
            <tr>
            <td style="text-align: center;">DME, time</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">DME_time</td>
            </tr>
            <tr>
            <td style="text-align: center;">DME, n-typ</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">DME_n_type</td>
            </tr>
            <tr>
            <td style="text-align: center;">DME–3, freq</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">DME_3_freq</td>
            </tr>
            <tr>
            <td style="text-align: center;" colspan="3"><code>GPS status</code></td>
            </tr>
            <tr>
            <td style="text-align: center;">GPS, mode</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">GPS_mode</td>
            </tr>
            <tr>
            <td style="text-align: center;">GPS, index</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">GPS_index</td>
            </tr>
            <tr>
            <td style="text-align: center;">dist, nm</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">dist_nm</td>
            </tr>
            <tr>
            <td style="text-align: center;">OBS, mag</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">OBS_mag</td>
            </tr>
            <tr>
            <td style="text-align: center;">crs, mag</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">crs_mag</td>
            </tr>
            <tr>
            <td style="text-align: center;">rel, brng</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">rel_brng</td>
            </tr>
            <tr>
            <td style="text-align: center;">hdef, dots</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">hdef_dots</td>
            </tr>
            <tr>
            <td style="text-align: center;">vdef, dots</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">vdef_dots</td>
            </tr>
            <tr>
            <td style="text-align: center;" colspan="3">Transponder status (<code>XPNDR status</code>)</td>
            </tr>
            <tr>
            <td style="text-align: center;">trans, mode</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">trans_mode</td>
            </tr>
            <tr>
            <td style="text-align: center;">trans, sett</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">trans_sett</td>
            </tr>
            <tr>
            <td style="text-align: center;">trans, ID</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">trans_ID</td>
            </tr>
            <tr>
            <td style="text-align: center;">trans, inter</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">trans_inter</td>
            </tr>
            <tr>
            <td style="text-align: center;" colspan="3"><code>Marker status</code></td>
            </tr>
            <tr>
            <td style="text-align: center;">OM, morse</td>
            <td style="text-align: left;">Signal from outer marker (OM)</td>
            <td style="text-align: left;">OM_morse</td>
            </tr>
            <tr>
            <td style="text-align: center;">MM, morse</td>
            <td style="text-align: left;">Signal from middle marker (MM)</td>
            <td style="text-align: left;">MM_morse</td>
            </tr>
            <tr>
            <td style="text-align: center;">IM, morse</td>
            <td style="text-align: left;">Signal from inner marker (IM)</td>
            <td style="text-align: left;">IM_morse</td>
            </tr>
            <tr>
            <td style="text-align: center;">audio, activ</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">audio_activ</td>
            </tr>
            <tr>
            <td style="text-align: center;" colspan="3"><code>Switches 1: electrical</code></td>
            </tr>
            <tr>
            <td style="text-align: center;">avio, 0/1</td>
            <td style="text-align: left;">The status of the AVIO switch.</td>
            <td style="text-align: left;">avio_0_1</td>
            </tr>
            <tr>
            <td style="text-align: center;">nav, lite</td>
            <td style="text-align: left;">The status of the navigation light switch.</td>
            <td style="text-align: left;">nav_lite</td>
            </tr>
            <tr>
            <td style="text-align: center;">beacn, lite</td>
            <td style="text-align: left;">The status of the beacon switch.</td>
            <td style="text-align: left;">beacn_lite</td>
            </tr>
            <tr>
            <td style="text-align: center;">strob, lite</td>
            <td style="text-align: left;">The status of the strobe light switch.</td>
            <td style="text-align: left;">strob_lite</td>
            </tr>
            <tr>
            <td style="text-align: center;">land, lite</td>
            <td style="text-align: left;">The status of the landing light switch.</td>
            <td style="text-align: left;">land_lite</td>
            </tr>
            <tr>
            <td style="text-align: center;">taxi, lite</td>
            <td style="text-align: left;">The status of the taxi light switch.</td>
            <td style="text-align: left;">taxi_lite</td>
            </tr>
            <tr>
            <td style="text-align: center;" colspan="3"><code>Switches 2: EFIS</code></td>
            </tr>
            <tr>
            <td style="text-align: center;">ECAM, mode</td>
            <td style="text-align: left;">The ECAM mode.</td>
            <td style="text-align: left;">ECAM_mode</td>
            </tr>
            <tr>
            <td style="text-align: center;">EFIS, sel <em>n</em></td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">EFIS_sel_n</td>
            </tr>
            <tr>
            <td style="text-align: center;">HSI, sel <em>n</em></td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">HSI_sel_n</td>
            </tr>
            <tr>
            <td style="text-align: center;">HSI, arc</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">HSI_arc</td>
            </tr>
            <tr>
            <td style="text-align: center;">map, r-sel</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">map_r_sel</td>
            </tr>
            <tr>
            <td style="text-align: center;">map, range</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">map_range</td>
            </tr>
            <tr>
            <td style="text-align: center;" colspan="3">Switches 3: Autopilot, flight director, and head-up display (<code>switches 3: AP/f-dir/HUD</code>)</td>
            </tr>
            <tr>
            <td style="text-align: center;">ap, src</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">ap_src</td>
            </tr>
            <tr>
            <td style="text-align: center;">fdir, mode</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">fdir_mode</td>
            </tr>
            <tr>
            <td style="text-align: center;">fdir, ptch</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">fdir_ptch</td>
            </tr>
            <tr>
            <td style="text-align: center;">fdir, roll</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">fdir_roll</td>
            </tr>
            <tr>
            <td style="text-align: center;">HUD, power</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">HUD_power</td>
            </tr>
            <tr>
            <td style="text-align: center;">HUD, brite</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">HUD_brite</td>
            </tr>
            <tr>
            <td style="text-align: center;" colspan="3"><code>Switches 4: anti-ice</code></td>
            </tr>
            <tr>
            <td style="text-align: center;">deice, all</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">deice_all</td>
            </tr>
            <tr>
            <td style="text-align: center;">deice, inlet</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">deice_inlet</td>
            </tr>
            <tr>
            <td style="text-align: center;">deice, prop</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">deice_prop</td>
            </tr>
            <tr>
            <td style="text-align: center;">deice, windo</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">deice_windo</td>
            </tr>
            <tr>
            <td style="text-align: center;">deice-<em>n</em>, pitot</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">deice_n_pitot</td>
            </tr>
            <tr>
            <td style="text-align: center;">deice, AOA</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">deice_AOA</td>
            </tr>
            <tr>
            <td style="text-align: center;">deice, wing</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">deice_wing</td>
            </tr>
            <tr>
            <td style="text-align: center;" colspan="3"><code>Switches 5: anti-ice/fuel</code></td>
            </tr>
            <tr>
            <td style="text-align: center;">alt, air<em>n</em></td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">alt_air_n</td>
            </tr>
            <tr>
            <td style="text-align: center;">auto, ignit</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">auto_ignit</td>
            </tr>
            <tr>
            <td style="text-align: center;">manul, ignit</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">manul_ignit</td>
            </tr>
            <tr>
            <td style="text-align: center;">l-eng, tank</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">l_eng_tank</td>
            </tr>
            <tr>
            <td style="text-align: center;">r-eng, tank</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">r_eng_tank</td>
            </tr>
            <tr>
            <td style="text-align: center;" colspan="3">Switches 6: clutch and artificial stability (<code>switches 6: clutch/astab</code>)</td>
            </tr>
            <tr>
            <td style="text-align: center;">prero, engag</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">prero_engag</td>
            </tr>
            <tr>
            <td style="text-align: center;">clutc, ratio</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">clutc_ratio</td>
            </tr>
            <tr>
            <td style="text-align: center;">art, ptch</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">art_ptch</td>
            </tr>
            <tr>
            <td style="text-align: center;">art, roll</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">art_roll</td>
            </tr>
            <tr>
            <td style="text-align: center;">yaw, damp</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">yaw_damp</td>
            </tr>
            <tr>
            <td style="text-align: center;">auto, brake</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">auto_brake</td>
            </tr>
            <tr>
            <td style="text-align: center;" colspan="3">Switches 7: miscellaneous (<code>switches 7: misc</code>)</td>
            </tr>
            <tr>
            <td style="text-align: center;">tot, energ</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">tot_energ</td>
            </tr>
            <tr>
            <td style="text-align: center;">radal, feet</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">radal_feet</td>
            </tr>
            <tr>
            <td style="text-align: center;">prop, sync</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">prop_sync</td>
            </tr>
            <tr>
            <td style="text-align: center;">fethr, mode</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">fethr_mode</td>
            </tr>
            <tr>
            <td style="text-align: center;">puffr, power</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">puffr_power</td>
            </tr>
            <tr>
            <td style="text-align: center;">water, scoop</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">water_scoop</td>
            </tr>
            <tr>
            <td style="text-align: center;">arrst, hook</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">arrst_hook</td>
            </tr>
            <tr>
            <td style="text-align: center;">chute, deply</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">chute_deply</td>
            </tr>
            <tr>
            <td style="text-align: center;" colspan="3"><code>Annunciators: general</code></td>
            </tr>
            <tr>
            <td style="text-align: center;">mast, cau</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">mast_cau</td>
            </tr>
            <tr>
            <td style="text-align: center;">mast, war</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">mast_war</td>
            </tr>
            <tr>
            <td style="text-align: center;">mast, accp</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">mast_accp</td>
            </tr>
            <tr>
            <td style="text-align: center;">auto, disco</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">auto_disco</td>
            </tr>
            <tr>
            <td style="text-align: center;">low, vacum</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">low_vacum</td>
            </tr>
            <tr>
            <td style="text-align: center;">low, volt</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">low_volt</td>
            </tr>
            <tr>
            <td style="text-align: center;">fuel, quant</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">fuel_quant</td>
            </tr>
            <tr>
            <td style="text-align: center;">hyd, press</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">hyd_press</td>
            </tr>
            <tr>
            <td style="text-align: center;" colspan="3"><code>Annunciators: general</code></td>
            </tr>
            <tr>
            <td style="text-align: center;">yawda, on</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">yawda_on</td>
            </tr>
            <tr>
            <td style="text-align: center;">sbrk, on</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">sbrk_on</td>
            </tr>
            <tr>
            <td style="text-align: center;">GPWS, warn</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">GPWS_warn</td>
            </tr>
            <tr>
            <td style="text-align: center;">ice, warn</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">ice_warn</td>
            </tr>
            <tr>
            <td style="text-align: center;">pitot, off</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">pitot_off</td>
            </tr>
            <tr>
            <td style="text-align: center;">cabin, althi</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">cabin_althi</td>
            </tr>
            <tr>
            <td style="text-align: center;">afthr, arm</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">afthr_arm</td>
            </tr>
            <tr>
            <td style="text-align: center;">ospd, time</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">ospd_time</td>
            </tr>
            <tr>
            <td style="text-align: center;" colspan="3"><code>Annunciators: engine</code></td>
            </tr>
            <tr>
            <td style="text-align: center;">fuel, press</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">fuel_press</td>
            </tr>
            <tr>
            <td style="text-align: center;">oil, press</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">oil_press</td>
            </tr>
            <tr>
            <td style="text-align: center;">oil, temp</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">oil_temp</td>
            </tr>
            <tr>
            <td style="text-align: center;">inver, warn</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">inver_warn</td>
            </tr>
            <tr>
            <td style="text-align: center;">gener, warn</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">gener_warn</td>
            </tr>
            <tr>
            <td style="text-align: center;">chip, detec</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">chip_detec</td>
            </tr>
            <tr>
            <td style="text-align: center;">engin, fire</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">engin_fire</td>
            </tr>
            <tr>
            <td style="text-align: center;">ignit, 0/1</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">ignit_0_1</td>
            </tr>
            <tr>
            <td style="text-align: center;" colspan="3">Armed autopilot functions (<code>autopilot arms</code>)</td>
            </tr>
            <tr>
            <td style="text-align: center;">nav, arm</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">nav_arm</td>
            </tr>
            <tr>
            <td style="text-align: center;">alt, arm</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">alt_arm</td>
            </tr>
            <tr>
            <td style="text-align: center;">app, arm</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">app_arm</td>
            </tr>
            <tr>
            <td style="text-align: center;">vnav, enab</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">vnav_enab</td>
            </tr>
            <tr>
            <td style="text-align: center;">vnav, arm</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">vnav_arm</td>
            </tr>
            <tr>
            <td style="text-align: center;">vnav, time</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">vnav_time</td>
            </tr>
            <tr>
            <td style="text-align: center;">gp, enabl</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">gp_enabl</td>
            </tr>
            <tr>
            <td style="text-align: center;">app, typ</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">app_typ</td>
            </tr>
            <tr>
            <td style="text-align: center;" colspan="3"><code>Autopilot modes</code></td>
            </tr>
            <tr>
            <td style="text-align: center;">auto, throt</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">auto_throt</td>
            </tr>
            <tr>
            <td style="text-align: center;">mode, hding</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">mode_hding</td>
            </tr>
            <tr>
            <td style="text-align: center;">mode, alt</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">mode_alt</td>
            </tr>
            <tr>
            <td style="text-align: center;">bac, 0/1</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">bac_0_1</td>
            </tr>
            <tr>
            <td style="text-align: center;">app,</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">app_</td>
            </tr>
            <tr>
            <td style="text-align: center;">sync, butn</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">sync_butn</td>
            </tr>
            <tr>
            <td style="text-align: center;" colspan="3"><code>Autopilot values</code></td>
            </tr>
            <tr>
            <td style="text-align: center;">set, speed</td>
            <td style="text-align: left;">The desired speed setting for the autopilot.</td>
            <td style="text-align: left;">set_speed</td>
            </tr>
            <tr>
            <td style="text-align: center;">set, hding</td>
            <td style="text-align: left;">The desired heading setting for the autopilot.</td>
            <td style="text-align: left;">set_hding</td>
            </tr>
            <tr>
            <td style="text-align: center;">set, vvi</td>
            <td style="text-align: left;">The desired vertical velocity setting for the autopilot.</td>
            <td style="text-align: left;">set_vvi</td>
            </tr>
            <tr>
            <td style="text-align: center;">dial, alt</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">dial_alt</td>
            </tr>
            <tr>
            <td style="text-align: center;">vnav, alt</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">vnav_alt</td>
            </tr>
            <tr>
            <td style="text-align: center;">use, alt</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">use_alt</td>
            </tr>
            <tr>
            <td style="text-align: center;">sync, roll</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">sync_roll</td>
            </tr>
            <tr>
            <td style="text-align: center;">sync, pitch</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">sync_pitch</td>
            </tr>
            <tr>
            <td style="text-align: center;" colspan="3"><code>Weapon status</code></td>
            </tr>
            <tr>
            <td style="text-align: center;">hdng, delta</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">hdng_delta</td>
            </tr>
            <tr>
            <td style="text-align: center;">pitch, delta</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">pitch_delta</td>
            </tr>
            <tr>
            <td style="text-align: center;">R, d/sec</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">R_d_sec</td>
            </tr>
            <tr>
            <td style="text-align: center;">Q, d/sec</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">Q_d_sec</td>
            </tr>
            <tr>
            <td style="text-align: center;">rudd, ratio</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">rudd_ratio</td>
            </tr>
            <tr>
            <td style="text-align: center;">elev, ratio</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">elev_ratio</td>
            </tr>
            <tr>
            <td style="text-align: center;">V, kts</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">V_kts</td>
            </tr>
            <tr>
            <td style="text-align: center;">dis, ft</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">dist_ft</td>
            </tr>
            <tr>
            <td style="text-align: center;" colspan="3"><code>Pressurization status</code></td>
            </tr>
            <tr>
            <td style="text-align: center;">alt, set</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">alt_set</td>
            </tr>
            <tr>
            <td style="text-align: center;">vvi, set</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">vvi_set</td>
            </tr>
            <tr>
            <td style="text-align: center;">alt, act</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">alt_act</td>
            </tr>
            <tr>
            <td style="text-align: center;">vvi, act</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">vvi_act</td>
            </tr>
            <tr>
            <td style="text-align: center;">test, time</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">test_time</td>
            </tr>
            <tr>
            <td style="text-align: center;">diff, psi</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">diff_psi</td>
            </tr>
            <tr>
            <td style="text-align: center;">dump, all</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">dump_all</td>
            </tr>
            <tr>
            <td style="text-align: center;">bleed, src</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">bleed_src</td>
            </tr>
            <tr>
            <td style="text-align: center;" colspan="3">Auxiliary power unit and ground power unit status (<code>APU/GPU status</code>)</td>
            </tr>
            <tr>
            <td style="text-align: center;">APU, eqipd</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">APU_eqipd</td>
            </tr>
            <tr>
            <td style="text-align: center;">APU, swtch</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">APU_swtch</td>
            </tr>
            <tr>
            <td style="text-align: center;">APU, runng</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">APU_runng</td>
            </tr>
            <tr>
            <td style="text-align: center;">APU, N1</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">APU_N1</td>
            </tr>
            <tr>
            <td style="text-align: center;">APU, genrt</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">APU_genrt</td>
            </tr>
            <tr>
            <td style="text-align: center;">GPU, power</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">GPU_power</td>
            </tr>
            <tr>
            <td style="text-align: center;" colspan="3"><code>Radar status</code></td>
            </tr>
            <tr>
            <td style="text-align: center;">targ, selct</td>
            <td style="text-align: left;">The status of the target selection.</td>
            <td style="text-align: left;">targ_selct</td>
            </tr>
            <tr>
            <td style="text-align: center;" colspan="3"><code>Hydraulic status</code></td>
            </tr>
            <tr>
            <td style="text-align: center;">hydr, pump<em>n</em></td>
            <td style="text-align: left;">The status of hydraulic pump <em>n</em>.</td>
            <td style="text-align: left;">hydr_pump_n</td>
            </tr>
            <tr>
            <td style="text-align: center;">hydr, qty<em>n</em></td>
            <td style="text-align: left;">The hydraulic fluid in pump <em>n</em>.</td>
            <td style="text-align: left;">hydr_qty_n</td>
            </tr>
            <tr>
            <td style="text-align: center;">hydr, pres<em>n</em></td>
            <td style="text-align: left;">The pressure of hydraulic pump <em>n</em>.</td>
            <td style="text-align: left;">hydr_pres_n</td>
            </tr>
            <tr>
            <td style="text-align: center;" colspan="3">Electrical and solar power status (<code>elec &amp; solar status</code>)</td>
            </tr>
            <tr>
            <td style="text-align: center;">bus<em>n</em>, amp</td>
            <td style="text-align: left;">Bus <em>n</em>’s amperage.</td>
            <td style="text-align: left;">bus_n_amp</td>
            </tr>
            <tr>
            <td style="text-align: center;">bus<em>n</em>, volt</td>
            <td style="text-align: left;">Bus <em>n</em>’s voltage.</td>
            <td style="text-align: left;">bus_n_volt</td>
            </tr>
            <tr>
            <td style="text-align: center;">engin, in W</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">engin_in_W</td>
            </tr>
            <tr>
            <td style="text-align: center;">solar, out W</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">solar_out_W</td>
            </tr>
            <tr>
            <td style="text-align: center;">batt, w-hr</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">batt_w_hr</td>
            </tr>
            <tr>
            <td style="text-align: center;">Cross, tie</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">Cross_tie</td>
            </tr>
            <tr>
            <td style="text-align: center;" colspan="3"><code>Icing status 1</code></td>
            </tr>
            <tr>
            <td style="text-align: center;">inlet, ice</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">inlet_ice</td>
            </tr>
            <tr>
            <td style="text-align: center;">prop, ice</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">prop_ice</td>
            </tr>
            <tr>
            <td style="text-align: center;">pitot, ice</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">pitot_ice</td>
            </tr>
            <tr>
            <td style="text-align: center;">statc, ice</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">statc_ice</td>
            </tr>
            <tr>
            <td style="text-align: center;" colspan="3"><code>Icing status 2</code></td>
            </tr>
            <tr>
            <td style="text-align: center;">aoa, ice</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">aoa_ice</td>
            </tr>
            <tr>
            <td style="text-align: center;">lwing, ice</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">lwing_ice</td>
            </tr>
            <tr>
            <td style="text-align: center;">rwing, ice</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">rwing_ice</td>
            </tr>
            <tr>
            <td style="text-align: center;">windo, ice</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">windo_ice</td>
            </tr>
            <tr>
            <td style="text-align: center;" colspan="3"><code>Warning status</code></td>
            </tr>
            <tr>
            <td style="text-align: center;">warn, time</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">warn_time</td>
            </tr>
            <tr>
            <td style="text-align: center;">caut, time</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">caut_time</td>
            </tr>
            <tr>
            <td style="text-align: center;">warn, work</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">warn_work</td>
            </tr>
            <tr>
            <td style="text-align: center;">caut, work</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">caut_work</td>
            </tr>
            <tr>
            <td style="text-align: center;">gear, work</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">gear_work</td>
            </tr>
            <tr>
            <td style="text-align: center;">gear, warn</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">gear_warn</td>
            </tr>
            <tr>
            <td style="text-align: center;">stall, warn</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">stall_warn</td>
            </tr>
            <tr>
            <td style="text-align: center;">VRS, ratio</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">VRS_ratio</td>
            </tr>
            <tr>
            <td style="text-align: center;" colspan="3">Flight plan legs (<code>flite-plan legs</code>)</td>
            </tr>
            <tr>
            <td style="text-align: center;">leg, #</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">leg__</td>
            </tr>
            <tr>
            <td style="text-align: center;">leg, type</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">leg_type</td>
            </tr>
            <tr>
            <td style="text-align: center;">leg, lat</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">leg_lat</td>
            </tr>
            <tr>
            <td style="text-align: center;">leg, lon</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">leg_lon</td>
            </tr>
            <tr>
            <td style="text-align: center;" colspan="3"><code>Hardware options</code></td>
            </tr>
            <tr>
            <td style="text-align: center;">pedal, nobrk</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">pedal_nobrk</td>
            </tr>
            <tr>
            <td style="text-align: center;">pedal, wibrk</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">pedal_wibrk</td>
            </tr>
            <tr>
            <td style="text-align: center;">yoke, PFC</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">yoke_PFC</td>
            </tr>
            <tr>
            <td style="text-align: center;">pedal, PFC</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">pedal_PFC</td>
            </tr>
            <tr>
            <td style="text-align: center;">throt, PFC</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">throt_PFC</td>
            </tr>
            <tr>
            <td style="text-align: center;">cecon, PFC</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">cecon_PFC</td>
            </tr>
            <tr>
            <td style="text-align: center;">switc, PFC</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">switc_PFC</td>
            </tr>
            <tr>
            <td style="text-align: center;">btogg, PFC</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">btogg_PFC</td>
            </tr>
            <tr>
            <td style="text-align: center;" colspan="3"><code>Camera location</code></td>
            </tr>
            <tr>
            <td style="text-align: center;">camra, lon</td>
            <td style="text-align: left;">The camera’s longitudinal location.</td>
            <td style="text-align: left;">camra_lon</td>
            </tr>
            <tr>
            <td style="text-align: center;">camra, lat</td>
            <td style="text-align: left;">The camera’s latitudinal location.</td>
            <td style="text-align: left;">camra_lat</td>
            </tr>
            <tr>
            <td style="text-align: center;">camra, ele</td>
            <td style="text-align: left;">The camera’s elevation.</td>
            <td style="text-align: left;">camra_ele</td>
            </tr>
            <tr>
            <td style="text-align: center;">camra, hdg</td>
            <td style="text-align: left;">The camera’s heading.</td>
            <td style="text-align: left;">camra_hdg</td>
            </tr>
            <tr>
            <td style="text-align: center;">camra, pitch</td>
            <td style="text-align: left;">The camera’s pitch.</td>
            <td style="text-align: left;">camra_pitch</td>
            </tr>
            <tr>
            <td style="text-align: center;">camra, roll</td>
            <td style="text-align: left;">The camera’s roll.</td>
            <td style="text-align: left;">camra_roll</td>
            </tr>
            <tr>
            <td style="text-align: center;">camra, clou</td>
            <td style="text-align: left;">The camera’s cloud cover.</td>
            <td style="text-align: left;">camra_clou</td>
            </tr>
            <tr>
            <td style="text-align: center;" colspan="3"><code>Ground location</code></td>
            </tr>
            <tr>
            <td style="text-align: center;">cntr, X</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">cntr_X</td>
            </tr>
            <tr>
            <td style="text-align: center;">cntr, Y</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">cntr_Y</td>
            </tr>
            <tr>
            <td style="text-align: center;">cntr, Z</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">cntr_Z</td>
            </tr>
            <tr>
            <td style="text-align: center;">slope, X</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">slope_X</td>
            </tr>
            <tr>
            <td style="text-align: center;">slope, Z</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">slope_Z</td>
            </tr>
            <tr>
            <td style="text-align: center;" colspan="3">Climb statistics (<code>climb stats</code>)</td>
            </tr>
            <tr>
            <td style="text-align: center;">h-spd, kt</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">h_spd_kt</td>
            </tr>
            <tr>
            <td style="text-align: center;">v-spd, fpm</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">v_spd_fpm</td>
            </tr>
            <tr>
            <td style="text-align: center;">mult, VxVVI</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">mult_VxVVI</td>
            </tr>
            <tr>
            <td style="text-align: center;" colspan="3">Cruise statistics (<code>cruise stats</code>)</td>
            </tr>
            <tr>
            <td style="text-align: center;">ff, pph</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">ff_pph</td>
            </tr>
            <tr>
            <td style="text-align: center;">ff, gph</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">ff_gph</td>
            </tr>
            <tr>
            <td style="text-align: center;">speed, mph</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">speed_mph</td>
            </tr>
            <tr>
            <td style="text-align: center;">eta, smpg</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">eta_smpg</td>
            </tr>
            <tr>
            <td style="text-align: center;">eta, nm/lb</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">eta_nm_lb</td>
            </tr>
            <tr>
            <td style="text-align: center;">range, sm</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">range_sm</td>
            </tr>
            <tr>
            <td style="text-align: center;">endur, hours</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">endur_hours</td>
            </tr>
            <tr>
            <td style="text-align: center;">mult, VxMPG</td>
            <td style="text-align: left;">•</td>
            <td style="text-align: left;">mult_VxMPG</td>
            </tr>
            </tbody>
            </table>

</details>

