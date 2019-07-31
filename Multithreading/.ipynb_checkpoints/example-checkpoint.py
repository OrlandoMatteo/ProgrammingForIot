import numpy as np
import time
x=np.arange(0,6.28,0.1)
y=np.sin(x)
t=0
def acquire():
	global t
	t+=1
	return np.roll(y,-t*10)
def process(data):
	return data
	
	
	