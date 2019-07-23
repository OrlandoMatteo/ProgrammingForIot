from Exercise_1 import *
import math
class Line(object):
	def __init__(self,m=0,q=0):
		super(Line,self).__init__()
		self.m=m
		self.q=q
		
	def __repr__(self):
		
		return "Line: y={}x+{}".format(self.m,self.q)
	
	def line_from_points(self,pointA,pointB):
		m=(pointB.y-pointA.y)/(pointB.x+pointA.y)
		q=-((pointB.y-pointA.y)/(pointB.x+pointA.y))*pointA.x+pointA.y
		#self.m=(pointB.y-pointA.y)/(pointB.x+pointA.y)
		#self.q=-((pointB.y-pointA.y)/(pointB.x+pointA.y))*pointA.x+pointA.y
		return Line(m,q)
		
		
	def distance(self,point):
		return (abs(point.y-(self.m*point.x+self.q))/math.sqrt(1+self.m**2))
	
	def intersection(self,other):
		if self.m==other.m:
			print('The lines are parallel')
			return None
		else:
			x=(other.q-self.q)/(self.m-other.m)
			y=self.m*((other.q-self.q)/(self.m-other.m))+self.q
			return Point(x,y)
		