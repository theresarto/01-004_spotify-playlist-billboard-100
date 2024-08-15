import os
from dotenv import load_dotenv
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from bs4 import BeautifulSoup
from datetime import datetime

load_dotenv()

BILLBOARD_URL = "https://www.billboard.com/charts/hot-100/"
# SPOTIFY_API_ENDPOINT = "https://accounts.spotify.com/api/token"

# --------------------- SPOTIFY GET TOKEN ---------------------#
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=os.getenv("CLIENT_ID"),
        client_secret=os.getenv("CLIENT_SECRET"),
        redirect_uri="https://example.com",  # provided
        scope="playlist-modify-private",  # provided
        cache_path="token.txt",
        show_dialog=True,
        username=os.getenv("SPOTIFY_USERNAME")
    ))

user_id = sp.current_user()['id']
print(user_id)

# --------------------- PARSE BILLBOARD 100 ---------------------#
date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
# date = "1988-08-03"
year = date.split("-")[0]

response = requests.get(f"{BILLBOARD_URL}/{date}")
response.raise_for_status()
webpage = response.text

soup = BeautifulSoup(webpage, 'html.parser')
#

# --------------------- GET BILLBOARD 100 SONG LIST ---------------------#
songs = soup.select(selector='li>#title-of-a-story ')
song_list = [song.text.strip() for song in songs]
print(song_list)
print(len(song_list))


# --------------------- SEARCH SPOTIFY SONG URI ---------------------#

song_uri_list = []
for song in song_list:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    # print(result)
    try:
        # /tracks/items/0/uri
        song_uri = result["tracks"]["items"][0]["uri"]
        song_uri_list.append(song_uri)
    except IndexError:
        # print(f"'{song}' doesn't exist in Spotify. Skipping song.")
        pass

print(song_uri_list)
print(len(song_uri_list))


# --------------------- CREATE PLAYLIST ---------------------#

date_obj = datetime.strptime(date, "%Y-%m-%d")
formatted_date = date_obj.strftime("%d %b %Y")

playlist_name = f"{formatted_date} Billboard 100"
response = sp.user_playlist_create(
    user=user_id,
    name=playlist_name,
    public=False,
    description=f"This is a Spotify playlist of the Billboard 100 on {formatted_date}"
)

playlist_id = response["id"]
print(f"Spotify Playlist ID: {playlist_id}")


# --------------------- ADD TRACKS TO PLAYLIST ---------------------#

response = sp.playlist_add_items(
    playlist_id=playlist_id,
    items=song_uri_list
)