import pandas as pd
import requests
from datetime import datetime 
import datetime


user_id = 'pharaoh'
token = 'b61c32bd88d04ab8a01913c2b3e655b2'

def return_dataframes(token):
    input_variables = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": "bearer {token}".format(token = token) 
    }
    return input_variables


today = datetime.datetime.now()
yesterday = today - datetime.timedelta(days=1)
yesterday_unix_timestamp = int(yesterday.timestamp()) * 1000

# downloading the songs played yesterday
headers = return_dataframes(token)
url = "https://api.spotify.com/v1/me/player/recently-played?after={yesterday_unix_timestamp}"
r = requests.get(url, headers = headers)
if r.status_code == 200:
    pass
else:
    raise Exception(f"Failed to fetch data: {r.status_code}")
data = r.json()
    
if 'items' not in data:
    raise ValueError("No 'items' key in the response data.")
    
song_names = []
artist_names = []
played_at_list = []
timestamps = []

# Extracting the relevant piece of data from the json object
for song in data['items']:
    song_names.append(song['track']['name'])
    artist_names.append(song['track']['album']['artist'][0]['name'])
    played_at_list.append(song['played_at'])
    timestamps.append(song['played_at'][0:10])

    # Creating a dictionary to be converted to a Dataframe
    song_dict = {
    'song_name' : song_names,
    'artist_name' : artist_names,
    'played_at' : played_at_list,
    'timestamp' : timestamps
    }

      