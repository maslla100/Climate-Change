from sqlalchemy import Column, Integer, String, Float
from src.db.database import Base

class GlobalMonthly(Base):
    __tablename__ = 'global_monthly'
    id = Column(Integer, primary_key=True, index=True)
    year = Column(Integer)
    jan = Column(Float)
    feb = Column(Float)
    mar = Column(Float)
    # Add the rest of your columns here
