#!/usr/bin/python3
"""
This module defines the State class,
a sub class of the Base class
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
Base = declarative_base()


class State(Base):
    """This class is a sub class of the Base class"""
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)

    # Defines the one-to-many relationship with City
    cities = relationship("City", back_populates='state',
            casecade="all, delete-orphan")
