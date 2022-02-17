# This version is for Team Treehouse Data Analyst Degree. I created the 
# original for Ptython Tech Degree 


from models import (csv_reader, brand_csv_reader, engine)
import models
import view_product, add_product, analyze_database, backup_database


def menu():
    selection = input('''\n*** Cody's Store Inventory Manager ***
            \rPlease Select from the Menu Below
            \rEnter V to view a single product
            \rEnter N to add a product
            \rEnter A to Analyze the Database
            \rEnter B to backup the database
            \rEnter Q to Exit the Program
            \rEnter Command: ''')

    # View Product
    if selection.lower() == "v":
        view_product.view_summary()
    
    # Add Product
    elif selection.lower() == "n":
        add_product.add_product()
    
    # Analyse Database
    elif selection.lower() == "a":
        analyze_database.analyze_database()
    
    #Backup Database
    elif selection.lower() == "b":
        backup_database.backup_csv()
    
    #Quit Program
    elif selection.lower() == 'q':
        print('Thank you for using this program!')
        exit()
    else:
        input('''\n*** A Valid Command Was Not Entered ***
                \rPress Enter To Try Again...''')
        menu()

if __name__ == '__main__':
    models.Base.metadata.create_all(engine)
    brand_csv_reader()
    csv_reader()
    menu()
