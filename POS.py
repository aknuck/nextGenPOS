import uuid
import sqlite3 as sql
import sys
import getpass

import Employee
import Transaction
import Store
import Item
import Payment
import RentalTransaction
import DbInteraction

# Class POS serves as a public singleton accessor for __POS which is private
class POS:
	instance = None

	def __init__(self):
		if not POS.instance:
			POS.instance = POS.__POS()            
		
	class __POS:
		
		# Constructor
		def __init__(self):
			self.__PID = str(uuid.uuid4().int)[:16]
			self.__currEmployee = None
			self.__store = self.loadStoreInfo()
			#print self.__store.getName()
			self.__num = 1 #need for the receipt, I guess it can incrememnt or something
			self.currentTransaction = None
			self.dbObj = DbInteraction.DbInteraction()
			
		def getId(self):
			return self.__PID
			
		def getCurrEmployee(self):
			return self.__currEmployee
		
		def getNum(self):
			return self.__num
			
		def getStore(self):
			return self.__store

		def login(self,u,p):
			if u != "":
				print "Dev. Login: ID:  0032, Password: Muffins"
				print "          : ID: 94210, Password: Cupcake"
				
				if (self.__currEmployee):
					print "Cannot login with a user already logged in"
					wasLoggedOut = self.logOut()
					if (wasLoggedOut == False):
						return False
				
				couldLogin = False
				
				while (not couldLogin):
					
					employee = self.__queryDBForLogin (u, p)
					
					if (employee):
						print "\n Login successful"
						self.__currEmployee = employee
						if self.currentTransaction != None:
							self.currentTransaction.setCashier(self.__currEmployee)
						return True
						
					else:
						print "\nCould not find employee with that information"
						return False
			else:
				return None
		
		def main(self):
			while (True):
				if (self.getCurrEmployee()):
					
					cmd = raw_input("\n> ").lower()
					
					permissions = self.getCurrEmployee().getEmpType()
					
					commands =  {"log out":            [self.login,             [], ["Cashier", "Manager", "Admin"]],
								 "store info":         [self.storeInfo,         [], ["Manager", "Admin"]],
								 "transaction log":    [self.viewTransLog,      [], ["Manager", "Admin"]],
								 "create transaction": [self.createTransaction, [], ["Cashier", "Manager", "Admin"]],
								 "help":               [self.viewValidCommands, [], ["Cashier", "Manager", "Admin"]]
								}
					
					if (not cmd or cmd.isspace()):
						pass
					
					elif (cmd in commands):
						if (permissions in commands[cmd][2]):
							commands[cmd][0](*commands[cmd][1])
							
						else:
							permissionStr = ""
							for pS in commands[cmd][2]:
								if permissionStr == "":
									permissionStr += pS
								else:
									permissionStr += " or " + pS
							
							print ("Permission denied.  User must be a " + permissionStr)
					
				else:
					self.login()
			
			
		
							
		def __queryDBForLogin(self, inputId, inputPassword):
			
			try:
				
				connection = sql.connect('DB.db')
		
				with connection:
			
					cursor = connection.cursor()    
					
					# Todo: REMOVE
					if (inputId == ""):
						return Employee.Employee("Sarah Kerigan", 0032, "Cashier")
					
					
					cursor.execute('SELECT e_password FROM Employee WHERE e_id = ?', (inputId,))
					password = cursor.fetchone()[0]
				  
				if (password == inputPassword):
					
					cursor.execute('SELECT name FROM Employee WHERE e_id = ?', (inputId,))
					name = cursor.fetchone()[0]
					
					cursor.execute('SELECT type FROM Employee WHERE e_id = ?', (inputId,))
					empType = cursor.fetchone()[0]
					
					employee = Employee.Employee (name, inputId, empType)
					return employee
					
				else:
					return None
			except:
				return None
				
		def queryDBForItem(self, itemID):
			
			connection = sql.connect('DB.db')
	
			with connection:
		
				cursor = connection.cursor()    
				
				cursor.execute('SELECT * FROM Item WHERE I_ID = ?', (itemID,))
				item = cursor.fetchone()
				
				if item:
					return Item.Item (item[0], item[1], item[2], item[3])
				else:
					return None
				
		def loadStoreInfo(self):
			try:
				f = open("storeinfo.txt",'r').readlines()
				for i in range(len(f)):
					f[i] = f[i].rstrip('\r\n')
				tempStore = Store.Store(f[0],f[1],f[2],float(f[3])/100.00) #file is set up so the first line is name, second is location, third is phone number, fourth is tax
				return tempStore
				
			except:
				print "Error - Store info file may not exist"
				return None
			
		def logOut(self):
			
			#inp0 = self.__getInput ("Are you sure you want to log out %s ? <y or n> " % (self.__currEmployee.getName()), ["y", "n"])
				
			#if (inp0 == "y"):
			if self.currentTransaction != None:
				self.currentTransaction.setCashier(None)
			name = self.__currEmployee.getName()
			self.__currEmployee = None
			print "\nEmployee %s has been logged off." % (name)
			return True
						
			#elif (inp0 == "n"):
			#	print "\nEmployee %s will remain logged on." % (self.__currEmployee.getName())
			#	return False
			#	
			#else:
			#	print "Error: input request failed. Retry command"
			#	return False

		def createRentalTransaction(self):
			if self.__currEmployee != None:
				print self.__currEmployee.getName()
			self.currentTransaction = RentalTransaction.RentalTransaction(self.__store,self.__currEmployee)
			
		def createTransaction(self):
			if self.__currEmployee != None:
				print self.__currEmployee.getName()
			self.currentTransaction = Transaction.Transaction(self.__store,self.__currEmployee)
		
		def getTransactionTotal(self):
			return self.currentTransaction.getCurrentTotal()

		def getTransactionItems(self):
			return self.currentTransaction.getItems()
		
		def addItemToTransaction(self,item):
			self.currentTransaction.addItem(item)
			self.dbObj.decreaseQuantity(item.getID(), 1)
		def addToInventory(self, item):
			self.dbObj.addItem(item, 1)
		def removeFromInventory(self, item):
			self.dbObj.removeItem(item, 0)
		#def increaseQuantity(self):
		#	self.dbObj.increaseQuantity(1,1)
		#def decreaseQuantity(self):
		#	self.dbObj.decreaseQuantity(1,1)
		def getTransactionReceipt(self):
			return self.currentTransaction.getReceipt()	

		def completeStuff(self):
			self.dbObj.newTransaction(self.currentTransaction.getID(),self.__currEmployee.getId(), self.currentTransaction.getType(), self.currentTransaction.getCurrentTotal())

		def setPayment(self,payment):
			self.currentTransaction.setPayment(payment)
		def getCurrentTransaction(self):
			return self.currentTransaction
		
		def getTax(self):
			return self.__store.getTax()
		
				
		def storeInfo(self):
	
			inp0 = self.__getInput("Would you like to change the store info? (y/n): ", ["y","n"]).lower()
				
			if inp0 == "y":
				self.__initStore()
				
			#Print store info
			print("\nName: " + self.getStore().getName())
			print("Location: " + self.getStore().getLocation())
			print("Phone: " + self.getStore().getPhone())
					
			
		def __initStore(self):
			
			if not self.__store:
				
				print "A store already exists in the system.  This command will overwrite this data."
				
				inp0 = self.__getInput ("Ok to overwrite? <y or n> ", ["y", "n"])
				
				if (inp0 == "y"):
					print "\nThe store will be overwritten"
				elif (inp0 == "n"):
					print "\nThe store will not be overwritten"
					return False
				else:
					print "Error: input request failed. Retry command"
					return False
				
			print "Creating new store information"
			processDone = False
			
			while (not processDone):
				
				inputName     = raw_input("\nStore Name: ")
				inputLocation = raw_input  ("  Location: ")
				inputPhoneNo  = raw_input  (" Phone No.: ")
				
				tax = 0.06 # TODO: Fetch tax from database
				
				newStore = Store.Store (inputName, inputLocation, inputPhoneNo, tax)
				  
				inp1 = self.__getInput ("Ok to initialize store with this information? <y or n> ", ["y", "n"])
				  
				if (inp1 == "y"):
					print "\nThe store has been created"
					self.__store = newStore
					processDone = True
	
				elif (inp1 == "n"):
					print "\nThe store was not created."
					inp2 = self.__getInput ("Would you like to re-enter the information? <y or n> ", ["y", "n"])
					
					if (inp2 == "y"):
						pass
					
					elif (inp2 == "n"):
						processDone = True
						
					else:
						print "Error: input request failed. Retry command"
						return False
					
				else:
					print "Error: input request failed. Retry command"
					return False
			
			return True
		   
		def viewTransLog(self):
			
			print "viewTransLog"
			
			
			return True
			
		def viewValidCommands (self):
			
			print "\nValid Commands: "
			
			currEmp = self.__currEmployee
			
			if (currEmp == None):
				return False
				
			permissions = self.__currEmployee.getEmpType()
			
			if (permissions == "Manager" or permissions == "Admin"):
				print "    Login              - Log in as a different user" 
				print "    Log Out            - Log out current user"
				print "    Store Info         - Change Store Info"
				print "    Create Transaction - Start new transaction"
				# print "    Transaction Log    - View Transaction Log"
				print "    Help               - View Valid commands"
			else:
				print "    Login              - Log in as a different user" 
				print "    Log Out            - Log out current user"
				# print "    Store Info         - Change Store Info"
				print "    Create Transaction - Start new transaction"
				# print "    Transaction Log    - View Transaction Log"
				print "    Help              - View Valid commands"
				
			return True
		
		def __getInput (self, inputRequest, validInputs):
			
			validInput = False
			while (not validInput):
		
				userInput = raw_input(inputRequest)
				if userInput in validInputs:
					return userInput
					
				else:
					print ("Command unrecognized.")
			
if __name__ == '__main__':
	System = POS().instance
	System.main()
