#!/usr/bin/python

from Read_Data import Read_Data
import Utilities
from channel import UI
import getopt
import sys

##### 
#Main

verbose = False
try:
	values, arguments = getopt.getopt(sys.argv[1:], "i:hv")
	if values == [] or "i" not in [i[0].strip('-') for i in values] :
		values = [('-h','')]
except getopt.GetoptError :
	print './left_edge.py -i <inputfile>'	
for opt, value in values :
	if opt == "-h" :
		print 'Usage:'
		print 'Required Arguments:'
		print '-i <inputfile>'
		sys.exit()
	elif opt == "-i" :
		input_file = value
	elif opt == "-v" :
		verbose = True

rd = Read_Data(value, "r")
top, bottom, columns, netlist = rd.getData()
if verbose :
	print "\nNetlist Information: "
	print "Columns: ", columns
	print "Top pins: ", top
	print "Bottom pins: ", bottom
	print "Netlist: ", netlist

rtop = top[:]
rbottom = bottom[:]
total_nelist = top + bottom
for i in list(set(top)|set(bottom)) :
	if total_nelist.count(i) < 2 and i != '0' :
		if i in rtop :
			rtop.insert(rtop.index(i), '0')
			rtop.remove(i)
		if i in rbottom :
			rbottom.insert(rbottom.index(i), '0')
		netlist.remove(i)

if verbose : print "\nVCG"
parents, nodes = Utilities.getVCG(rtop, rbottom)
if verbose : print "Parents: ", parents
if verbose : print "Nodes: ", nodes

if verbose : print "\nZone Representation"
zones = Utilities.getZoneRepresentation(rtop, rbottom)
if verbose : print "Zones: ", zones

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
for i, t in enumerate(final_zone) :
	print "Track %i" % (i+1), " has the following netlists: ", t

UI(top, bottom, final_zone)