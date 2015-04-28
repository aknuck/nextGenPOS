#main menu

from Tkinter import *
import tkFont
from ttk import *
from Tkinter import Frame
from Tkinter import Button
from Tkinter import Label
from Payment import *
class RentalPaymentWindow(Frame):

	def __init__(self,parent,graphics):
		Frame.__init__(self)
		self.parent = parent
		self.graphics = graphics
		self.config(bg=self.graphics.mainColor)
		self.selected = ""
		self.font = tkFont.Font(family="Courier", size=12)
		#self.color = '#FFFFFF'

		#Title Label
		self.outputLabel = Label(self, text="", bg=self.graphics.mainColor)
		self.outputLabel.grid(row=0,column=0,sticky='ns',padx=6,pady=5)

		#Title Label
		self.creditCardNumberLabel = Label(self, text="Credit Card Number", bg=self.graphics.mainColor)
		self.creditCardNumberLabel.grid(row=2,column=0,sticky='ns',padx=6,pady=5)

		#Manual Enter Output
		self.creditCardNumber = Entry(self,width=20)
		self.creditCardNumber.grid(row=2,column=1,sticky='ns',padx=6)

		#Title Label
		self.nameLabel = Label(self, text="Enter Name", bg=self.graphics.mainColor)
		self.nameLabel.grid(row=3,column=0,sticky='ns',padx=6,pady=5)

		#Manual Enter Output
		self.name = Entry(self,width=20)
		self.name.grid(row=3,column=1,sticky='ns',padx=6)

		self.addressLabel = Label(self, text="Enter Address", bg=self.graphics.mainColor)
		self.addressLabel.grid(row=4,column=0,sticky='ns',padx=6,pady=5)

		#Manual Enter Output
		self.address = Entry(self,width=20)
		self.address.grid(row=4,column=1,sticky='ns',padx=6)		

		self.submitButton = Button(self, text="Submit", width=15, command=lambda: self.submit())
		self.submitButton.grid(row=5,column=0)

		self.cancelButton = Button(self, text="Cancel", width=15, command=lambda: self.cancel())
		self.cancelButton.grid(row=5,column=1)
	

#		Style().configure('green/black.TButton', foreground='black', background='black')
#		
#		self.L1 = Entry(self,state = DISABLED, disabledforeground = parent.cget('bg'))
#		self.L1.pack()#

#		self.B1 = Button(self, text = "Are You Alive???", command = self.hello)
#		self.B1.pack()#

#		self.B2 = Button(self, text = "DISSAPEAR???", command = self.goodbye)
#		self.B2.pack()

	def submit(self):
		self.creditCardNumber.config(text="f")
		self.name.config(text="f")
		self.address.config(text="f")
		number = self.creditCardNumber.get()
		name = self.name.get()
		payment = Payment(self.selected,number)


		self.graphics.POS.getCurrentTransaction().setPayment(payment)
		self.complete()

	def cancel(self):
		self.graphics.liftLayer("transaction")

	def credit(self):
		print "credit"

	def complete(self):
		self.creditCardNumber.config(text="")
		self.name.config(text="")
		self.outputLabel.config(text=" ")
		
		print "completing transaction"

		#color = "#D1D1D1"
		color = "#e8e8e8"
		width=35

		# Create progress bar pop-up window
		receiptWindow = Toplevel(self)
		receiptWindow.configure(bg=color)
		#Should be 7.35 x width
		receiptWindow.geometry("500"+"x"+str(int(13.05*(len(self.graphics.POS.getTransactionReceipt().split('\n'))+5)+100))+"+150+50")
		self.graphics.POS.completeStuff()
		# Text Field Object, used in the submission function
		receiptText = Label(receiptWindow, text=self.graphics.POS.getTransactionReceipt(), bg='white',font=self.font)#self.graphics.POS.getTransactionReceipt()
		receiptText.pack(side="top")
		#self.itemIDField.delete(0, 'end')
		self.graphics.liftLayer("main")

