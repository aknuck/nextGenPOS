#main menu


from Tkinter import *
from ttk import *
from Tkinter import Button
#from PIL import ImageTk, Image

class MainMenu(Frame):

	def __init__(self,parent,graphics):
		Frame.__init__(self)
		self.parent = parent
		self.graphics = graphics
		self.color = '#D1D1D1'
		#self.color = '#FFFFFF'
		Style().configure('green/black.TButton', foreground='black', background='black')
		Style().configure("Red.TLabel", foreground="red")

		btnWidth = 60
		btnHeight = 2

		self.frame = Frame (self)		
		self.frame.grid (row=1, column=1)	

		# Add the location to the list button
		self.adminLoginButton = Button(self.frame, text="Admin", bg='light gray', width=10, command=lambda: self.adminLogin())
		self.adminLoginButton.grid(row=0, column=1, sticky='e')

		# create transaction 
		self.createTransBtn = Button(self.frame, text="Create Transaction", bg='light gray', width=btnWidth, height=btnHeight, command=lambda: self.createTransaction())
		self.createTransBtn.grid(row=1, column=0, columnspan=2, pady=10)

		# create transaction
		self.createRentalBtn = Button(self.frame, text="Create Rental Transaction", bg='light gray', width=btnWidth, height=btnHeight, command=lambda: self.manageUsers())		
		self.createRentalBtn.grid(row=2, column=0, columnspan=2, pady=10)

		# create transaction
		self.createReturnBtn = Button(self.frame, text="Return", bg='light gray', width=btnWidth, height=btnHeight, command=lambda: self.returnItem())		
		self.createReturnBtn.grid(row=3, column=0, columnspan=2, pady=10)

		# logout
		self.logoutBtn = Button(self.frame, text="Log Out", bg='light gray', width=btnWidth, height=btnHeight, command=lambda: self.logout())		
		self.logoutBtn.grid(row=4, column=0, columnspan=2, pady=10)

		self.outputLabel = Label(self.frame, text=" ")
		self.outputLabel.grid(row=5, column=0, columnspan=2, sticky='n')
		self.outputLabel.config(style="Red.TLabel")

		self.grid_columnconfigure (0, weight=1)
		self.grid_columnconfigure (2, weight=1)
		self.grid_rowconfigure 	  (0, weight=1)
		self.grid_rowconfigure    (2, weight=1)

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

	def logout(self):
		self.graphics.POS.logOut()
		self.graphics.liftLayer("login")

	def adminLogin(self,event=None):

		color = "#D1D1D1"

		# Create progress bar pop-up window
		self.adminWindow = Toplevel(self)
		#self.adminWindow.configure(bg=color)
		self.adminWindow.color = "D1D1D1"
		self.adminWindow.geometry("480x220+550+150")

		self.adminWindow.adminFrame = Frame (self.adminWindow)		
		self.adminWindow.adminFrame.grid (row=1, column=1)

		# Enter Username
		usernameLabel = Label(self.adminWindow.adminFrame, text="Username")#, bg=self.color,padx=5)
		#usernameLabel = Label(self, text="username", bg=self.color,padx=5)
		usernameLabel.grid(row=0,column=0,sticky='s')
		usernameField = Entry(self.adminWindow.adminFrame, width=40)#bd =0, width=40)
		#usernameField = Entry(self, width=40,bd =1)
		usernameField.grid(row=1,column=0,sticky='n')
		usernameField.bind("<Return>",(lambda event: self.login(usernameField,passwordField)))
		usernameField.focus()

		# Enter Password
		passwordLabel = Label(self.adminWindow.adminFrame, text="Password")#, bg=self.color,padx=5)
		#passwordLabel = Label(self, text="password", bg=self.color,padx=5)
		passwordLabel.grid(row=2,column=0,sticky='s')
		passwordField = Entry(self.adminWindow.adminFrame, show="*", width=40)#bd =0, width=40)
		#passwordField = Entry(self, show="*", width=40,bd =1)
		passwordField.grid(row=3,column=0,sticky='n')
		passwordField.bind("<Return>",(lambda event: self.login(usernameField,passwordField)))

		#output
		self.adminOutputLabel = Label(self.adminWindow.adminFrame,text="",style="Red.TLabel")#,bg=self.color,padx=5)
		self.adminOutputLabel.grid(row=4,column=0,sticky='s')

		# Attempt to login
		loginButton = Button(self.adminWindow.adminFrame, text="Login", width=15, bg="light gray", command=lambda: self.login(usernameField, passwordField))
		#loginButton = Button(self, text="Enter", width=15, command=lambda: self.login(usernameField, passwordField))
		loginButton.grid(row=5,column=0,pady=10)

		self.adminWindow.grid_columnconfigure (0, weight=1)
		self.adminWindow.grid_columnconfigure (2, weight=1)
		self.adminWindow.grid_rowconfigure 	  (0, weight=1)
		self.adminWindow.grid_rowconfigure    (2, weight=1)

	def login(self, username, password, event=None):
		if self.graphics.POS.login(username.get(),password.get()) == True:
			print "logged in!"
			self.adminWindow.destroy()
		else:
			if self.graphics.POS.login(username.get(),password.get()) != None:
				self.adminOutputLabel.config(text="Incorrect Login")

