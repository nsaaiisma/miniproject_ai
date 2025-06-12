
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Ganti dengan client ID dan secret dari Spotify Developer Dashboard
client_id = '36081acc93f449879852bb4c2b700bfc'
client_secret = 'c484f3eb560946c097cf05a11b2764a3'

auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(auth_manager=auth_manager)

def search_song_by_pitch(keyword):

    results = sp.search(q=keyword, type='track', limit=5)
    return results['tracks']['items']
