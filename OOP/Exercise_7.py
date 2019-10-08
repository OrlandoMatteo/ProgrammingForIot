import math
class Circle(object):
	"""docstring for Circle"""
	def __init__(self, radius):
		self.radius=radius
	def perimeter(self):
		return (2*math.pi*self.radius)
	def area(self):
		return (math.pi*self.radius**2)

class Cylinder(Circle):
	"""docstring for Cylinder"""
	def __init__(self, radius,height):
		Circle.__init__(self,radius)
		self.height=height
	def area(self):
		return (self.perimeter()*self.height+2*Circle(self.radius).area())
	def volume(self):
		return (Circle(self.radius).area()*self.height)

if __name__ == '__main__':
	a=Circle(3)
	print(a.perimeter())
	print(a.area())
	b=Cylinder(3,8)
	print(b.area())
	print(b.volume())