import random

class Store:

    def __init__(self,name,location,phone,tax):
        self.store_ID=1
        self.name = name
        self.location = location
        self.phoneNumber = phone
        self.tax = tax
    
    def getTax(self):
        return self.tax
    
    def getName(self):
        return self.name
    
    def getLocation(self):
        return self.location
    
    def getPhone(self):
        return self.phoneNumber
        
    def getID(self):
        return self.store_ID
        
    def __repr__(self):
        return "ITEM: name=%s, location=%s, phoneNumber=%s, tax=%0.2f" % (self.name, self.location, self.phoneNumber, self.tax)
  
        
#if __name__ == '__main__':
#    i=Store(['Item1','Item2'],['Boss', 'Cashier'],"Bob Sagat's Junk","Bob Sagat's Garage",""+str(random.randint(100,999))+"-"+str(random.randint(100,999))+"-"+str(random.randint(100,999)))
#    print(i)