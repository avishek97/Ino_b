from src.db import Base
from sqlalchemy import Column, Integer, String

class UserModel(Base):
    __tablename__ = "user_details"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)
    confirm_password = Column(String)