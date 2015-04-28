#temp payment class
import random

class Payment:

	def __init__(self,typ,number=None,name=None):
		self.cardNum = number
		self.name = name
		if typ == "credit":
			if self.cardNum == None:
				self.cardNum = random.randint(1000000000000000,9999999999999999)
		self.typ = typ

	def getCardNumber(self):
		return self.cardNum

	def getName(self):
		return self.name

	def getType(self):
		return self.typ
