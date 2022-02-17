# Finished, Pep 8 Verified
from models import (session, Product, Brand)
import csv
import app
import time


def backup_csv():
    
    # For Product Database
    with open('backup_inventory.csv', 'a') as csvfile:
        field_names = ['product_name', 'product_price', 'product_quantity',
                        'date_updated', 'brand_name']
        backup_writer = csv.DictWriter(csvfile, fieldnames=field_names)
        backup_writer.writeheader()

    # Pull Database
        info = session.query(Product)
        for rows in info:
            product_name = rows.name
            product_price = '$' + str(format(rows.price / 100, '.2f'))
            product_quantity = rows.quantity
            date_updated = rows.date_updated.strftime('%m/%d/%Y')
            backup_writer.writerow({
                'product_name': product_name,
                'product_price': product_price,
                'product_quantity': product_quantity,
                'date_updated': date_updated,
                'brand_name': rows.brand.name})

    # For Brand Database
    with open('backup_brand.csv', 'a') as csvfile:
        brand_field_names = ['brand_id', 'brand_name']
        brand_backup = csv.DictWriter(csvfile, fieldnames=brand_field_names)
        brand_backup.writeheader()
    
    # Pull Brand Database
        brand_info = session.query(Brand)
        for rows in brand_info:
            brand_name = rows.name
            brand_id = rows.id
            brand_backup.writerow({
                'brand_id': brand_id,
                'brand_name': brand_name})
    print('''\nBackup File "backup_inventoryt.csv" and "backup_brand.csv" Created!
                \rReturning Back To Menu''')
    time.sleep(1.5)
    app.menu()
