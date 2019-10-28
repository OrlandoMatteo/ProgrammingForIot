class Calculator(object):
	"""Calculator that has an attribute "brand" and 4 methods:
	add(),sub(),mul(),div()"""
	def __init__(self,brand):
		self.brand=brand
	def add(self,a,b):
		"""it sill sum a and b"""
		addition=a+b
		return addition
	def sub(self,a,b):
		return a-b
	def mult(self,a,b):
		return a+b
	def divide(self,a,b):
		if b!=0:
			return	a/b
		else:
			return None
	def showBrand(self):
		print(self.brand)
		
		