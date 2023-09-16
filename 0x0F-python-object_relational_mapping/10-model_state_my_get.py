#!/usr/bin/python3
"""
The script lists all the State object with the *name* passed
as argument from the database hbtn_0e_6_usa.
"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    if len(sys.argv) == 5:
        fmt = 'mysql+mysqldb://{}:{}@localhost/{}'
        engine = create_engine(
                fmt.format(sys.argv[1], sys.argv[2], sys.argv[3]),
                pool_pre_ping=True
        )
        Base.metadata.create_all(engine)

        Session = sessionmaker(bind=engine)
        session = Session()

        state = session.query(State).filter(
                State.name == sys.argv[4]).one_or_none()
        if state:
            print(state.id)
        else:
            print('Not found')

        session.close()
