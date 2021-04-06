from database import Database


db = Database()

# 1. Create the Database
# db.create_db()

# 2. Add one record
# db.add_one('Mari', 'Glez', 'mglez@edu.com')

# 2. Add Many records
# add Many ------------------------
customer_list = [
    ('Pete', 'Lo', 'pete@ng.com'),
    ('Aldo', 'Lau', 'aldo@lu.com'),
    ('Mario', 'Glu', 'mglu@edu.com')
]
db.add_many(customer_list)

# Update
# db.update_by_value('Gin', 'Mari')
# db.update_by_id('Ana', 9)

# Delete One record
# db.delete_one('1')

# Search custom by characters in name, last name
# db.custom_search('a', 'e')

# Show All records
# db.show_all()
