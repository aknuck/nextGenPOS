class Credit(Payment):
    
    
    def __init__(self, pid, ptype, amount, cardNumber):
        Payment.__init__(self, ptype, amount, pid)
        self.cardNumber = cardNumber
        
    
    def getCardNumber(self):
        return self.cardNumber
