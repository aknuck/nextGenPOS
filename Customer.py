class Customer:
        
    def __init__(self, name, budget):
        self.name = name
        self.budget = budget
        self.C_ID = 1
        self.cart=[]
        
    
    def getCart(self):
        return self.cart
        
    def addToCart(self,item):
        self.cart.append(item)
        
    def __repr__(self):
        return "CUSTOMER: name=%s, budget=%0.2f, C_ID=%d," % (self.name, self.budget, self.C_ID)

        
#if __name__ == '__main__':
#    c=Customer("Me",123456)
#    c.addToCart("Item1")
#    c.addToCart("Item2")
#    print(c.getCart())
#    print(c)