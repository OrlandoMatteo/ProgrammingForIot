class Calculator(object):
	def __init__ (self):
		pass
	def add(self,a,b):
		print(f"{a} + {b} = {a+b}")
	def sub(self,a,b):
		print(f"{a} - {b} = {a-b}")
	def mul(self,a,b):
		print(f"{a} * {b} = {a*b}")
	def div(self,a,b):
		print(f"{a} / {b} = {a/b:.3}")