class Parser:

	"""Parses a document the instruction are:
	1: move
	2: lookUp
	3: turnRight
	4: lookDown
	5: putItem
	6: pickItem
	

	--- control statements --- (comming soon)
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
  """

	def __init__(self):
		pass

	def parse(self, string):
		commands = []
		lines = [ l.strip() for l in string.split()]
		for aline in lines:
			self.insertToken(aline, commands)
		return commands

	def insertToken(self,line, commands):
		if line == "move":
			commands.append(1)
		elif line == "lookUp":
			commands.append(2)
		elif line == "turnRight":
			commands.append(3)
		elif line == "lookDown":
			commands.append(4)
		elif line == "putItem":
			commands.append(5)
		elif line == "pickItem":
			commands.append(6)
		elif line == "isWallInfront":
			commands.append(80)
		elif line == "isWallAtRight":
			commands.append(81)
		elif line == "isWallBehind":
			commands.append(82)
		elif line == "isWallAtLeft":
			commands.append(83)
		elif line == "isOverItem":
			commands.append(84)
		elif line == "hasItem":
			commands.append(85)
		elif line == "":
			commands.append(98)
		else: 
			commands.append(99)



	def parseFile(self, filelocation):
		txt = open(filelocation)
		lines = txt.read()
		txt.close()
		return parse(lines)

