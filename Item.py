class Item:


    def __init__(self, ID, name, price, saleValue):
        self.ID = ID
        self.name = name
        self.price = price
        self.saleValue = saleValue #Sale off. 0.0=normal price, 0.2=20% off
        self.itemID = 1
        self.notes = "" #additional information on the item, for example "Damaged" if the item being sold is damaged to explain a discount, or if food item being prepared, maybe "extra mayo" or something like that
    
    def getName(self):
        return self.name
    
    def getNotes(self):
        return self.notes
    
    def addNote(self,note):
        self.notes += note
    
    def clearNotes(self):
        self.notes = ""
    
    def setSaleValue(self,newSaleValue):
        self.saleValue=newSaleValue
    
    def getPrice(self):
        return self.price
    
    def getSalePrice(self):
        return self.price-(self.saleValue*self.price)
    
    def getSaleValue(self):
        return self.saleValue
    
    def getID(self):
        return self.ID
        
    def __repr__(self):
        return "ITEM: name=%s, price=%0.2f, saleValue=%f, itemID=%d, saleprice is calculated as->%0.2f" % (self.name, self.price, self.saleValue, self.itemID, self.getSalePrice())
        
if __name__ == '__main__':
    i=Item("Shoes",29.99,0.0)
    print(i)
    i.setSaleValue(0.1)
    print(i)