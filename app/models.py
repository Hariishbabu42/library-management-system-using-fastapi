from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Text, String, Float

Base = declarative_base()

class Books(Base):

    __tablename__ = "Books"
    book_id = Column(Integer, primary_key=True)
    book_title = Column(String(255), nullable= False)
    book_description = Column(Text, nullable=True)
    category = Column(String, nullable=False)
    purchased_year = Column(String, nullable= False)
    price = Column(Float, nullable=False)
    availability = Column(String, default=True)

class Users(Base):
    __tablename__ = "Library_users"
    user_id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    department = Column(String, nullable=False)
    pending_dues = Column(Float, nullable=False)
    mobile_no = Column(String, nullable=False)

