import sqlite3

### BUILD functions ###

# Query the database and return all Records
def show_all():
## connect to a database
    conn = sqlite3.connect('customer.db')
## create cursor
    c = conn.cursor()

    # query the database
    c.execute("SELECT rowid, * FROM customers")
    items = c.fetchall()

    for item in items:
        print(item)
    ##commit our command below
    conn.commit()
    # close connection
    conn.close()

### ADD RECORD ###
def add_one(first, last, email):
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    c.execute("INSERT INTO customers VALUES(?,?,?)", (first, last, email))
    ## COMMIT OUR COMMAND##
    conn.commit()
    ##CLOSE OUR connection
    conn.close()


### ADD MANY ###
def add_many(list):
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    c.executemany("INSERT INTO customers VALUES (?,?,?)", (list))
    ## COMMIT CHANFES ##
    conn.commit()
    conn.close()

### DELETE A RECORD FROM A TABLE ###

def delete_rec(id):
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    c.execute("DELETE FROM customers WHERE rowid - (?) ")
    ## COMMIT TO CLOSE APP
    conn.commit()
    conn.close()



###FORMART RESULTS###
#c.execute("SELECT * FROM customers WHERE first_name LIKE 'Ja%'")
#c.execute("SELECT * FROM customers")
#c.fetchone()
#c.fetchmany(3)

#items = c.fetchall()

#print items

#print("NAME " + "\t\tEMAIL")
#print("-------" + "\t\t-------")

#for item in items:
    #print(item[0] + " " + item[1] + " \t\t " + item[2])

###END FORMAT RESULTS

### PRIMARY KEY ###
## add to the select query ("SELECT rowid, * FROM customers")
### END PRIMARY KEY ###

### ADDING MANY VAlUES TO A TABLE###

#many_customers = [
#                    ('jack', 'brown', 'jack@brown.com'),
#                    ('Margot', 'Robbers', 'margot@robbers.com'),
#                    ('Natalie', 'Portland', 'natalie@portalnd.com'),
#                    ]

#c.executemany("INSERT INTO customers VALUES(?,?,?)", many_customers)
#print('Successful insert for many')
#### ADDING MANY End ###

### Update Records 

#c.execute("""UPDATE customers SET first_name = 'Chiara'
#            WHERE rowid = 1
#    """)

#print items

### DELETE ITEMS ###

#c.execute("DELETE from customers WHERE rowid = 1")

#print items

##N#TE: NOT INDEXED

### END DELETE ITEMS ##

### ORDER RESULTS BY ###

#c.execute("SELECT rowid, * FROM customers ORDER BY last_name")

#print items

### END ORDER RESULTS BY ##

### AND OR ###

#c.execute("SELECT rowid, * FROM customers WHERE last_name LIKE 'Bro%' AND rowid = 2")
#OR Example
#c.execute("SELECT rowid, * FROM customers WHERE last_name LIKE 'Bro%' OR rowid = 3")
#c.fetchall()

#print items
### END AND OR ###

### LIMIT ###

##c.execute("SELECT rowid, * FROM customers sORDER BY rowid DESC LIMIT 2") ## Error message

##items = c.fetchall()

##for  item in items:
##    print(item)


### END LIMIT ###

### Drop TABLE ###

##c.execute("DROP TABLE customers") # will drop the table
##conn.commit()

#items = c.fetchall()

#for item in items: 
#    print(item)
### END Drop TABLE ###




### DATATYPES ###
##NULL
#INTEGER
#REAL= numbers with decimals
#TEXT
#Blob - mp3 file,
