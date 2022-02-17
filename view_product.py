# Finished, Pep8 Verified
from asyncio.windows_events import NULL
from models import (session, Product)
import app
import update_product


def view_summary():
    id_list = []
    for id_list_maker in session.query(Product):
        id_list.append(id_list_maker.id)
    product_selection = input(f'''\nPlease Enter the Product ID To View Product
            \rProduct IDs: {id_list}
            \rEnter ID: ''')
    try:
        view_product = session.query(Product).filter(
            Product.id == product_selection).first()
        easy_date = view_product.date_updated.strftime('%m-%d-%Y')
        print(f'''\nProduct Information for Product ID {product_selection}
                \r* Product Name: {view_product.name}
                \r* Product Price: ${format(view_product.price / 100, '.2f')}
                \r* Product Quantity: {view_product.quantity}''')
        try: 
            print(f'''\r* Product Brand: {view_product.brand.name}''')
        except AttributeError:
            print(f'''\r* No Brand Name''')
        selection = input(f'''        
                \r* Information Last Updated: {easy_date}
                \nEnter A To Return To Main Menu
                \rEnter B To Go Back To Product ID Screen
                \rEnter C To Update Product
                \rCommand: ''')
    except AttributeError:
        input('''\n*- Invalid Product Was Entered -*
                \rPress Enter to Try again...''')
        view_summary()

    if selection.lower() == "a":
            app.menu()
    elif selection.lower() == "b":
            view_summary()
    elif selection.lower() == 'c':
        update_id = view_product.id
        update_product.update_product(update_id)
    else:
        input('''\nValid input not Entered
                \rPress Enter to return main Menu''')
        app.menu()
