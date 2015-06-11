class Map:
	map_items = {}
	bounds = {}
	walls = []

	def __init__(self, pitemlist, pbounds, pwalls):
		map_items = pitemlist
		self.bounds.update(pbounds)
		self.walls += pwalls

	def isItem(self, x ,y):
		return (str(x)+ '-' + str(y)) in map_items

	def placeItem(self, x , y):
		key = str(x) + '-' + str(y)
		if( key in map_items):
			map_items[key] += 1
		else:
			map_items[key] = 1

	def takeItem(self, x , y):
		key = str(x) + '-' + str(y)
		if(key in map_items):
			map_items[key] -= 1
			return True
		else:
			return False