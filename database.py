import sqlite3

## connect to a database
conn = sqlite3.connect('customer.db')

## create cursor
c = conn.cursor()

###FORMART RESULTS###
#c.execute("SELECT * FROM customers WHERE first_name LIKE 'Ja%'")
c.execute("SELECT * FROM customers")
#c.fetchone()
#c.fetchmany(3)

items = c.fetchall()

print items

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

c.execute("SELECT rowid, * FROM customers sORDER BY rowid DESC LIMIT 2") ## Error message

items = c.fetchall()

for  item in items:
    print(item)


### END LIMIT ###
### DATATYPES ###
##NULL
#INTEGER
#REAL= numbers with decimals
#TEXT
#Blob - mp3 file,

##commit our command below
conn.commit()

# close connection

conn.close()
