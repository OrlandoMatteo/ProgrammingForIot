import random
if __name__=="__main__":
	#Create a vector of random numbers (just to avoid to insert the numbers manually)
	numbers=[random.randint(1,20) for i in range(16)]
	#Set the value of the sum to 0 and max and min to the first number of the array
	sum_of_n=0
	l=len(numbers)
	maximum=numbers[0]
	minimum=numbers[0]	
	#Add each number to the sum and check if it's the max or the min
	for n in numbers:
		sum_of_n+=n
		if n>maximum:
			maximum=n
		if n<minimum:
			mimnimum=n
	print(f"The list of numbers is {numbers}")
	print(f"Average : {sum_of_n/len(numbers)}")
	print(f"Max : {maximum}")
	print(f"min : {minimum}")
		
    