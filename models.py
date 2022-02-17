# For Data Analysist, PEP 8 Verified
from sqlalchemy import (create_engine, Column, Integer,
                        String, Date, ForeignKey)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
import csv
from datetime import datetime


engine = create_engine('sqlite:///inventory.db', echo=False)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


# For brands.csv
class Brand(Base):
    __tablename__ = 'brands'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    products = relationship('Product', back_populates='brand')


def brand_csv_reader():
    with open('brands.csv', newline='') as brands_csv:
        brands_reader = csv.reader(brands_csv, delimiter=',')
        next(brands_reader)
        rows = list(brands_reader)
        for row in rows:
            add_to_db = Brand(name=row[0])
            check_brand_double = session.query(Brand). \
                filter(Brand.name == add_to_db.name).one_or_none()
            if check_brand_double:
                pass
            else:
                session.add(add_to_db)
                session.commit()


# For Producs.Csv
class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Integer)
    quantity = Column(Integer)
    date_updated = Column(Date)
    brand_id = Column(Integer, ForeignKey("brands.id"))
    brand = relationship('Brand', back_populates='products')


def __repr__(self):
    return f'<User(name={self.name}, quantity={self.quantity}, \
    price={self.price}, date_updated={self.date_updated}, \
    brand={self.brand_id})'


def csv_reader():
    with open('inventory.csv', newline='') as inventory_csv:
        inventory_reader = csv.reader(inventory_csv, delimiter=',')
        next(inventory_reader)
        rows = list(inventory_reader)
        for row in rows:
            add_to_db = Product(name=row[0],
                                price=price_cleaner_db_initializer(row),
                                quantity=quantity_db_initializer(row),
                                date_updated=date_cleaner_db_initializer(row),
                                brand_id=brand_select(row))
            # Check for duplicates
            check_double = session.query(Product). \
                filter(Product.name == add_to_db.name).one_or_none()
            if check_double:
                if add_to_db.date_updated.date() > check_double.date_updated:
                    check_double.name = add_to_db.name
                    check_double.price = add_to_db.price
                    check_double.quantity = add_to_db.quantity
                    check_double.date_updated = add_to_db.date_updated
                    check_double.brand_id = add_to_db.brand_id
                    session.commit()
                else:
                    pass
            else:
                session.add(add_to_db)
                session.commit()


def price_cleaner_db_initializer(row):
    price_to_clean = row[1]
    without_sign = price_to_clean.replace("$", "")
    try:
        without_sign_float = float(without_sign)
    except ValueError:
        pass
    else:
        return int(without_sign_float * 100)


def quantity_db_initializer(row):
    quantity_start = row[2]
    try:
        quantity_int = int(quantity_start)
    except ValueError:
        pass
    else:
        return quantity_int


def date_cleaner_db_initializer(row):
        date_time_string = row[3]
        try:
            date_time_obj = datetime.strptime(date_time_string, '%m/%d/%Y')
            return date_time_obj
        except ValueError:
            pass


def brand_select(row):
    brand_id_fetch = session.query(Brand). \
        filter(Brand.name == row[4]).one_or_none()
    id = brand_id_fetch.id
    return id

if __name__ == '__main__':
    print("Please Use app.py instead")
