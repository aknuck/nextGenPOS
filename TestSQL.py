import sqlite3 as lite
import sys
con = None
try:
    con = lite.connect('test.db')
    cur = con.cursor()    
    cur.execute('SELECT SQLITE_VERSION()')
    data = cur.fetchone()
    print "SQLite version: %s" % data                
except lite.Error, e:
    print "Error %s:" % e.args[0]
finally:
    if con:
        con.close()
        
        
        
        
        
# To view all tables        
cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
print(cursor.fetchall())