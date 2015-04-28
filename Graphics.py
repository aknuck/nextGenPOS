from Tkinter import *

from LoginWindow import *
from MainMenu import *
from TransactionWindow import *
from ManageUsersWindow import *
from PaymentWindow import *
from ReturnWindow import *
from RentalPaymentWindow import *
from POS import *

class Graphics(Frame):
	def __init__(self,parent):
		Frame.__init__(self,parent)
		self.POS = POS().instance
		self.parent = parent

		# Thematic settings
		self.mainColor = "#99ccff"
		self.btnWidth1 = 20
		self.btnWidth2 = 10
		self.btnWidth3 = 40
		self.btnHeight1 = 1
		self.btnFontHeight1 = 9
		self.grey = "#818181"

		self.mainMenu = MainMenu(parent,self)
		self.loginWindow = LoginWindow(parent,self)
		self.transactionWindow = TransactionWindow(parent,self)
		self.manageUsers = ManageUsersWindow(parent,self)
		self.paymentWindow = PaymentWindow(parent,self)
		self.returnWindow = ReturnWindow(parent,self)
		self.rentalPaymentWindow = RentalPaymentWindow(parent,self)

		container = Frame(self)
		container.pack(side="top", fill="both", expand=True)

		self.mainMenu.place(x=0,y=0,relwidth=1,relheight=1)
		self.loginWindow.place(x=0,y=0,relwidth=1,relheight=1)
		self.transactionWindow.place(x=0,y=0,relwidth=1,relheight=1)
		self.manageUsers.place(x=0,y=0,relwidth=1,relheight=1)
		self.paymentWindow.place(x=0,y=0,relwidth=1,relheight=1)
		self.returnWindow.place(x=0,y=0,relwidth=1,relheight=1)
		self.rentalPaymentWindow.place(x=0,y=0,relwidth=1,relheight=1)

		self.loginWindow.lift()

		self.initUI()

	def initUI(self):

		self.parent.title("NextGen POS")

		#can do menubar stuff here if we want

	def onExit(self):
		self.quit()

	def liftLayer(self,layer):
		if layer == "main":
			self.mainMenu.lift()
		elif layer == "login":
			self.loginWindow.lift()
			#add something here to logout as the current user
		elif layer == "transaction":
			self.transactionWindow.lift()
		elif layer == "manageUsers":
			self.manageUsers.lift()
		elif layer == "payment":
			self.paymentWindow.lift()
		elif layer == "return":
			self.returnWindow.lift()
		elif layer == "Rpayment":
			self.rentalPaymentWindow.lift()

def main():

	root = Tk()
	root.geometry("680x555+300+20")
	app = Graphics(root)
	root.mainloop()

if __name__ == '__main__':
	main()


