#
# PySNMP MIB module ENTITY-SENSOR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/michal/.snmp/mibs/ENTITY-SENSOR-MIB
# Produced by pysmi-0.3.4 at Wed Dec  2 12:15:59 2020
# On host LogicAir.local platform Darwin version 19.6.0 by user michal
# Using Python version 3.8.5 (default, Sep  6 2020, 03:54:05) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion")
entPhysicalIndex, entityPhysicalGroup = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalIndex", "entityPhysicalGroup")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, iso, MibIdentifier, ModuleIdentity, mib_2, Counter32, ObjectIdentity, NotificationType, Unsigned32, Integer32, Counter64, IpAddress, Bits, TimeTicks, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "MibIdentifier", "ModuleIdentity", "mib-2", "Counter32", "ObjectIdentity", "NotificationType", "Unsigned32", "Integer32", "Counter64", "IpAddress", "Bits", "TimeTicks", "Gauge32")
TimeStamp, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TimeStamp", "DisplayString", "TextualConvention")
entitySensorMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 99))
entitySensorMIB.setRevisions(('2002-12-16 00:00',))
if mibBuilder.loadTexts: entitySensorMIB.setLastUpdated('200212160000Z')
if mibBuilder.loadTexts: entitySensorMIB.setOrganization('IETF Entity MIB Working Group')
entitySensorObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 99, 1))
entitySensorConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 99, 3))
class EntitySensorDataType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))
    namedValues = NamedValues(("other", 1), ("unknown", 2), ("voltsAC", 3), ("voltsDC", 4), ("amperes", 5), ("watts", 6), ("hertz", 7), ("celsius", 8), ("percentRH", 9), ("rpm", 10), ("cmm", 11), ("truthvalue", 12))

class EntitySensorDataScale(TextualConvention, Integer32):
    reference = 'The International System of Units (SI), National Institute of Standards and Technology, Spec. Publ. 330, August 1991.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17))
    namedValues = NamedValues(("yocto", 1), ("zepto", 2), ("atto", 3), ("femto", 4), ("pico", 5), ("nano", 6), ("micro", 7), ("milli", 8), ("units", 9), ("kilo", 10), ("mega", 11), ("giga", 12), ("tera", 13), ("exa", 14), ("peta", 15), ("zetta", 16), ("yotta", 17))

class EntitySensorPrecision(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(-8, 9)

class EntitySensorValue(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(-1000000000, 1000000000)

class EntitySensorStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("ok", 1), ("unavailable", 2), ("nonoperational", 3))

entPhySensorTable = MibTable((1, 3, 6, 1, 2, 1, 99, 1, 1), )
if mibBuilder.loadTexts: entPhySensorTable.setStatus('current')
entPhySensorEntry = MibTableRow((1, 3, 6, 1, 2, 1, 99, 1, 1, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: entPhySensorEntry.setStatus('current')
entPhySensorType = MibTableColumn((1, 3, 6, 1, 2, 1, 99, 1, 1, 1, 1), EntitySensorDataType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: entPhySensorType.setStatus('current')
entPhySensorScale = MibTableColumn((1, 3, 6, 1, 2, 1, 99, 1, 1, 1, 2), EntitySensorDataScale()).setMaxAccess("readonly")
if mibBuilder.loadTexts: entPhySensorScale.setStatus('current')
entPhySensorPrecision = MibTableColumn((1, 3, 6, 1, 2, 1, 99, 1, 1, 1, 3), EntitySensorPrecision()).setMaxAccess("readonly")
if mibBuilder.loadTexts: entPhySensorPrecision.setStatus('current')
entPhySensorValue = MibTableColumn((1, 3, 6, 1, 2, 1, 99, 1, 1, 1, 4), EntitySensorValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: entPhySensorValue.setStatus('current')
entPhySensorOperStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 99, 1, 1, 1, 5), EntitySensorStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: entPhySensorOperStatus.setStatus('current')
entPhySensorUnitsDisplay = MibTableColumn((1, 3, 6, 1, 2, 1, 99, 1, 1, 1, 6), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: entPhySensorUnitsDisplay.setStatus('current')
entPhySensorValueTimeStamp = MibTableColumn((1, 3, 6, 1, 2, 1, 99, 1, 1, 1, 7), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: entPhySensorValueTimeStamp.setStatus('current')
entPhySensorValueUpdateRate = MibTableColumn((1, 3, 6, 1, 2, 1, 99, 1, 1, 1, 8), Unsigned32()).setUnits('milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: entPhySensorValueUpdateRate.setStatus('current')
entitySensorCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 99, 3, 1))
entitySensorGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 99, 3, 2))
entitySensorCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 99, 3, 1, 1)).setObjects(("ENTITY-SENSOR-MIB", "entitySensorValueGroup"), ("ENTITY-MIB", "entityPhysicalGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    entitySensorCompliance = entitySensorCompliance.setStatus('current')
entitySensorValueGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 99, 3, 2, 1)).setObjects(("ENTITY-SENSOR-MIB", "entPhySensorType"), ("ENTITY-SENSOR-MIB", "entPhySensorScale"), ("ENTITY-SENSOR-MIB", "entPhySensorPrecision"), ("ENTITY-SENSOR-MIB", "entPhySensorValue"), ("ENTITY-SENSOR-MIB", "entPhySensorOperStatus"), ("ENTITY-SENSOR-MIB", "entPhySensorUnitsDisplay"), ("ENTITY-SENSOR-MIB", "entPhySensorValueTimeStamp"), ("ENTITY-SENSOR-MIB", "entPhySensorValueUpdateRate"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    entitySensorValueGroup = entitySensorValueGroup.setStatus('current')
mibBuilder.exportSymbols("ENTITY-SENSOR-MIB", PYSNMP_MODULE_ID=entitySensorMIB, entPhySensorTable=entPhySensorTable, EntitySensorValue=EntitySensorValue, entPhySensorPrecision=entPhySensorPrecision, EntitySensorDataScale=EntitySensorDataScale, entitySensorGroups=entitySensorGroups, entitySensorValueGroup=entitySensorValueGroup, EntitySensorStatus=EntitySensorStatus, EntitySensorDataType=EntitySensorDataType, EntitySensorPrecision=EntitySensorPrecision, entitySensorConformance=entitySensorConformance, entPhySensorScale=entPhySensorScale, entitySensorCompliance=entitySensorCompliance, entPhySensorEntry=entPhySensorEntry, entPhySensorValue=entPhySensorValue, entPhySensorValueUpdateRate=entPhySensorValueUpdateRate, entitySensorMIB=entitySensorMIB, entitySensorCompliances=entitySensorCompliances, entPhySensorValueTimeStamp=entPhySensorValueTimeStamp, entPhySensorOperStatus=entPhySensorOperStatus, entPhySensorUnitsDisplay=entPhySensorUnitsDisplay, entPhySensorType=entPhySensorType, entitySensorObjects=entitySensorObjects)
