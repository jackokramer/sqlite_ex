import sqlite3

## connect to a database
conn = sqlite3.connect('customer.db')

## create cursor
c = conn.cursor()

#

c.execute("SELECT * FROM customers")
#c.fetchone()
#c.fetchmany(3)

print(c.fetchall())

#many_customers = [
#                    ('jack', 'brown', 'jack@brown.com'),
#                    ('Margot', 'Robbers', 'margot@robbers.com'),
#                    ('Natalie', 'Portland', 'natalie@portalnd.com'),
#                    ]

#c.executemany("INSERT INTO customers VALUES(?,?,?)", many_customers)
#print('Successful insert for many')

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