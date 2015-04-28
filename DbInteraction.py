import Item
import Store
import sqlite3 as sql
import time

class DbInteraction:
    
    def __init__(self):
        self.connection = sql.connect('DB.db')

    def addItem(self, item):
        with self.connection:
            cursor = self.connection.cursor()    
            cursor.execute('SELECT MAX(I_ID) from Item')
            i = cursor.fetchone()
            print 
            j = int(i[0])+ 1
            cursor.execute('INSERT into Item (I_ID, Name, Price, SaleValue, Store_ID) values (\'' + str(j) + '\',\'' + item.getName() + '\',\'' + str(item.getPrice()) + '\',\'' + str(item.getSaleValue()) + '\',\'' + str(1) + '\')')
            var = "INSERT into Inventory values('" + str(j) + "','900')"
            print var
            cursor.execute(var) 
            return j

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

    def newTransaction(self, trans, empID, tType, amount, pType):
        with self.connection:
            timev = time.strftime('%Y-%m-%d %H:%M:%S')
            cursor = self.connection.cursor()
            var1 = "Select MAX(Pay_ID) from Payment"
            cursor.execute(var1)
            dd = cursor.fetchone()
            payID = (int) (dd[0]) + 1
            if (tType == 'rental'):
                var = "INSERT into Trans values('" + str(trans.getID()) + "','" + timev + "','" + str(1) + "','" + str(empID) + "','" + str(payID) + "','" + str(0.15) + "','" + str(0) + "')" #the 0 marks incomplete
            else:
                var = "INSERT into Trans values('" + str(trans.getID()) + "','" + timev + "','" + str(1) + "','" + str(empID) + "','" + str(payID) + "','" + str(0.15) + "','" + str(1) + "')"                
            
            var2 = "INSERT into Payment values('" + str(payID) + "','" + pType + "','" + str(amount) + "')"
            print var
            cursor.execute(var)
            cursor.execute(var2)

            items = trans.getItems()
            print len(items)
            if(tType == 'rental'): 
                for x in range(0, len(items)):
                    var = "INSERT into TransItemList values('" + str(trans.getID()) + "','" + str(items[x].getID()) + "','" + str(0) +"')"
                    print var
                    cursor.execute(var)
            else:
                for x in range(0, len(items)):
                    var = "INSERT into TransItemList values('" + str(trans.getID()) + "','" + str(items[x].getID()) + "','" + str(1) +"')"
                    print var
                    cursor.execute(var)                    

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
    def processReturn(self, trans, item):
        with self.connection:
            cursor = self.connection.cursor()
            var1 = self.searchForReturn(trans)
#            if(var1):
#                var = "UPDATE Trans set isComplete = '" + str(1) + "' where T_ID = '" + str(transID) + "'"
#                cursor.execute(var)
#                return True
#            else:
#                print "transaction not found"
#                return False
            
            if(var1):
                # var2 = "SELECT isComplete from Trans where T_ID = '" + str(trans) + "'"
                # cursor.execute(var2)
                # merp = cursor.fetchone()
                # isComp = (int) (merp[0])

                if(self.checkTransType(trans, item)):

                    var = "UPDATE TransItemList set isReturned = '" + str(1) + "' where T_ID = '" + str(trans) + "' AND I_ID = '" + str(item) + "'"
                    print var
                    cursor.execute(var)
                else:
                    var = "DELETE from TransItemList where T_ID = '" + str(trans) + "' AND I_ID = '" + str(item) + "'"
                    print var
                    cursor.execute(var)
                return True
            else:
                print "transaction not found"
                return False            
    def checkRentalExistence(self, transID, itemID):
        with self.connection:
            cursor = self.connection.cursor()
            var = "SELECT isReturned from TransItemList where T_ID = '" + str(transID) + "' AND I_ID = '" + str(itemID) + "'"
            print var
            cursor.execute(var)
            ladada = cursor.fetchone()
            if(ladada is not None):
                good = ladada[0]
            if(self.checkTransType(transID, itemID)):    
                if(ladada is not None):
                    if(good == 0):
                        return 1
                    else:
                        return 2
                else:
                    return 5
            else:
                if(ladada is not None):
                    return 3
                else:
                    return 4
    def checkTransType(self, transID, itemID):
        with self.connection:
            cursor = self.connection.cursor()            
            var2 = "SELECT isComplete from Trans where T_ID = '" + str(transID) + "'"
            cursor.execute(var2)
            merp = cursor.fetchone()
            isComp = (int) (merp[0])        
            if(isComp == 0):
                return True
            else:
                return False
 #   def returnItem(self, transID, itemID):
 #       with self.connection:
 #           cursor = self.connection.cursor()
 #           var = "DELETE from TransItemList where  "'"