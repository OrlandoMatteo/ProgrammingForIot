def add(a,b):
	print(f"{a} + {b} = {a+b}")
def sub(a,b):
	print(f"{a} - {b} = {a-b}")
def mul(a,b):
	print(f"{a} * {b} = {a*b}")
def div(a,b):
	print(f"{a} / {b} = {a/b:.3}")

if __name__=="__main__":
	a=2
	b=7
	add(a,b)
	sub(a,b)
	mul(a,b)
	div(a,b)