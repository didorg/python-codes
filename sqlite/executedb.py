from database import Database


db = Database()

# db.create_db()
# db.add_one('Mari', 'Glez', 'mglez@edu.com')

# add Many ------------------------
customer_list = [
    ('Adam', 'Pe', 'adamp@ng.com'),
    ('Lu', 'Shin', 'gao@lu.com'),
    ('Mari', 'Glez', 'mglez@edu.com')
]
# db.add_many(customer_list)

# Delete One ------------------------
# db.delete_one('3')

# db.search_name("a")

# Show All --------------------------
# db.show_all()
