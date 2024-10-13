import sqlite3

sqlite3.connect('my_users.db')

#Connect to db
conn=sqlite3.connect('my_users.db')

#Python+SQL
sql=conn.cursor()

#Create table users
sql.execute('CREATE TABLE IF NOT EXISTS users(user_id INTEGER, username STRING);')


sql.execute('INSERT INTO users VALUES (2, "TOMAS");')
conn.commit()

print(sql.execute('SELECT * FROM users WHERE user_id=2;').fetchone())