import json
import os
import base64
import ssl
import smtplib
from email.message import EmailMessage
from requests import get, post
from pprint import pprint, pformat

client_id = os.environ.get("SPOTIFYCLIENTID")
client_secret = os.environ.get("SPOTIFYSECRETID")

def get_token():
    auth_string = client_id + ":" + client_secret
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")

    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": "Basic " + auth_base64,
        "Content-Type": "application/x-www-form-urlencoded"
    }

    data = {"grant_type": "client_credentials"}
    result = post(url, headers=headers, data=data)
    json_result = json.loads(result.content)
    token = json_result["access_token"]
    return token

def get_auth_header(token):
    return {"Authorization": "Bearer " + token}

def get_playlist(token, playlist_id):
    url = f"https://api.spotify.com/v1/playlists/{playlist_id}"
    headers = get_auth_header(token)

    result = get(url, headers=headers)
    json_result = json.loads(result.content)

    all_tracks = set()  

    for item in json_result['tracks']['items']:
        track = item['track']
        track_name = track['name']
        artists = ', '.join([artist['name'] for artist in track['artists']])
        track_info = f"Artists: {artists} | Track: {track_name}"
        
        all_tracks.add(track_info)  


    all_tracks_list = list(all_tracks)

    email_message = '\n'.join(all_tracks_list)
    send_email(email_message)
    print(email_message)

def send_email(email_message):

    username = os.environ.get("USERNAMEEMAIL")
    password = os.environ.get("PASSWORD")
    receiver = "Dandiggasmusic@gmail.com"


    context = ssl.create_default_context()

    email = EmailMessage()
    email.set_content(email_message)
    email["Subject"] = "NewMusicFriday"
    email["From"] = username
    email["To"] = receiver

    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(username, password)
        server.send_message(email)

    print("Email sent successfully")

token = get_token()
get_playlist(token, "37i9dQZF1DX4JAvHpjipBk")



