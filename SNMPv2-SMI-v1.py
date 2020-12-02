#
# PySNMP MIB module SNMPv2-SMI-v1 (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/michal/.snmp/mibs/SNMPv2-SMI-v1
# Produced by pysmi-0.3.4 at Wed Dec  2 12:15:59 2020
# On host LogicAir.local platform Darwin version 19.6.0 by user michal
# Using Python version 3.8.5 (default, Sep  6 2020, 03:54:05) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, iso, MibIdentifier, ModuleIdentity, ObjectIdentity, Counter32, NotificationType, Unsigned32, Integer32, Counter64, IpAddress, Bits, TimeTicks, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "MibIdentifier", "ModuleIdentity", "ObjectIdentity", "Counter32", "NotificationType", "Unsigned32", "Integer32", "Counter64", "IpAddress", "Bits", "TimeTicks", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
class Counter_32(Counter32):
    pass

class Gauge_32(Gauge32):
    pass

class Integer_32(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(-2147483648, 2147483647)

class Unsigned_32(Gauge32):
    pass

internet = MibIdentifier((1, 3, 6, 1))
directory = MibIdentifier((1, 3, 6, 1, 1))
mgmt = MibIdentifier((1, 3, 6, 1, 2))
experimental = MibIdentifier((1, 3, 6, 1, 3))
private = MibIdentifier((1, 3, 6, 1, 4))
enterprises = MibIdentifier((1, 3, 6, 1, 4, 1))
security = MibIdentifier((1, 3, 6, 1, 5))
snmpV2 = MibIdentifier((1, 3, 6, 1, 6))
snmpDomains = MibIdentifier((1, 3, 6, 1, 6, 1))
snmpProxys = MibIdentifier((1, 3, 6, 1, 6, 2))
snmpModules = MibIdentifier((1, 3, 6, 1, 6, 3))
mibBuilder.exportSymbols("SNMPv2-SMI-v1", internet=internet, directory=directory, snmpModules=snmpModules, Integer_32=Integer_32, private=private, snmpV2=snmpV2, snmpProxys=snmpProxys, experimental=experimental, Gauge_32=Gauge_32, enterprises=enterprises, snmpDomains=snmpDomains, Unsigned_32=Unsigned_32, Counter_32=Counter_32, mgmt=mgmt, security=security)
