#!/usr/bin/python3
"""
List all State objects
"""
if __name__ == "__main__":
    import sys
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    mysql = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(sys.argv[1],
                                                             sys.argv[2],
                                                             sys.argv[3])
    engine = create_engine(mysql)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    first = session.query(State).first()
    if first is None:
        print("Nothing")
    else:
        print("{:d}: {:s}".format(first.id, first.name))
