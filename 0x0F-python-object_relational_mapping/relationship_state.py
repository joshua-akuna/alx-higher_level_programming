#!/usr/bin/python3
"""
This module defines the State class,
a sub class of the Base class
"""
from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

_metadata = MetaData()
Base = declarative_base(metadata=_metadata)


class State(Base):
    """This class is a sub class of the Base class"""
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    # Defines the one-to-many relationship with City
    cities = relationship("City", backref="states")
