import pdb

if __name__ == '__main__':
	addition=0
	print("you can type p <name_of_variable> to see the value of the variable\n and c to continue until the next breakpoint")
	for i in range(9):
		addition+=1
		pdb.set_trace()