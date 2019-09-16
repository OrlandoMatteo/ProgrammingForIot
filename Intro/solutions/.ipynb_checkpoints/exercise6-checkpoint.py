if __name__=="__main__":
    #Receive 1 number as input
	number=int(input('Write a number: '))
	
	#The input is a multiple of both 2 and 3
	if number%3==0 and number%2==0:
		print(f" {number} is a multiple of both 2 and 3")
	#The input is a multiple of 2
	elif number%2==0:
		print(f"{number} is a multiple of 2")
	#The input is a multiple of 3
	elif number%3==0:
		print(f" {number} is a multiple of 3")
	#All the other cases
	else:
		print(f"{number} is not a multiple of 2 nor 3")