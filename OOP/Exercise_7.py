import math
class Circle(object):
	"""Create a circle knowing his radius"""
	def __init__(self, radius):
		self.radius=radius
	def perimeter(self):
		"""Returns the perimeter of the circle"""
		return (2*math.pi*self.radius)
	def area(self):
		"""Returns the area of the circle"""
		return (math.pi*self.radius**2)

class Cylinder(Circle):
	""""Create a cylinder knowing his radius and his height"""
	def __init__(self, radius,height):
		Circle.__init__(self,radius)
		self.height=height
	def area(self):
		"""Returns the area of the cylinder"""
		return (self.perimeter()*self.height+2*Circle(self.radius).area())
	def volume(self):
		"""Returns the volume of the cylinder"""
		return (Circle(self.radius).area()*self.height)

if __name__ == '__main__':
	a=Circle(3)
	print(a.perimeter())
	print(a.area())
	b=Cylinder(3,8)
	print(b.area())
	print(b.volume())