from Node import Node

def getVCG(top, bottom) :

	nodes = {pin:list() for pin in set(top) if pin != '0'}

	for t, b in zip(top, bottom) :
		if '0' not in [t, b] :
			nodes[t].append(b)

	for pin, connections in nodes.copy().iteritems() :
		for p in connections :
			if p in nodes.keys() :
				nodes[pin] = list(set(nodes[pin])-set(nodes[p])) 

	n = list()
	for x in nodes.values() :
		n += x
	
	roots = sorted((list((set(top)|set(bottom))-set(n)-set('0'))))

	return roots, nodes

def getZoneRepresentation(top, bottom) :

	pins = list((set(top)|set(bottom))-set('0'))
	zones = [set() for i in top]

	for p in pins :
		rtop = top[:]
		rtop.reverse()
		rbottom = bottom[:]
		rbottom.reverse()
		
		init = len(top)
		end = 0
		if p in top :
			init = top.index(p)
			end = len(top)-rtop.index(p)-1

		if p in bottom :
			foo = bottom.index(p)
			init = foo if init > foo else init
			foo = len(bottom)-rbottom.index(p)-1
			end = foo if end < foo else end

		for i in range(init, end+1) :
			zones[i].update(p)

	for z in zones[:] :
		for zn in zones :
			if z <= zn and z is not zn :
				zones.remove(z)
				# z = zones[0]
				break

	return [sorted(i) for i in list(zones)] 
	#for each position check if it is a sub set of other position, if so
	#delete that position

def noConflict(p, zones, current_net) :
	if not list(current_net) :
		return True
	else :
		for z in zones :
			if len(set(current_net)&set(z))>0 and set(p) <= set(z) :
				return False
		return True

def updateVCG(parents, current_net, nodes) :

	parents = set(parents) - set(current_net)

	parent_implicant = set()
	for n in current_net :
		if n in nodes.keys() :
			parent_implicant.update(nodes[n])

	for key, value in nodes.copy().iteritems() :
		if key in current_net :
			del nodes[key]
		else :
			parent_implicant -= (set(value)&set(parent_implicant))	

	return sorted(list(parent_implicant|parents))