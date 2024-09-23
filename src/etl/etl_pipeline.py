import os
import sys
import pandas as pd
from sqlalchemy import create_engine

# Add the project root to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

# Import Base after ensuring the path is added
from src.db.database import Base

# Connect to PostgreSQL
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:@localhost/climate_change")
engine = create_engine(DATABASE_URL)

# Create tables if they don't exist (this uses your models to create the schema)
Base.metadata.create_all(engine)

def load_data():
    try:
        # Construct absolute paths to the cleaned data files
        base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../data/cleaned'))
        
        global_monthly_path = os.path.join(base_path, 'cleaned_globalmonthlyandseasonal.csv')
        northern_hemisphere_path = os.path.join(base_path, 'cleaned_northernhemisphere.csv')
        southern_hemisphere_path = os.path.join(base_path, 'cleaned_southernhemisphere.csv')
        zone_annual_path = os.path.join(base_path, 'cleaned_zoneannual.csv')

        # Load cleaned data using absolute paths
        global_monthly = pd.read_csv(global_monthly_path)
        northern_hemisphere = pd.read_csv(northern_hemisphere_path)
        southern_hemisphere = pd.read_csv(southern_hemisphere_path)
        zone_annual = pd.read_csv(zone_annual_path)

        # Normalize column names to match database schema (lowercase, replace hyphens with underscores)
        global_monthly.columns = global_monthly.columns.str.lower().str.replace('-', '_')
        northern_hemisphere.columns = northern_hemisphere.columns.str.lower().str.replace('-', '_')
        southern_hemisphere.columns = southern_hemisphere.columns.str.lower().str.replace('-', '_')
        zone_annual.columns = ['year', 'glob', 'nhem', 'shem', 'n24_90n', 's24_24n', 's90_24s', 'n64_90n', 'n44_64n', 'n24_44n', 'equ_24n', 's24_equ', 's44_24s', 's64_44s', 's90_64s']

        # Append data to existing tables (to avoid replacing the table structure)
        global_monthly.to_sql('global_monthly', engine, index=False, if_exists='append', chunksize=1000)
        northern_hemisphere.to_sql('northern_hemisphere', engine, index=False, if_exists='append', chunksize=1000)
        southern_hemisphere.to_sql('southern_hemisphere', engine, index=False, if_exists='append', chunksize=1000)
        zone_annual.to_sql('zone_annual', engine, index=False, if_exists='append', chunksize=1000)

        print("Data has been successfully loaded into PostgreSQL!")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    load_data()

