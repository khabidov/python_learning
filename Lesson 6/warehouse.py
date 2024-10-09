all_products={'Whole warehouse':{}}
while True:
    admin=input('What would you like to do? ')
    if admin=='add':
        product_name=input('Enter product name: ')
    if admin=='products':
    product_count=input('Enter quantity: ')
all_products['Whole warehouse'][product_name]=product_count

print(all_products)