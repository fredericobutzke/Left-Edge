#!/usr/bin/python

from Read_Data import Read_Data
import Utilities
from channel import UI

rd = Read_Data("netlist.data", "r")
top, bottom, columns, netlist = rd.getData()
print "\nNetlist Information: "
print "Columns: ", columns
print "Top pins: ", top
print "Bottom pins: ", bottom
print "Netlist: ", netlist

print "\nVCG"
parents, nodes = Utilities.getVCG(top, bottom)
print "Parents: ", parents
print "Nodes: ", nodes

print "\nZone Representation"
zones = Utilities.getZoneRepresentation(top, bottom)
print "Zones: ", zones

final_zone = list()

while list(netlist) :
	current_net = list()

	for p in parents :
		if Utilities.noConflict(p, zones, current_net) :
			current_net.append(p)
			netlist.remove(p)
	parents = Utilities.updateVCG(parents, current_net, nodes)

	final_zone.append(current_net)


print "\nSolution: "
print final_zone

UI(top, bottom, final_zone)