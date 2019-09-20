import random

class Card(object):
	"""docstring for Card"""
	
	def __init__(self, suit, value):
		self.suit = suit
		self.value= value
	
	def __repr__(self):
		return "{} of {}".format(self.value,self.suit)

class Deck(object):
	
	suits=['Hearts','Diamonds','Clubs','Spades']	
	values=['A','2','3','4','5','6','7','8','9','10','J','Q','K']
	
	"""docstring for ClassName"""
	def __init__(self ):
		self.cards=[ Card(s,v) for s in Deck.suits for v in Deck.values]
	
	def shuffle(self):
		random.shuffle(self.cards)
	
	def draw(self,n=1):
		if n<=len(self.cards):
			drawn=[]
			for i in range(n):
				drawn.append(self.cards.pop())
			return drawn
		elif n>len(self.cards) and len(self.cards)!=0:
			return self.draw(len(self.cards))
		else:
			return None