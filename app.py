import database

#database.add_one('Laura', 'Numbers', 'lauara@numbers.com')

## Add many records##

stuff = [
    ('Kira', 'Knightly', 'kira@knightly.com'),
    ('Jessica', 'Alba', 'jessica@alba.com'),
    ('Sienna', 'Miller', 'sienna@miller.com')
]
database.add_many(stuff)

database.show_all()

#database.delete_rec(6) ## need to pass the intger as a string
