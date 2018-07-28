from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String


engine = create_engine('sqlite:///student.db', echo=True)
Base = declarative_base()