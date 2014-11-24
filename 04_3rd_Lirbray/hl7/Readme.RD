HL7一种医疗系统中电子病历的数据格式
它的典型格式是：
MSH|^~\&|iNTERFACEWARE|Lab|Main HIS|St. Micheals|20110213144932||ADT^A03|9B38584D9903051F0D2B52CC0148965775D2D23FE4C51BE060B33B6ED27DA820|P|2.6|
EVN||20110213144532||||20110213145902|
PID|||4525285^^^ADT1||Smith^Tracy||10-Feb-1998|F||Martian|86 Yonge St.^^ST. LOUIS^MO^51460||1185438871|8530031194||||10-346-6|284-517-569|
NK1|1|Smith^Gary|Second Cousin|
PV1||E||||||5101^Garland^Mary^F^^DR|||||||||||1318095^^^ADT1|||||||||||||||||||||||||20110213144956|
OBX|||WT^WEIGHT||102|pounds|
OBX|||HT^HEIGHT||32|cm|
ZID||tracy.smith@acmemed.com|||

HL7是由segment组成的，每一行是一个segment。前三个字母是segment name。
HL7体系中一共有250+segment，每一个segment都有若干不等的field，总计250+segment中
有2466个不同的field。

python hl7 是一个hl7的parser，可以将hl7 string变成structured data