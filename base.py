from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from engine import engine

Session = sessionmaker(bind=engine)

Base = declarative_base()
