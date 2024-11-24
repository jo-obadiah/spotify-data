import extract
import transform
import sqlalchemy
import pandas as pd 
from sqlalchemy.orm import sessionmaker
import requests
import json
from datetime import datetime
import datetime
import sqlite3

DATABASE_LOCATION = "sqlite:///my_played_tracks.sqlite"

if __name__ == "__main__":

#Importing the songs_df from the Extract.py
    load_df=extract.return_dataframe()
    if(transform.Data_Quality(load_df) == False):
        raise ("Failed at Data Validation")

engine = sqlalchemy.create_engine(DATABASE_LOCATION)
conn = sqlite3.connect('my_played_tracks.sqlite')
cursor = conn.cursor()

