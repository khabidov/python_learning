import sqlite3

#Connect to db
conn=sqlite3.connect('bank_account.db')

#Python+SQL
sql=conn.cursor()

#Create clients' table
sql.execute('CREATE TABLE IF NOT EXISTS clients(name TEXT, number TEXT, balance REAL);')

#Client registration function
def register(name, number, balance=0.0):
    sql.execute('INSERT INTO client VALUES(?,?,?);', (name, number, balance))
    #Commit changes
    conn.commit()

#Client search by name
def search_by_name(name):
    return sql.execute('SELECT * FROM clients WHERE name=?;',(name,)).fetchone()

#Balance change
def change_balance(amount, choice, name):
    if choice=='increment':
        balance=sql.execute('SELECT balance FROM clients WHERE name=?;', (name,)).fetchone()
        sql.execute('UPDATE clients SET balance=? WHERE name=?;', (amount+balance[0], name))
    if choice=='decrement':
        balance=sql.execute('SELECT balance FROM clients WHERE name=?;', (name,)).fetchone()
        if balance[0]>= amount:
            sql.execute('UPDATE clients SET balance=? WHERE name=?;', (balance[0]-amount, name))
        else:
            return False
        