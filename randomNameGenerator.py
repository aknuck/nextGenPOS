import random
import sqlite3


def newRandomName():
    vowels = "aaaeeeeiiiioouu"
    consenants = "wrtttypssdfghhjklccvbnnmm"
    
    word = ""
    lastVowel = False #make sure to alternate vowel and consenants
    
    if random.randint(0,1) == 1:
    	lastVowel = True
    	word += random.choice(vowels)
    else:
    	lastVowel = False
    	for x in range(random.randint(1,2)):
    		word += random.choice(consenants)
    
    
    if not lastVowel:
    	lastVowel = True
    	word += random.choice(vowels)
    else:
    	lastVowel = False
    	for x in range(random.randint(1,2)):
    		word += random.choice(consenants)
    
    r = random.randint(1,3)
    if r != 2:
    	if not lastVowel:
    		lastVowel = True
    		word += random.choice(vowels)
    	else:
    		lastVowel = False
    		for x in range(random.randint(1,2)):
    			word += random.choice(consenants)
    
    	r = random.randint(1,3)
    	if r != 2:
    		if not lastVowel:
    			lastVowel = True
    			word += random.choice(vowels)
    		else:
    			lastVowel = False
    			for x in range(random.randint(1,2)):
    				word += random.choice(consenants)
    		r = random.randint(1,3)
    		if r != 2:
    			if not lastVowel:
    				lastVowel = True
    				word += random.choice(vowels)
    			else:
    				lastVowel = False
    				for x in range(random.randint(1,2)):
    					word += random.choice(consenants)
    return word


con = sqlite3.connect("DB.db")
con.isolation_level = None
cur = con.cursor()

buffer = ""

for i in range(7,60):
    buffer = ""
    itemName = newRandomName()
    itemPrice = random.randint(99,9999)/100.00
    itemSale = 0
    if random.randint(1,5) == 1:
        itemSale = random.randint(1,5)/10.00
    line = "insert into Item (I_ID,Name,Price,SaleValue,Store_ID) values ("+str(i)+",\""+itemName+"\","+str(itemPrice)+","+str(itemSale)+",1);"
    buffer += line
    if sqlite3.complete_statement(buffer):
        try:
            buffer = buffer.strip()
            cur.execute(buffer)
            if buffer.lstrip().upper().startswith("SELECT"):
                print cur.fetchall()
        except sqlite3.Error as e:
            print "An error occurred:", e.args[0]
        buffer = ""

con.close()