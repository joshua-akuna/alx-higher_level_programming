#!/usr/bin/python3
"""
The script prints all thee city objects from the database hbtn_0e_14_usa
"""
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    if len(sys.argv) == 4:
        fmt = 'mysql+mysqldb://{}:{}@localhost/{}'
        engine = create_engine(
                fmt.format(sys.argv[1], sys.argv[2], sys.argv[3]),
                pool_pre_ping=True
        )
        Base.metadata.create_all(engine)

        Session = sessionmaker(bind=engine)
        session = Session()

        new_state = State()
        new_state.name = 'California'
        new_city = City(name='San Francisco')
        new_state.cities.append(new_city)

        session.add(new_state)
        session.add(new_city)
        session.commit()

        session.close()
