#main menu

from Tkinter import *
import tkFont
#from PIL import ImageTk, Image
from ttk import *
from Payment import *
class PaymentWindow(Frame):

	def __init__(self,parent,graphics):
		Frame.__init__(self)
		self.parent = parent
		self.graphics = graphics
		self.color = '#D1D1D1'
		self.selected = ""
		self.font = tkFont.Font(family="Courier", size=12)
		#self.color = '#FFFFFF'

		#Title Label
		self.outputLabel = Label(self, text="")
		self.outputLabel.grid(row=0,column=0,sticky='ns',padx=6,pady=5)

		v = IntVar()

		self.b1 = Radiobutton(self, text="Cash", variable=v, value=1,command=lambda: self.cash())
		self.b1.grid(row=1,column=0)
		self.b2 = Radiobutton(self, text="Credit", variable=v, value=2,command=lambda: self.credit())
		self.b2.grid(row=1,column=1)

		#Title Label
		self.creditCardNumberLabel = Label(self, text="Credit Card Number")
		self.creditCardNumberLabel.grid(row=2,column=0,sticky='ns',padx=6,pady=5)

		#Manual Enter Output
		self.creditCardNumber = Entry(self,width=20)
		self.creditCardNumber.grid(row=2,column=1,sticky='ns',padx=6)

		#Title Label
		self.nameLabel = Label(self, text="Enter Name")
		self.nameLabel.grid(row=3,column=0,sticky='ns',padx=6,pady=5)

		#Manual Enter Output
		self.name = Entry(self,width=20)
		self.name.grid(row=3,column=1,sticky='ns',padx=6)

		self.submitButton = Button(self, text="Submit", width=15, command=lambda: self.submit())
		self.submitButton.grid(row=4,column=0)

		self.cancelButton = Button(self, text="Cance", width=15, command=lambda: self.cancel())
		self.cancelButton.grid(row=4,column=1)
	

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
		if self.selected == "credit":
			number = self.creditCardNumber.get()
			name = self.name.get()
			payment = Payment(self.selected,number)
		else:
			payment = Payment(self.selected)

		self.graphics.POS.getCurrentTransaction().setPayment(payment)
		self.complete()


	def credit(self):
		print "credit"
		self.selected = "credit"
		self.creditCardNumberLabel.config(state="active")
		self.creditCardNumber.config(state="active")
		self.nameLabel.config(state="active")
		self.name.config(state="active")

	def cash(self):
		print "cash"
		self.selected = "cash"
		self.creditCardNumberLabel.config(state="disabled")
		self.creditCardNumber.config(state="disabled")
		self.nameLabel.config(state="disabled")
		self.name.config(state="disabled")	

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
		receiptWindow.geometry(str(int(8.35*width))+"x"+str(int(13.05*(len(self.graphics.POS.getTransactionReceipt().split('\n'))+5)))+"+150+50")

		# Text Field Object, used in the submission function
		receiptText = Label(receiptWindow, text=self.graphics.POS.getTransactionReceipt(), style='white.TLabel',font=self.font)#self.graphics.POS.getTransactionReceipt()
		self.graphics.POS.completeStuff()
		receiptText.pack(side="top")
		#self.itemIDField.delete(0, 'end')
		self.graphics.liftLayer("main")

