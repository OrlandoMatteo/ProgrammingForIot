class Block(object):
	"""docstring for Block"""
	def __init__(self,name,toolToUse,breakable):
		self.name=name
		self.toolToUse=toolToUse
		self.breakable=breakable
	def __repr__(self):
		return self.name
	def isBreakable(self):
		return self.breakable
	def breakWith(self,tool):
		if self.isBreakable():
			if tool in self.toolToUse:
				pass
			else:
				pass
		else:
			print("You can't break it!")
			pass
class Cobblestone(Block):
	def __init__(self,name,toolToUse,breakable):
		Block.__init__(self,name,toolToUse,breakable)
		self.drop=self
	def breakWith(self,tool):
		if self.isBreakable():
			if tool in self.toolToUse:
				return self.drop
			else:
				return None
		else:
			print("You can't break it!")
			return None


class Stone(Block):
	def __init__(self,name,toolToUse,breakable):
		Cobblestone.__init__(self,name,toolToUse,breakable)
		self.drop=Cobblestone("cobblestone","pickaxe",True)
	def breakWith(self,tool):
		if self.isBreakable():
			if tool in self.toolToUse:
				return self.drop
			else:
				return None
		else:
			print("You can't break it!")
			return None


class Chest(Block):
	"""docstring for Chest"""
	def __init__(self,name,toolToUse,breakable):
		Block.__init__(self,name,toolToUse,breakable)
		self.content=[]

	def breakWith(self,tool):
		if self.isBreakable():
			if tool in self.toolToUse:
				drop=[item for item in self.content]
				self.content=[]
				drop.append(self)
				return drop
			else:
				return None
		else:
			print("You can't break it!")
			return None
	def insertItem(self,item):
		self.content.append(item)


if __name__ == '__main__':
	cobblestone=Cobblestone("cobblestone","pickaxe",True)
	stone=Stone("stone","pickaxe",True)
	chest=Chest("myChest",["pickaxe","axe","hand"],True)
	cb=cobblestone.breakWith("pickaxe")
	print(cb)
	st=stone.breakWith("pickaxe")
	print(st)
	for i in range(4):
		chest.insertItem(cb)
	ct=chest.breakWith("")
	print(ct)

		
		
		