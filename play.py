import sys
from Tkinter import * 
import tkMessageBox

import resources.robot as robot
import resources.mapa as mapa
import resources.parser as parser


canvasWidth = 421
canvasHeigth = 421
rectSize = 20
problem = False

#definitions
def realcoordinate(x, y):
	"""recives the file and column but relative to the bacground grid """
	return (x*rectSize+1, (421-rectSize)-rectSize*y)
def move_up():
	canvas.move(pyrelrobot, 0,-20)
def move_right():
	canvas.move(pyrelrobot,20,0)
def move_dow():
	canvas.move(pyrelrobot,0,20)
def move_left():
	canvas.move(pyrelrobot,-20,0)
def rotate_right(index):
	canvas.itemconfig(pyrelrobot, image = pyrel[index-1])
def lookUp():
	canvas.itemconfig(pyrelrobot, image = pyrel[0])
def lookDown():
	canvas.itemconfig(pyrelrobot, image = pyrel[2])


def logic():
	if not instruction:
		return False
	i = instruction.pop(0)
	if i == 1: #move
		canDo = arobot.robot_moveinfront();
		if canDo:
			look = arobot.robot_getLooking()
			print("moving")
			if look == 1:
				move_up()
			elif look == 2:
				move_right()
			elif look == 3:
				move_dow()
			elif look == 4:
				move_left()
		else:
			problem = True 
			print "HIT D:"
			instruction[:] = [] #ends the execution
			tkMessageBox.showwarning("Hit", "The robot was broken, in a wall :(")
	elif i == 2: #lookUp
		print("looking Up now sir")
		lookUp()
		arobot.robot_setLooking(1)
	elif i == 3: #turnRight
		print("Turning right")
		look = arobot.robot_getLooking()
		if look == 4:
			arobot.robot_setLooking(1)
			rotate_right(1)
		else:
			arobot.robot_setLooking(look+1)
			rotate_right(look + 1)
	elif i == 4: #lookDown
		lookDown()
		arobot.robot_setLooking(3)
	elif i == 5: #putItem
		pass
	elif i == 6: #pickItem
		pass
	elif i == 99: #wrong instruction
		pass
	else:
		pass

	if(instruction):
		start()
	elif(not problem):
		tkMessageBo.showinfo("Good","Execution complete :D")

def start():
	master.after(1000, logic)

#setting up variables
aparser = parser.Parser()
instruction = aparser.parse(sys.argv[1]) #no validation yet
boundss = {'minx':0, 'maxx':20, 'miny':0, 'maxy':20}
walls = []
amap = mapa.Map([],boundss, walls)
arobot = robot.Robot(1,0,0,0, amap)

#GUI
master = Tk()
canvas = Canvas(master, 
		  width=421,
		  height=421)
canvas.pack()

bg = PhotoImage(file="./resources/rejilla.ppm")
pyrel = []
pyrel.append(PhotoImage(file="./resources/robot.gif"))
pyrel.append(PhotoImage(file="./resources/robot_r.gif"))
pyrel.append(PhotoImage(file="./resources/robot_d.gif"))
pyrel.append(PhotoImage(file="./resources/robot_l.gif"))


canvas.create_image(1,1, anchor = NW, image=bg)
cord = realcoordinate(0, 0) #set the initial position of the robot

pyrelrobot = canvas.create_image(cord[0],cord[1], anchor=NW, image=pyrel[0])

btnStart = Button(master, text="Start", command=start)
btnQuit = Button(master, text="Quit", command=master.quit)

btnStart.pack()
btnQuit.pack()

mainloop()