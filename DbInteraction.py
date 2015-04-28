import Item
import Store
import sqlite3 as sql
import time

class DbInteraction:
    
    def __init__(self):
        self.connection = sql.connect('DB.db')

    def addItem(self, item, store):
        with self.connection:
            cursor = self.connection.cursor()    
            cursor.execute('SELECT MAX(I_ID) from Item')
            i = cursor.fetchone()
            print 
            j = int(i[0])+ 1
            cursor.execute('INSERT into Item (I_ID, Name, Price, SaleValue, Store_ID) values (\'' + str(j) + '\',\'' + item.getName() + '\',\'' + str(item.getPrice()) + '\',\'' + str(item.getSaleValue()) + '\',\'' + str(store) + '\')')
            var = "INSERT into Inventory values('" + str(j) + "','0')"
            print var
            cursor.execute(var) 

    def removeItem(self, item):
        with self.connection:
            cursor = self.connection.cursor()    
            cursor.execute('DELETE from Item where I_ID = \''+ str(item.getID())+'\'')

    def increaseQuantity(self, itemID, quantity):
        with self.connection:
            newQuant = quantity
            cursor = self.connection.cursor()    
            cursor.execute('SELECT quantity from Inventory where I_ID = \''+str(itemID)+'\'')

            quant = cursor.fetchone()
            newQuant = newQuant + quant[0]
            cursor.execute('UPDATE Inventory set quantity = \''+str(newQuant)+'\' where I_ID = \'' +str(itemID)+'\'')

    def decreaseQuantity(self, itemID, quantity):
        with self.connection:
            cursor = self.connection.cursor()    
            cursor.execute('SELECT quantity from Inventory where I_ID = \''+str(itemID)+'\'')
            quant = cursor.fetchone()
            newQuant = quant[0] - quantity
            cursor.execute('UPDATE Inventory set quantity = \''+str(newQuant)+'\' where I_ID = \'' +str(itemID)+'\'')

    def newTransaction(self, transID, empID, tType, amount, pType):
        with self.connection:
            timev = time.strftime('%Y-%m-%d %H:%M:%S')
            cursor = self.connection.cursor()
            var1 = "Select MAX(Pay_ID) from Payment"
            cursor.execute(var1)
            dd = cursor.fetchone()
            payID = (int) (dd[0]) + 1
            if (tType == 'rental'):
                var = "INSERT into Trans values('" + str(transID) + "','" + timev + "','" + str(1) + "','" + str(empID) + "','" + str(payID) + "','" + str(0.15) + "','" + str(0) + "')" #the 0 marks incomplete
            else:
                var = "INSERT into Trans values('" + str(transID) + "','" + timev + "','" + str(1) + "','" + str(empID) + "','" + str(payID) + "','" + str(0.15) + "','" + str(1) + "')"                
            var2 = "INSERT into Payment values('" + str(payID) + "','" + pType + "','" + str(amount) + "')"
            print var
            cursor.execute(var)
            cursor.execute(var2)

    def searchForReturn(self, transID):
        with self.connection:
            cursor = self.connection.cursor()
            var = "select * from Trans where T_ID = '" + str(transID) +"'"
            #print var
            cursor.execute(var)

            tid = cursor.fetchone()
            if(tid is not None):
                return True
            else:
                return False
    def rentalReturn(self, transID):
        with self.connection:
            cursor = self.connection.cursor()
            var1 = self.searchForReturn(transID)
            if(var1):
                var = "UPDATE Trans set isComplete = '" + str(1) + "' where T_ID = '" + str(transID) + "'"
                cursor.execute(var)
                return True
            else:
                print "transaction not found"
                return False
            
