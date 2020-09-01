from pointClass import *
if __name__ == '__main__':
	a=Point(2,2)
	b=Point(2,8)
	dist=a.distance(b)
	print(dist)
	a.move(2,2)
	print(a.x,a.y)
	