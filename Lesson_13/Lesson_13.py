import sqlite3

#Create db
sqlite3.connect('cars.db')

#connecting to database
conn=sqlite3.connect('cars.db')

#create environment for sql commands
sql=conn.cursor()

#send some code for db using execute() method
sql.execute('CREATE TABLE IF NOT EXISTS my_cars (model TEXT, name TEXT, year INTEGER);')

conn.commit()