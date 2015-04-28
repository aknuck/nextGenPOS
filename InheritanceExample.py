class SuperC(object):
    def __init__(self,thing1,thing2):
        print thing1
        print thing2

class SubC(SuperC):
    def __init__(self,thing1,thing2,thing3):
        super(SubC,self).__init__(thing1,thing2)
        print thing1
        print thing2
        print thing3

c = SubC("f","g","h")
