import pandas as pd
from sqlalchemy import create_engine
import os

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///../data/local.db")

def load_data():
    engine = create_engine(DATABASE_URL)
    
    # Load datasets
    global_monthly = pd.read_csv('../data/cleaned/cleaned_globalmonthlyandseasonal.csv')
    southern_hemisphere = pd.read_csv('../data/cleaned/cleaned_southernhemisphere.csv')

    # Load data into database
    global_monthly.to_sql('global_monthly', con=engine, if_exists='replace')
    southern_hemisphere.to_sql('southern_hemisphere', con=engine, if_exists='replace')

if __name__ == "__main__":
    load_data()
