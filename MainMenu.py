#main menu

from Tkinter import *
#from PIL import ImageTk, Image
from ttk import *

class MainMenu(Frame):

	def __init__(self,parent,graphics):
		Frame.__init__(self)
		self.parent = parent
		self.graphics = graphics
		self.color = '#D1D1D1'
		#self.color = '#FFFFFF'
		Style().configure('green/black.TButton', foreground='black', background='black')
		Style().configure("Red.TLabel", foreground="red")
		
		#buffers
		#buff = Label(self,text="Logged in as "+self.user)#,bg=self.color,padx=5)
		#buff.grid(row=0,column=0,padx=10,pady=10,columnspan=5,sticky=('n', 's', 'e', 'w'))#,sticky='CENTER')

		#buff2 = Label(self,text="               ")#,bg=self.color,padx=5)
		#buff2.grid(row=0,column=0,rowspan=3,sticky='n')

		# Add the location to the list button
		self.adminLoginButton = Button(self, text="*", width=0,style='green/black.TButton',command=lambda: self.adminLogin())
		self.adminLoginButton.grid(row=0,column=2,sticky='e')

		# create transaction
		loginButton = Button(self, text="Create Transaction", width=15, style='green/black.TButton', command=lambda: self.createTransaction())
		#loginButton = Button(self, text="Enter", width=15, command=lambda: self.login(usernameField, passwordField))
		loginButton.grid(row=1,column=0,pady=10)

		# create transaction
		loginButton = Button(self, text="Create Rental Transaction", width=15, style='green/black.TButton', command=lambda: self.manageUsers())
		#loginButton = Button(self, text="Enter", width=15, command=lambda: self.login(usernameField, passwordField))
		loginButton.grid(row=2,column=0,pady=10)

		# create transaction
		loginButton = Button(self, text="Return", width=15, style='green/black.TButton', command=lambda: self.returnItem())
		#loginButton = Button(self, text="Enter", width=15, command=lambda: self.login(usernameField, passwordField))
		loginButton.grid(row=3,column=0,pady=10)

		self.outputLabel = Label(self,text=" ")
		self.outputLabel.grid(row=4,column=0,sticky='n')
		self.outputLabel.config(style="Red.TLabel")

	def createTransaction(self):
		self.outputLabel.config(text="")
		print "creating transaction"
		#lift transacion screen
		self.graphics.POS.createTransaction()
		self.graphics.liftLayer("transaction")

	def manageUsers(self):
		self.outputLabel.config(text="")
		print "managing users"
		self.graphics.POS.createRentalTransaction()
		self.graphics.liftLayer("manageUsers")

	def returnItem(self):
		if self.graphics.POS.getCurrEmployee().getEmpType() == "Manager":
			self.graphics.liftLayer("return")
		else:
			self.outputLabel.config(text="requires manager")

	def adminLogin(self,event=None):
		try:
			self.graphics.POS.logOut()
		except:
			print "already logged out probs"
		print "admin login"

		color = "#e8e8e8"

		# Create progress bar pop-up window
		self.adminWindow = Toplevel(self)
		self.adminWindow.configure(bg=color)
		self.adminWindow.geometry("480x220+550+150")

		#buffers
		buff = Label(self.adminWindow,text="               ")#,bg=self.color,padx=5)
		buff.grid(row=1,column=0,sticky='w')	

		buff2 = Label(self.adminWindow,text="               ")#,bg=self.color,padx=5)
		buff2.grid(row=2,column=1,sticky='n')

		# Enter Username
		usernameLabel = Label(self.adminWindow, text="username")#, bg=self.color,padx=5)
		#usernameLabel = Label(self, text="username", bg=self.color,padx=5)
		usernameLabel.grid(row=3,column=1,sticky='s')
		usernameField = Entry(self.adminWindow, width=40)#bd =0, width=40)
		#usernameField = Entry(self, width=40,bd =1)
		usernameField.grid(row=4,column=1,sticky='n')
		usernameField.bind("<Return>",(lambda event: self.login(usernameField,passwordField)))

		# Enter Password
		passwordLabel = Label(self.adminWindow, text="password")#, bg=self.color,padx=5)
		#passwordLabel = Label(self, text="password", bg=self.color,padx=5)
		passwordLabel.grid(row=5,column=1,sticky='s')
		passwordField = Entry(self.adminWindow, show="*", width=40)#bd =0, width=40)
		#passwordField = Entry(self, show="*", width=40,bd =1)
		passwordField.grid(row=6,column=1,sticky='n')
		passwordField.bind("<Return>",(lambda event: self.login(usernameField,passwordField)))

		#output
		self.adminOutputLabel = Label(self.adminWindow,text="",style="Red.TLabel")#,bg=self.color,padx=5)
		self.adminOutputLabel.grid(row=7,column=1,sticky='s')

		# Attempt to login
		loginButton = Button(self.adminWindow, text="Enter", width=15, style='green/black.TButton', command=lambda: self.login(usernameField, passwordField))
		#loginButton = Button(self, text="Enter", width=15, command=lambda: self.login(usernameField, passwordField))
		loginButton.grid(row=8,column=1,pady=10)

	def login(self,username,password,event=None):
		if self.graphics.POS.login(username.get(),password.get()) == True:
			print "logged in!"
			self.adminWindow.destroy()
		else:
			if self.graphics.POS.login(username.get(),password.get()) != None:
				self.adminOutputLabel.config(text="Incorrect Login")

