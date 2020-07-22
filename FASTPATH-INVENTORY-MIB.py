#
# PySNMP MIB module FASTPATH-INVENTORY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/michal/.snmp/mibs/FASTPATH-INVENTORY-MIB
# Produced by pysmi-0.3.4 at Wed Jul 22 15:57:17 2020
# On host LogicAir.local platform Darwin version 19.6.0 by user michal
# Using Python version 3.7.3 (default, Apr 24 2020, 18:51:23) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint")
fastPath, = mibBuilder.importSymbols("BROADCOM-REF-MIB", "fastPath")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
NotificationType, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, MibIdentifier, TimeTicks, Gauge32, IpAddress, ObjectIdentity, iso, ModuleIdentity, Unsigned32, Integer32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "MibIdentifier", "TimeTicks", "Gauge32", "IpAddress", "ObjectIdentity", "iso", "ModuleIdentity", "Unsigned32", "Integer32", "Counter32")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
fastPathInventory = ModuleIdentity((1, 3, 6, 1, 4, 1, 4413, 1, 1, 13))
fastPathInventory.setRevisions(('2013-10-15 00:00', '2011-01-26 00:00', '2007-05-23 00:00', '2004-10-28 20:37', '2003-05-26 19:30',))
if mibBuilder.loadTexts: fastPathInventory.setLastUpdated('201310150000Z')
if mibBuilder.loadTexts: fastPathInventory.setOrganization('Broadcom Corporation')
class AgentInventoryUnitPreference(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("disabled", 0), ("unsassigned", 1), ("assigned", 2))

class AgentInventoryUnitType(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'x'

class AgentInventoryCardType(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'x'

agentInventoryStackGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 1))
agentInventoryStackSTKname = MibScalar((1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("unconfigured", 1), ("image1", 2), ("image2", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentInventoryStackSTKname.setStatus('current')
agentInventoryStackActivateSTK = MibScalar((1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentInventoryStackActivateSTK.setStatus('current')
agentInventoryStackDeleteSTK = MibScalar((1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentInventoryStackDeleteSTK.setStatus('current')
agentInventoryCardGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 4))
agentInventoryCardTypeTable = MibTable((1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 4, 1), )
if mibBuilder.loadTexts: agentInventoryCardTypeTable.setStatus('current')
agentInventoryCardTypeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 4, 1, 1), ).setIndexNames((0, "FASTPATH-INVENTORY-MIB", "agentInventoryCardIndex"))
if mibBuilder.loadTexts: agentInventoryCardTypeEntry.setStatus('current')
agentInventoryCardIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 4, 1, 1, 1), Unsigned32())
if mibBuilder.loadTexts: agentInventoryCardIndex.setStatus('current')
agentInventoryCardType = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 4, 1, 1, 2), AgentInventoryCardType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentInventoryCardType.setStatus('current')
agentInventoryCardModelIdentifier = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 4, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentInventoryCardModelIdentifier.setStatus('current')
agentInventoryCardDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 4, 1, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentInventoryCardDescription.setStatus('current')
agentInventoryComponentGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 5))
agentInventoryComponentTable = MibTable((1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 5, 1), )
if mibBuilder.loadTexts: agentInventoryComponentTable.setStatus('current')
agentInventoryComponentEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 5, 1, 1), ).setIndexNames((0, "FASTPATH-INVENTORY-MIB", "agentInventoryComponentIndex"))
if mibBuilder.loadTexts: agentInventoryComponentEntry.setStatus('current')
agentInventoryComponentIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 5, 1, 1, 1), Unsigned32())
if mibBuilder.loadTexts: agentInventoryComponentIndex.setStatus('current')
agentInventoryComponentMnemonic = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 5, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentInventoryComponentMnemonic.setStatus('current')
agentInventoryComponentName = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 5, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentInventoryComponentName.setStatus('current')
mibBuilder.exportSymbols("FASTPATH-INVENTORY-MIB", agentInventoryStackGroup=agentInventoryStackGroup, agentInventoryComponentIndex=agentInventoryComponentIndex, agentInventoryComponentGroup=agentInventoryComponentGroup, agentInventoryStackActivateSTK=agentInventoryStackActivateSTK, agentInventoryStackSTKname=agentInventoryStackSTKname, agentInventoryComponentTable=agentInventoryComponentTable, agentInventoryCardType=agentInventoryCardType, PYSNMP_MODULE_ID=fastPathInventory, agentInventoryStackDeleteSTK=agentInventoryStackDeleteSTK, agentInventoryComponentEntry=agentInventoryComponentEntry, fastPathInventory=fastPathInventory, AgentInventoryUnitPreference=AgentInventoryUnitPreference, AgentInventoryCardType=AgentInventoryCardType, agentInventoryCardTypeTable=agentInventoryCardTypeTable, agentInventoryCardModelIdentifier=agentInventoryCardModelIdentifier, agentInventoryComponentMnemonic=agentInventoryComponentMnemonic, agentInventoryCardIndex=agentInventoryCardIndex, agentInventoryCardDescription=agentInventoryCardDescription, agentInventoryCardTypeEntry=agentInventoryCardTypeEntry, agentInventoryCardGroup=agentInventoryCardGroup, AgentInventoryUnitType=AgentInventoryUnitType, agentInventoryComponentName=agentInventoryComponentName)
