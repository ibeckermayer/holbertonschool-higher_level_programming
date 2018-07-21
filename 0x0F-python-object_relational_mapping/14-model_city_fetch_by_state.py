#!/usr/bin/python3
"""
List all State objects with a
"""
if __name__ == "__main__":
    import sys
    from model_state import Base, State
    from model_city import City
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    mysql = 'mysql+mysqldb://{}:{}@localhost:3306/{}'
    engine = create_engine(mysql.format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State, City).filter(State.id == City.state_id)
    for s, c in states.order_by(City.id).all():
        print("{:s}: ({:d}) {:s}".format(s.name, c.id, c.name))
