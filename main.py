import json
import os
import base64
from requests import get, post

client_id = "**"
client_secret = "**"


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
#    print(json_result)

    for item in json_result['tracks']['items']:
        track = item['track']
        track_name = track['name']
        artists = ', '.join([artist['name'] for artist in track['artists']])
        print(f"Track: {track_name} | Artists: {artists}")


token = get_token()
get_playlist(token, "**")

print(token)