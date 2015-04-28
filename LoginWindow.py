#login screen

from Tkinter import *
#from PIL import ImageTk, Image
from ttk import *
from Tkinter import Frame
from Tkinter import Label
from Tkinter import Button

class LoginWindow(Frame):

	def __init__(self,parent,graphics):
		Frame.__init__(self)
		self.grid()
		self.parent = parent
		self.graphics = graphics		
		self.configure(bg=self.graphics.mainColor)
		Style().configure('green/black.TButton', background='black', foreground='black')
		Style().configure("Red.TLabel", foreground="red")
		
		
		self.grid_columnconfigure (1, weight=1)
		self.grid_rowconfigure 	  (0, weight=1)
		self.grid_rowconfigure    (9, weight=1)

		# Enter Username
		self.usernameLabel = Label(self, text="Username", bg = self.graphics.mainColor)#, bg=self.color,padx=5)
		#usernameLabel = Label(self, text="username", bg=self.color,padx=5)
		self.usernameLabel.grid(row=3,column=1,sticky='s')
		self.usernameField = Entry(self, width=40)#bd =0, width=40)
		#usernameField = Entry(self, width=40,bd =1)
		self.usernameField.insert(END, '')
		self.usernameField.grid(row=4,column=1,sticky='n')
		self.usernameField.bind("<Return>",(lambda event: self.login(self.usernameField, self.passwordField)))
		self.usernameField.focus()

		# Enter Password
		self.passwordLabel = Label(self, text="Password", bg = self.graphics.mainColor)#, bg=self.color,padx=5)
		#passwordLabel = Label(self, text="password", bg=self.color,padx=5)
		self.passwordLabel.grid(row=5,column=1,sticky='s')
		self.passwordField = Entry(self, show="*", width=40)#bd =0, width=40)
		#passwordField = Entry(self, show="*", width=40,bd =1)
		self.passwordField.grid(row=6,column=1,sticky='n')
		self.passwordField.bind("<Return>",(lambda event: self.login(self.usernameField,self.passwordField)))

		#output
		self.outputLabel = Label(self, text="", fg='red', bg = self.graphics.mainColor)#,bg=self.color,padx=5)
		self.outputLabel.grid(row=7,column=1, pady=5, sticky='s')

		# Attempt to login
		self.loginButton = Button(self, text="Enter", width=15, command=lambda: self.login(self.usernameField, self.passwordField))
		#loginButton = Button(self, text="Enter", width=15, command=lambda: self.login(usernameField, passwordField))
		self.loginButton.grid(row=8,column=1,pady=5)

	def login(self,username,password,event=None):		

		if self.graphics.POS.login(username.get(),password.get()) == True:
			print "logged in!"
			self.graphics.liftLayer("main")
			self.usernameField.delete(0, 'end')
			self.passwordField.delete(0, 'end')
			self.outputLabel.config(text="")
		else:
			if self.graphics.POS.login(username.get(),password.get()) != None:
				self.outputLabel.config(text="Incorrect Login")
