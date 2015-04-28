import Payment

class Debit(Payment):
    
    
    def __init__(self, payment_id, amount, cardNumber, pin):
        super(Debit, self).__init__("debit",amount, payment_id)
        self.cardNumber = cardNumber
        self.pin = pin
        
    
    def getCardNumber(self):
        return self.cardNumber
        
    def getPin(self):
        return self.pin
        
#if __name__ == '__main__':
#    d = Debit(1, 32, 213141, 2312)
#    print d.getCardNumber()