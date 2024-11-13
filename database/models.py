# coding: utf-8
from sqlalchemy import DECIMAL, DateTime  # API Logic Server GenAI assist
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

########################################################################################################################
# Classes describing database for SqlAlchemy ORM, initially created by schema introspection.
#
# Alter this file per your database maintenance policy
#    See https://apilogicserver.github.io/Docs/Project-Rebuild/#rebuilding
#
# Created:  November 13, 2024 17:04:26
# Database: sqlite:////tmp/tmp.5YBDWZ9E4x-01JCK7PNK49HDWTR0MCZ5R5AFM/WoodInventoryManagement/database/db.sqlite
# Dialect:  sqlite
#
# mypy: ignore-errors
########################################################################################################################
 
from database.system.SAFRSBaseX import SAFRSBaseX
from flask_login import UserMixin
import safrs, flask_sqlalchemy
from safrs import jsonapi_attr
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped
from sqlalchemy.sql.sqltypes import NullType
from typing import List

db = SQLAlchemy() 
Base = declarative_base()  # type: flask_sqlalchemy.model.DefaultMeta
metadata = Base.metadata

#NullType = db.String  # datatype fixup
#TIMESTAMP= db.TIMESTAMP

from sqlalchemy.dialects.sqlite import *



class Store(SAFRSBaseX, Base):
    """
    description: Information on stores for wooden goods.
    """
    __tablename__ = 'store'
    _s_collection_name = 'Store'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    location = Column(String)
    manager_name = Column(String)

    # parent relationships (access parent)

    # child relationships (access children)
    StoreInventoryList : Mapped[List["StoreInventory"]] = relationship(back_populates="store")



class Supplier(SAFRSBaseX, Base):
    """
    description: Information on wood suppliers.
    """
    __tablename__ = 'supplier'
    _s_collection_name = 'Supplier'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    country = Column(String)
    contact_number = Column(String)

    # parent relationships (access parent)

    # child relationships (access children)
    SupplierWoodList : Mapped[List["SupplierWood"]] = relationship(back_populates="supplier")



class Wood(SAFRSBaseX, Base):
    """
    description: Stores information about the types of wood.
    """
    __tablename__ = 'wood'
    _s_collection_name = 'Wood'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    type = Column(String)
    origin = Column(String)
    cost = Column(Integer)

    # parent relationships (access parent)

    # child relationships (access children)
    InventoryList : Mapped[List["Inventory"]] = relationship(back_populates="wood")
    StoreInventoryList : Mapped[List["StoreInventory"]] = relationship(back_populates="wood")
    SupplierWoodList : Mapped[List["SupplierWood"]] = relationship(back_populates="wood")



class Inventory(SAFRSBaseX, Base):
    """
    description: Current wooden inventory in the warehouse.
    """
    __tablename__ = 'inventory'
    _s_collection_name = 'Inventory'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    wood_id = Column(ForeignKey('wood.id'))
    quantity = Column(Integer, nullable=False)
    arrived_on = Column(DateTime)
    expected_date = Column(DateTime)
    cost = Column(Integer)
    total_value = Column(Integer, nullable=False)

    # parent relationships (access parent)
    wood : Mapped["Wood"] = relationship(back_populates=("InventoryList"))

    # child relationships (access children)



class StoreInventory(SAFRSBaseX, Base):
    """
    description: Wooden inventory held by each store.
    """
    __tablename__ = 'store_inventory'
    _s_collection_name = 'StoreInventory'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    store_id = Column(ForeignKey('store.id'), nullable=False)
    wood_id = Column(ForeignKey('wood.id'), nullable=False)
    quantity = Column(Integer, nullable=False)
    total_value = Column(Integer, nullable=False)

    # parent relationships (access parent)
    store : Mapped["Store"] = relationship(back_populates=("StoreInventoryList"))
    wood : Mapped["Wood"] = relationship(back_populates=("StoreInventoryList"))

    # child relationships (access children)



class SupplierWood(SAFRSBaseX, Base):
    """
    description: Link table between Supplier and Wood; details which Supplier provides which Wood.
    """
    __tablename__ = 'supplier_wood'
    _s_collection_name = 'SupplierWood'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    supplier_id = Column(ForeignKey('supplier.id'), nullable=False)
    wood_id = Column(ForeignKey('wood.id'), nullable=False)

    # parent relationships (access parent)
    supplier : Mapped["Supplier"] = relationship(back_populates=("SupplierWoodList"))
    wood : Mapped["Wood"] = relationship(back_populates=("SupplierWoodList"))

    # child relationships (access children)
