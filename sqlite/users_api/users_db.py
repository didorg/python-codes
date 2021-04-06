# SQLite implicitly  creates a column named rowid
# and automatically assigns an integer value whenever you insert a new row into the table
# The maximum value of the rowid column is 9,223,372,036,854,775,807
import sqlite3


class UserDB:

    # Create the connection
    def create_connection(self):
        self.conn = sqlite3.connect('users.db')
        self.cur = self.conn.cursor()

    # Create the Database
    def create_db(self):
        # self.create_connection()
        self.cur.execute(""" DROP TABLE IF EXISTS user """)
        self.cur.execute(""" CREATE TABLE user( 
            name TEXT, 
            username TEXT,
            city TEXT, 
            zipcode TEXT)
            """)
        self.conn.commit()
        self.conn.close()

    # Add a new record to the Database
    def add_one(self, name, username, city, zipcode):
        self.cur.execute("""INSERT INTO user VALUES (?, ?, ?, ?)""", (
            name,
            username,
            city,
            zipcode
        ))
        # Commit our command
        self.conn.commit()

    # Commit and Close the connection
    def close_conn(self):
        # Close our connection
        self.conn.close()
