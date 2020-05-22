import sqlite3

## connect to a database
conn = sqlite3.connect('customer.db')

## create cursor
c = conn.cursor()

###FORMART RESULTS###
#c.execute("SELECT * FROM customers")

#c.fetchone()
#c.fetchmany(3)

#items = c.fetchall()

#print items

#print("NAME " + "\t\tEMAIL")
#print("-------" + "\t\t-------")

#for item in items:
#    print(item[0] + " " + item[1] + " \t\t " + item[2])

###END FORMAT RESULTS

## ADDING MANY ##

#many_customers = [
#                    ('jack', 'brown', 'jack@brown.com'),
#                    ('Margot', 'Robbers', 'margot@robbers.com'),
#                    ('Natalie', 'Portland', 'natalie@portalnd.com'),
#                    ]

#c.executemany("INSERT INTO customers VALUES(?,?,?)", many_customers)
#print('Successful insert for many')
#### ADDING MANY ###
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