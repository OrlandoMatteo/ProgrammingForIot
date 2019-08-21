import random
import requests
import time
import threading
import string
class MyThread(threading.Thread):
	def __init__(self, threadID, shift,c_sentence,og_sentence):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.shift = shift
		self.crypted_sentence=c_sentence
		self.og_sentence=og_sentence		
	def run(self):
		shifted_alphabet=create_dict(self.shift)
		test_uncrypt=decrypt(self.crypted_sentence,shifted_alphabet)
		if test_uncrypt==self.og_sentence:
			pass
			#print(self.crypted_sentence+'=>'+self.og_sentence)
			#print('DECRYPTED!!! Shifted of {} letter'.format(self.shift))

def create_dict(shift):
	alphabet=list(string.ascii_lowercase)
	for i in range(shift):
		alphabet.append(alphabet.pop(0))
	return dict(zip(string.ascii_lowercase,alphabet))
def crypt(sentence):
	shifted_alphabet=create_dict(random.randint(0,26))
	crypto_list=[]
	for c in sentence :
		if c!=' ':
			crypto_list.append(shifted_alphabet[c])
		else:
			crypto_list.append(' ')
	return ''.join(crypto_list)

def decrypt(crypted_sentence,test_dict):
	uncrypted_list=[]
	for c in crypted_sentence :
		if c!=' ':
			uncrypted_list.append(test_dict[c])
		else:
			uncrypted_list.append(' ')
	return ''.join(uncrypted_list)

def main():
	text=open('wordlist.txt','r').read()
	words_list=text.lower().splitlines()

	c_words=[]
	for w in words_list[:5000]:
		c_w=crypt(w)
		c_words.append(c_w)


	#og_sentence='frase di prova per controllare che vada tutto brne in questo programma'
	#shift=2
	#shifted_alphabet=create_dict(shift)
	#crypted_sentence=crypt(og_sentence,shifted_alphabet)
	threads=[]
	for j in range(len(c_words)):
		for i in range(len(string.ascii_lowercase)):
			threads.append(MyThread(i,i,c_words[j],words_list[j]))

	inizio=time.time()
	for t in threads:
		 t.start()
	threads[-1].join()
	stop=time.time()
	done=stop-inizio
	print('Done in {}'.format(done))


	inizio=time.time()
	j=0
	for w in c_words:
		for i in range(len(string.ascii_lowercase)):
			test_dict=create_dict(i)
			test_decrypt=decrypt(w,test_dict)
			if test_decrypt==words_list[j]:
				pass
				#print(w+'=>'+words_list[j])
				#print('Decripted {}'.format(i))
		j+=1

	stop=time.time()
	done=stop-inizio
	print('Done in {}'.format(done))
