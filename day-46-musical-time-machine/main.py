import requests
from bs4 import BeautifulSoup
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth

SPOTIFY_ID = os.getenv("SPOTIFY_ID")
SPOTIFY_SECRET = os.getenv("SPOTIFY_SECRET")
SPOTIFY_REDIRECT_URL = os.getenv("SPOTIFY_REDIRECT_URL")

# ----------------------Get HOT 100 songs from Billboard according to user's input date-------------------------#
URL = "https://www.billboard.com/charts/hot-100"
date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
response = requests.get(f"{URL}/{date}")
soup = BeautifulSoup(response.text, "html.parser")
titles_html = soup.select(selector="ul li h3")
song_titles = [title.getText().strip() for title in titles_html][:100]
# print(song_titles)

# ----------------------Connect to Spotify and Get User id-------------------------#
auth = SpotifyOAuth(
    client_id=SPOTIFY_ID,
    client_secret=SPOTIFY_SECRET,
    redirect_uri=SPOTIFY_REDIRECT_URL,
    scope="playlist-modify-private",
    show_dialog=True
)
sp = spotipy.Spotify(auth_manager=auth)
user_id = sp.current_user()["id"]
# print(user_id)

# ----------------------Search song uri from connected spotify-------------------------#
song_uris = []
year = date.split("-")[0]
for song in song_titles:
    results = sp.search(q=f"track:{song} year:{year}", type="track", limit=1)
    try:
        uri = results["tracks"]["items"][0]['uri']
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

# ----------------------Create playlist and add songs-------------------------#
# print(song_uri)
playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
