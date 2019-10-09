import random

class Card(object):
	"""Each a card has a suit and a value defined when it's created"""
	
	def __init__(self, suit, value):
		self.suit = suit
		self.value= value
	
	def __repr__(self):
		return f"{self.value} of {self.suit}"

class Deck(object):
	"""The deck is composed by 13 cards for each of the 4 suits. 
	It also has:
		a shuffle() method that returns the shffled deck
		a draw(n) method that returns a list of n cards """

	suits=['Hearts','Diamonds','Clubs','Spades']	
	values=['A','2','3','4','5','6','7','8','9','10','J','Q','K']
	
	
	def __init__(self ):
		self.cards=[ Card(s,v) for s in Deck.suits for v in Deck.values]
	
	def shuffle(self):
		"""Shuffles the deck"""
		random.shuffle(self.cards)
	
	def draw(self,n=1):
		"""Returns n cards, 1 if n is not specified"""
		if n<=len(self.cards):
			drawn=[]
			for i in range(n):
				drawn.append(self.cards.pop())
			return drawn
		elif n>len(self.cards) and len(self.cards)!=0:
			return self.draw(len(self.cards))
		else:
			return None