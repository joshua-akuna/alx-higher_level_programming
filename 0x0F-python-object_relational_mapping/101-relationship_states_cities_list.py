#!/usr/bin/python3
"""
The script lists all State objects, and correspoding city objects,
contained in the database hbtn_0e_101_usa
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

        rs = session.query(State).order_by(State.id).all()

        for row in rs:
            print('{}: {}'.format(row.id, row.name))
            for city in row.cities:
                print('    {}: {}'.format(city.id, city.name))

        session.close()
