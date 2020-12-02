#
# PySNMP MIB module SNMPv2-TC-v1 (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/michal/.snmp/mibs/SNMPv2-TC-v1
# Produced by pysmi-0.3.4 at Wed Dec  2 12:15:59 2020
# On host LogicAir.local platform Darwin version 19.6.0 by user michal
# Using Python version 3.8.5 (default, Sep  6 2020, 03:54:05) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
iso, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, ModuleIdentity, ObjectIdentity, Counter32, NotificationType, Unsigned32, Integer32, Counter64, IpAddress, Bits, TimeTicks, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "ModuleIdentity", "ObjectIdentity", "Counter32", "NotificationType", "Unsigned32", "Integer32", "Counter64", "IpAddress", "Bits", "TimeTicks", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
class DisplayString(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class PhysAddress(OctetString):
    pass

class MacAddress(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(6, 6)
    fixedLength = 6

class TruthValue(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("true", 1), ("false", 2))

class TestAndIncr(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class AutonomousType(ObjectIdentifier):
    pass

class InstancePointer(ObjectIdentifier):
    pass

class VariablePointer(ObjectIdentifier):
    pass

class RowPointer(ObjectIdentifier):
    pass

class RowStatus(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("active", 1), ("notInService", 2), ("notReady", 3), ("createAndGo", 4), ("createAndWait", 5), ("destroy", 6))

class TimeStamp(TimeTicks):
    pass

class TimeInterval(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class DateAndTime(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(11, 11)
    fixedLength = 11

class StorageType(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("other", 1), ("volatile", 2), ("nonVolatile", 3), ("permanent", 4), ("readOnly", 5))

class TDomain(ObjectIdentifier):
    pass

class TAddress(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 255)

mibBuilder.exportSymbols("SNMPv2-TC-v1", DisplayString=DisplayString, TimeStamp=TimeStamp, VariablePointer=VariablePointer, TDomain=TDomain, MacAddress=MacAddress, TAddress=TAddress, InstancePointer=InstancePointer, AutonomousType=AutonomousType, PhysAddress=PhysAddress, TestAndIncr=TestAndIncr, StorageType=StorageType, DateAndTime=DateAndTime, TimeInterval=TimeInterval, RowStatus=RowStatus, TruthValue=TruthValue, RowPointer=RowPointer)
