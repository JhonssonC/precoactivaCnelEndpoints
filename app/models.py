from sqlalchemy import Column, Integer, String, Float
from .database import Base

class Sequence(Base):
    __tablename__ = "sequences"
    
    id = Column(String, primary_key=True, index=True)
    x = Column(Float, nullable=False)
    y = Column(Float, nullable=False)
    sequence = Column(String, nullable=False)
    descripcion = Column(String, nullable=False) 
    mru = Column(String, nullable=False)