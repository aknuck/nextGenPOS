class Employee:
    
    def __init__(self, name, EID, empType):
        
        self.__name = name
        self.__EID = EID
        
        if ((empType == "Manager") or (empType == "Cashier")):
            self.__empType = empType
        else:
            print "Error: Employee Type Unrecognized"
            self.__empType = None
        
    def getName(self):
        return self.__name  
        
    def getId(self):
        return self.__EID
        
    def getEmpType(self):
        return self.__empType
        
#if __name__ == '__main__':
#    x = Employee("tyler", 5, "Cashier")
#    print x.getId()
#    print x.getEmpType()
        