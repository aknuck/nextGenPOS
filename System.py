from Tkinter import *

from LoginWindow import *

class Graphics(Frame):
	def __init__(self,parent):
		Frame.__init__(self,parent)

		self.parent = parent

		self.loginWindow = LoginWindow(parent)

		container = Frame(self)
		container.pack(side="top", fill="both", expand=True)

		self.loginWindow.place(x=0,y=0,relwidth=1,relheight=1)

		self.loginWindow.lift()

		self.initUI()

	def initUI(self):

		self.parent.title("NextGen POS")

		#can do menubar stuff here if we want

	def onExit(self):
		self.quit()

def main():

	root = Tk()
	#mycolor = '#26D4B1'
	mycolor = '#D1D1D1'
	root.configure(bg=mycolor)
	root.geometry("480x360+300+300")
	app = Graphics(root)
	root.mainloop()

if __name__ == '__main__':
	main()


