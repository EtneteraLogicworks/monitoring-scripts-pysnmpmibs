#
# PySNMP MIB module HH3C-OID-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/michal/.snmp/mibs/HH3C-OID-MIB
# Produced by pysmi-0.3.4 at Tue Apr  7 15:55:38 2020
# On host LogicAir-MacBookAir.local platform Darwin version 19.4.0 by user michal
# Using Python version 3.7.3 (default, Mar  6 2020, 22:34:30) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Integer32, ModuleIdentity, MibIdentifier, Gauge32, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ObjectIdentity, NotificationType, iso, IpAddress, Counter32, enterprises, Counter64, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "ModuleIdentity", "MibIdentifier", "Gauge32", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "ObjectIdentity", "NotificationType", "iso", "IpAddress", "Counter32", "enterprises", "Counter64", "Unsigned32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
hh3c = MibIdentifier((1, 3, 6, 1, 4, 1, 25506))
hh3cProductId = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 1))
hh3cCommon = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2))
hh3cEntityVendorTypeOID = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 3))
hh3cNM = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 4))
hh3cSystem = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 6))
hh3cSNMPAgCpb = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 7))
hh3cRhw = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 8))
hh3cSurveillanceMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 9))
hh3cStorageRef = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 10))
hpNetworking = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 11))
hh3cJointMibs = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 12))
hh3c2014 = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 13))
hh3cJointVendorId = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 12, 1))
hh3cFtm = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 1))
hh3cUIMgt = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 2))
hh3cSystemMan = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 3))
hh3cConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 4))
hh3cFlash = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 5))
hh3cEntityExtend = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 6))
hh3cIPSecMonitor = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 7))
hh3cAcl = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 8))
hh3cVoiceVlan = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 9))
hh3cL4Redirect = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 10))
hh3cIpPBX = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 11))
hh3cUser = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 12))
hh3cRadius = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 13))
hh3cPowerEthernetExt = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 14))
hh3cEntityRelation = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 15))
hh3cProtocolVlan = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 16))
hh3cQosProfile = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 17))
hh3cNat = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 18))
hh3cPos = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 19))
hh3cNS = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 20))
hh3cAAL5 = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 21))
hh3cSSH = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 22))
hh3cRSA = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 23))
hh3cVrrpExt = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 24))
hh3cIpa = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 25))
hh3cPortSecurity = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 26))
hh3cVpls = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 27))
hh3cE1 = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 28))
hh3cT1 = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 29))
hh3cIKEMonitor = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 30))
hh3cWebSwitch = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 31))
hh3cAutoDetect = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 32))
hh3cIpBroadcast = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 33))
hh3cIpx = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 34))
hh3cIPS = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 35))
hh3cDhcpSnoop = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 36))
hh3cProtocolPriority = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 37))
hh3cTrap = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 38))
hh3cVoice = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 39))
hh3cIfExt = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 40))
hh3cCfCard = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 41))
hh3cEpon = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 42))
hh3cDldp = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 43))
hh3cUnicast = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 44))
hh3cRrpp = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 45))
hh3cDomain = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 46))
hh3cIds = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 47))
hh3cRcr = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 48))
hh3cAtmDxi = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 49))
hh3cMulticast = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 50))
hh3cMpm = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 51))
hh3cOadp = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 52))
hh3cTunnel = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 53))
hh3cGre = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 54))
hh3cObjectInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 55))
hh3cStorage = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 56))
hh3cDvpn = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 57))
hh3cDhcpRelay = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 58))
hh3cIsis = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 59))
hh3cRpr = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 60))
hh3cSubnetVlan = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 61))
hh3cDlswExt = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 62))
hh3cSyslog = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 63))
hh3cFlowTemplate = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 64))
hh3cQos2 = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 65))
hh3cStormConstrain = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 66))
hh3cIpAddrMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 67))
hh3cMirrGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 68))
hh3cQINQ = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 69))
hh3cTransceiver = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 70))
hh3cIpv6AddrMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 71))
hh3cBfdMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 72))
hh3cRCP = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 73))
hh3cAcfp = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 74))
hh3cDot11 = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 75))
hh3cE1T1VI = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 76))
hh3cL2VpnPwe3 = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 78))
hh3cMplsOam = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 79))
hh3cMplsOamPs = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 80))
hh3cSiemMib = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 81))
hh3cUps = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 82))
hh3cEOCCommon = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 83))
hh3cHPEOC = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 84))
hh3cAFC = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 85))
hh3cMultCDR = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 86))
hh3cMACInformation = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 87))
hh3cFireWall = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 88))
hh3cDSP = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 89))
hh3cNetMan = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 90))
hh3cStack = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 91))
hh3cPosa = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 92))
hh3cWebAuthentication = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 93))
hh3cCATVTransceiver = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 94))
hh3cLpbkdt = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 95))
hh3cMultiMedia = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 96))
hh3cDns = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 97))
hh3c3GModem = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 98))
hh3cPortal = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 99))
hh3clldp = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 100))
hh3cDHCPServer = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 101))
hh3cPPPoEServer = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 102))
hh3cL2Isolate = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 103))
hh3cSnmpExt = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 104))
hh3cVsi = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 105))
hh3cEvc = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 106))
hh3cMinm = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 107))
hh3cBlg = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 108))
hh3cRS485 = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 109))
hh3cARPRatelimit = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 110))
hh3cLI = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 111))
hh3cDar = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 112))
hh3cPBR = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 113))
hh3cAAANasId = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 114))
hh3cTeTunnel = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 115))
hh3cLB = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 116))
hh3cDldp2 = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 117))
hh3cWIPS = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 118))
hh3cInfoCenter = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 119))
hh3cFCoE = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 120))
hh3cTRNG2 = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 121))
hh3cDhcp4 = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 122))
hh3cMulticastSnoop = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 123))
hh3cDhcpSnoop2 = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 124))
hh3cRmonExt = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 125))
hh3cIPsecMonitorV2 = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 126))
hh3cSan = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 127))
hh3cSpb = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 128))
hh3cPex = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 129))
hh3cSlbg = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 130))
hh3cPvst = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 131))
hh3cEvi = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 132))
hh3cIssuUpgrade = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 133))
hh3cEvb = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 134))
hh3cFcoeMode = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 135))
hh3cMDC = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 136))
hh3cQinQv2 = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 137))
hh3cVmap = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 138))
hh3cL2tp = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 139))
hh3cMultilinkPPPV2 = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 140))
hh3cLocAAASrv = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 141))
hh3cMplsExt = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 142))
hh3cMplsTe = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 143))
hh3cBpa = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 144))
hh3cLicense = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 145))
hh3cSmlk = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 147))
hh3cARPSourceSuppression = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 146))
hh3cLBv2 = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 148))
hh3cSession = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 149))
hh3cVxlan = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 150))
hh3cRddc = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 151))
hh3cIpRanDcn = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 152))
hh3c8021XExt2 = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 153))
hh3cContext = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 154))
hh3cObjp = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 155))
hh3cNvgre = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 156))
hh3cWlanMt = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 157))
hh3cRbac = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 158))
hh3cDHCP6Server = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 159))
hh3cMplsVpnBgp = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 160))
hh3cOspf = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 161))
hh3cL2vpn = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 162))
hh3cMACsec = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 163))
hh3cFailover = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 164))
hh3cVpnPeer = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 165))
hh3cSecp = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 166))
hh3cOfp = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 167))
hh3cARPEntry = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 168))
hh3cResMon = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 169))
hh3cSslvpn = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 170))
hh3cSecHigh = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 171))
hh3cBgpEvpn = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 172))
hh3cEvpn = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 173))
hh3cLTE = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 174))
hh3cPPP = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 175))
hh3cDrni = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 176))
hh3cFlexE = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 177))
hh3cVlanGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 178))
hh3cDhcp6 = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 179))
hh3cVbr = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 180))
hh3cIfQos2 = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 65, 1))
hh3cCBQos2 = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 65, 2))
hh3cQosCapability = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 7, 1))
hh3cDHCPRelayMib = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 8, 1))
hh3cDHCPServerMib = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 8, 2))
hh3cNqa = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 8, 3))
hh3crmonExtend = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 8, 4))
hh3cpaeExtMib = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 8, 6))
hh3cHgmp = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 8, 7))
hh3cDevice = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 8, 8))
hh3cMpls = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 8, 12))
hh3cTRNG = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 8, 13))
hh3cUserLogMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 8, 18))
hh3cNTP = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 8, 22))
hh3cLAG = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 8, 25))
hh3cSmonExtend = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 8, 26))
hh3cQoS = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 8, 32))
hh3cMultilinkPPP = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 8, 33))
hh3clswCommon = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 8, 35))
hh3cmlsr = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 8, 36))
hh3cdlsw = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 8, 37))
hh3cVMMan = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 9, 1))
hh3cPUMan = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 9, 2))
hh3cMSMan = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 9, 3))
hh3cStorageMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 10, 1))
hh3cStorageSnap = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 10, 2))
hh3cDisk = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 10, 3))
hh3cRaid = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 10, 4))
hh3cLogicVolume = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 10, 5))
hh3cMplsLsr = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 8, 12, 1))
hh3cMplsLdp = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 8, 12, 2))
hh3cMplsVpn = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 8, 12, 3))
hh3cLswExtInterface = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 8, 35, 1))
hh3cLswVlan = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 8, 35, 2))
hh3cLswMacPort = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 8, 35, 3))
hh3cLswArpMib = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 8, 35, 4))
hh3cLswL2InfMib = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 8, 35, 5))
hh3cLswRstpMib = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 8, 35, 6))
hh3cLswIgmpsnoopingMib = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 8, 35, 7))
hh3cLswDhcpMib = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 8, 35, 8))
hh3cLswdevMMib = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 8, 35, 9))
hh3cLswTrapMib = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 8, 35, 12))
hh3cdot1sMstp = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 8, 35, 14))
hh3cLswQosAclMib = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 8, 35, 16))
hh3cLswMix = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 8, 35, 17))
hh3cLswDeviceAdmin = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 8, 35, 18))
hh3cNDEC = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 8, 36, 2))
hh3credundancyPower = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 8, 36, 4))
hh3credundancyFan = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 8, 36, 5))
hh3cpos = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 8, 36, 8))
hh3cIsdnMib = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 8, 36, 9))
mibBuilder.exportSymbols("HH3C-OID-MIB", hh3cPPPoEServer=hh3cPPPoEServer, hh3cLswDeviceAdmin=hh3cLswDeviceAdmin, hh3cSyslog=hh3cSyslog, hh3cLswExtInterface=hh3cLswExtInterface, hh3cVpls=hh3cVpls, hh3cFlash=hh3cFlash, hh3cEpon=hh3cEpon, hh3cObjp=hh3cObjp, hh3cNqa=hh3cNqa, hh3cLswDhcpMib=hh3cLswDhcpMib, hh3cQos2=hh3cQos2, hh3cL2VpnPwe3=hh3cL2VpnPwe3, hh3cFireWall=hh3cFireWall, hh3cUIMgt=hh3cUIMgt, hh3cMpls=hh3cMpls, hh3cVlanGroup=hh3cVlanGroup, hh3cMulticast=hh3cMulticast, hh3cARPSourceSuppression=hh3cARPSourceSuppression, hh3cMinm=hh3cMinm, hh3cVbr=hh3cVbr, hh3cUserLogMIB=hh3cUserLogMIB, hh3cLswRstpMib=hh3cLswRstpMib, hh3c=hh3c, hh3cNS=hh3cNS, hh3clldp=hh3clldp, hh3cRcr=hh3cRcr, hh3cStorage=hh3cStorage, hh3cDHCPServer=hh3cDHCPServer, hh3cSubnetVlan=hh3cSubnetVlan, hh3cIpBroadcast=hh3cIpBroadcast, hh3cpaeExtMib=hh3cpaeExtMib, hh3cDhcp4=hh3cDhcp4, hh3crmonExtend=hh3crmonExtend, hh3cRmonExt=hh3cRmonExt, hh3cPortSecurity=hh3cPortSecurity, hh3cLswArpMib=hh3cLswArpMib, hh3cDldp=hh3cDldp, hh3cE1=hh3cE1, hh3cRbac=hh3cRbac, hh3cSmonExtend=hh3cSmonExtend, hh3cIpAddrMIB=hh3cIpAddrMIB, hh3cdlsw=hh3cdlsw, hh3cProtocolPriority=hh3cProtocolPriority, hh3cFailover=hh3cFailover, hh3cSnmpExt=hh3cSnmpExt, hh3cDHCP6Server=hh3cDHCP6Server, hh3cOfp=hh3cOfp, hh3cFlowTemplate=hh3cFlowTemplate, hh3cWebAuthentication=hh3cWebAuthentication, hh3credundancyFan=hh3credundancyFan, hh3c8021XExt2=hh3c8021XExt2, hh3cRpr=hh3cRpr, hh3cPex=hh3cPex, hh3cL4Redirect=hh3cL4Redirect, hh3cQosProfile=hh3cQosProfile, hh3cTunnel=hh3cTunnel, hh3cStorageSnap=hh3cStorageSnap, hh3cMACInformation=hh3cMACInformation, hh3cDhcpRelay=hh3cDhcpRelay, hh3cRSA=hh3cRSA, hh3cDar=hh3cDar, hh3cPowerEthernetExt=hh3cPowerEthernetExt, hh3cSecp=hh3cSecp, hh3cIpRanDcn=hh3cIpRanDcn, hh3cIfExt=hh3cIfExt, hh3cSession=hh3cSession, hh3cMultCDR=hh3cMultCDR, hh3cPUMan=hh3cPUMan, hh3cPos=hh3cPos, hh3cCATVTransceiver=hh3cCATVTransceiver, hh3cInfoCenter=hh3cInfoCenter, hh3cIPS=hh3cIPS, hh3cMplsTe=hh3cMplsTe, hh3cProductId=hh3cProductId, hh3cUps=hh3cUps, hh3cVpnPeer=hh3cVpnPeer, hh3cQINQ=hh3cQINQ, hh3cLswQosAclMib=hh3cLswQosAclMib, hh3cVrrpExt=hh3cVrrpExt, hh3cMulticastSnoop=hh3cMulticastSnoop, hh3cWlanMt=hh3cWlanMt, hh3cRhw=hh3cRhw, hh3cARPEntry=hh3cARPEntry, hh3cConfig=hh3cConfig, hh3cIpx=hh3cIpx, hh3cCfCard=hh3cCfCard, hh3cStormConstrain=hh3cStormConstrain, hh3cLpbkdt=hh3cLpbkdt, hh3c3GModem=hh3c3GModem, hh3cDisk=hh3cDisk, hh3cDHCPRelayMib=hh3cDHCPRelayMib, hh3cMplsOamPs=hh3cMplsOamPs, hh3cMplsExt=hh3cMplsExt, hh3cBlg=hh3cBlg, hh3cVxlan=hh3cVxlan, hh3cRCP=hh3cRCP, hh3cIds=hh3cIds, hh3cLBv2=hh3cLBv2, hh3c2014=hh3c2014, hh3cDrni=hh3cDrni, hh3cSmlk=hh3cSmlk, hh3cRrpp=hh3cRrpp, hh3cOspf=hh3cOspf, hh3cFtm=hh3cFtm, hh3cIfQos2=hh3cIfQos2, hh3cPvst=hh3cPvst, hh3cSystem=hh3cSystem, hh3cObjectInfo=hh3cObjectInfo, hh3cQosCapability=hh3cQosCapability, hh3cAtmDxi=hh3cAtmDxi, hh3cPosa=hh3cPosa, hh3cLocAAASrv=hh3cLocAAASrv, hh3cLswL2InfMib=hh3cLswL2InfMib, hh3cL2Isolate=hh3cL2Isolate, hh3cTransceiver=hh3cTransceiver, hh3cIsis=hh3cIsis, hh3cE1T1VI=hh3cE1T1VI, hh3cLswMacPort=hh3cLswMacPort, hh3cLswTrapMib=hh3cLswTrapMib, hh3cDot11=hh3cDot11, hh3cDvpn=hh3cDvpn, hh3cARPRatelimit=hh3cARPRatelimit, hh3cPortal=hh3cPortal, hh3cDhcp6=hh3cDhcp6, hh3cMirrGroup=hh3cMirrGroup, hh3cLI=hh3cLI, hh3cJointVendorId=hh3cJointVendorId, hh3cSlbg=hh3cSlbg, hh3cVsi=hh3cVsi, hh3cEOCCommon=hh3cEOCCommon, hh3cSiemMib=hh3cSiemMib, hh3cSpb=hh3cSpb, hh3cPBR=hh3cPBR, hh3cEvi=hh3cEvi, hh3cSSH=hh3cSSH, hh3cIKEMonitor=hh3cIKEMonitor, hh3cEvb=hh3cEvb, hh3cTRNG=hh3cTRNG, hh3cCBQos2=hh3cCBQos2, hh3cTrap=hh3cTrap, hh3cAFC=hh3cAFC, hh3cWIPS=hh3cWIPS, hh3cResMon=hh3cResMon, hh3cFlexE=hh3cFlexE, hh3cVMMan=hh3cVMMan, hh3cIpPBX=hh3cIpPBX, hh3cMpm=hh3cMpm, hh3cLAG=hh3cLAG, hh3cSNMPAgCpb=hh3cSNMPAgCpb, hh3cmlsr=hh3cmlsr, hh3cMplsOam=hh3cMplsOam, hh3cStorageMIB=hh3cStorageMIB, hh3cRaid=hh3cRaid, hh3cMultilinkPPPV2=hh3cMultilinkPPPV2, hh3cAcl=hh3cAcl, hh3cTRNG2=hh3cTRNG2, hpNetworking=hpNetworking, hh3cCommon=hh3cCommon, hh3cJointMibs=hh3cJointMibs, hh3cMultiMedia=hh3cMultiMedia, hh3cSan=hh3cSan, hh3cContext=hh3cContext, hh3cpos=hh3cpos, hh3cSystemMan=hh3cSystemMan, hh3cIsdnMib=hh3cIsdnMib, hh3cMultilinkPPP=hh3cMultilinkPPP, hh3cL2vpn=hh3cL2vpn, hh3cPPP=hh3cPPP, hh3cDhcpSnoop2=hh3cDhcpSnoop2, hh3cDns=hh3cDns, hh3cStack=hh3cStack, hh3cMplsVpn=hh3cMplsVpn, hh3cNM=hh3cNM, hh3cProtocolVlan=hh3cProtocolVlan, hh3cVoice=hh3cVoice, hh3cEvc=hh3cEvc, hh3cIssuUpgrade=hh3cIssuUpgrade, hh3cIpv6AddrMIB=hh3cIpv6AddrMIB, hh3cRS485=hh3cRS485, hh3cL2tp=hh3cL2tp, hh3cNvgre=hh3cNvgre, hh3cLswdevMMib=hh3cLswdevMMib, hh3cMplsVpnBgp=hh3cMplsVpnBgp, hh3cTeTunnel=hh3cTeTunnel, hh3cT1=hh3cT1, hh3cEntityVendorTypeOID=hh3cEntityVendorTypeOID, hh3cLswIgmpsnoopingMib=hh3cLswIgmpsnoopingMib, hh3cNTP=hh3cNTP, hh3cFCoE=hh3cFCoE, hh3cdot1sMstp=hh3cdot1sMstp, hh3cGre=hh3cGre, hh3cBfdMIB=hh3cBfdMIB, hh3cFcoeMode=hh3cFcoeMode, hh3cDevice=hh3cDevice, hh3cLTE=hh3cLTE, hh3credundancyPower=hh3credundancyPower, hh3cQinQv2=hh3cQinQv2, hh3cHgmp=hh3cHgmp, hh3cAAANasId=hh3cAAANasId, hh3cSurveillanceMIB=hh3cSurveillanceMIB, hh3cWebSwitch=hh3cWebSwitch, hh3cMACsec=hh3cMACsec, hh3cMSMan=hh3cMSMan, hh3cEntityExtend=hh3cEntityExtend, hh3cMDC=hh3cMDC, hh3cBgpEvpn=hh3cBgpEvpn, hh3cIpa=hh3cIpa, hh3cQoS=hh3cQoS, hh3cLogicVolume=hh3cLogicVolume, hh3cBpa=hh3cBpa, hh3cSslvpn=hh3cSslvpn, hh3cLB=hh3cLB, hh3cIPsecMonitorV2=hh3cIPsecMonitorV2, hh3cNetMan=hh3cNetMan, hh3cSecHigh=hh3cSecHigh, hh3clswCommon=hh3clswCommon, hh3cLswVlan=hh3cLswVlan, hh3cNat=hh3cNat, hh3cNDEC=hh3cNDEC, hh3cAAL5=hh3cAAL5, hh3cStorageRef=hh3cStorageRef, hh3cIPSecMonitor=hh3cIPSecMonitor, hh3cUser=hh3cUser, hh3cEntityRelation=hh3cEntityRelation, hh3cHPEOC=hh3cHPEOC, hh3cDldp2=hh3cDldp2, hh3cAutoDetect=hh3cAutoDetect, hh3cDhcpSnoop=hh3cDhcpSnoop, hh3cOadp=hh3cOadp, hh3cLswMix=hh3cLswMix, hh3cEvpn=hh3cEvpn, hh3cLicense=hh3cLicense, hh3cUnicast=hh3cUnicast, hh3cRadius=hh3cRadius, hh3cDlswExt=hh3cDlswExt, hh3cVoiceVlan=hh3cVoiceVlan, hh3cMplsLdp=hh3cMplsLdp, hh3cDomain=hh3cDomain, hh3cDSP=hh3cDSP, hh3cVmap=hh3cVmap, hh3cAcfp=hh3cAcfp, hh3cMplsLsr=hh3cMplsLsr, hh3cRddc=hh3cRddc, hh3cDHCPServerMib=hh3cDHCPServerMib)