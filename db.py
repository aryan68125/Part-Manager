import sqlite3

class Database:
    #constructor of the class Database also called as an initializer in python
    #a constructor runs when the object is instanciated
    #self = this , db = database name
    def __init__(self,db):
        #db is the name of the database
        #connection is the property through which we will be connecting to our database
        self.connection = sqlite3.connect(db)
        #database_cursor is the name of the cursor for database db
        self.database_cursor = self.connection.cursor()
        #now here we are executing our cursor to create a database if not already present
        #the table inside the database db is parts table
        #parts table will be created inside this database db
        self.database_cursor.execute("CREATE TABLE IF NOT EXISTS parts (id INTEGER PRIMARY KEY, part text, customer text, retailer text, price text)")
        #now we will commiting these changes to our database db
        self.connection.commit()

    def fetch(self):
        #here we are reading the parts table from our database db
        # * means we want all the information present inside our parts table of our database db
        self.database_cursor.execute("SELECT * FROM parts")
        #it will get all the rows
        rows = self.database_cursor.fetchall()
        return rows

    def insert(self, part, customer, retailer, price):
        #the "INSERT INTO parts VALUES" line will insert the values passed by the user
        #"(NULL, ?, ?, ?, ?)" prevents from sql injection
        # variable python tuple => (part,customer, retailer, price) are the arguments that are passed in to this insert function
        self.database_cursor.execute("INSERT INTO parts VALUES(NULL, ?, ?, ?, ?)", (part,customer, retailer, price))
        #now commit these changes to our database
        self.connection.commit()

    def remove(self,id):
        # "DELETE FROM parts WHERE id=?" is the sql command to delete a record from the table named parts
        # (id,) is a tuple a normal python tuple id is the variable passed in this function remove as an argument
        self.database_cursor.execute("DELETE FROM parts WHERE id=?",(id,))
        self.connection.commit()

    def update(self, id, part, customer, retailer, price):
        #"UPDATE parts SET part = ? , customer = ? , retailer = ? , price = ? WHERE id=?" is the sql command that will update the information in our parts column
        #part = ? , customer = ? , retailer = ? , price = ? are the column names of our parts table
        # WHERE id=? is the where clause which will match the id and update the information of the record of matching id
        # (part,customer,retailer,price,id) is a python tuple containing our arguments passed on to this update function
        self.database_cursor.execute("UPDATE parts SET part = ? , customer = ? , retailer = ? , price = ? WHERE id=?", (part,customer,retailer,price,id))
        self.connection.commit()

    # now here we will call the destructor
    #destructor is called when all references of the objects have been deleted
    def __del__(self):
        self.connection.close()