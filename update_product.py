from asyncio.windows_events import NULL
from models import (session, Product, Brand)
import app
from datetime import datetime
import time


def update_product(update_id):
    to_update = session.query(Product).filter(
        Product.id == update_id).first()
    while True:
        print(f'\n**** Updating: {to_update.name}')
        command = input('''\nEnter Command From The List
                        \rEnter A To Update the Product Name
                        \rEnter B To Update Products Price
                        \rEnter C To Update Product Quantity
                        \rEnter D To Update Products Date
                        \rEnter E To Update Product Brand
                        \rEnter F To Delete Product
                        \rEnter G To Cancel and Return to Main Menu
                        \rCommand: ''')
        # Update Name
        if command.lower() == 'a':
            update_name(to_update)
        # Update Price
        elif command.lower() == 'b':
            update_price(to_update)
        # Update Quantity
        elif command.lower() == 'c':
            update_quantity(to_update)
        # Update Date
        elif command.lower() == 'd':
            update_date(to_update)
        # Change Brand
        elif command.lower() == 'e':
            new_brand = brand_name()
            try:
                to_update.brand_id = new_brand.id
            except AttributeError:
                to_update.brand_id = NULL    
            print("Brand updated!")
            session.commit()
        # Delete Product
        elif command.lower() == 'f':
            delete_product(to_update)
        # Return To Menu
        elif command.lower() == 'g':
            print("Returning to Main Menu")
            app.menu()
            break


def update_name(to_update):
    while True:
                update_name = input(f'''\nCurrent Name Is: {to_update.name}
                            \rEnter A New Name: ''')
                selection = input(f'''\nConfirming New Name: {update_name}?
                                \rEnter A To Confirm
                                \rEnter B To Retype name
                                \rEnter C to Go Back To Product Modification Menu
                                \rCommand: ''')
                if selection.lower() == 'a':
                    to_update.name = update_name
                    session.commit()
                    print('''\nProduct Name Updated!
                            \rReturning Back to Sub Menu''')
                    time.sleep(1.5)
                    break
                elif selection.lower() == 'b':
                    pass
                elif selection.lower() == 'c':
                    break


def update_price(to_update):
    while True:
        product_price = input(f'''\nCurrent Price: {to_update.price / 100}
                    \rPlease Enter A New Price Below
                    \r** Do Not Use a Currency Symbol **
                    \rNew Price: ''')
        update_price = price_checker(product_price)
        confirm = input(f'''\nConfirming: {update_price / 100}?
                        \rEnter A To Confirm
                        \rEnter B To Enter a New Price
                        \rEnter C to Go Back To Product Modification Menu
                        \rCommand: ''')
        if confirm.lower() == 'a':
            to_update.price = update_price
            session.commit()
            print('''\n Product Price Updated!
                    \rReturning Back To Sub Menu''')
            time.sleep(1.5)
            break
        elif confirm.lower() == 'b':
            pass
        elif confirm.lower() == 'c':
            break


def update_quantity(to_update):
    while True:
        product_quantity = input(f'''\nCurrent Quanitity: {to_update.quantity}
                    \rEnter a New Quantity: ''')
        update_quantity = quantity_checker(product_quantity)
        confirm = input(f'''\nConfirming New Quanitity: {product_quantity}
                        \rEnter A To Confirm
                        \rEnter B To Enter a New Quantity
                        \rEnter C To Go Back to Product Modification Menu
                        \rCommand: ''')
        if confirm.lower() == 'a':
            to_update.quantity = update_quantity
            session.commit()
            print('''\nProduct Quantity Updated!
                \rReturning Back to Sub Menu''')
            time.sleep(1.5)
            break

        elif confirm.lower() == 'b':
            pass
        elif confirm.lower() == 'c':
            break


def update_date(to_update):
    easy_date2 = to_update.date_updated.strftime('%m-%d-%Y')
    while True:
        product_date = input(f'''\nCurrent Product Date: {easy_date2}
                        \rEnter A New Date (MM-DD-YYYY): ''')
        update_date = date_checker(product_date)
        easy_date = update_date.strftime('%m-%d-%Y')
        confirm = input(f'''
                            \nConfirming New Date: {easy_date}
                            \rEnter A To Confirm
                            \rEnter B To Enter a New Date
                            \rEnter C To Go Back to Product Modification Menu
                            \rCommand: ''')
        if confirm.lower() == 'a':
            to_update.date_updated = update_date
            session.commit()
            print('''\nProduct Date Updated!
                \rReturning Back to Sub Menu''')
            time.sleep(1.5)
            break
        elif confirm.lower() == 'b':
            pass
        elif confirm.lower() == 'c':
            break


def delete_product(to_update):
    while True:
        confirm = input(f'''\nDeleting: {to_update.name}
                    \rEnter A To Confirm
                    \rEnter B To Cancel
                    \rCommand: ''')
        if confirm.lower() == 'a':
            session.delete(to_update)
            session.commit()
            print("\nItem Deleted! Returning Back To Main Menu")
            time.sleep(1.5)
            app.menu()
            break
        elif confirm.lower() == 'b':
            break


def price_checker(product_price):
    while True:
        try:
            product_price_check = float(product_price)
        except ValueError:
            product_price = input('''\n** Invalid Price Was Entered **
                                    \rDo not use a Currency Symbol(e.g $)
                                    \rNew Entry: ''')
        else:
            return float(product_price_check * 100)


def quantity_checker(product_quantity):
    while True:
        try:
            num_check = float(product_quantity)
        except ValueError:
            product_quantity = input('''\n ** Invalid Quantity Entered **
                                    \r Please Enter A New Number for Quantity
                                    \rNew Entry: ''')
        else:
            return float(num_check)


def duplicate_checker(product_name_check):
    id_list = []
    print("Checking for prior entries...\n")
    checking = session.query(Product). \
        filter(Product.name.like('%' + product_name_check + '%')).all()
    question = False
    for returns in checking:
        print(f'\r{returns.id} - {returns.name}')
        id_list.append(returns.id)
        question = True
    while question:
        if question:
            proceed = input('''\nMatching item located in database.
                        \rEnter A to Add New Item
                        \rEnter B to Update An Item
                        \rEnter Q to Go Back to Main Menu
                        \rCommand: ''')
            if proceed.lower() == "a":
                question = False
            elif proceed.lower() == "b":
                update_id = input(f'''\nProduct IDs: {id_list}
                        \rEnter Product ID To Update: ''')
                question = False
                update_product(update_id)

            elif proceed.lower() == 'q':
                print("\nReturning to Main Menu")
                question = False
                app.menu()
            else:
                input('''Valid Command Not Entered.
                \rPress Enter to Try Again''')
    return product_name_check


def date_checker(product_date):
    while True:
        try:
            product_date_obj = datetime.strptime(product_date, '%m-%d-%Y')
            return product_date_obj
        except ValueError:
            product_date = input('''\nIncorrect date entered.
                            \rPlease Enter a new date in the Following Format
                            \rMM-DD-YYYY Example: 05-06-2018
                            \rEnter New Date: ''')


def brand_name():
    print('\n** Avaliable Brands')
    names = session.query(Brand).all()
    ids = []
    for stuff in names:
        print(str(stuff.id) + ") " + stuff.name)
        ids.append(stuff.id)
    while True:
        brand = input('''\nEnter Brand Number from List
            \ror X for other brand
            \rEnter: ''')
        if brand.lower() == 'x':
            brand_return = NULL
            break
        else:
            brand_num = int(brand)
            if brand_num in ids:
                brand_return_get = session.query(Brand). \
                    filter(Brand.id == brand_num).one()
                brand_return = brand_return_get
                break
            else:
                print('** Invalid Entry! Enter X or ID from List. **')
    return brand_return


def confirmation(verified_product, price_verified, quantity_verified,
                    date_verified, brand_name_check):
    date = date_verified.strftime('%m-%d-%y')
    print(f'''\n*** Confirmation ***
            \rProduct Name: {verified_product.title()}
            \rPrice: {price_verified / 100}
            \rQuantity: {quantity_verified}
            \rDate: {date}''')
    if brand_name_check:
            print('''\rBrand: {brand_name_check.name}''')
    else:
            print('''\rOther Brand (Will go in as NULL)''')
    confirm = input('''
            \nEnter A to confirm
            \rEnter B to cancel and return back to the main menu
            \rCommand: ''')
    while True:
        if confirm.lower() == "a":
            if brand_name_check:
                new_product = Product(name=verified_product.title(),
                                        price=price_verified, 
                                        quantity=quantity_verified,
                                        date_updated=date_verified,
                                        brand_id=brand_name_check.id)
            else:
                new_product = Product(name=verified_product.title(),
                                    price=price_verified,
                                    quantity=quantity_verified,
                                    date_updated=date_verified, 
                                    brand_id=NULL)
            check_double = session.query(Product).filter(
                Product.name == new_product.name).one_or_none()
            if check_double is None:
                session.add(new_product)
                session.commit()
                print(f'''Product: {verified_product.title()}
                        Added to the Database!''')
                time.sleep(1.5)
                app.menu()
                break
            else:
                if new_product.date_updated.date() > check_double.date_updated:
                    print('''\nDuplicate was found in Database with Older Date!
                            \rAdding this item!''')
                    session.delete(check_double)
                    session.add(new_product)
                    session.commit()
                    print(f'''Product: {verified_product.title()}
                            Added to the Database!''')
                    time.sleep(1.5)
                    app.menu()
                    break
                else:
                    print('''\n** Error! Duplicate Item in Database
                            with Newer Date! **
                            \r** Returning to Main Menu **''')
                    app.menu()
                    break

        elif confirm.lower() == 'b':
            print('\nReturn to Main Menu')
            app.menu()
            break
        else:
            confirm = input(f'\nInvalid input \rEnter A Command:')
