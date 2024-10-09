from itertools import product


#Deleting product from DB
def del_product(pr_name):
    sql.execute('DELETE FROM products WHERE')












##Cart methods##
#Showing cart
def show_cart(tg_id):
    return sql.execute('SELECT * FROM cart WHERE user_id=?;',(tg_id,)).fetchall()


#Adding to cart
def add_to_cart(tg_id, product, product_amount):
    sql.execute('INSRT INTO cart VALUES (?,?,?);',(tg_id,product, product_amount))
    #Changes fixation
    connection.commit()









#placing an order
def make_order(tg_id):
    #Getting product names and their amounts from users' cart
    product_names=sql.execute('SELECT user_product FROM cart WHERE user_id=?;',(tg_id,)).fetchall()
    product_quantities=sql.execute('SELECT product_amount FROM cart WHERE user_id=?;',(tg_id,)).fetchall()

#Working with warehouse
product_counts=[sql.execute('SELECT pr_count FROM products WHERE pr_name=?;',i[0],)).fetchone()[0] for i in product_names]
totals=[]

for e in product_quantities:
    for c in product_counts:
        totals.append(c-e[0])

for t in totals:
    for n in product_names:
        sql.execute('UPDATE products SET pr_count=? WHERE pr_name=?;',(t,n))