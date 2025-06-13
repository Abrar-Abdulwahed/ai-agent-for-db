import os
from dotenv import load_dotenv
import pandas as pd

from sqlalchemy import create_engine

# create a db from csv file
database_file_path = "./db/salary.db"


# Create an engine to connect to the SQLite database
# SQLite only requires the path to the database file
engine = create_engine(f"sqlite:///{database_file_path}")
file_url = "./data/salaries_2023.csv"
os.makedirs(os.path.dirname(database_file_path), exist_ok=True)
df = pd.read_csv(file_url).fillna(value=0)
df.to_sql("salaries_2023", con=engine, if_exists="replace", index=False)