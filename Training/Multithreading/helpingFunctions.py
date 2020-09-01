def bubbleSort(array):
	"""bubbleSort(array)
		array: is the list to sort"""
	for i in range(len(array)):
			for j in range(len(array)-i-1):
				if array[j]>array[j+1]:
						array[j],array[j+1]=array[j+1],array[j]

def binarySearch(toFind,array):
	""" binarySearch(toFind,array)
	toFind: is the number to find
	array: the array to search into """
	found=False
	splitSize=len(array)//2
	indexToCheck=len(array)//2
	position=None
	while not found:
		splitSize=splitSize//2
		if splitSize==0:
			splitSize=1
		if toFind< array[indexToCheck]:		
			indexToCheck=indexToCheck-splitSize
		elif toFind>array[indexToCheck]:
			indexToCheck=indexToCheck+splitSize
		else:
			found=True
			position=indexToCheck
	return position
			
