#!/usr/bin/python3
"""
The script changes the name of a State object from
the database hbtn_0e_6_usa.
"""
import sys
from model_state import Base, State
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

        state = session.query(State).filter_by(id=2).first()
        if state:
            state.name = 'New Mexico'

        session.commit()
        session.close()
