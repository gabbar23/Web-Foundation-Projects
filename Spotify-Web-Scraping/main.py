from os import name
import requests
from bs4 import BeautifulSoup
from requests.models import Response
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import dotenv_values


config = dotenv_values(".env")
client_id=config["CLIENT_ID"]
client_sec=config["CLIENT_SEC"]
redirect_uri=config["REDIRECT_URL"]

URL="https://www.billboard.com/charts/hot-100"
date=input("Which Year's Top song you want to get? Please Type in YYYY-MM-DD Format \n")
year=date.split("-")[0]

response=requests.get((f"{URL}/{date}"))
data=response.text
soup=BeautifulSoup(data,"html.parser")

songs_list=soup.find_all(name="span",class_="chart-element__information__song text--truncate color--primary")


final_output=[]
for song in songs_list:
    final_output.append(song.get_text())


sp=spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=client_id,
    client_secret=client_sec,
    redirect_uri=redirect_uri,
    scope="playlist-modify-private",
    cache_path="token.txt",
    show_dialog=True
))

user_id=(sp.current_user()["id"])

songs_uri=[]
for song in final_output:
    results = sp.search(q=f"track:{song} year:{year}",type='track')

    try:
       uri=(results["tracks"]["items"][0]["uri"])
       songs_uri.append(uri)
    except IndexError:
        print(f"This Track:{song} is not available on Spotify \n Skipped!")

playlist=sp.user_playlist_create(user=user_id,name=f"{date} top 100 Songs!",public=None )


sp.playlist_add_items(playlist_id=playlist["id"],items=songs_uri)