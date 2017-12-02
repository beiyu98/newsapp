from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# base orm class object
Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    id = Column(String(20), primary_key=True)
    name = Column(String(20))
    password = Column(String(20))


engine = create_engine("sqlite:///news.db", echo=True, convert_unicode=True)
DBSession = sessionmaker(bind=engine)
