from Exercise_1 import *
import math
class Line(object):
	def __init__(self,m=0,q=0):
		"""Line stored as y=mx+q"""
		super(Line,self).__init__()
		self.m=m
		self.q=q
		
	def __repr__(self):
		
		return "Line: y={self.m}x+{self.q}"
	
	def line_from_points(self,pointA,pointB):
		""" line_from_points(A,B)
		Calculate the equation of the line y=mx+q crossing two points A and B"""
		m=(pointB.y-pointA.y)/(pointB.x-pointA.x)
		q=-((pointB.y-pointA.y)/(pointB.x-pointA.x))*pointA.x+pointA.y
		return Line(m,q)
		
		
	def distance(self,point):
		"""distance(point)
		Calculates the distance between the line and the given point"""
		return (abs(point.y-(self.m*point.x+self.q))/math.sqrt(1+self.m**2))
	
	def intersection(self,other):
		"""intersection(otherLine)
		Calculates the point of intersection between the two lines"""
		if self.m==other.m:
			print('The lines are parallel')
			return None
		else:
			x=(other.q-self.q)/(self.m-other.m)
			y=self.m*((other.q-self.q)/(self.m-other.m))+self.q
			return Point(x,y)
		