class Parser:

	"""Parses a document the instruction are:
	1: move
	2: lookUp
	3: turnRight
	4: lookDown
	5: putItem
	6: pickItem
	98: -whiteline
	99: -noRealInstruction
  """

	def __init__(self):
		pass

	def parse(self, location):
		commands = []
		txt = open(location)
		lines = [line.strip() for line in txt]
		txt.close()
		for line in lines:
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
			elif line == "":
				commands.append(98)
			else: 
				commands.append(99)
		return commands
