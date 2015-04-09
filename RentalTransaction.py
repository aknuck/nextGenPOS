#Transaction

#NEED TO ADD:
#method for combined cash/credit/debit transaction. Would probably do it through a "pay" method that pays off a certain amount of the total and records how much and with what it was payed

import uuid
import datetime
import Store
import Employee
#import Customer
import Payment
import Item

class RentalTransaction:

	def __init__(self,store,cash):#cust,tax):
		self.transactionID = str(uuid.uuid4().int)[:16]
		self.date = datetime.date.today()
		self.time = datetime.datetime.now().time()
		self.items = []
		self.cashier = cash
		#self.customer = cust
		self.store = store
		self.taxRate = store.getTax() #tax rate may change based on state, set to 0 if for item without tax (e.g. food)
		self.runningTotal = 0.00
		self.payment = None #set later in the transaction, after being called by POS with the payment object being passed
		

	#adds an item to the transaction
	def addItem(self,item):
		if self.cashier != None:
			self.items.append(item)
			print "Added Item"
			self.runningTotal += item.getSalePrice()
			print "Current total: $"+str("{0:.2f}".format(self.getCurrentTotal()))
			return True
		else:
			return False

	def setCashier(self,cash):
		self.cashier = cash

	#returns a formatted receipt that can be printed out
	#receipt is 40 wide
	def getReceipt(self):
		if len(self.items) > 0 and self.payment != None:
			width = 35
			nameLine = self.center(self.store.getName(),width)
			locationLine = self.center(self.store.getLocation(),width)
			phoneNumberLine = self.center(self.store.getPhone(),width)


			#starts and ends with a buffer for when the receipt prints
			receipt = '''


'''+nameLine+'''
'''+locationLine+'''
'''+phoneNumberLine+'''

Store: '''+str(self.store.getID())+'''  Register: '''+str(self.store.getID())+'''
Transaction ID: '''+str(self.transactionID)+'''
Cashier: '''+self.cashier.getName()+'''

'''

			count = 0
			for item in self.items:
				count += 1
				receipt += ""+str(count)+"   "+item.getName()+(" "*(width-len(""+str(count)+"   "+item.getName()+"$"+str("{0:.2f}".format(item.getSalePrice())))))+"$"+str("{0:.2f}".format(item.getSalePrice()))+"/day\n"
				if item.getSaleValue() != 0.00:
					receipt += "       SALE ("+str(int(item.getSaleValue()*100))+"%)\n"
				receipt += "       "+item.getNotes()+"\n"

			receipt += ("-"*width)+"\n"
			receipt += "Subtotal"+(" "*(width-len("Subtotal"+"$"+str("{0:.2f}".format(self.getCurrentTotal())))))+"$"+str("{0:.2f}".format(self.getCurrentTotal()))+"/day\n"
			if self.taxRate != 0:
				receipt += "Sales Tax ("+str(self.taxRate*100)+"%)"+(" "*(width-len("Sales Tax ("+str(self.taxRate*100)+"%)"+"$"+str("{0:.2f}".format(self.taxRate*self.getCurrentTotal())))))+"$"+str("{0:.2f}".format(self.taxRate*self.getCurrentTotal()))+"\n"
			receipt += "\nTotal "+(" "*(width-len("Total $"+str("{0:.2f}".format(self.getCurrentTotal()*(1+self.taxRate))))))+"$"+str("{0:.2f}".format(self.getCurrentTotal()*(1+self.taxRate)))+"/day\n\n"
			receipt += ("-"*width)+"\n"
			receipt += "Payed With:\n\n"
			if self.payment.getType() == "cash":
				receipt += self.center("Cash",width)+"\n"
			else:
				receipt += "Credit"+"\n"
				receipt += "Card Num: "+("*"*12)+str(self.payment.getCardNumber())[12:]



			return receipt

		else:
			return "NO ITEMS OR NO PAYMENT"

	#returns a list of all the items in the current transaction
	def getItems(self):
		return self.items

	#used by the getReceipt to center text
	def center(self,s,width):
		return (" "*((width-len(s))/2))+s+(" "*((width-len(s))/2))

	#Gets running total to be displayed as items are added
	def getCurrentTotal(self):
		return self.runningTotal

	#returns the tax rate
	def getTaxRate(self):
		return self.taxRate

	#Applys a discount to an item
	#NOTE NEED TO ADD THAT ONLY MANAGERS CAN DO THIS, MIGHT BE BEFORE THIS IS CALLED (POS)
	def applyDiscount(self,item,discount):
		items.index

	def getItem(self,itemID):
		for item in self.items:
			if item.getID() == itemID:
				return item
		return None

	#removes an item from the current transaction
	def removeItem(self,item):
		response = ""
		#while response.lower() not in ("y","n"):
		#	response = raw_input("Are you sure you want to remove "+item.getName()+" (y/n)")
		#if response.lower() == "y":
		try:
			self.items.remove(item)
			print "item removed"
		except:
			print "error in removing item: "+sys.exc_info()[0]

	#called by POS when at the point point of paying, passes a verified payment method
	def setPayment(self,payment):
		self.payment = payment

	#change payment method. really just calls getPayment again, but that works for now
	def changePayment(self):
		self.getPayment(self)
