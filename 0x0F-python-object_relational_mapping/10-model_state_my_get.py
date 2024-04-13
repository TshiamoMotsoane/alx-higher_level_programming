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
    State = session.query(State).filter(State.name == state_name_to_search).first()
    if state:
        print(f"{state.id}: {state.name}")
    else:
        print("Not found")

    session.close()
