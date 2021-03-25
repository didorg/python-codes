# SQLite implicitly  creates a column named rowid
# and automatically assigns an integer value whenever you insert a new row into the table
# The maximum value of the rowid column is 9,223,372,036,854,775,807
import sqlite3
from loguru import logger


class Database:

    # Create the connection
    def create_connection(self):
        logger.info('Creating the connection')
        self.conn = sqlite3.connect('customer.db')
        self.cur = self.conn.cursor()

    # Create the Database
    def create_db(self):
        self.create_connection()
        logger.info('Creating the Database')
        self.cur.execute(""" DROP TABLE IF EXISTS customers """)
        self.cur.execute(""" create table customers( 
            name TEXT, 
            last_name TEXT, 
            email TEXT)
            """)
        self.commit_and_close()

    # Add a new record to the Database
    def add_one(self, name, last_name, email):
        self.create_connection()
        logger.info('Adding One')
        self.cur.execute("""INSERT INTO customers VALUES (?, ?, ?)""", (
            name,
            last_name,
            email
        ))
        self.commit_and_close()

    # Add many records to the Database
    def add_many(self, customer_list):
        self.create_connection()
        logger.info('Adding Many')
        self.cur.executemany("""INSERT INTO customers VALUES (?, ?, ?)""", customer_list)
        self.commit_and_close()

    # Delete One record in the Database
    def delete_one(self, id):
        self.create_connection()
        logger.info('Deleting One')
        self.cur.execute("DELETE FROM customers WHERE rowid = (?)", id)
        self.commit_and_close()

    # Query the Database ------------------------------------------------------------------------
    # Search custom by name
    def custom_search(self, name, last_name):
        self.create_connection()
        logger.info(f'Searching for {name} and {last_name}')
        # list 1
        print(f'------- By /{name}/ in Name -----------')
        items = self.cur.execute("SELECT rowid, * FROM customers WHERE name LIKE ?", ('%' + name + '%',))
        for item in items:
            print(item)
        # list 2
        print(f'------- By /{name}/ in Name and /{last_name}/ in Last Name -----------')
        name_and_last = self.cur.execute(
            "SELECT rowid, * FROM customers WHERE name LIKE ? AND last_name LIKE ?",
            ('%' + name + '%', '%' + last_name + '%'))
        for item in name_and_last:
            print(item)

        self.commit_and_close()

    # Show All
    def show_all(self):
        self.create_connection()
        logger.info('Showing All')
        items = self.cur.execute("SELECT rowid, * FROM customers")
        for item in items:
            print(item)
        self.commit_and_close()

    # Commit and Close the connection
    def commit_and_close(self):
        logger.info('Commit & Closing Connection')
        # Commit our command
        self.conn.commit()
        # Close our connection
        self.conn.close()
