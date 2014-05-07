import Tkinter 
from Tkinter import *

top = Tkinter.Tk()

tracks = 5
track_heigh = 4
track_space = 2

pins = 5
pin_width = 100
pin_space = 50

w = pins * pin_width + pins * pin_space * 2
h = tracks * track_heigh * track_space * 2

w = Canvas(top)
w.pack()

#Create a pin
bbox = (0, 0, 100, 100)
sq = w.create_rectangle(bbox, fill="light pink", tags=("pin", "A"))
x1, y1, x2, y2 = w.coords(sq)
bbox = (25, 25, 75, 75)
sq = w.create_rectangle(bbox, fill="black", tags=("pin", "A"))
tx = w.create_text((100, 100), text="A", width=25, fill="white")
items = w.find_withtag("A")

for i in items :
	w.move(i, 50, 50)

mainloop()

