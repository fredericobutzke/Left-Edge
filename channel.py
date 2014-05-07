import Tkinter 
from Tkinter import *

# top_pins = ['0','A','D','E','A','F','G','0','D','I','J','J']
# bottom_pins = ['B','C','E','C','E','B','F','H','I','H','G','I']
# tracks = [['A', 'J'], ['D'], ['E', 'G'], ['C', 'F', 'I'], ['B', 'H']]

class UI():
	def __init__ (self, top_pins, bottom_pins, tracks) :
		self.top_pins = top_pins
		self.bottom_pins = bottom_pins
		self.tracks = tracks

		print tracks
		top = Tkinter.Tk()
		
		track_heigh = 50
		track_space = 25
		
		pin_width = 100
		pin_space = 50
		
		frame=Frame(top)
		frame.grid(row=0,column=0)
		w=Canvas(frame,bg='#FFFFFF',width=1000,height=600,scrollregion=(0,0,200*len(top_pins),400+100*len(tracks)))
		hbar=Scrollbar(frame,orient=HORIZONTAL)
		hbar.pack(side=BOTTOM,fill=X)
		hbar.config(command=w.xview)
		vbar=Scrollbar(frame,orient=VERTICAL)
		vbar.pack(side=RIGHT,fill=Y)
		vbar.config(command=w.yview)
		w.config(xscrollcommand=hbar.set, yscrollcommand=vbar.set)
		w.pack(side=LEFT,expand=TRUE,fill=BOTH)
		
		for j, p in enumerate(self.top_pins) :
			if p is not '0' :
				print p
				xplace = j*150+50
				bbox = (xplace, 5, xplace+100, 105)
				q = w.create_rectangle(bbox, fill="white", tags=('pino', p))
				bbox = (xplace+25, 5+25, xplace+100-25, 105-25)
				sq = w.create_rectangle(bbox, fill="black", tags=("r2", "pin", "top", p, j))
				tx = w.create_text((xplace+50, 5+50), text=p, width=25, fill="white", tags=("text", "pin", "top", p, j))
		
		bottom_y = 75*len(self.tracks)+125
		for j, p in enumerate(self.bottom_pins) :
			if p is not '0' :
				xplace = j*150+50
				bbox = (xplace, bottom_y, xplace+100, bottom_y+pin_width)
				q = w.create_rectangle(bbox, fill="white", tags=("r1", "pin","bottom",  p, j))
				bbox = (xplace+25, bottom_y+25, xplace+100-25, bottom_y+pin_width-25)
				sq = w.create_rectangle(bbox, fill="black", tags=("r2", "pin", "bottom", p, j))
				tx = w.create_text((xplace+50, bottom_y+50), text=p, width=25, fill="white", tags=("text", "pin", "bottom", p, j))
		
		
		# for i in range(5) :
			# 
			# bbox = (50, yplace, 300, yplace+track_heigh)
			# q = w.create_rectangle(bbox, fill="light blue", outline="light blue", tags=("track", i))
		
		# x1, y1, x2, y2 = w.coords(sq)
		
		for i, pins in enumerate(self.tracks) :
		
			yplace = i*75+125
		
			for n in pins :
		
				# find first and last
				rtop = self.top_pins[:]
				rtop.reverse()
				rbottom = self.bottom_pins[:]
				rbottom.reverse()
				
				init = len(self.top_pins)
				end = 0
				if n in self.top_pins :
					init = self.top_pins.index(n)
					end = len(self.top_pins)-rtop.index(n)-1
		
				if n in self.bottom_pins :
					foo = self.bottom_pins.index(n)
					init = foo if init > foo else init
					foo = len(self.bottom_pins)-rbottom.index(n)-1
					end = foo if end < foo else end
				
				# draw the rectangle between them
				bbox = (150*init+75, yplace, 150*end+125, yplace+track_heigh)
				tr = w.create_rectangle(bbox, fill="light blue", outline="light blue", tags=("track", n, i))
		
				# for each pin of that netlist
				ids = tuple(set(w.find_withtag('top'))&set(w.find_withtag(n))&set(w.find_withtag('r2')))
				for pn in ids :
					# 	draw rectangle from its center to the track
					px1, py1, px2, py2 = w.coords(pn)
					qx1, qy1, qx2, qy2 = w.coords(tr)
					bbox = (px1, py2, px1+50, qy2)
					q = w.create_rectangle(bbox, fill="light pink", outline="light pink", tags=("track", "HORIZONTAL", n, i))
					bbox = (px1, qy1, px1+50, qy2)
					q = w.create_rectangle(bbox, fill="light blue", outline="light pink")
					bbox = (px1+10, qy1+10, px1+40, qy2-10)
					q = w.create_rectangle(bbox, fill="light pink", outline="light blue")
				#for each pin of that netlist
				ids = tuple(set(w.find_withtag('bottom'))&set(w.find_withtag(n))&set(w.find_withtag('r2')))
				for pn in ids :
					# 	draw rectangle from its center to the track
					px1, py1, px2, py2 = w.coords(pn)
					qx1, qy1, qx2, qy2 = w.coords(tr)
					bbox = (px1, qy2, px1+50, py1)
					q = w.create_rectangle(bbox, fill="light pink", outline="light pink", tags=("track", "HORIZONTAL", n, i))
					bbox = (px1, qy1, px1+50, qy2)
					q = w.create_rectangle(bbox, fill="light blue", outline="light pink")
					bbox = (px1+10, qy1+10, px1+40, qy2-10)
					q = w.create_rectangle(bbox, fill="light pink", outline="light blue")
		
		top.mainloop()