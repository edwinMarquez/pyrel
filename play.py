import sys
from Tkinter import * 
import tkMessageBox

import resources.robot as robot
import resources.mapa as mapa
import resources.parser as parser



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


def drawItem(x, y):
	cor = realcoordinate(x,y)
	return canvas.create_image(cor[0],cor[1], anchor = NW, image=itmImg)
def pickItem(itemId):
	canvas.delete(itemId)



def logic():
	global problem
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
		print("placing Item")
		x = arobot.robot_getX()
		y = arobot.robot_getY()
		numItems = amap.itemsInPosition(x,y)
		amap.placeItem(x, y)
		if(numItems == 0):
			itmInMap[str(x)+"-"+str(y)] = drawItem(x,y) #no need to update if there is already an Image
		
	elif i == 6: #pickItem
		print("picking Item")
		x = arobot.robot_getX()
		y = arobot.robot_getY()
		numItems = amap.itemsInPosition(x,y)
		if(numItems == 0):
			problem = True
			print "robot says: No item to take"
			instruction[:] = []
			tkMessageBox.showwarning("No Item","The robot didn't find an Item and turned off")
		else:
			amap.takeItem(x,y)
			if(numItems == 1):
				pickItem(itmInMap[str(x)+"-"+str(y)])
	elif i == 99: #wrong instruction
		problem = True
		print("robot says: I can't understand")
		instruction[:] = []
		tkMessageBox.showwarning("Language","The robot can't understand and has turned off")
	else:
		pass
	if(instruction):
		master.after(1000, logic)
	elif(not problem):
		tkMessageBox.showinfo("Good","Execution complete :D")

def start():
	iltext = text.get(1.0, END)
	aparser = parser.Parser()
	instruction[:] = aparser.parse(iltext)
	master.after(1000,logic)


canvasWidth = 421
canvasHeigth = 421
rectSize = 20
problem = False #was there a problem in the execution
instruction = []
boundss = {'minx':0, 'maxx':20, 'miny':0, 'maxy':20}
walls = []
amap = mapa.Map([],boundss, walls)
arobot = robot.Robot(1,0,0,0, amap)

#GUI
master = Tk()
canvas = Canvas(master, 
		  width=canvasWidth,
		  height=canvasHeigth)
canvas.pack(side = LEFT)

bg = PhotoImage(file="./resources/rejilla.ppm")
pyrel = []
pyrel.append(PhotoImage(file="./resources/robot.gif"))
pyrel.append(PhotoImage(file="./resources/robot_r.gif"))
pyrel.append(PhotoImage(file="./resources/robot_d.gif"))
pyrel.append(PhotoImage(file="./resources/robot_l.gif"))
itmImg = PhotoImage(file = "./resources/item.gif")
itmInMap = {} #here ill register the positions of the items  sintax = {'x-y':imgId} 


canvas.create_image(1,1, anchor = NW, image=bg)
cord = realcoordinate(0, 0) #set the initial position of the robot

pyrelrobot = canvas.create_image(cord[0],cord[1], anchor=NW, image=pyrel[0])

textFrame = Frame(master)

yscrollbar = Scrollbar(textFrame)
text = Text(textFrame, height = 29, width = 50,yscrollcommand = yscrollbar.set, wrap = NONE)
text.pack(side = LEFT)
yscrollbar.config(command=text.yview)

textFrame.pack(side = RIGHT)
yscrollbar.pack(side=RIGHT, fill=Y)

#input of a filename through command line 
if len(sys.argv) > 1 :
	print sys.argv
	afile = open(sys.argv[1])
	lines = afile.read()
	afile.close()
	text.insert(INSERT, lines, "a")
#input code from a file 

#buttons
btnStart = Button(master, text="Start", command=start)
btnQuit = Button(master, text="Quit", command=master.quit)

btnStart.pack(side = BOTTOM, fill=X)
btnQuit.pack(side = BOTTOM, fill = X)

mainloop()