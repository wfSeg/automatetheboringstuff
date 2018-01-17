#! python

#practice some regex with Real life data from work :|

import re
import pprint

data = '''================================================================================================================================
BIOS    >> Mfr:American Megatrends Inc. Version:3.0a   Date:01/10/2018 Revision:5.6     Start:(01/10/18 17:31)
SYSTEM  >> Mfr:Supermicro Name:Super Server     Ser:0123456789             Fmly:Default st SKU:Default st
BOARD   >> Mfr:Supermicro Name:X10DRU-i+        Ser:OM15CS034412         ATag:Default string BID:0844 CPLD:nf.nf.nf SVR:platypus
CHASSIS >> Mfr:Supermicro Type:Main Server Chas Ser:0123456789             ATag:Default string   GEO:SMC_US  
--------------------------------------------------------------------------------------------------------------------------------
CPU0    >> Mfr:Intel       Model:Xeon(R) CPU E5-2618L v4 @ 2.20GHz          Speed:2200  Cores:10  Threads:20 
CPU1    >> Mfr:Intel       Model:Xeon(R) CPU E5-2618L v4 @ 2.20GHz          Speed:2200  Cores:10  Threads:20 
--------------------------------------------------------------------------------------------------------------------------------
DIMM0   >> P1-DIMMA1    dc:16/02          Sz:32    Typ:DDR4  Rnk:2 Spd:2400:2133 Mfr:Micron   #:11700BC9   Mdl:36ASF4G72LZ-2G3A
DIMM3   >> P1-DIMMB1    dc:16/02          Sz:32    Typ:DDR4  Rnk:2 Spd:2400:2133 Mfr:Micron   #:11700C0A   Mdl:36ASF4G72LZ-2G3A
DIMM6   >> P1-DIMMC1    dc:16/02          Sz:32    Typ:DDR4  Rnk:2 Spd:2400:2133 Mfr:Micron   #:11700BCA   Mdl:36ASF4G72LZ-2G3A
DIMM9   >> P1-DIMMD1    dc:16/02          Sz:32    Typ:DDR4  Rnk:2 Spd:2400:2133 Mfr:Micron   #:11700B52   Mdl:36ASF4G72LZ-2G3A
DIMM12  >> P2-DIMME1    dc:15/51          Sz:32    Typ:DDR4  Rnk:2 Spd:2400:2133 Mfr:Micron   #:114641B7   Mdl:36ASF4G72LZ-2G3A
DIMM15  >> P2-DIMMF1    dc:15/51          Sz:32    Typ:DDR4  Rnk:2 Spd:2400:2133 Mfr:Micron   #:114641AC   Mdl:36ASF4G72LZ-2G3A
DIMM18  >> P2-DIMMG1    dc:15/51          Sz:32    Typ:DDR4  Rnk:2 Spd:2400:2133 Mfr:Micron   #:1146420D   Mdl:36ASF4G72LZ-2G3A
DIMM21  >> P2-DIMMH1    dc:15/51          Sz:32    Typ:DDR4  Rnk:2 Spd:2400:2133 Mfr:Micron   #:114640E8   Mdl:36ASF4G72LZ-2G3A
--------------------------------------------------------------------------------------------------------------------------------
PCIE0   >> 00:01.0  Cap:Gen3 x8   Sta:Gen2 x8   Intel Corporation Xeon E7 v4/Xeon E5 v4/Xeon E3 v4/Xeon D PCI Express Root Port 
PCIE1   >> 00:02.0  Cap:Gen3 x8   Sta:Gen2 x8   Intel Corporation Xeon E7 v4/Xeon E5 v4/Xeon E3 v4/Xeon D PCI Express Root Port 
PCIE2   >> 00:1c.2  Cap:Gen2 x1   Sta:Gen1 x1   Intel Corporation C610/X99 series chipset PCI Express Root Port #3 (rev d5) (pro
PCIE3   >> 01:00.0  Cap:Gen2 x8   Sta:Gen2 x8   Intel Corporation Ethernet Controller X540-AT2 (rev 01)                         
PCIE4   >> 01:00.1  Cap:Gen2 x8   Sta:Gen2 x8   Intel Corporation Ethernet Controller X540-AT2 (rev 01)                         
PCIE5   >> 02:00.0  Cap:Gen2 x8   Sta:Gen2 x8   Intel Corporation Ethernet Controller X540-AT2 (rev 01)                         
PCIE6   >> 02:00.1  Cap:Gen2 x8   Sta:Gen2 x8   Intel Corporation Ethernet Controller X540-AT2 (rev 01)                         
PCIE7   >> 05:00.0  Cap:Gen1 x1   Sta:Gen1 x1   ASPEED Technology, Inc. AST1150 PCI-to-PCI Bridge (rev 03) (prog-if 00 [Normal d
--------------------------------------------------------------------------------------------------------------------------------
HDD0    >> sda  Tp:ATA Spd:6.0  Mf:intel      Md:INTEL SSDSC2BX01     Sz:1.60TB Fw:0150  Bus:0:0:0:0    Ser:BTHC64030C5R1P6PGN  
HDD1    >> sdb  Tp:ATA Spd:6.0  Mf:micron     Md:MICRON_M510DC_MT     Sz:960GB  Fw:0013  Bus:1:0:0:0    Ser:153511C58EAB        
HDD2    >> sdc  Tp:ATA Spd:6.0  Mf:seagate    Md:ST2000NX0253         Sz:2.00TB Fw:SN02  Bus:2:0:0:0    Ser:W4608NBP            
HDD3    >> sdd  Tp:ATA Spd:6.0  Mf:seagate    Md:ST2000NX0253         Sz:2.00TB Fw:SN02  Bus:3:0:0:0    Ser:W4609CX2            
HDD4    >> sde  Tp:ATA Spd:6.0  Mf:seagate    Md:ST2000NX0253         Sz:2.00TB Fw:SN02  Bus:4:0:0:0    Ser:W4609L5M            
HDD5    >> sdf  Tp:ATA Spd:6.0  Mf:seagate    Md:ST2000NX0253         Sz:2.00TB Fw:SN02  Bus:5:0:0:0    Ser:W46086GS            
HDD6    >> sdg  Tp:ATA Spd:6.0  Mf:seagate    Md:ST2000NX0253         Sz:2.00TB Fw:SN02  Bus:6:0:0:0    Ser:W4609CJL            
HDD7    >> sdh  Tp:ATA Spd:6.0  Mf:seagate    Md:ST2000NX0253         Sz:2.00TB Fw:SN02  Bus:7:0:0:0    Ser:W4608P2F            
HDD8    >> sdi  Tp:ATA Spd:6.0  Mf:seagate    Md:ST2000NX0253         Sz:2.00TB Fw:SN02  Bus:8:0:0:0    Ser:W4609JZ8            
HDD9    >> sdj  Tp:ATA Spd:6.0  Mf:seagate    Md:ST2000NX0253         Sz:2.00TB Fw:SN02  Bus:9:0:0:0    Ser:W4609H41            
--------------------------------------------------------------------------------------------------------------------------------
LAN0    >> eth0  IP:172.16.114.237  Mac:0c:c4:7a:a3:ff:e0 eep:0x800003e2            Bus:0000:01:00.0 Drv:ixgbe,5.2.1   Spd:10000
LAN1    >> eth1  IP:172.16.114.236  Mac:0c:c4:7a:a3:ff:e1 eep:0x800003e2            Bus:0000:01:00.1 Drv:ixgbe,5.2.1   Spd:10000
LAN2    >> eth2  IP:172.16.114.239  Mac:0c:c4:7a:a3:ff:e2 eep:0x800003e1            Bus:0000:02:00.0 Drv:ixgbe,5.2.1   Spd:10000
LAN3    >> eth3  IP:172.16.114.238  Mac:0c:c4:7a:a3:ff:e3 eep:0x800003e1            Bus:0000:02:00.1 Drv:ixgbe,5.2.1   Spd:10000
--------------------------------------------------------------------------------------------------------------------------------
BMC     >>  IP:172.16.102.159   Mac:0c:c4:7a:67:b0:7e  Id:ASPEED     Fw:3.65           | CL:0.66.1 CS:5.26   CF:0.24   |
BMC_PRO >> Mfr:Supermicro  Name:              Part:SYS-1028U-TR4T+  Ser:S16746326435213         ATag:                         
BMC_BRD >> Mfr:Supermicro  Name:              Part:X10DRU-i+        Ser:OM15CS034412            Date:Sun Dec 31 16:00:00 1995 
BMC_CHS >> Typ:01                             Part:CSE-119UTS-R751  Ser:C119UAF03B20282         FRU_ver:      SDR_ver:    
--------------------------------------------------------------------------------------------------------------------------------
FAN     >> F1:14600  F2:14100  F3:13900  F4:14900  F5:14300  F6:14900  F7:15200  F8:14000  
--------------------------------------------------------------------------------------------------------------------------------
PS0     >> Mfr:SUPERMICRO Mdel:PWS-751P-1R  Rev:1.0   Watt:750W  Ser:P751PCF49A03098 Slt:PSU1   Sta:Present,OK Plg:Yes Rpl:Yes
PS1     >> Mfr:SUPERMICRO Mdel:PWS-751P-1R  Rev:1.0   Watt:750W  Ser:P751PCF49A03099 Slt:PSU2   Sta:Present,OK Plg:Yes Rpl:Yes
--------------------------------------------------------------------------------------------------------------------------------
SUM HW  >> CPU Ins=2, Skt=2, LPJ=2199 | MEM Sze=264038908KB, Ins=8, Slt=24 | DSK=10 | NVME=0 | PCI=8 | LAN=4 | GPU=0 | FAN=8
SUM CM  >> KER:3.10.0-327 IMG:r72 CVER:7.2||DIR=sysv/longn/x10dru-i+/bios2018-01-10/onoff1|MDELT=90|ONOFF=1|
================================================================================================================================
'''

#hddRegex = re.compile(r'Mf:(.*)\s+Md:(.*)\s+Sz:(.*)\s+Fw:(.*)\s+Bus:(.*)\s+Ser:(.*)\s+')
#need to remove the extra spaces somehow
#hddRegex = re.compile(r'Md:(.*?)\s+') #works, but freaking Intel SSD truncated after Intel
#hddRegex = re.compile(r'Md:(.*?)\s{2,}') #works! if there's more than 2 space, then it cuts off
#hddRegex = re.compile(r'Mf:(.*?)\s{2,}Md:(.*?)\s{2,}Sz:(.*?)\sFw:(.*?)\s{2,}Bus:(.*?)\s{2,}Ser:(.*?)\s{2,}')

def info(self):
    hdd = str(self) + ' Info'
    newhdd = hdd.center(40,'=')
    print(str(newhdd))

info('HDD')
hddRegex = re.compile(r'(HDD\d+).*(sd\w+).*Mf:(.*?)\s{2,}Md:(.*?)\s{2,}Sz:(.*?)\sFw:(.*?)\s{2,}.*Ser:(.*?)\s+')
pprint.pprint(hddRegex.findall(data))
#ohhh yeah baby, i figured it out. so proud. *smug face*
#still, how do i indent a regex? :|, the string is getting super long

info('DIMM')
dimmRegex = re.compile(r'(DIMM\d+).*(P\d-DIMM\w+).*Sz:(.*?)\s+Typ:(DDR\d).*Spd:(.*:.*)\s+Mfr:(\w+).*Mdl:(.*?)\s+')
pprint.pprint(dimmRegex.findall(data))

info('LAN')
lanRegex = re.compile(r'(LAN\d+).*(eth\d+)\s+IP:(.*?)\s+Mac:(.*?).\s+eep:(.*?)\s+.*Drv:(.*?)\s+Spd:(.*?)\s')
pprint.pprint(lanRegex.findall(data))

info('BMC')
bmcRegex = re.compile(r'BMC.*IP:(.\S*).*Mac:(.\S*).*Fw:(.\S*).*')
pprint.pprint(bmcRegex.findall(data))

#for LAN I used (.*?)\s+ , and for BMC I used (.\S*).* . both do the same thing, but differently :/
info('CPU')
cpuRegex = re.compile(r'Model:(.*?)\s{2,}')
pprint.pprint(cpuRegex.findall(data))
