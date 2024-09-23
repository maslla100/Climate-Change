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
    glob = Column(Float, nullable=True)
    nhem = Column(Float, nullable=True)  # Northern Hemisphere
    shem = Column(Float, nullable=True)  # Southern Hemisphere
    n24_90n = Column(Float, nullable=True)  # 24N-90N
    s24_24n = Column(Float, nullable=True)  # 24S-24N
    s90_24s = Column(Float, nullable=True)  # 90S-24S
    n64_90n = Column(Float, nullable=True)  # 64N-90N
    n44_64n = Column(Float, nullable=True)  # 44N-64N
    n24_44n = Column(Float, nullable=True)  # 24N-44N
    equ_24n = Column(Float, nullable=True)  # EQU-24N
    s24_equ = Column(Float, nullable=True)  # 24S-EQU
    s44_24s = Column(Float, nullable=True)  # 44S-24S
    s64_44s = Column(Float, nullable=True)  # 64S-44S
    s90_64s = Column(Float, nullable=True)  # 90S-64S
