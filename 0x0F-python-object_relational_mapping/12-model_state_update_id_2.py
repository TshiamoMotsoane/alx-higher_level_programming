#!/usr/bin/python3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sys import argv

if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    database = argv[3]

    engine = create_engine(f'mysql+mysqldb://{username}:
    {password}@localhost:3306/{database}')

    Base.metadata.bind = engine
    Session = sessionmaker(bind=engine)
    session = Session()
    state_to_update = session.query(State).get(2)
    if state_to_update:
        state_to_update.name = 'New Mexico'
        session.commit()

    session.close()
