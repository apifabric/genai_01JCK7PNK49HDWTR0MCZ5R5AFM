# using resolved_model gpt-4o-2024-08-06# created from response, to create create_db_models.sqlite, with test data
#    that is used to create project
# should run without error in manager 
#    if not, check for decimal, indent, or import issues

import decimal
import logging
import sqlalchemy
from sqlalchemy.sql import func 
from logic_bank.logic_bank import Rule
from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, Date, DateTime, Numeric, Boolean, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship
from datetime import date   
from datetime import datetime

logging.getLogger('sqlalchemy.engine.Engine').disabled = True  # remove for additional logging

Base = declarative_base()  # from system/genai/create_db_models_inserts/create_db_models_prefix.py


class Wood(Base):
    """description: Stores information about the types of wood."""
    __tablename__ = 'wood'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    type = Column(String)
    origin = Column(String)
    cost = Column(Integer)


class Inventory(Base):
    """description: Current wooden inventory in the warehouse."""
    __tablename__ = 'inventory'

    id = Column(Integer, primary_key=True, autoincrement=True)
    wood_id = Column(Integer, ForeignKey('wood.id'))
    quantity = Column(Integer, nullable=False)
    arrived_on = Column(DateTime)
    expected_date = Column(DateTime)
    cost = Column(Integer)
    total_value = Column(Integer, nullable=False)  # Derived as quantity * cost


class Supplier(Base):
    """description: Information on wood suppliers."""
    __tablename__ = 'supplier'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    country = Column(String)
    contact_number = Column(String)


class SupplierWood(Base):
    """description: Link table between Supplier and Wood; details which Supplier provides which Wood."""
    __tablename__ = 'supplier_wood'

    id = Column(Integer, primary_key=True, autoincrement=True)
    supplier_id = Column(Integer, ForeignKey('supplier.id'), nullable=False)
    wood_id = Column(Integer, ForeignKey('wood.id'), nullable=False)


class Store(Base):
    """description: Information on stores for wooden goods."""
    __tablename__ = 'store'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    location = Column(String)
    manager_name = Column(String)


class StoreInventory(Base):
    """description: Wooden inventory held by each store."""
    __tablename__ = 'store_inventory'

    id = Column(Integer, primary_key=True, autoincrement=True)
    store_id = Column(Integer, ForeignKey('store.id'), nullable=False)
    wood_id = Column(Integer, ForeignKey('wood.id'), nullable=False)
    quantity = Column(Integer, nullable=False)
    total_value = Column(Integer, nullable=False)  # Derived as StoreInventory.quantity * Inventory.cost


# ALS/GenAI: Create an SQLite database
engine = create_engine('sqlite:///system/genai/temp/create_db_models.sqlite')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# ALS/GenAI: Prepare for sample data

from datetime import date

# Test data for Wood
eopine = Wood(name='Neo Pine', type='Softwood', origin='Norway', cost=200)
oak = Wood(name='Oak', type='Hardwood', origin='USA', cost=350)
maple = Wood(name='Maple', type='Hardwood', origin='Canada', cost=300)
mahogany = Wood(name='Mahogany', type='Hardwood', origin='Brazil', cost=400)

# Test data for Inventory
inventory1 = Inventory(wood_id=1, quantity=500, arrived_on=date(2023, 1, 15), expected_date=date(2023, 2, 15), cost=200, total_value=100000)
inventory2 = Inventory(wood_id=2, quantity=300, arrived_on=date(2023, 1, 20), expected_date=date(2023, 2, 10), cost=350, total_value=105000)
inventory3 = Inventory(wood_id=3, quantity=200, arrived_on=date(2023, 1, 25), expected_date=date(2023, 2, 5), cost=300, total_value=60000)
inventory4 = Inventory(wood_id=4, quantity=400, arrived_on=date(2023, 1, 30), expected_date=date(2023, 2, 1), cost=400, total_value=160000)

# Test data for Supplier
supplier1 = Supplier(name='Green Timber', country='Norway', contact_number='123-456-7890')
supplier2 = Supplier(name='Timber Masters', country='USA', contact_number='234-567-8901')
supplier3 = Supplier(name='Maple Leaf Lumber', country='Canada', contact_number='345-678-9012')
supplier4 = Supplier(name='Amazon Woods', country='Brazil', contact_number='456-789-0123')

# Test data for SupplierWood
supplierwood1 = SupplierWood(supplier_id=1, wood_id=1)
supplierwood2 = SupplierWood(supplier_id=2, wood_id=2)
supplierwood3 = SupplierWood(supplier_id=3, wood_id=3)
supplierwood4 = SupplierWood(supplier_id=4, wood_id=4)

# Test data for Store
store1 = Store(name='Wooden Wonders', location='City Center', manager_name='Alice Smith')
store2 = Store(name='Timber Town', location='Uptown', manager_name='Bob Johnson')
store3 = Store(name='Lumber Land', location='Downtown', manager_name='Charlie Brown')
store4 = Store(name='Wood Works', location='Suburb', manager_name='Diana Prince')

# Test data for StoreInventory
storeinventory1 = StoreInventory(store_id=1, wood_id=1, quantity=50, total_value=10000)
storeinventory2 = StoreInventory(store_id=2, wood_id=2, quantity=30, total_value=10500)
storeinventory3 = StoreInventory(store_id=3, wood_id=3, quantity=20, total_value=6000)
storeinventory4 = StoreInventory(store_id=4, wood_id=4, quantity=40, total_value=16000)


session.add_all([eopine, oak, maple, mahogany, inventory1, inventory2, inventory3, inventory4, supplier1, supplier2, supplier3, supplier4, supplierwood1, supplierwood2, supplierwood3, supplierwood4, store1, store2, store3, store4, storeinventory1, storeinventory2, storeinventory3, storeinventory4])
session.commit()
