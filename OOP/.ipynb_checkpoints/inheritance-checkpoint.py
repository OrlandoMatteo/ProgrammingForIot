class Animal(object):
	"""docstring for Animal"""
	def __init__(self, name):
		self.name=name
	def __repr__(self):
		return "{} is an animal".format(self.name)

class Quadruped(Animal):
	"""docstring for Quadruped"""
	def __init__(self,name):
		Animal.__init__(self,name)
		self.n_of_legs=4		
	def __repr__(self):
		return "{} is a quadruped".format(self.name)

class Dog(Quadruped):
	"""docstring for Dog"""
	def __init__(self, name,family):
		Quadruped.__init__(self,name)
		self.family=family
	def __repr__(self):
		return "{} is a dog of the family {}".format(self.name,self.family)

if __name__ == '__main__':
	pongo=Animal('Pongo')
	print(pongo)
	pongo=Quadruped('Pongo')
	print(pongo)
	pongo=Dog('Pongo','Dalmata')
	print(pongo)
	print(pongo.n_of_legs)