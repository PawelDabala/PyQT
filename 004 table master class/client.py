from sqlalchemy import Column, String, Integer
from base import Base




class Client(Base):
    __tablename__ = 'client'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)

    
    def __init__(self, name):
        self.name = name
        
    def __str__(self):
        return f'{self.name}'
    
    