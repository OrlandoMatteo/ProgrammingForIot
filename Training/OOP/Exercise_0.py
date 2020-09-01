import math
class SquareManager(object):
	def __init__(self,side):
		self.side=side
	
	def area(self):
		return self.side**2

	def perimeter(self):
		return self.side*4

	def diagonal(self):
		return self.side*math.sqrt(2)
