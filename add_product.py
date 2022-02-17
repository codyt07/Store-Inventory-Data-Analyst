import update_product

def add_product():
    print("\nAdd Product")
    product_name_check = input("Enter Product Name: ")
    verified_product = update_product.duplicate_checker(product_name_check)
    product_price = input("Enter Product Price Without Currency Symbol: ")
    price_verified = update_product.price_checker(product_price)
    product_quantity = input('Enter Product Quantity: ')
    quantity_verified = update_product.quantity_checker(product_quantity)
    product_date = input('Enter Date (MM-DD-YYYY) (10-27-2021): ')
    date_verified = update_product.date_checker(product_date)
    brand_name_check = update_product.brand_name()
    update_product.confirmation(verified_product, price_verified, quantity_verified, date_verified, brand_name_check)