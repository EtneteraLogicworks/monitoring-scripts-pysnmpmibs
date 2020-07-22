#
# PySNMP MIB module EdgeSwitch-REF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/michal/.snmp/mibs/EdgeSwitch-REF-MIB
# Produced by pysmi-0.3.4 at Wed Jul 22 15:30:48 2020
# On host LogicAir.local platform Darwin version 19.6.0 by user michal
# Using Python version 3.7.3 (default, Apr 24 2020, 18:51:23) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter32, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, iso, Counter64, TimeTicks, ObjectIdentity, MibIdentifier, Bits, NotificationType, Integer32, Unsigned32, enterprises, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "iso", "Counter64", "TimeTicks", "ObjectIdentity", "MibIdentifier", "Bits", "NotificationType", "Integer32", "Unsigned32", "enterprises", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
broadcom = ModuleIdentity((1, 3, 6, 1, 4, 1, 4413))
broadcom.setRevisions(('2007-05-23 00:00', '2003-11-21 00:00', '2003-02-06 12:00',))
if mibBuilder.loadTexts: broadcom.setLastUpdated('200705230000Z')
if mibBuilder.loadTexts: broadcom.setOrganization('Broadcom Inc')
broadcomProducts = MibIdentifier((1, 3, 6, 1, 4, 1, 4413, 1))
fastPath = MibIdentifier((1, 3, 6, 1, 4, 1, 4413, 1, 1))
class AgentPortMask(TextualConvention, OctetString):
    status = 'current'

mibBuilder.exportSymbols("EdgeSwitch-REF-MIB", fastPath=fastPath, AgentPortMask=AgentPortMask, PYSNMP_MODULE_ID=broadcom, broadcomProducts=broadcomProducts, broadcom=broadcom)
