#!/usr/bin/python3
"""
A script that lists all states from the database hbtn_0e_0_usa
"""


from sqlalchemy import create_engine
from model_state import Base, State
from model_city import City
from sqlalchemy.orm import sessionmaker
from sys import argv
if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    db_name = argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, db_name),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    quer = session.query(State, City).filter(State.id == City.state_id).order_by(City.id).all()
    for i, j in quer:
        print("{}: ({}) {}".format(i.name, j.id, j.name))
