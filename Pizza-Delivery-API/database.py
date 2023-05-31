from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine('postgresql://p10:123@localhost/pizza_db', echo=True)

Base = declarative_base()

Session = sessionmaker()
