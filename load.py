import Extract
import Transform
import sqlalchemy
import pandas as pd 
from sqlalchemy.orm import sessionmaker
import requests
import json
from datetime import datetime
import datetime
import sqlite3


if __name__ == "__main__":

#Importing the songs_df from the Extract.py
    load_df=Extract.return_dataframe()
    if(Transform.Data_Quality(load_df) == False):
        raise ("Failed at Data Validation")