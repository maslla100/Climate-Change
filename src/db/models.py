from sqlalchemy import Column, Integer, Float
from src.db.database import Base

class GlobalMonthly(Base):
    __tablename__ = 'global_monthly'
    id = Column(Integer, primary_key=True, index=True)
    year = Column(Integer, nullable=False, index=True)
    jan = Column(Float, nullable=True)
    feb = Column(Float, nullable=True)
    mar = Column(Float, nullable=True)
    apr = Column(Float, nullable=True)
    may = Column(Float, nullable=True)
    jun = Column(Float, nullable=True)
    jul = Column(Float, nullable=True)
    aug = Column(Float, nullable=True)
    sep = Column(Float, nullable=True)
    oct = Column(Float, nullable=True)
    nov = Column(Float, nullable=True)
    dec = Column(Float, nullable=True)
    j_d = Column(Float, nullable=True)  # J-D column
    d_n = Column(Float, nullable=True)  # D-N column
    djf = Column(Float, nullable=True)  # DJF column
    mam = Column(Float, nullable=True)  # MAM column
    jja = Column(Float, nullable=True)  # JJA column
    son = Column(Float, nullable=True)  # SON column

class NorthernHemisphere(Base):
    __tablename__ = 'northern_hemisphere'
    id = Column(Integer, primary_key=True, index=True)
    year = Column(Integer, nullable=False, index=True)
    jan = Column(Float, nullable=True)
    feb = Column(Float, nullable=True)
    mar = Column(Float, nullable=True)
    apr = Column(Float, nullable=True)
    may = Column(Float, nullable=True)
    jun = Column(Float, nullable=True)
    jul = Column(Float, nullable=True)
    aug = Column(Float, nullable=True)
    sep = Column(Float, nullable=True)
    oct = Column(Float, nullable=True)
    nov = Column(Float, nullable=True)
    dec = Column(Float, nullable=True)
    j_d = Column(Float, nullable=True)  # J-D column
    d_n = Column(Float, nullable=True)  # D-N column
    djf = Column(Float, nullable=True)  # DJF column
    mam = Column(Float, nullable=True)  # MAM column
    jja = Column(Float, nullable=True)  # JJA column
    son = Column(Float, nullable=True)  # SON column

class SouthernHemisphere(Base):
    __tablename__ = 'southern_hemisphere'
    id = Column(Integer, primary_key=True, index=True)
    year = Column(Integer, nullable=False, index=True)
    jan = Column(Float, nullable=True)
    feb = Column(Float, nullable=True)
    mar = Column(Float, nullable=True)
    apr = Column(Float, nullable=True)
    may = Column(Float, nullable=True)
    jun = Column(Float, nullable=True)
    jul = Column(Float, nullable=True)
    aug = Column(Float, nullable=True)
    sep = Column(Float, nullable=True)
    oct = Column(Float, nullable=True)
    nov = Column(Float, nullable=True)
    dec = Column(Float, nullable=True)
    j_d = Column(Float, nullable=True)  # J-D column
    d_n = Column(Float, nullable=True)  # D-N column
    djf = Column(Float, nullable=True)  # DJF column
    mam = Column(Float, nullable=True)  # MAM column
    jja = Column(Float, nullable=True)  # JJA column
    son = Column(Float, nullable=True)  # SON column

class ZoneAnnual(Base):
    __tablename__ = 'zone_annual'
    id = Column(Integer, primary_key=True, index=True)
    year = Column(Integer, nullable=False, index=True)
    jan = Column(Float, nullable=True)
    feb = Column(Float, nullable=True)
    mar = Column(Float, nullable=True)
    apr = Column(Float, nullable=True)
    may = Column(Float, nullable=True)
    jun = Column(Float, nullable=True)
    jul = Column(Float, nullable=True)
    aug = Column(Float, nullable=True)
    sep = Column(Float, nullable=True)
    oct = Column(Float, nullable=True)
    nov = Column(Float, nullable=True)
    dec = Column(Float, nullable=True)
    j_d = Column(Float, nullable=True)  # J-D column
    d_n = Column(Float, nullable=True)  # D-N column
    djf = Column(Float, nullable=True)  # DJF column
    mam = Column(Float, nullable=True)  # MAM column
    jja = Column(Float, nullable=True)  # JJA column
    son = Column(Float, nullable=True)  # SON column
