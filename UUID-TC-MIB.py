#
# PySNMP MIB module UUID-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source http://mibs.snmplabs.com:80/asn1/UUID-TC-MIB
# Produced by pysmi-0.3.4 at Tue Apr  7 15:55:38 2020
# On host LogicAir-MacBookAir.local platform Darwin version 19.4.0 by user michal
# Using Python version 3.7.3 (default, Mar  6 2020, 22:34:30) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Integer32, ModuleIdentity, Gauge32, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ObjectIdentity, NotificationType, mib_2, iso, IpAddress, Counter32, MibIdentifier, Counter64, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "ModuleIdentity", "Gauge32", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "ObjectIdentity", "NotificationType", "mib-2", "iso", "IpAddress", "Counter32", "MibIdentifier", "Counter64", "Unsigned32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
uuidTCMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 217))
uuidTCMIB.setRevisions(('2013-04-05 00:00',))
if mibBuilder.loadTexts: uuidTCMIB.setLastUpdated('201304050000Z')
if mibBuilder.loadTexts: uuidTCMIB.setOrganization('IETF Energy Management Working Group')
class UUID(TextualConvention, OctetString):
    status = 'current'
    displayHint = '4x-2x-2x-1x1x-6x'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(16, 16)
    fixedLength = 16

class UUIDorZero(TextualConvention, OctetString):
    status = 'current'
    displayHint = '4x-2x-2x-1x1x-6x'
    subtypeSpec = OctetString.subtypeSpec + ConstraintsUnion(ValueSizeConstraint(0, 0), ValueSizeConstraint(16, 16), )
mibBuilder.exportSymbols("UUID-TC-MIB", UUIDorZero=UUIDorZero, uuidTCMIB=uuidTCMIB, PYSNMP_MODULE_ID=uuidTCMIB, UUID=UUID)
