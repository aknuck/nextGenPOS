from Tkinter import *


class Top(Toplevel):
    def __init__(self, parent, title = "How to Cheat and Hide Text"):
        Toplevel.__init__(self,parent)
        parent.geometry("250x360+100+150")
        if title:
            self.title(title)
        parent.withdraw()
        self.parent = parent
        self.result = None
        dialog = Frame(self)
        self.initial_focus = self.dialog(dialog)
        dialog.pack()


    def dialog(self,parent):

        self.parent = parent

        self.L1 = Entry(parent,text = "Hello, World!",state = DISABLED, disabledforeground = parent.cget('bg'))
        self.L1.pack()

        self.B1 = Button(parent, text = "Are You Alive???", command = self.hello)
        self.B1.pack()

        self.B2 = Button(parent, text = "DISSAPEAR???", command = self.goodbye)
        self.B2.pack()

    def hello(self):
        self.L1['state']="normal"

    def goodbye(self):
        self.L1['state']="disabled"


if __name__ == '__main__':
    root=Tk()   
    ds = Top(root)
    root.mainloop()