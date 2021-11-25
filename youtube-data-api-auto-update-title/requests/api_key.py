import requests
import json

from requests import api

api_key = 'AIzaSyCr3TDnPccQDPdBBBBpdC-DAu5bIfdWhdM'
base_url = 'https://www.googleapis.com/youtube/v3/'
complete_videos_url = f'{base_url}videos?id=jGN0cjQNgJc&part=snippet&part=statistics&key={api_key}'

response = requests.get(complete_videos_url)
json_response = response.json()

titulo = json_response['items'][0]['snippet']['title']
id = json_response['items'][0]['id']
views = '{:,}'.format(int(json_response["items"][0]["statistics"]["viewCount"])).replace(',', '.')
comments = '{:,}'.format(int(json_response['items'][0]['statistics']['commentCount'])).replace(',', '.')
likes = '{:,}'.format(int(json_response['items'][0]['statistics']['likeCount'])).replace(',', '.')
dislikes = '{:,}'.format(int(json_response['items'][0]['statistics']['dislikeCount'])).replace(',', '.')
channel = json_response["items"][0]

print('\n', 'Vídeo', '\n', sep='')
print('Título:', titulo)
print('ID:', id)
print('Visualizações:', views)
print('Comentários', comments)
print('Gosteis:', likes)
print('Não-gosteis', dislikes)

complete_channels_url = f'{base_url}channels?id={channel["snippet"]["channelId"]}&part=contentDetails&part=snippet&key={api_key}'
response = requests.get(complete_channels_url)
json_response = response.json()

channel = json_response["items"][0]

channel_name = json_response['items'][0]['snippet']['title']

print()
print('Canal', '\n')
print('Nome:', channel_name)
print('Playlists:')

complete_playlists_url = f'{base_url}playlists?channelId={channel["id"]}&maxResults=50&part=snippet&key={api_key}'
response = requests.get(complete_playlists_url)
json_response = response.json()

for playlist in json_response['items']:
    print(playlist['snippet']['title'], f'({playlist["id"]})')

complete_playlistItems_url = f'{base_url}playlistItems?playlistId={channel["contentDetails"]["relatedPlaylists"]["uploads"]}&part=snippet&maxResults=50&part=contentDetails&key={api_key}'
response = requests.get(complete_playlistItems_url)
json_response = response.json()

print()
print('Uploads', '\n')
for video in json_response['items']:
    print(video['snippet']['title'], video['snippet']['resourceId']['videoId'])

response = requests.get(f'{base_url}?channelsv?mine=true&key={api_key}')
print(response.status_code)
