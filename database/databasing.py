#joshua hodder
#working on accessing a database 
#started 3/3/23

import sqlite3 

connection = sqlite3.connect('test_db.db') 
cursor = connection.cursor()

if connection is not None:
    pass
    #commands 
else:
    print("Error! cannot create the database connection.")

connection.close()