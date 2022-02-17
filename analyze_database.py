# Finished, PEP 8 Verified
from models import (session, Product, Brand)
from sqlalchemy import func
import app


def analyze_database():
    # Get the most expensive product
    most_expensive_start = session.query(func.max(Product.price)).first()
    target = most_expensive_start[0]
    most_expensive_product = session.query(Product). \
        filter(Product.price == target).all()
    print("\n** The Most Expensive Item(s) Are: ** ")
    for x in most_expensive_product:
        print(f'''\n* Product Name: {x.name}
        \r* Product Price: ${format(x.price / 100, '.2f')}
        \r* Product Brand: {x.brand.name}''')

    # Least Expensive
    least_expensive = session.query(func.min(Product.price)).one()
    least_target = least_expensive[0]
    least_expensive_product = session.query(Product). \
        filter(Product.price == least_target).all()
    print("\n ** The Least Expensive Item(s) Are: **")
    for x in least_expensive_product:
        print(f'''\n* Product Name: {x.name}
        \r* Product Price: ${format(x.price / 100, '.2f')}
        \r* Product Brand: {x.brand.name}''')

    # Most Common Brand
    brand_name_count = []
    for x in session.query(Product.brand_id).all():
        brand_name_count.append(x)

    most_brand = max(brand_name_count, key=brand_name_count.count)
    least_brand = min(brand_name_count, key=brand_name_count.count)
    most_number = most_brand[0]
    least_number = least_brand[0]
    most_result = session.query(Brand).filter(Brand.id == most_number).first()
    least_result = session.query(Brand).filter(Brand.id == least_number).first()
    print(f'''\n *-* The Most Common Brand is: {most_result.name} *-*
                \r-*- The Least CommonBrand is: {least_result.name} -*-''')

    #Low Quantity
    quantity = []
    for x in session.query(Product.quantity).all():
        quantity.append(x)
    low_quantity = min(quantity)
    low_quantity_num = low_quantity[0]
    low_quantity_query = session.query(Product).filter(Product.quantity == low_quantity_num).all()
    print(f'''\nProduct(s) with the lowest quantity are: ''') 
    for all in low_quantity_query:
        print(f'''\nProduct Name: {all.name}
                \rProduct Quantity: {all.quantity}''')

    input('''\nPress Enter to return back to the menu! 
            \r''')
    app.menu()

