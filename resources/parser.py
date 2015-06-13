import re
class Parser:

	"""Parses a document the instruction are:
	1: move
	2: lookUp
	3: turnRight
	4: lookDown
	5: putItem
	6: pickItem
	
	--- conditional statements --- (not yet)
	60: if [cond] 
	61: else
	62: ifEnd


	--- control statements ---
	70: repeat [n] times
	71: repeatEnd 

	---booleans---
	80: isWallInfront
	81: isWallAtRight
	82: isWallBehind
	83: isWallAtLeft
	84: isOverItem
	85: hasItem

	---errors and other non instructions---
	98: -whiteline
	99: -noRealInstruction
	100: -endOfIntructions
  """
  	patternRepeat = re.compile("repeat[ ]+\d+[ ]+times") #repeat statement

	def __init__(self):
		pass

	def parse(self, string):   #first command to be called
		commands = []
		lines = [ l.strip() for l in string.split("\n")]
		while(lines):
			aline = lines.pop(0)
			self.preProcess(aline, lines, commands)
		commands.append(100)
		return commands


	def preProcess(self, string, inputList, resultList):  #preprocess checks for command statements
		if(self.patternRepeat.match(string)):
			forList = []
			forList.append(70)
			forList.extend([int(n) for n in string.split() if n.isdigit()])
			inerList = []
			self.createInnerList("repeatEnd",inputList, inerList)
			forList.append(inerList)
			resultList.append(forList)
		else:
			self.insertToken(string, resultList)



	def createInnerList(self, terminator, inputList, outputList): #creanes a list of parameters until end val
		while(inputList):
			bline = inputList.pop(0)
			if(bline == terminator):
				outputList.append(71)
				break
			else:
				self.preProcess(bline,inputList,outputList) #recursion in case of nested operations

	def insertToken(self,line, alist):
		if line == "move":
			alist.append(1)
		elif line == "lookUp":
			alist.append(2)
		elif line == "turnRight":
			alist.append(3)
		elif line == "lookDown":
			alist.append(4)
		elif line == "putItem":
			alist.append(5)
		elif line == "pickItem":
			alist.append(6)
		elif line == "isWallInfront":
			alist.append(80)
		elif line == "isWallAtRight":
			alist.append(81)
		elif line == "isWallBehind":
			alist.append(82)
		elif line == "isWallAtLeft":
			alist.append(83)
		elif line == "isOverItem":
			alist.append(84)
		elif line == "hasItem":
			alist.append(85)
		elif line == "":
			alist.append(98)
		else: 
			alist.append(99)



	def parseFile(self, filelocation):
		txt = open(filelocation)
		lines = txt.read()
		txt.close()
		return parse(lines)

