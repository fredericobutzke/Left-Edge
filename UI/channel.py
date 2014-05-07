import Tkinter 
from Tkinter import *

top_pins = ['0','A','D','E','A','F','G','0','D','I','J','J']
bottom_pins = ['B','C','E','C','E','B','F','H','I','H','G','I']
tracks = [['A', 'J'], ['D'], ['E', 'G'], ['C', 'F', 'I'], ['B', 'H']]

top = Tkinter.Tk()

track_heigh = 50
track_space = 25

pins = len(top_pins)
pin_width = 100
pin_space = 50

w = pins * pin_width + pins * pin_space * 2
h = tracks * track_heigh * track_space * 2

w = Canvas(top)
w.config(width=150+50*len(top_pins)*5, height=205+len(tracks)*100)
w.pack()

for j, p in enumerate(top_pins) :
	if p is not '0' :
		xplace = j*150+50
		bbox = (xplace, 5, xplace+100, 105)
		q = w.create_rectangle(bbox, fill="white", tags=("r1", "pin", p, j))
		bbox = (xplace+25, 5+25, xplace+100-25, 105-25)
		sq = w.create_rectangle(bbox, fill="black", tags=("r2", "pin", p, j))
		tx = w.create_text((xplace+50, 5+50), text=p, width=25, fill="white", tags=("text", "pin", p, j))

bottom_y = 105+100*len(tracks)
for j, p in enumerate(bottom_pins) :
	if p is not '0' :
		xplace = j*150+50
		bbox = (xplace, bottom_y, xplace+100, bottom_y+pin_width)
		q = w.create_rectangle(bbox, fill="white", tags=("r1", "pin", p, j))
		bbox = (xplace+25, bottom_y+25, xplace+100-25, bottom_y+pin_width-25)
		sq = w.create_rectangle(bbox, fill="black", tags=("r2", "pin", p, j))
		tx = w.create_text((xplace+50, bottom_y+50), text=p, width=25, fill="white", tags=("text", "pin", p, j))

# DRAW FIVE TRACKS

mainloop()

# x1, y1, x2, y2 = w.coords(sq)