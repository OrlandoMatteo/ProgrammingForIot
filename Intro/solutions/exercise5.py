if __name__=="__main__":
	#Open the original file read the content and close it
	f_original=open('original.txt')
	original=f_original.read()
	f_original.close()
	
	sentence_to_add='The content of the original file is:'
	#Open the original file, write on it and close it
	f_copy=open('copy.txt','w')
	f_copy.write(sentence_to_add+'\n'+original)
	f_copy.close()