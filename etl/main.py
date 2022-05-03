import requests 
import datetime 
import json
import pandas as pd
import logging

TOKEN = 'BQDzY7A4QDiFKHj8uOm5GH7Y3u2eQ-ba8Q_t1k4YzH0o-XBQ4-CvWoAu_gQNLpAM-emisxAQ1S8JIKY9L3k0Qbst1MYltX8GVdzYRI0CP0laq6gRhCdjxW5v3ilgLoFVQnk4mVyYNxB6dSWZHs4f4GxDt-fD_pOUD1I2'
logger = logging.getLogger()
headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "Authorization": "Bearer {token}".format(token=TOKEN)
}

def check_data(df:pd.DataFrame) -> bool:
    # Check if the df is empty
    if df.empty: 
        logger.info("No song dowloaded, Finished execution")
        return False

    # Primary Key Check
    if df['Playing Time'].is_unique:
        pass
    else: 
        raise Exception('Primary Key Check is violated')
    
    #Check if any value in the no None columns is None 
    if df[['Song Name', 'Album Name', 'Artist Name',  'Url Songs','Url Artists', 'Url Albums','Playing Time', 'Images']].isnull().values.any():
        raise Exception('Some values no allow are None')

    return True 
    

def to_df(data):
    song_names = []
    album_names = []
    artist_names = []
    url_playlists = []
    url_songs = []
    url_artists = []
    url_albums = []
    playing_time = []
    images = []

    for song in data['items']:
        song_names.append(song['track']['name'])
        album_names.append(song['track']['album']['name'])
        artist_names.append(song['track']['album']['artists'][0]['name'])
        try:
            url_playlists.append(song['context']['external_urls']['spotify'])
        except TypeError:
            url_playlists.append(None)
        url_songs.append(song['track']['external_urls']['spotify'])
        url_artists.append(song['track']['artists'][0]['external_urls']['spotify'])
        url_albums.append(song['track']['album']['external_urls']['spotify'])
        playing_time.append(song['played_at'])
        images.append(song['track']['album']['images'][0]['url'])

    song_dict = {
    'Song Name':song_names,
    'Album Name':album_names,
    'Artist Name':artist_names,
    'Url Playlist':url_playlists,
    'Url Songs':url_songs,
    'Url Artists':url_artists,
    'Url Albums':url_albums,
    'Playing Time':playing_time,
    'Images':images
    }

    df = pd.DataFrame(song_dict)
    return df


def transform(data):
    df = to_df(data)
    if check_data(df):
        logger.info('Data valid, proceed to load stage')
    print(df.shape)


def extract():
    today = datetime.datetime.now()
    yesterday = today - datetime.timedelta(days=1)
    yesterday_unix_timestamp = int(yesterday.timestamp()) * 1000

    r = requests.get("https://api.spotify.com/v1/me/player/recently-played?limit=50&after={time}".format(time=yesterday_unix_timestamp), headers=headers)
    data = r.json()
    transform(data)


if __name__ == "__main__":
    extract()