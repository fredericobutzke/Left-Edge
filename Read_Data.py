class Read_Data():
	"This class reads the data input file"
	def __init__ (self, file_name, permission) :
		fo = open(file_name, permission)
		self.lines = fo.readlines()
		self.top = list()
		self.bottom = list()
	def getData(self) :
		for line in self.lines :
			if ".top" in line :
				self.option = 0
				continue
			elif ".bottom" in line :
				self.option = 1
				continue
			elif ".end" in line :
				netlist = list((set(self.top)|set(self.bottom))-set('0'))
				return self.top, self.bottom, len(self.top), sorted(netlist)

			if self.option == 0 :
				# self.top = [ord(l) for l in line.split()]
				self.top = line.split()
			elif self.option == 1 :
				self.bottom = line.split()
				if len(self.top) != len(self.bottom) :
					raise Exception("Different Lengths")
