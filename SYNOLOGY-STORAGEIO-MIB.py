#
# PySNMP MIB module SYNOLOGY-STORAGEIO-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/michal/.snmp/mibs/SYNOLOGY-STORAGEIO-MIB
# Produced by pysmi-0.3.4 at Tue Apr 21 17:44:20 2020
# On host LogicAir-MacBookAir.local platform Darwin version 19.4.0 by user michal
# Using Python version 3.7.3 (default, Mar  6 2020, 22:34:30) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
IpAddress, Gauge32, iso, Bits, MibIdentifier, Unsigned32, enterprises, TimeTicks, ModuleIdentity, NotificationType, Counter64, Integer32, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Gauge32", "iso", "Bits", "MibIdentifier", "Unsigned32", "enterprises", "TimeTicks", "ModuleIdentity", "NotificationType", "Counter64", "Integer32", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
storageIO = ModuleIdentity((1, 3, 6, 1, 4, 1, 6574, 101))
storageIO.setRevisions(('2013-09-11 00:00',))
if mibBuilder.loadTexts: storageIO.setLastUpdated('201309110000Z')
if mibBuilder.loadTexts: storageIO.setOrganization('www.synology.com')
synology = MibIdentifier((1, 3, 6, 1, 4, 1, 6574))
storageIOTable = MibTable((1, 3, 6, 1, 4, 1, 6574, 101, 1), )
if mibBuilder.loadTexts: storageIOTable.setStatus('current')
storageIOEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6574, 101, 1, 1), ).setIndexNames((0, "SYNOLOGY-STORAGEIO-MIB", "storageIOIndex"))
if mibBuilder.loadTexts: storageIOEntry.setStatus('current')
storageIOIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 6574, 101, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)))
if mibBuilder.loadTexts: storageIOIndex.setStatus('current')
storageIODevice = MibTableColumn((1, 3, 6, 1, 4, 1, 6574, 101, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: storageIODevice.setStatus('current')
storageIONRead = MibTableColumn((1, 3, 6, 1, 4, 1, 6574, 101, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: storageIONRead.setStatus('current')
storageIONWritten = MibTableColumn((1, 3, 6, 1, 4, 1, 6574, 101, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: storageIONWritten.setStatus('current')
storageIOReads = MibTableColumn((1, 3, 6, 1, 4, 1, 6574, 101, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: storageIOReads.setStatus('current')
storageIOWrites = MibTableColumn((1, 3, 6, 1, 4, 1, 6574, 101, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: storageIOWrites.setStatus('current')
storageIOLA = MibTableColumn((1, 3, 6, 1, 4, 1, 6574, 101, 1, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: storageIOLA.setStatus('current')
storageIOLA1 = MibTableColumn((1, 3, 6, 1, 4, 1, 6574, 101, 1, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: storageIOLA1.setStatus('current')
storageIOLA5 = MibTableColumn((1, 3, 6, 1, 4, 1, 6574, 101, 1, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: storageIOLA5.setStatus('current')
storageIOLA15 = MibTableColumn((1, 3, 6, 1, 4, 1, 6574, 101, 1, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: storageIOLA15.setStatus('current')
storageIONReadX = MibTableColumn((1, 3, 6, 1, 4, 1, 6574, 101, 1, 1, 12), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: storageIONReadX.setStatus('current')
storageIONWrittenX = MibTableColumn((1, 3, 6, 1, 4, 1, 6574, 101, 1, 1, 13), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: storageIONWrittenX.setStatus('current')
storageIOConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 6574, 101, 2))
storageIOCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 6574, 101, 2, 1))
storageIOGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 6574, 101, 2, 2))
storageIOCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 6574, 101, 2, 1, 1)).setObjects(("SYNOLOGY-STORAGEIO-MIB", "storageIOGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    storageIOCompliance = storageIOCompliance.setStatus('current')
storageIOGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6574, 101, 2, 2, 1)).setObjects(("SYNOLOGY-STORAGEIO-MIB", "storageIODevice"), ("SYNOLOGY-STORAGEIO-MIB", "storageIONRead"), ("SYNOLOGY-STORAGEIO-MIB", "storageIONWritten"), ("SYNOLOGY-STORAGEIO-MIB", "storageIOReads"), ("SYNOLOGY-STORAGEIO-MIB", "storageIOWrites"), ("SYNOLOGY-STORAGEIO-MIB", "storageIOLA"), ("SYNOLOGY-STORAGEIO-MIB", "storageIOLA1"), ("SYNOLOGY-STORAGEIO-MIB", "storageIOLA5"), ("SYNOLOGY-STORAGEIO-MIB", "storageIOLA15"), ("SYNOLOGY-STORAGEIO-MIB", "storageIONReadX"), ("SYNOLOGY-STORAGEIO-MIB", "storageIONWrittenX"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    storageIOGroup = storageIOGroup.setStatus('current')
mibBuilder.exportSymbols("SYNOLOGY-STORAGEIO-MIB", storageIOConformance=storageIOConformance, storageIODevice=storageIODevice, storageIOReads=storageIOReads, storageIO=storageIO, storageIOEntry=storageIOEntry, storageIOLA=storageIOLA, storageIONWrittenX=storageIONWrittenX, storageIOWrites=storageIOWrites, storageIOCompliances=storageIOCompliances, storageIOCompliance=storageIOCompliance, storageIOIndex=storageIOIndex, storageIOLA15=storageIOLA15, storageIONRead=storageIONRead, storageIOGroup=storageIOGroup, storageIONWritten=storageIONWritten, storageIOLA5=storageIOLA5, storageIOGroups=storageIOGroups, storageIOTable=storageIOTable, storageIOLA1=storageIOLA1, storageIONReadX=storageIONReadX, PYSNMP_MODULE_ID=storageIO, synology=synology)
