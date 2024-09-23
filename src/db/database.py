from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# Pull DATABASE_URL from environment variable
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:@localhost/climate_change")

# Create the database engine
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Import models
from src.db.models import GlobalMonthly, NorthernHemisphere, SouthernHemisphere, ZoneAnnual

# Dependency to get the DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create tables if they don't exist
Base.metadata.create_all(engine)

print("Tables have been created successfully!")
