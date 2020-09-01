class Car(object):
	"""docstring for Car"""
	def __init__(self, name, speed):
		self.__name=name
		self.__speed=__limitSpeed(speed)
		self.__gear=1

	def __limitSpeed(self,speed):
		if speed < 250:
			return speed
		else:
			return 250
			
	def getName(self):
		return self.__name

	def getSpeed(self):
		return self.__speed
	
	def setSpeed(self, speed):
		self.__speed=__limitSpeed(speed)

	def gearUp(self):
		if self.__gear<6:
			self.__gear+=1

	def gearDown(self):
		if self.__gear > 1:
			self.ger-=1

	def getGear(self):
		return self.__gear
		
		