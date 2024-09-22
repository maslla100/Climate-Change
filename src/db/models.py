from sqlalchemy import Column, Integer, Float
from src.db.database import Base

class GlobalMonthly(Base):
    __tablename__ = 'global_monthly'
    
    id = Column(Integer, primary_key=True, index=True)
    year = Column(Integer)
    jan = Column(Float)
    feb = Column(Float)
    mar = Column(Float)
    apr = Column(Float)
    may = Column(Float)
    jun = Column(Float)
    jul = Column(Float)
    aug = Column(Float)
    sep = Column(Float)
    oct = Column(Float)
    nov = Column(Float)
    dec = Column(Float)
    j_d = Column(Float)  # J-D column
    d_n = Column(Float)  # D-N column
    djf = Column(Float)  # DJF column
    mam = Column(Float)  # MAM column
    jja = Column(Float)  # JJA column
    son = Column(Float)  # SON column
