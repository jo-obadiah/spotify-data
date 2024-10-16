import pandas as pd
import requests
import datetime
from datetime import datetime 

user_id = 'pharaoh'
token = 'b61c32bd88d04ab8a01913c2b3e655b2'

def return_dataframe():
    headers = {
        "Accept" : "application/json"
        'Content-Type' : "application/json"
        'Authorization' : "bearer{token}".format(token = token)
    }

today = datetime.datetime.now()
yesterday = today - datetime.timedelta(days=1)
yesterday_unix_timestamp = int(yesterday.timestamp()) * 1000

# downloading the songs played yesterday
r = requests.get("https://api.spotify.com/v1/me/player/recently-played?after={time}".format(time=yesterday_unix_timestamp), headers = headers")

data = r.json()
song_names = []
artist_names = []
played_at_list = []
timestamp = []

# Extracting the relevant piece of data from the json object
for song in data['items']: