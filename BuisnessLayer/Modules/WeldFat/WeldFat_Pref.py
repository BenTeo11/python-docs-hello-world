# Weld Fatigue Preference V192.6 Ansys R19.2, 2019R1/R2/R3

# Hot-Spot extrapolation defaults
default_stress = 'Normal'
#default_stress = 'Principal'
default_method = 'Linear'
#default_method = 'Quadratic'
default_thickness = 0.0, 'mm'
# Linear method
a_lin = 0.4
b_lin = 1.0
# Quadratic method
a_quad = 0.4
b_quad = 0.9
c_quad = 1.4
AlwaysPlotHotSpot = True
#AlwaysPlotHotSpot = False

# S-N Curve Nominal and Linearized Stress
fat_Nom = 160.0, 'MPa'
Nfat_Nom = 2.0e6
Nc_Nom = 1.0e7
m1_Nom = 5.0
m2_Nom = 22.0

# S-N Curve Hot-Spot Stress
fat_HS = 90.0, 'MPa'
Nfat_HS = 2.0e6
Nc_HS = 1.0e7
m1_HS = 3.0
m2_HS = 22.0

# S-N Curve Effective Notch Stress
fat_R1 = 225.0, 'MPa'
Nfat_R1 = 2.0e6
Nc_R1 = 1.0e7
m1_R1 = 3.0
m2_R1 = 22.0

# Load case definition
#default_loadType = 'Zero Based'
default_loadType = 'Fully Reversed'
#default_loadType = 'Load Combination'
#default_loadType = 'Load Scanning'
default_cycles = 1.0

# FAT Class Dictionary
fatClassDict = {}
fatClassDict['User defined']={'index':0,'Ncutoff':1e10}
# Nominal & Hot-Spot Method steel. Standard application Fig 3.1 [1] (Constant amplitude)
#fatClassDict.Add('IIW FAT160 steel',{'index':1, 'FAT':[160, 'MPa'],'Nfat':2e6,'Nc':1e7,'Ncutoff':1e10,'m1':5,'m2':1e6})
#fatClassDict.Add('IIW FAT125 steel',{'index':2, 'FAT':[125, 'MPa'],'Nfat':2e6,'Nc':1e7,'Ncutoff':1e10,'m1':3,'m2':1e6,'N0':314018,'m0':5})
#fatClassDict.Add('IIW FAT112 steel',{'index':3, 'FAT':[112, 'MPa'],'Nfat':2e6,'Nc':1e7,'Ncutoff':1e10,'m1':3,'m2':1e6,'N0':137805,'m0':5})
#fatClassDict.Add('IIW FAT100 steel',{'index':4, 'FAT':[100, 'MPa'],'Nfat':2e6,'Nc':1e7,'Ncutoff':1e10,'m1':3,'m2':1e6,'N0':58902,'m0':5})
#fatClassDict.Add('IIW FAT90 steel',{'index':5, 'FAT':[90, 'MPa'],'Nfat':2e6,'Nc':1e7,'Ncutoff':1e10,'m1':3,'m2':1e6,'N0':26727,'m0':5})
#fatClassDict.Add('IIW FAT80 steel',{'index':6, 'FAT':[80, 'MPa'],'Nfat':2e6,'Nc':1e7,'Ncutoff':1e10,'m1':3,'m2':1e6,'N0':11049,'m0':5})
#fatClassDict.Add('IIW FAT71 steel',{'index':7, 'FAT':[71, 'MPa'],'Nfat':2e6,'Nc':1e7,'Ncutoff':1e10,'m1':3,'m2':1e6,'N0':4514,'m0':5})
#fatClassDict.Add('IIW FAT63 steel',{'index':8, 'FAT':[63, 'MPa'],'Nfat':2e6,'Nc':1e7,'Ncutoff':1e10,'m1':3,'m2':1e6,'N0':1842,'m0':5})
#fatClassDict.Add('IIW FAT56 steel',{'index':9, 'FAT':[56, 'MPa'],'Nfat':2e6,'Nc':1e7,'Ncutoff':1e10,'m1':3,'m2':1e6,'N0':761,'m0':5})
#fatClassDict.Add('IIW FAT50 steel',{'index':10, 'FAT':[50, 'MPa'],'Nfat':2e6,'Nc':1e7,'Ncutoff':1e10,'m1':3,'m2':1e6,'N0':325,'m0':5})
#fatClassDict.Add('IIW FAT45 steel',{'index':11, 'FAT':[45, 'MPa'],'Nfat':2e6,'Nc':1e7,'Ncutoff':1e10,'m1':3,'m2':1e6,'N0':148,'m0':5})
#fatClassDict.Add('IIW FAT40 steel',{'index':12, 'FAT':[40, 'MPa'],'Nfat':2e6,'Nc':1e7,'Ncutoff':1e10,'m1':3,'m2':1e6,'N0':61,'m0':5})
#fatClassDict.Add('IIW FAT36 steel',{'index':13, 'FAT':[36, 'MPa'],'Nfat':2e6,'Nc':1e7,'Ncutoff':1e10,'m1':3,'m2':1e6,'N0':28,'m0':5})
# Nominal & Hot-Spot Method steel. Very high cycle application Fig 3.2 [1] (Constant amplitude)
fatClassDict['IIW FAT160 steel']={'index':1, 'FAT':[160, 'MPa'],'Nfat':2e6,'Nc':1e7,'Ncutoff':1e10,'m1':5,'m2':22}
fatClassDict['IIW FAT125 steel']={'index':2, 'FAT':[125, 'MPa'],'Nfat':2e6,'Nc':1e7,'Ncutoff':1e10,'m1':3,'m2':22,'N0':314018,'m0':5}
fatClassDict['IIW FAT112 steel']={'index':3, 'FAT':[112, 'MPa'],'Nfat':2e6,'Nc':1e7,'Ncutoff':1e10,'m1':3,'m2':22,'N0':137805,'m0':5}
fatClassDict['IIW FAT100 steel']={'index':4, 'FAT':[100, 'MPa'],'Nfat':2e6,'Nc':1e7,'Ncutoff':1e10,'m1':3,'m2':22,'N0':58902,'m0':5}
fatClassDict['IIW FAT90 steel']={'index':5, 'FAT':[90, 'MPa'],'Nfat':2e6,'Nc':1e7,'Ncutoff':1e10,'m1':3,'m2':22,'N0':26727,'m0':5}
fatClassDict['IIW FAT80 steel']={'index':6, 'FAT':[80, 'MPa'],'Nfat':2e6,'Nc':1e7,'Ncutoff':1e10,'m1':3,'m2':22,'N0':11049,'m0':5}
fatClassDict['IIW FAT71 steel']={'index':7, 'FAT':[71, 'MPa'],'Nfat':2e6,'Nc':1e7,'Ncutoff':1e10,'m1':3,'m2':22,'N0':4514,'m0':5}
fatClassDict['IIW FAT63 steel']={'index':8, 'FAT':[63, 'MPa'],'Nfat':2e6,'Nc':1e7,'Ncutoff':1e10,'m1':3,'m2':22,'N0':1842,'m0':5}
fatClassDict['IIW FAT56 steel']={'index':9, 'FAT':[56, 'MPa'],'Nfat':2e6,'Nc':1e7,'Ncutoff':1e10,'m1':3,'m2':22,'N0':761,'m0':5}
fatClassDict['IIW FAT50 steel']={'index':10, 'FAT':[50, 'MPa'],'Nfat':2e6,'Nc':1e7,'Ncutoff':1e10,'m1':3,'m2':22,'N0':325,'m0':5}
fatClassDict['IIW FAT45 steel']={'index':11, 'FAT':[45, 'MPa'],'Nfat':2e6,'Nc':1e7,'Ncutoff':1e10,'m1':3,'m2':22,'N0':148,'m0':5}
fatClassDict['IIW FAT40 steel']={'index':12, 'FAT':[40, 'MPa'],'Nfat':2e6,'Nc':1e7,'Ncutoff':1e10,'m1':3,'m2':22,'N0':61,'m0':5}
fatClassDict['IIW FAT36 steel']={'index':13, 'FAT':[36, 'MPa'],'Nfat':2e6,'Nc':1e7,'Ncutoff':1e10,'m1':3,'m2':22,'N0':28,'m0':5}
# Nominal & Hot-Spot Method steel. Modified resistance for Palmgren-Miner summation Fig 4.1 [1] (Variable amplitude)
fatClassDict['IIW FAT160 steel vari']={'index':14, 'FAT':[160, 'MPa'],'Nfat':2e6,'Nc':1e7,'Ncutoff':1e10,'m1':5,'m2':9}
fatClassDict['IIW FAT125 steel vari']={'index':15, 'FAT':[125, 'MPa'],'Nfat':2e6,'Nc':1e7,'Ncutoff':1e10,'m1':3,'m2':5,'N0':314018,'m0':5}
fatClassDict['IIW FAT112 steel vari']={'index':16, 'FAT':[112, 'MPa'],'Nfat':2e6,'Nc':1e7,'Ncutoff':1e10,'m1':3,'m2':5,'N0':137805,'m0':5}
fatClassDict['IIW FAT100 steel vari']={'index':17, 'FAT':[100, 'MPa'],'Nfat':2e6,'Nc':1e7,'Ncutoff':1e10,'m1':3,'m2':5,'N0':58902,'m0':5}
fatClassDict['IIW FAT90 steel vari']={'index':18, 'FAT':[90, 'MPa'],'Nfat':2e6,'Nc':1e7,'Ncutoff':1e10,'m1':3,'m2':5,'N0':26727,'m0':5}
fatClassDict['IIW FAT80 steel vari']={'index':19, 'FAT':[80, 'MPa'],'Nfat':2e6,'Nc':1e7,'Ncutoff':1e10,'m1':3,'m2':5,'N0':11049,'m0':5}
fatClassDict['IIW FAT71 steel vari']={'index':20, 'FAT':[71, 'MPa'],'Nfat':2e6,'Nc':1e7,'Ncutoff':1e10,'m1':3,'m2':5,'N0':4514,'m0':5}
fatClassDict['IIW FAT63 steel vari']={'index':21, 'FAT':[63, 'MPa'],'Nfat':2e6,'Nc':1e7,'Ncutoff':1e10,'m1':3,'m2':5,'N0':1842,'m0':5}
fatClassDict['IIW FAT56 steel vari']={'index':22, 'FAT':[56, 'MPa'],'Nfat':2e6,'Nc':1e7,'Ncutoff':1e10,'m1':3,'m2':5,'N0':761,'m0':5}
fatClassDict['IIW FAT50 steel vari']={'index':23, 'FAT':[50, 'MPa'],'Nfat':2e6,'Nc':1e7,'Ncutoff':1e10,'m1':3,'m2':5,'N0':325,'m0':5}
fatClassDict['IIW FAT45 steel vari']={'index':24, 'FAT':[45, 'MPa'],'Nfat':2e6,'Nc':1e7,'Ncutoff':1e10,'m1':3,'m2':5,'N0':148,'m0':5}
fatClassDict['IIW FAT40 steel vari']={'index':25, 'FAT':[40, 'MPa'],'Nfat':2e6,'Nc':1e7,'Ncutoff':1e10,'m1':3,'m2':5,'N0':61,'m0':5}
fatClassDict['IIW FAT36 steel vari']={'index':26, 'FAT':[36, 'MPa'],'Nfat':2e6,'Nc':1e7,'Ncutoff':1e10,'m1':3,'m2':5,'N0':28,'m0':5}
# Nominal & Hot-Spot Method aluminium. Normal stress Fig. 3.3 (Constant amplitude)
fatClassDict['IIW FAT71 aluminium']={'index':27, 'FAT':[71, 'MPa'],'Nfat':2e6,'Nc':1e7,'Ncutoff':1e10,'m1':5,'m2':22}
fatClassDict['IIW FAT50 aluminium']={'index':28, 'FAT':[50, 'MPa'],'Nfat':2e6,'Nc':1e7,'Ncutoff':1e10,'m1':3,'m2':22,'N0':144168,'m0':5}
fatClassDict['IIW FAT45 aluminium']={'index':29, 'FAT':[45, 'MPa'],'Nfat':2e6,'Nc':1e7,'Ncutoff':1e10,'m1':3,'m2':22,'N0':65416,'m0':5}
fatClassDict['IIW FAT40 aluminium']={'index':30, 'FAT':[40, 'MPa'],'Nfat':2e6,'Nc':1e7,'Ncutoff':1e10,'m1':3,'m2':22,'N0':27042,'m0':5}
fatClassDict['IIW FAT36 aluminium']={'index':31, 'FAT':[36, 'MPa'],'Nfat':2e6,'Nc':1e7,'Ncutoff':1e10,'m1':3,'m2':22,'N0':12270,'m0':5}
fatClassDict['IIW FAT32 aluminium']={'index':32, 'FAT':[32, 'MPa'],'Nfat':2e6,'Nc':1e7,'Ncutoff':1e10,'m1':3,'m2':22,'N0':5072,'m0':5}
fatClassDict['IIW FAT28 aluminium']={'index':33, 'FAT':[28, 'MPa'],'Nfat':2e6,'Nc':1e7,'Ncutoff':1e10,'m1':3,'m2':22,'N0':1863,'m0':5}
fatClassDict['IIW FAT25 aluminium']={'index':34, 'FAT':[25, 'MPa'],'Nfat':2e6,'Nc':1e7,'Ncutoff':1e10,'m1':3,'m2':22,'N0':796,'m0':5}
fatClassDict['IIW FAT22 aluminium']={'index':35, 'FAT':[22, 'MPa'],'Nfat':2e6,'Nc':1e7,'Ncutoff':1e10,'m1':3,'m2':22,'N0':305,'m0':5}
fatClassDict['IIW FAT18 aluminium']={'index':36, 'FAT':[18, 'MPa'],'Nfat':2e6,'Nc':1e7,'Ncutoff':1e10,'m1':3,'m2':22,'N0':68,'m0':5}
fatClassDict['IIW FAT16 aluminium']={'index':37, 'FAT':[16, 'MPa'],'Nfat':2e6,'Nc':1e7,'Ncutoff':1e10,'m1':3,'m2':22,'N0':28,'m0':5}
fatClassDict['IIW FAT14 aluminium']={'index':38, 'FAT':[14, 'MPa'],'Nfat':2e6,'Nc':1e7,'Ncutoff':1e10,'m1':3,'m2':22,'N0':10,'m0':5}
fatClassDict['IIW FAT12 aluminium']={'index':39, 'FAT':[12, 'MPa'],'Nfat':2e6,'Nc':1e7,'Ncutoff':1e10,'m1':3,'m2':22,'N0':3,'m0':5}
# Nominal & Hot-Spot Method aluminium. Modified resistance for Palmgren-Miner summation Fig 4.2 [1] (Variable amplitude)
fatClassDict['IIW FAT71 alu vari']={'index':40, 'FAT':[71, 'MPa'],'Nfat':2e6,'Nc':1e7,'Ncutoff':1e10,'m1':5,'m2':9}
fatClassDict['IIW FAT50 alu vari']={'index':41, 'FAT':[50, 'MPa'],'Nfat':2e6,'Nc':1e7,'Ncutoff':1e10,'m1':3,'m2':5,'N0':144168,'m0':5}
fatClassDict['IIW FAT45 alu vari']={'index':42, 'FAT':[45, 'MPa'],'Nfat':2e6,'Nc':1e7,'Ncutoff':1e10,'m1':3,'m2':5,'N0':65416,'m0':5}
fatClassDict['IIW FAT40 alu vari']={'index':43, 'FAT':[40, 'MPa'],'Nfat':2e6,'Nc':1e7,'Ncutoff':1e10,'m1':3,'m2':5,'N0':27042,'m0':5}
fatClassDict['IIW FAT36 alu vari']={'index':44, 'FAT':[36, 'MPa'],'Nfat':2e6,'Nc':1e7,'Ncutoff':1e10,'m1':3,'m2':5,'N0':12270,'m0':5}
fatClassDict['IIW FAT32 alu vari']={'index':45, 'FAT':[32, 'MPa'],'Nfat':2e6,'Nc':1e7,'Ncutoff':1e10,'m1':3,'m2':5,'N0':5072,'m0':5}
fatClassDict['IIW FAT28 alu vari']={'index':46, 'FAT':[28, 'MPa'],'Nfat':2e6,'Nc':1e7,'Ncutoff':1e10,'m1':3,'m2':5,'N0':1863,'m0':5}
fatClassDict['IIW FAT25 alu vari']={'index':47, 'FAT':[25, 'MPa'],'Nfat':2e6,'Nc':1e7,'Ncutoff':1e10,'m1':3,'m2':5,'N0':796,'m0':5}
fatClassDict['IIW FAT22 alu vari']={'index':48, 'FAT':[22, 'MPa'],'Nfat':2e6,'Nc':1e7,'Ncutoff':1e10,'m1':3,'m2':5,'N0':305,'m0':5}
fatClassDict['IIW FAT18 alu vari']={'index':49, 'FAT':[18, 'MPa'],'Nfat':2e6,'Nc':1e7,'Ncutoff':1e10,'m1':3,'m2':5,'N0':68,'m0':5}
fatClassDict['IIW FAT16 alu vari']={'index':50, 'FAT':[16, 'MPa'],'Nfat':2e6,'Nc':1e7,'Ncutoff':1e10,'m1':3,'m2':5,'N0':28,'m0':5}
fatClassDict['IIW FAT14 alu vari']={'index':51, 'FAT':[14, 'MPa'],'Nfat':2e6,'Nc':1e7,'Ncutoff':1e10,'m1':3,'m2':5,'N0':10,'m0':5}
fatClassDict['IIW FAT12 alu vari']={'index':52, 'FAT':[12, 'MPa'],'Nfat':2e6,'Nc':1e7,'Ncutoff':1e10,'m1':3,'m2':5,'N0':3,'m0':5}
# Effective Notch Method (Constant & Variable amplitude)
fatClassDict['IIW FAT225 R1 steel']={'index':53, 'FAT':[225, 'MPa'],'Nfat':2e6,'Nc':1e7,'Ncutoff':1e10,'m1':3,'m2':22}
fatClassDict['IIW FAT71 R1 aluminium']={'index':54, 'FAT':[71, 'MPa'],'Nfat':2e6,'Nc':1e7,'Ncutoff':1e10,'m1':3,'m2':22}
fatClassDict['IIW FAT28 R1 magnesium']={'index':55, 'FAT':[28, 'MPa'],'Nfat':2e6,'Nc':1e7,'Ncutoff':1e10,'m1':3,'m2':22}
fatClassDict['IIW FAT630 R0.05 steel']={'index':56, 'FAT':[630, 'MPa'],'Nfat':2e6,'Nc':1e7,'Ncutoff':1e10,'m1':3,'m2':22}
fatClassDict['IIW FAT180 R0.05 aluminium']={'index':57, 'FAT':[180, 'MPa'],'Nfat':2e6,'Nc':1e7,'Ncutoff':1e10,'m1':3,'m2':22}
fatClassDict['IIW FAT71 R0.05 magnesium']={'index':58, 'FAT':[71, 'MPa'],'Nfat':2e6,'Nc':1e7,'Ncutoff':1e10,'m1':3,'m2':22}
fatClassDict['IIW FAT225 R1 steel vari']={'index':59, 'FAT':[225, 'MPa'],'Nfat':2e6,'Nc':1e7,'Ncutoff':1e10,'m1':3,'m2':5}
fatClassDict['IIW FAT71 R1 alu vari']={'index':60, 'FAT':[71, 'MPa'],'Nfat':2e6,'Nc':1e7,'Ncutoff':1e10,'m1':3,'m2':5}
fatClassDict['IIW FAT28 R1 magn vari']={'index':61, 'FAT':[28, 'MPa'],'Nfat':2e6,'Nc':1e7,'Ncutoff':1e10,'m1':3,'m2':5}
fatClassDict['IIW FAT630 R0.05 steel vari']={'index':62, 'FAT':[630, 'MPa'],'Nfat':2e6,'Nc':1e7,'Ncutoff':1e10,'m1':3,'m2':5}
fatClassDict['IIW FAT180 R0.05 alu vari']={'index':63, 'FAT':[180, 'MPa'],'Nfat':2e6,'Nc':1e7,'Ncutoff':1e10,'m1':3,'m2':5}
fatClassDict['IIW FAT71 R0.05 magn vari']={'index':64, 'FAT':[71, 'MPa'],'Nfat':2e6,'Nc':1e7,'Ncutoff':1e10,'m1':3,'m2':5}
# DNV Table 2-1 S-N curves in air. Note: FAT values are defined at N=1e6 for all three tables for consistensy
fatClassDict['DNV T.2-1 B1']={'index':65, 'FAT':[190.22, 'MPa'],'Nfat':1e6,'Nc':1e7,'Ncutoff':1e10,'m1':4,'m2':5,'k':0}
fatClassDict['DNV T.2-1 B2']={'index':66, 'FAT':[166.43, 'MPa'],'Nfat':1e6,'Nc':1e7,'Ncutoff':1e10,'m1':4,'m2':5,'k':0}
fatClassDict['DNV T.2-1 C']={'index':67, 'FAT':[157.49, 'MPa'],'Nfat':1e6,'Nc':1e7,'Ncutoff':1e10,'m1':3,'m2':5,'k':0.05,'N0':103992,'m0':4}
fatClassDict['DNV T.2-1 C1']={'index':68, 'FAT':[141.12, 'MPa'],'Nfat':1e6,'Nc':1e7,'Ncutoff':1e10,'m1':3,'m2':5,'k':0.1,'N0':27861,'m0':4}
fatClassDict['DNV T.2-1 C2']={'index':69, 'FAT':[125.99, 'MPa'],'Nfat':1e6,'Nc':1e7,'Ncutoff':1e10,'m1':3,'m2':5,'k':0.15,'N0':7129,'m0':4}
fatClassDict['DNV T.2-1 D']={'index':70, 'FAT':[113.39, 'MPa'],'Nfat':1e6,'Nc':1e7,'Ncutoff':1e10,'m1':3,'m2':5,'k':0.2,'N0':2018,'m0':4}
fatClassDict['DNV T.2-1 E']={'index':71, 'FAT':[100.78, 'MPa'],'Nfat':1e6,'Nc':1e7,'Ncutoff':1e10,'m1':3,'m2':5,'k':0.2,'N0':489,'m0':4}
fatClassDict['DNV T.2-1 F']={'index':72, 'FAT':[89.45, 'MPa'],'Nfat':1e6,'Nc':1e7,'Ncutoff':1e10,'m1':3,'m2':5,'k':0.25,'N0':117,'m0':4}
fatClassDict['DNV T.2-1 F1']={'index':73, 'FAT':[79.37, 'MPa'],'Nfat':1e6,'Nc':1e7,'Ncutoff':1e10,'m1':3,'m2':5,'k':0.25,'N0':28,'m0':4}
fatClassDict['DNV T.2-1 F3']={'index':74, 'FAT':[70.56, 'MPa'],'Nfat':1e6,'Nc':1e7,'Ncutoff':1e10,'m1':3,'m2':5,'k':0.25,'N0':7,'m0':4}
fatClassDict['DNV T.2-1 G']={'index':75, 'FAT':[63, 'MPa'],'Nfat':1e6,'Nc':1e7,'Ncutoff':1e10,'m1':3,'m2':5,'k':0.25,'N0':2,'m0':4}
fatClassDict['DNV T.2-1 W1']={'index':76, 'FAT':[56.7, 'MPa'],'Nfat':1e6,'Nc':1e7,'Ncutoff':1e10,'m1':3,'m2':5,'k':0.25}
fatClassDict['DNV T.2-1 W2']={'index':77, 'FAT':[50.39, 'MPa'],'Nfat':1e6,'Nc':1e7,'Ncutoff':1e10,'m1':3,'m2':5,'k':0.25}
fatClassDict['DNV T.2-1 W3']={'index':78, 'FAT':[45.35, 'MPa'],'Nfat':1e6,'Nc':1e7,'Ncutoff':1e10,'m1':3,'m2':5,'k':0.25}
fatClassDict['DNV T.2-1 T']={'index':79, 'FAT':[113.39, 'MPa'],'Nfat':1e6,'Nc':1e7,'Ncutoff':1e10,'m1':3,'m2':5,'k':0.25,'N0':2018,'m0':4}
fatClassDict['DNV (2.4.6) Steel']={'index':80, 'FAT':[272.47, 'MPa'],'Nfat':1e6,'Nc':1e7,'Ncutoff':1e10,'m1':4.7,'m2':5}
# DNV Table 2-2 S-N curves in sea water with cathodic protection
fatClassDict['DNV T.2-2 B1']={'index':81, 'FAT':[169.54, 'MPa'],'Nfat':1e6,'Nc':1e6,'Ncutoff':1e10,'m1':4,'m2':5,'k':0}
fatClassDict['DNV T.2-2 B2']={'index':82, 'FAT':[148.33, 'MPa'],'Nfat':1e6,'Nc':1e6,'Ncutoff':1e10,'m1':4,'m2':5,'k':0}
fatClassDict['DNV T.2-2 C']={'index':83, 'FAT':[115.86, 'MPa'],'Nfat':1e6,'Nc':1e6,'Ncutoff':1e10,'m1':3,'m2':5,'k':0.05,'N0':10399,'m0':4}
fatClassDict['DNV T.2-2 C1']={'index':84, 'FAT':[103.81, 'MPa'],'Nfat':1e6,'Nc':1e6,'Ncutoff':1e10,'m1':3,'m2':5,'k':0.1,'N0':2786,'m0':4}
fatClassDict['DNV T.2-2 C2']={'index':85, 'FAT':[92.68, 'MPa'],'Nfat':1e6,'Nc':1e6,'Ncutoff':1e10,'m1':3,'m2':5,'k':0.15,'N0':713,'m0':4}
fatClassDict['DNV T.2-2 D']={'index':86, 'FAT':[83.41, 'MPa'],'Nfat':1e6,'Nc':1e6,'Ncutoff':1e10,'m1':3,'m2':5,'k':0.2,'N0':202,'m0':4}
fatClassDict['DNV T.2-2 E']={'index':87, 'FAT':[74.14, 'MPa'],'Nfat':1e6,'Nc':1e6,'Ncutoff':1e10,'m1':3,'m2':5,'k':0.2,'N0':49,'m0':4}
fatClassDict['DNV T.2-2 F']={'index':88, 'FAT':[65.8, 'MPa'],'Nfat':1e6,'Nc':1e6,'Ncutoff':1e10,'m1':3,'m2':5,'k':0.25,'N0':12,'m0':4}
fatClassDict['DNV T.2-2 F1']={'index':89, 'FAT':[58.39, 'MPa'],'Nfat':1e6,'Nc':1e6,'Ncutoff':1e10,'m1':3,'m2':5,'k':0.25,'N0':3,'m0':4}
fatClassDict['DNV T.2-2 F3']={'index':90, 'FAT':[51.91, 'MPa'],'Nfat':1e6,'Nc':1e6,'Ncutoff':1e10,'m1':3,'m2':5,'k':0.25,'N0':1,'m0':4}
fatClassDict['DNV T.2-2 G']={'index':91, 'FAT':[46.34, 'MPa'],'Nfat':1e6,'Nc':1e6,'Ncutoff':1e10,'m1':3,'m2':5,'k':0.25}
fatClassDict['DNV T.2-2 W1']={'index':92, 'FAT':[41.71, 'MPa'],'Nfat':1e6,'Nc':1e6,'Ncutoff':1e10,'m1':3,'m2':5,'k':0.25}
fatClassDict['DNV T.2-2 W2']={'index':93, 'FAT':[37.07, 'MPa'],'Nfat':1e6,'Nc':1e6,'Ncutoff':1e10,'m1':3,'m2':5,'k':0.25}
fatClassDict['DNV T.2-2 W3']={'index':94, 'FAT':[33.36, 'MPa'],'Nfat':1e6,'Nc':1e6,'Ncutoff':1e10,'m1':3,'m2':5,'k':0.25}
fatClassDict['DNV T.2-2 T']={'index':95, 'FAT':[83.41, 'MPa'],'Nfat':1e6,'Nc':1e6,'Ncutoff':1e10,'m1':3,'m2':5,'k':0.25,'N0':202,'m0':4}
# DNV Table 2-3 S-N curves in seawater for free corrosion
fatClassDict['DNV T.2-3 B1']={'index':96, 'FAT':[139.74, 'MPa'],'Nfat':1e6,'Nc':1e6,'Ncutoff':1e10,'m1':3,'m2':3,'k':0}
fatClassDict['DNV T.2-3 B2']={'index':97, 'FAT':[122.27, 'MPa'],'Nfat':1e6,'Nc':1e6,'Ncutoff':1e10,'m1':3,'m2':3,'k':0}
fatClassDict['DNV T.2-3 C']={'index':98, 'FAT':[109.23, 'MPa'],'Nfat':1e6,'Nc':1e6,'Ncutoff':1e10,'m1':3,'m2':3,'k':0.15}
fatClassDict['DNV T.2-3 C1']={'index':99, 'FAT':[97.87, 'MPa'],'Nfat':1e6,'Nc':1e6,'Ncutoff':1e10,'m1':3,'m2':3,'k':0.15}
fatClassDict['DNV T.2-3 C2']={'index':100, 'FAT':[87.36, 'MPa'],'Nfat':1e6,'Nc':1e6,'Ncutoff':1e10,'m1':3,'m2':3,'k':0.15}
fatClassDict['DNV T.2-3 D']={'index':101, 'FAT':[78.64, 'MPa'],'Nfat':1e6,'Nc':1e6,'Ncutoff':1e10,'m1':3,'m2':3,'k':0.2}
fatClassDict['DNV T.2-3 E']={'index':102, 'FAT':[69.88, 'MPa'],'Nfat':1e6,'Nc':1e6,'Ncutoff':1e10,'m1':3,'m2':3,'k':0.2}
fatClassDict['DNV T.2-3 F']={'index':103, 'FAT':[62.04, 'MPa'],'Nfat':1e6,'Nc':1e6,'Ncutoff':1e10,'m1':3,'m2':3,'k':0.25}
fatClassDict['DNV T.2-3 F1']={'index':104, 'FAT':[55.04, 'MPa'],'Nfat':1e6,'Nc':1e6,'Ncutoff':1e10,'m1':3,'m2':3,'k':0.25}
fatClassDict['DNV T.2-3 F3']={'index':105, 'FAT':[48.9, 'MPa'],'Nfat':1e6,'Nc':1e6,'Ncutoff':1e10,'m1':3,'m2':3,'k':0.25}
fatClassDict['DNV T.2-3 G']={'index':106, 'FAT':[43.69, 'MPa'],'Nfat':1e6,'Nc':1e6,'Ncutoff':1e10,'m1':3,'m2':3,'k':0.25}
fatClassDict['DNV T.2-3 W1']={'index':107, 'FAT':[39.32, 'MPa'],'Nfat':1e6,'Nc':1e6,'Ncutoff':1e10,'m1':3,'m2':3,'k':0.25}
fatClassDict['DNV T.2-3 W2']={'index':108, 'FAT':[34.94, 'MPa'],'Nfat':1e6,'Nc':1e6,'Ncutoff':1e10,'m1':3,'m2':3,'k':0.25}
fatClassDict['DNV T.2-3 W3']={'index':109, 'FAT':[31.45, 'MPa'],'Nfat':1e6,'Nc':1e6,'Ncutoff':1e10,'m1':3,'m2':3,'k':0.25}
fatClassDict['DNV T.2-3 T']={'index':110, 'FAT':[78.64, 'MPa'],'Nfat':1e6,'Nc':1e6,'Ncutoff':1e10,'m1':3,'m2':3,'k':0.25}
# Eurocode 3 EN 1993-1-9 (2005) Figure 7.1 Constant amplitude
fatClassDict['EC3 FAT160']={'index':111, 'FAT':[160, 'MPa'],'Nfat':2e6,'Nc':5e6,'Ncutoff':1e8,'m1':3,'m2':1e6}
fatClassDict['EC3 FAT140']={'index':112, 'FAT':[140, 'MPa'],'Nfat':2e6,'Nc':5e6,'Ncutoff':1e8,'m1':3,'m2':1e6}
fatClassDict['EC3 FAT125']={'index':113, 'FAT':[125, 'MPa'],'Nfat':2e6,'Nc':5e6,'Ncutoff':1e8,'m1':3,'m2':1e6}
fatClassDict['EC3 FAT112']={'index':114, 'FAT':[112, 'MPa'],'Nfat':2e6,'Nc':5e6,'Ncutoff':1e8,'m1':3,'m2':1e6}
fatClassDict['EC3 FAT100']={'index':115, 'FAT':[100, 'MPa'],'Nfat':2e6,'Nc':5e6,'Ncutoff':1e8,'m1':3,'m2':1e6}
fatClassDict['EC3 FAT90']={'index':116, 'FAT':[90, 'MPa'],'Nfat':2e6,'Nc':5e6,'Ncutoff':1e8,'m1':3,'m2':1e6}
fatClassDict['EC3 FAT80']={'index':117, 'FAT':[80, 'MPa'],'Nfat':2e6,'Nc':5e6,'Ncutoff':1e8,'m1':3,'m2':1e6}
fatClassDict['EC3 FAT71']={'index':118, 'FAT':[71, 'MPa'],'Nfat':2e6,'Nc':5e6,'Ncutoff':1e8,'m1':3,'m2':1e6}
fatClassDict['EC3 FAT63']={'index':119, 'FAT':[63, 'MPa'],'Nfat':2e6,'Nc':5e6,'Ncutoff':1e8,'m1':3,'m2':1e6}
fatClassDict['EC3 FAT56']={'index':120, 'FAT':[56, 'MPa'],'Nfat':2e6,'Nc':5e6,'Ncutoff':1e8,'m1':3,'m2':1e6}
fatClassDict['EC3 FAT50']={'index':121, 'FAT':[50, 'MPa'],'Nfat':2e6,'Nc':5e6,'Ncutoff':1e8,'m1':3,'m2':1e6}
fatClassDict['EC3 FAT45']={'index':122, 'FAT':[45, 'MPa'],'Nfat':2e6,'Nc':5e6,'Ncutoff':1e8,'m1':3,'m2':1e6}
fatClassDict['EC3 FAT40']={'index':123, 'FAT':[40, 'MPa'],'Nfat':2e6,'Nc':5e6,'Ncutoff':1e8,'m1':3,'m2':1e6}
fatClassDict['EC3 FAT36']={'index':124, 'FAT':[36, 'MPa'],'Nfat':2e6,'Nc':5e6,'Ncutoff':1e8,'m1':3,'m2':1e6}
# Eurocode 3 EN 1993-1-9 (2005) Figure 7.1 Variable amplitude
fatClassDict['EC3 FAT160 vari']={'index':125, 'FAT':[160, 'MPa'],'Nfat':2e6,'Nc':5e6,'Ncutoff':1e8,'m1':3,'m2':5}
fatClassDict['EC3 FAT140 vari']={'index':126, 'FAT':[140, 'MPa'],'Nfat':2e6,'Nc':5e6,'Ncutoff':1e8,'m1':3,'m2':5}
fatClassDict['EC3 FAT125 vari']={'index':126, 'FAT':[125, 'MPa'],'Nfat':2e6,'Nc':5e6,'Ncutoff':1e8,'m1':3,'m2':5}
fatClassDict['EC3 FAT112 vari']={'index':127, 'FAT':[112, 'MPa'],'Nfat':2e6,'Nc':5e6,'Ncutoff':1e8,'m1':3,'m2':5}
fatClassDict['EC3 FAT100 vari']={'index':128, 'FAT':[100, 'MPa'],'Nfat':2e6,'Nc':5e6,'Ncutoff':1e8,'m1':3,'m2':5}
fatClassDict['EC3 FAT90 vari']={'index':129, 'FAT':[90, 'MPa'],'Nfat':2e6,'Nc':5e6,'Ncutoff':1e8,'m1':3,'m2':5}
fatClassDict['EC3 FAT80 vari']={'index':130, 'FAT':[80, 'MPa'],'Nfat':2e6,'Nc':5e6,'Ncutoff':1e8,'m1':3,'m2':5}
fatClassDict['EC3 FAT71 vari']={'index':131, 'FAT':[71, 'MPa'],'Nfat':2e6,'Nc':5e6,'Ncutoff':1e8,'m1':3,'m2':5}
fatClassDict['EC3 FAT63 vari']={'index':133, 'FAT':[56, 'MPa'],'Nfat':2e6,'Nc':5e6,'Ncutoff':1e8,'m1':3,'m2':5}
fatClassDict['EC3 FAT50 vari']={'index':134, 'FAT':[50, 'MPa'],'Nfat':2e6,'Nc':5e6,'Ncutoff':1e8,'m1':3,'m2':5}
fatClassDict['EC3 FAT45 vari']={'index':135, 'FAT':[45, 'MPa'],'Nfat':2e6,'Nc':5e6,'Ncutoff':1e8,'m1':3,'m2':5}
fatClassDict['EC3 FAT40 vari']={'index':136, 'FAT':[40, 'MPa'],'Nfat':2e6,'Nc':5e6,'Ncutoff':1e8,'m1':3,'m2':5}
fatClassDict['EC3 FAT36 vari']={'index':137, 'FAT':[36, 'MPa'],'Nfat':2e6,'Nc':5e6,'Ncutoff':1e8,'m1':3,'m2':5}
