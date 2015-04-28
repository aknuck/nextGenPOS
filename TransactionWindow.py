#main menu

from Tkinter import *
import tkFont
#from PIL import ImageTk, Image
from ttk import *
from Tkinter import Frame
from Tkinter import Button
from Tkinter import Label
import thread
import Item
import POS

class TransactionWindow(Frame):

	def __init__(self,parent,graphics):
		Frame.__init__(self)
		self.parent = parent
		self.graphics = graphics
		self.items = []
		self.config(bg=self.graphics.mainColor)
		self.font = tkFont.Font(family="Courier", size=12)

		#self.font = ('system', 10)
		Style().configure('green/black.TButton', foreground='black', background='black')
		Style().configure('white.TLabel', foreground='black', background='white')
		Style().configure("Red.TLabel", foreground="red")
		Style().configure("MyStyle.Vertical.TSeparator", background="black")

		self.frame = Frame (self, bg=self.graphics.mainColor)
		self.frame.grid(row=1, column=1)

		# Add the location to the list button
		self.adminLoginButton = Button(self.frame, text="Admin", bg=self.graphics.grey, fg="white", width=self.graphics.btnWidth2, command=lambda: self.adminLogin())
		self.adminLoginButton.grid(row=0,column=3, sticky='e')

		# Enter item ID
		itemIDLabel = Label(self.frame, text="Enter Item ID", bg=self.graphics.mainColor)
		itemIDLabel.grid(row=1,column=3, pady=10, sticky='s')
		self.itemIDField = Entry(self.frame, width=20)
		self.itemIDField.grid(row=2,column=3,sticky='n')
		self.itemIDField.bind("<Return>",(lambda event: self.add(self.itemIDField.get())))

		self.outputLabel = Label(self.frame,text=" ", bg=self.graphics.mainColor)
		self.outputLabel.grid(row=3,column=3,sticky='n')
		self.outputLabel.config(fg="red")

		# Add the location to the list button
		setLocB = Button(self.frame, text="Add", width=self.graphics.btnWidth1, height=self.graphics.btnHeight1, font=("Helvetica", self.graphics.btnFontHeight1), command=lambda: self.add(self.itemIDField.get()))
		setLocB.grid(row=4,column=3)

		# Add the location to the list button
		setLocB = Button(self.frame, text="Manual", width=self.graphics.btnWidth1, height=self.graphics.btnHeight1, font=("Helvetica", self.graphics.btnFontHeight1), command=lambda: self.manual(self.itemIDField))
		setLocB.grid(row=5,column=3)

		# Add the location to the list button
		setLocB = Button(self.frame, text="Complete", width=self.graphics.btnWidth1, height=self.graphics.btnHeight1, font=("Helvetica", self.graphics.btnFontHeight1), command=lambda: self.complete(self.itemIDField))
		setLocB.grid(row=6,column=3)

		# Add the location to the list button
		setLocB = Button(self.frame, text="Cancel", width=self.graphics.btnWidth1, height=self.graphics.btnHeight1, font=("Helvetica", self.graphics.btnFontHeight1), command=lambda: self.cancel(self.itemIDField))
		setLocB.grid(row=7,column=3)

		# Add the location to the list button
		setLocB = Button(self.frame, text="Save", width=self.graphics.btnWidth1, height=self.graphics.btnHeight1, font=("Helvetica", self.graphics.btnFontHeight1), command=lambda: self.save())
		setLocB.grid(row=12,column=3)

		# Add the location to the list button
		setLocB = Button(self.frame, text="Load", width=self.graphics.btnWidth1, height=self.graphics.btnHeight1, font=("Helvetica", self.graphics.btnFontHeight1), command=lambda: self.load())
		setLocB.grid(row=13,column=3)

		l = Label(self.frame,text="             ", bg=self.graphics.mainColor)
		l.grid(row=0,column=2,rowspan=8)

		sep = Separator(self.frame, orient=VERTICAL, style="MyStyle.Vertical.TSeparator")
		sep.grid(row=0, column=1, rowspan=20, sticky="ns",padx=3)

		# Make and fill listbox
		self.itemsListBox = Listbox(self.frame, height=24,font=self.font)
		self.itemsListBox.config(width=25)
		self.itemsListBox.grid(row=0,column=0,rowspan=20,pady=6,padx=8)
		self.itemsListBox.bind("<BackSpace>",(lambda event: self.remove(self.itemsListBox.curselection())))

		
		# Change location to the one selected
		removeLocB = Button(self.frame, text="Remove Item", width=self.graphics.btnWidth1, height=self.graphics.btnHeight1, font=("Helvetica", self.graphics.btnFontHeight1), command=lambda: self.remove(self.itemsListBox.curselection()))
		removeLocB.grid(row=18,column=3,pady=5,padx=5)
	
		self.grid_columnconfigure (0, weight=1)
		self.grid_columnconfigure (2, weight=1)
		self.grid_rowconfigure 	  (0, weight=1)
		self.grid_rowconfigure    (2, weight=1)

	def add(self,itemID):
		if self.graphics.POS.getCurrEmployee() != None:
			self.outputLabel.config(text=" ")
			if itemID != "":
				item = self.graphics.POS.queryDBForItem(itemID)
				self.items.append(itemID)
				if item != None:
					if self.graphics.POS.addItemToTransaction(item) == False:
						self.outputLabel.config(text="Must Be Logged In")
					self.itemsListBox.insert(END,self.textFormatter(item,24))
				else:
					self.outputLabel.config(text="Item Doesn't Exist")
			else:
				self.outputLabel.config(text="Nothing entered")
			self.itemIDField.delete(0, 'end')
		else:
			self.outputLabel.config(text="Must Be Logged In")

	def remove(self,selection):
		self.outputLabel.config(text=" ")
		try:
			print "removing "+str(int(selection[0]))
			self.itemsListBox.delete(int(selection[0]))
			self.graphics.POS.getCurrentTransaction().removeItem(self.graphics.POS.getCurrentTransaction().getItems()[int(selection[0])])
		except:
			self.outputLabel.config(text="Nothing Selected")

	def manual(self,itemID):
		if self.graphics.POS.getCurrEmployee().getEmpType() == "Manager":
			self.outputLabel.config(text=" ")
			print "adding manually"

			color = self.graphics.mainColor 

			# Create progress bar pop-up window
			self.adminWindow = Toplevel(self)
			self.adminWindow.configure(bg=color)
			self.adminWindow.geometry("270x165+550+150")

			#Title Label
			titleLabel = Label(self.adminWindow, text="Enter Item Information", bg=color)
			titleLabel.grid(row=0,column=0,columnspan=2,sticky='ns',padx=6,pady=5)

			#Manual Enter Output
			self.manualEntryOutput = Label(self.adminWindow, text="",fg='red', bg=color)
			self.manualEntryOutput.grid(row=1,column=0,columnspan=2,sticky='ns',padx=6)

			#Item Name Label
			itemNameLabel = Label(self.adminWindow, text="Item Name", bg=color)
			itemNameLabel.grid(row=2,column=0,sticky='w',padx=6)

			#Item Name Field
			itemNameField = Entry(self.adminWindow, width=15)
			itemNameField.grid(row=2,column=1,sticky='e',padx=6)
			itemNameField.bind("<Return>",(lambda event: self.manualAdd(itemNameField,itemPriceField,itemSaleField)))

			#Item Price Label
			itemPriceLabel = Label(self.adminWindow, text="Item Price", bg=color)
			itemPriceLabel.grid(row=3,column=0,sticky='w',padx=6)

			#Item Price Field
			itemPriceField = Entry(self.adminWindow, width=15)
			itemPriceField.grid(row=3,column=1,sticky='e',padx=6)
			itemPriceField.bind("<Return>",(lambda event: self.manualAdd(itemNameField,itemPriceField,itemSaleField)))

			#Item Sale Label
			itemSaleLabel = Label(self.adminWindow, text="Percent Sale", bg=color)
			itemSaleLabel.grid(row=4,column=0,sticky='w',padx=6)

			#Item Sale Field
			itemSaleField = Entry(self.adminWindow, width=15)
			itemSaleField.grid(row=4,column=1,sticky='e',padx=6)
			itemSaleField.bind("<Return>",(lambda event: self.manualAdd(itemNameField,itemPriceField,itemSaleField)))

			#Add the Item
			itemAddButton = Button(self.adminWindow, text="Add Item", width=10, command=lambda: self.manualAdd(itemNameField,itemPriceField,itemSaleField))
			itemAddButton.grid(row=5,column=0,sticky='e',padx=5)

			#Cancel Adding the Item
			cancelButton = Button(self.adminWindow, text="Cancel", width=10, command=lambda: self.adminWindow.destroy())
			cancelButton.grid(row=5,column=1,pady=5,padx=5)
		else:
			self.outputLabel.config(text="Requires Manager")

	def manualAdd(self,name,price,sale):
		if name.get() == "" or price.get() == "":
			self.manualEntryOutput.config(text="incomplete information")
		elif isinstance(price.get(), ( int, long )):
			self.manualEntryOutput.config(text="Price Must be a Number")
		else:
			if sale.get() == "":
				item = Item.Item(-1,name.get(),float(price.get()),0)
			else:
				item = Item.Item(-1,name.get(),float(price.get()),float(sale.get())/100.00)
			self.graphics.POS.addItemToTransaction(item)
			self.itemsListBox.insert(END,self.textFormatter(item,24))
			self.adminWindow.destroy()


	def complete(self,itemID):
		self.itemIDField.delete(0, 'end')
		self.itemsListBox.delete(0, END)
		self.graphics.liftLayer("payment")

	def cancel(self,itemID):
		self.items = []
		self.outputLabel.config(text=" ")
		print "cancelling transaction"
		self.itemIDField.delete(0, 'end')
		self.itemsListBox.delete(0, END)
		self.graphics.liftLayer("main")

	def textFormatter(self,item,width):
		name = item.getName()
		price = item.getSalePrice()
		disc = item.getSaleValue()
		line = ""
		if disc != 0:
			length = len(name)+len("("+str(int(disc*100))+"% off)")+len("$"+str("{0:.2f}".format(price)))
		else:
			length = len(name)+len("$"+str("{0:.2f}".format(price)))

		if length+2 <= width:
			overage = width - length
			if overage % 2 != 0:
				overage -= 1
				spacing = int(overage/2)
				sp1 = spacing
				sp2 = spacing + 1
			else:
				spacing = int(overage/2)
				sp1 = spacing
				sp2 = spacing
			if disc != 0:
				line = name+(sp1*" ")+"("+str(int(disc*100))+"% off)"+(sp2*" ")+"$"+str("{0:.2f}".format(price))
			else:
				line = name+(sp1*" ")+(sp2*" ")+"$"+str("{0:.2f}".format(price))
		else:
			overage = length+2 - width
			name = name[:len(name)-overage]
			if disc != 0:
				line = name+" "+"("+str(int(disc*100))+"% off)"+" "+"$"+str("{0:.2f}".format(price))
			else:
				line = name+" "+" "+"$"+str("{0:.2f}".format(price))

		return line

	def adminLogin(self,event=None):

		color = "#D1D1D1"

		# Create progress bar pop-up window
		self.adminWindow = Toplevel(self, bg=self.graphics.mainColor)
		#self.adminWindow.configure(bg=color)
		self.adminWindow.geometry("480x220+550+150")

		self.adminWindow.adminFrame = Frame (self.adminWindow, bg=self.graphics.mainColor)		
		self.adminWindow.adminFrame.grid (row=1, column=1)

		# Enter Username
		usernameLabel = Label(self.adminWindow.adminFrame, text="Username", bg=self.graphics.mainColor)#, bg=self.color,padx=5)
		#usernameLabel = Label(self, text="username", bg=self.color,padx=5)
		usernameLabel.grid(row=0,column=0,sticky='s')
		usernameField = Entry(self.adminWindow.adminFrame, width=40)#bd =0, width=40)
		#usernameField = Entry(self, width=40,bd =1)
		usernameField.grid(row=1,column=0,sticky='n')
		usernameField.bind("<Return>",(lambda event: self.login(usernameField,passwordField)))
		usernameField.focus()

		# Enter Password
		passwordLabel = Label(self.adminWindow.adminFrame, text="Password", bg=self.graphics.mainColor)#, bg=self.color,padx=5)
		#passwordLabel = Label(self, text="password", bg=self.color,padx=5)
		passwordLabel.grid(row=2,column=0,sticky='s')
		passwordField = Entry(self.adminWindow.adminFrame, show="*", width=40)#bd =0, width=40)
		#passwordField = Entry(self, show="*", width=40,bd =1)
		passwordField.grid(row=3,column=0,sticky='n')
		passwordField.bind("<Return>",(lambda event: self.login(usernameField,passwordField)))

		#output
		self.adminOutputLabel = Label(self.adminWindow.adminFrame,text="",fg="red", bg=self.graphics.mainColor)#,bg=self.color,padx=5)
		self.adminOutputLabel.grid(row=4,column=0,sticky='s')

		# Attempt to login
		loginButton = Button(self.adminWindow.adminFrame, text="Login", width=15, command=lambda: self.login(usernameField, passwordField))
		#loginButton = Button(self, text="Enter", width=15, command=lambda: self.login(usernameField, passwordField))
		loginButton.grid(row=5,column=0,pady=10)

		self.adminWindow.grid_columnconfigure (0, weight=1)
		self.adminWindow.grid_columnconfigure (2, weight=1)
		self.adminWindow.grid_rowconfigure 	  (0, weight=1)
		self.adminWindow.grid_rowconfigure    (2, weight=1)


	def login(self,username,password,event=None):
		if self.graphics.POS.login(username.get(),password.get()) == True:
			print "logged in!"
			self.adminWindow.destroy()
		else:
			if self.graphics.POS.login(username.get(),password.get()) != None:
				self.adminOutputLabel.config(text="Incorrect Login")

	def save(self):
		print "saving"
		f = open("saved_transaction.txt",'w')
		text = ""
		for item in self.items:
			text+=item+":"
		text = text[:len(text)-1]
		f.write(text)
		f.close()

	def load(self):
		print "loading"
		for item in self.items:
			self.remove([0])
		f = open("saved_transaction.txt",'r')
		text = f.read()
		items = text.split(":")
		for item in items:
			self.items.append(item)
			self.add(item)


