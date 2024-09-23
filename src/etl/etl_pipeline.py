import pandas as pd
from sqlalchemy import create_engine
import os

# Connect to PostgreSQL
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:your_password@localhost/climate_change")
engine = create_engine(DATABASE_URL)

def load_data():
    # Load cleaned data
    global_monthly = pd.read_csv('../data/cleaned/cleaned_globalmonthlyandseasonal.csv')
    northern_hemisphere = pd.read_csv('../data/cleaned/cleaned_northernhemisphere.csv')
    southern_hemisphere = pd.read_csv('../data/cleaned/cleaned_southernhemisphere.csv')
    zone_annual = pd.read_csv('../data/cleaned/cleaned_zoneannual.csv')

    # Load data into PostgreSQL
    global_monthly.to_sql('global_monthly', con=engine, if_exists='replace')
    northern_hemisphere.to_sql('northern_hemisphere', con=engine, if_exists='replace')
    southern_hemisphere.to_sql('southern_hemisphere', con=engine, if_exists='replace')
    zone_annual.to_sql('zone_annual', con=engine, if_exists='replace')

if __name__ == "__main__":
    load_data()
