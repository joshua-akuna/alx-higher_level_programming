#!/usr/bin/python3
"""
The script prints all city objects from the database hbtn_0e_14_usa
"""
import sys
from model_state import Base, State
from model_city import City
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

        rs = session.query(State.name, City.id, City.name).filter(
                State.id == City.state_id).order_by(City.id).all()

        for row in rs:
            print('{}: ({}) {}'.format(row[0], row[1], row[2]))

        session.close()
