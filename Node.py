class Node():
	"""docstring for Node"""
	def __init__(self, name):
		self.name = name
		self.previous = list()
		self.next = list()

	def getPreviousList() :
		return self.previous

	def addPreviousNode(arg) :
		self.previous.append(arg)

	def removePreviousNode(arg) :
		if arg in self.previous :
			self.previous.remove(arg)

	def getPreviousList() :
		return self.next

	def addNextNode(arg) :
		self.next.append(arg)

	def removeNextNode(arg) :
		if arg in self.next :
			self.next.remove(arg)


		