import math
class Point(object):
	"""Class for a Point object: the available methods are move(x,y) and distance(another_point)"""
	def __init__(self, x,y,):
		super(Point, self).__init__()
		self.x = x
		self.y = y
	def __repr__(self):
		return "{},{}".format(self.x,self.y)
	def move(self,vectorX=0,vectorY=0):
		"""
		Insert the x and the y component of the vector you want to apply to the point
		"""
		self.x+=vectorX
		self.y+=vectorY
	def distance(self,other):
		return math.sqrt((self.x-other.x)**2+(self.y-other.y)**2)
		