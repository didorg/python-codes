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

    def delete_one(self, id):
        self.create_connection()
        logger.info('Deleting One')
        self.cur.execute("DELETE FROM customers WHERE rowid = (?)", id)
        self.commit_and_close()

    def search_name(self, name):
        self.create_connection()
        logger.info(f'Searching for {name}')
        self.cur.execute("SELECT rowid, * FROM customers WHERE name LIKE ?", (name+'%',))
        items = self.cur.fetchall()
        for item in items:
            print(item)
        self.commit_and_close()

    # Query the Database ------------------------------------------------------------------------
    def show_all(self):
        self.create_connection()
        logger.info('Showing All')
        self.cur.execute("SELECT rowid, * FROM customers")
        items = self.cur.fetchall()
        for item in items:
            print(item)
        self.commit_and_close()

    def commit_and_close(self):
        logger.info('Commit & Closing Connection')
        # Commit our command
        self.conn.commit()
        # Close our connection
        self.conn.close()
