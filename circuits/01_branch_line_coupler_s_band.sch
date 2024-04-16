<Qucs Schematic 24.2.1>
<Properties>
  <View=-1812,-115,2322,1470,0.593325,762,0>
  <Grid=10,10,1>
  <DataSet=01_branch_line_coupler_s_band.dat>
  <DataDisplay=01_branch_line_coupler_s_band.dpl>
  <OpenDisplay=0>
  <Script=01_branch_line_coupler_s_band.m>
  <RunScript=0>
  <showFrame=0>
  <FrameText0=Название>
  <FrameText1=Чертил:>
  <FrameText2=Дата:>
  <FrameText3=Версия:>
</Properties>
<Symbol>
</Symbol>
<Components>
  <SUBST Ro4350b 1 160 140 -30 24 0 0 "3.48" 1 "0.508 mm" 1 "18 um" 1 "2e-4" 1 "0.022e-6" 1 "0.15e-6" 1>
  <.SP SP1 1 310 110 0 79 0 0 "lin" 1 "1.9 GHz" 1 "2.5 GHz" 1 "201" 1 "no" 0 "1" 0 "2" 0 "no" 0 "no" 0>
  <Eqn Eqn1 1 590 120 -40 18 0 0 "w1=1.13e-3" 1 "l1=20.2e-3" 1 "w2=1.91e-3" 1 "l2=l1" 1 "db_S21=dB(S[2,1])" 1 "ph_S21=rad2deg(unwrap(arg(S[2,1])))" 1 "ph_S31=rad2deg(unwrap(arg(S[3,1])))" 1 "db_S31=dB(S[3,1])" 1 "db_S32=dB(S[3,2])" 1 "db_S11=dB(S[1,1])" 1 "yes" 1>
  <Pac P2 1 740 550 18 -26 0 1 "2" 1 "50 Ohm" 1 "0 dBm" 0 "1 MHz" 0 "26.85" 0 "true" 0>
  <GND * 1 740 580 0 0 0 0>
  <Pac P3 1 740 760 18 -26 0 1 "3" 1 "50 Ohm" 1 "0 dBm" 0 "1 MHz" 0 "26.85" 0 "true" 0>
  <GND * 1 740 790 0 0 0 0>
  <Pac P4 1 150 750 18 -26 0 1 "4" 1 "50 Ohm" 1 "0 dBm" 0 "1 MHz" 0 "26.85" 0 "true" 0>
  <GND * 1 150 780 0 0 0 0>
  <Pac P1 1 150 560 18 -26 0 1 "1" 1 "50 Ohm" 1 "0 dBm" 0 "1 MHz" 0 "26.85" 0 "true" 0>
  <GND * 1 150 590 0 0 0 0>
  <MLIN MS1 1 420 480 -26 15 0 0 "Ro4350b" 0 "w2" 1 "l2" 1 "Hammerstad" 0 "Kirschning" 0 "26.85" 0>
  <MLIN MS3 1 310 590 -60 -26 0 3 "Ro4350b" 0 "w1" 1 "l1" 1 "Hammerstad" 0 "Kirschning" 0 "26.85" 0>
  <MTEE MS6 1 310 680 -26 15 1 0 "Ro4350b" 0 "w1" 1 "w2" 1 "w1" 1 "Hammerstad" 0 "Kirschning" 0 "26.85" 0 "showNumbers" 0>
  <MLIN MS2 1 420 680 -26 15 0 0 "Ro4350b" 0 "w2" 1 "l2" 1 "Hammerstad" 0 "Kirschning" 0 "26.85" 0>
  <MTEE MS7 1 550 680 -91 15 0 2 "Ro4350b" 0 "w1" 1 "w2" 1 "w1" 1 "Hammerstad" 0 "Kirschning" 0 "26.85" 0 "showNumbers" 0>
  <MLIN MS4 1 550 590 15 -26 0 1 "Ro4350b" 0 "w1" 1 "l1" 1 "Hammerstad" 0 "Kirschning" 0 "26.85" 0>
  <MTEE MS8 1 550 480 -26 -103 1 2 "Ro4350b" 0 "w1" 1 "w2" 1 "w1" 1 "Hammerstad" 0 "Kirschning" 0 "26.85" 0 "showNumbers" 0>
  <MTEE MS5 1 310 480 -26 -103 0 0 "Ro4350b" 0 "w1" 1 "w2" 1 "w1" 1 "Hammerstad" 0 "Kirschning" 0 "26.85" 0 "showNumbers" 0>
</Components>
<Wires>
  <450 680 520 680 "" 0 0 0 "">
  <740 480 740 520 "" 0 0 0 "">
  <740 680 740 730 "" 0 0 0 "">
  <150 680 280 680 "stub" 220 650 41 "">
  <150 680 150 720 "" 0 0 0 "">
  <340 680 390 680 "" 0 0 0 "">
  <580 680 740 680 "out_180" 690 650 75 "">
  <580 480 740 480 "out_90" 690 450 81 "">
  <150 480 280 480 "in" 240 450 50 "">
  <150 480 150 530 "" 0 0 0 "">
  <310 620 310 650 "" 0 0 0 "">
  <310 510 310 560 "" 0 0 0 "">
  <550 510 550 560 "" 0 0 0 "">
  <550 620 550 650 "" 0 0 0 "">
  <450 480 520 480 "" 0 0 0 "">
  <340 480 390 480 "" 0 0 0 "">
</Wires>
<Diagrams>
</Diagrams>
<Paintings>
</Paintings>
