##encoding=utf-8
##version =py27
##author  =sanhe
##date    =2014-09-06

import hl7

def prt_seg(h, name):
    '''打印segment中的所有field以及index'''
    counter = 0
    for i in h[name][0]:
        counter += 1
        print i, counter
# msg = '''MSH|^~\&|iNTERFACEWARE|Lab|Main HIS|St. Micheals|20110213144932||ADT^A03|9B38584D9903051F0D2B52CC0148965775D2D23FE4C51BE060B33B6ED27DA820|P|2.6|\rEVN||20110213144532||||20110213145902|\rPID|||4525285^^^ADT1||Smith^Tracy||10-Feb-1998|F||Martian|86 Yonge St.^^ST. LOUIS^MO^51460||1185438871|8530031194||||10-346-6|284-517-569|\rNK1|1|Smith^Gary|Second Cousin|\rPV1||E||||||5101^Garland^Mary^F^^DR|||||||||||1318095^^^ADT1|||||||||||||||||||||||||20110213144956|\rOBX|||WT^WEIGHT||102|pounds|\rOBX|||HT^HEIGHT||32|cm|\rZID||tracy.smith@acmemed.com|||F'''

msg = 'MSH|^~\&|GHH LAB|ELAB-3|GHH OE|BLDG4|200202150930||ORU^R01|CNTRL-3456|P|2.4\r'
msg += 'PID|||555-44-4444||EVERYWOMAN^EVE^E^^^^L|JONES|196203520|F|||153 FERNWOOD DR.^^STATESVILLE^OH^35292||(206)3345232|(206)752-121||||AC555444444||67-A4335^OH^20030520\r'
msg += 'OBR|1|845439^GHH OE|1045813^GHH LAB|1554-5^GLUCOSE|||200202150730||||||||555-55-5555^PRIMARY^PATRICIA P^^^^MD^^LEVEL SEVEN HEALTHCARE, INC.|||||||||F||||||444-44-4444^HIPPOCRATES^HOWARD H^^^^MD\r'
msg += 'OBX|1|SN|1554-5^GLUCOSE^POST 12H CFST:MCNC:PT:SER/PLAS:QN||^182|mg/dl|70_105|H|||F'

def example1():
    h = hl7.parse(msg)
    for seg in h:
        print seg # 打印所有的segment segment
    print '================================='
    prt_seg(h, 'PID')
    
# example1()
    
def example2():
    '''打印某些segment中的关键信息'''
    h = hl7.parse(msg)
    print h['PID'][0][5] ## Name
    print h['PID'][0][7] ## DOB
    print h['PID'][0][8] ## Gender
    print h['PID'][0][10] ## Country
    print h['PID'][0][19] ## Address
    
    print h['OBX'][0][3] ## Vital sign name
    print h['OBX'][0][5] ## Vital sign value

example2()
