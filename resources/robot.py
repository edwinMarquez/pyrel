
class Robot:

	def __init__(self, looking, x, y, items, mapa):
		""" start the robot \n
			looking is the direction that the robot is looking at
			1 up, 2 right, 3 down, 4 left \n
			boundss is a dictionari with the limits of the map in maxy miny maxx minx"""
		self.looking = looking   
		self.x = x			     #position x in the grid
		self.y = y               #position y in the grid
		self.items = items       #the number of items to carry   
		self.mapa = mapa

	def __createWallKey(self, x, y):
		return str(self.x) + '-'+ str(self.y) + '&'+ str(x) + '-' + str(y)

	def robot_moveinfront(self):
		if self.looking == 1:
			if(self.y == self.mapa.bounds['maxy']):
				return False
			elif(self.robot_wallUp()):
				return False
			else: 
				self.y += 1
				return True
		elif self.looking == 2:
			if(self.x == self.mapa.bounds['maxx']):
				return False
			elif(self.robot_wallAtRight()):
				return False
			else:
				self.x += 1
				return True
		elif self.looking == 3:
			if(self.y == self.mapa.bounds['miny']):
				return False
			elif(self.robot_wallDown()):
				return False
			else:
				self.y -= 1
				return True
		elif self.looking == 4:
			if(self.x == self.mapa.bounds['minx']):
				return False
			elif(robot_wallAtLeft()):
				return False
			else:
				self.x -= 1
				return True

	def robot_changeDirection(self, direction):
		self.looking = direction

	def robot_putItem(self):
		if(self.items > 0):
			self.items -= 1
			self.mapa.placeItem(x,y)
			return True
		else:
			return False

	def robot_getLooking(self):
		return self.looking

	def robot_setLooking(self, looking):
		self.looking = looking

	def robot_wallUp(self):
		return self.__createWallKey(self.x+1,self.y) in self.mapa.walls

	def robot_wallAtRight(self):
		return self.__createWallKey(self.x,self.y+1) in self.mapa.walls

	def robot_wallDown(self):
		return self.__createWallKey(self.x,self.y-1) in self.mapa.walls

	def robot_wallAtLeft(self):
		return self.__createWallKey(self.x-1,self.y) in self.mapa.walls

	def robot_isWallInfront(self):
		if(self.looking == 1):
			return self.robot_wallUp() or self.y == self.mapa.bounds['maxy']
		elif(self.looking == 2):
			return self.robot_wallAtRight() or self.x == self.mapa.bounds['maxx']
		elif(self.looking == 3):
			return self.robot_wallDown() or self.y == self.mapa.bounds['miny']
		elif(self.looking == 4):
			return self.robot_wallAtLeft() or self.x == self.mapa.bounds['minx']

	def robot_isWallAtRight(self):
		if(self.looking == 1):
			return self.robot_wallAtRight() or self.x == self.mapa.bounds['maxx']
		elif(self.looking == 2):
			return self.robot_wallDown() or self.y == self.mapa.bounds['miny']
		elif(self.looking == 3):
			return self.robot_wallAtLeft() or self.x == self.mapa.bounds['minx']
		elif(self.looking == 4):
			return self.robot_wallUp() or self.y == self.mapa.bounds['maxy']

	def robot_isWallBehind(self):
		if(self.looking == 1):
			return self.robot_wallDown() or self.y == self.mapa.bounds['miny']
		elif(self.looking == 2):
			return self.robot_wallAtLeft() or self.x == self.mapa.bounds['minx']
		elif(self.looking == 3):
			return self.robot_wallUp() or self.y == self.mapa.bounds['maxy']
		elif(self.looking == 4):
			return self.robot_wallAtRight() or self.x == self.mapa.bounds['maxx']

	def robot_isWallAtLeft(self):
		if(self.looking == 1):
			return self.robot_wallAtLeft() or self.x == self.mapa.bounds['minx']
		elif(self.looking == 2):
			return self.robot_wallUp() or self.y == self.mapa.bounds['maxy']
		elif(self.looking == 3):
			return self.robot_wallAtRight() or self.x == self.mapa.bounds['maxx']
		elif(self.looking == 4):
			return self.robot_wallDown() or self.y == self.mapa.bounds['miny']

	def robot_isOverItem(self):
		return self.mapa.itemsInPosition(self.x, self.y) > 0

	def robot_hasItem(self):
		return self.items > 0

	def robot_getX(self):
		return self.x
	def robot_getY(self):
		return self.y




