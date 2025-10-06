from sqlalchemy import Column, Integer, String
from App.Database import Base

# Mapping class object to MySQL table
class User(Base):
    __tablename__="users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    email = Column(String(50), unique=True, index=True, nullable=False)
    password = Column(String(50), nullable=False)