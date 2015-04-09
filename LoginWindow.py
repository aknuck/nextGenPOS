#login screen

from Tkinter import *
#from PIL import ImageTk, Image
from ttk import *

class LoginWindow(Frame):

	def __init__(self,parent,graphics):
		Frame.__init__(self)
		self.parent = parent
		self.graphics = graphics
		#self.color = "#26D4B1"
		self.color = '#D1D1D1'
		#self.configure(bg=self.color)
		Style().configure('green/black.TButton', foreground='black', background='black')
		Style().configure("Red.TLabel", foreground="red")

		#storeLogo = "resources/storeLogo.png"
		#i = Image.open(storeLogo)
		#img = ImageTk.PhotoImage(file=storeLogo)
		#logoPanel = Label(self,image=img,bd=0)
		#logoPanel.image = img
		#logoPanel.grid(row=1,column=1)

		#buffers
		buff = Label(self,text="               ")#,bg=self.color,padx=5)
		buff.grid(row=1,column=0,sticky='w')	

		buff2 = Label(self,text="               ")#,bg=self.color,padx=5)
		buff2.grid(row=2,column=1,sticky='n')

		# Enter Username
		usernameLabel = Label(self, text="username")#, bg=self.color,padx=5)
		#usernameLabel = Label(self, text="username", bg=self.color,padx=5)
		usernameLabel.grid(row=3,column=1,sticky='s')
		usernameField = Entry(self, width=40)#bd =0, width=40)
		#usernameField = Entry(self, width=40,bd =1)
		usernameField.grid(row=4,column=1,sticky='n')
		usernameField.bind("<Return>",(lambda event: self.login(usernameField,passwordField)))

		# Enter Password
		passwordLabel = Label(self, text="password")#, bg=self.color,padx=5)
		#passwordLabel = Label(self, text="password", bg=self.color,padx=5)
		passwordLabel.grid(row=5,column=1,sticky='s')
		passwordField = Entry(self, show="*", width=40)#bd =0, width=40)
		#passwordField = Entry(self, show="*", width=40,bd =1)
		passwordField.grid(row=6,column=1,sticky='n')
		passwordField.bind("<Return>",(lambda event: self.login(usernameField,passwordField)))

		#output
		self.outputLabel = Label(self,text="",style="Red.TLabel")#,bg=self.color,padx=5)
		self.outputLabel.grid(row=7,column=1,sticky='s')

		# Attempt to login
		loginButton = Button(self, text="Enter", width=15, style='green/black.TButton', command=lambda: self.login(usernameField, passwordField))
		#loginButton = Button(self, text="Enter", width=15, command=lambda: self.login(usernameField, passwordField))
		loginButton.grid(row=8,column=1,pady=10)

	def login(self,username,password,event=None):
		if self.graphics.POS.login(username.get(),password.get()) == True:
			print "logged in!"
			self.graphics.liftLayer("main")
		else:
			if self.graphics.POS.login(username.get(),password.get()) != None:
				self.outputLabel.config(text="Incorrect Login")
