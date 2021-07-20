import json
import os
import requests

def get_all_albums():
    params = {
        'fields': 'count,link,privacy,type,photos{images,album,link},name,from,location,updated_time,description,picture',
        'access_token': os.environ['ACCESS_TOKEN'],
        'limit': 500
    }
    resp = requests.get('https://graph.facebook.com/v11.0/me/albums', params=params)
    resp_json = resp.json()
    with open('albums/response_0.json', 'w') as my_file:
            json.dump(resp_json, my_file, indent=2)

    albums = resp.json()['data']
    all_albums = albums
    
    page = 0
    while ('paging' in resp_json) and ('next' in resp_json['paging']):
        page = page + 1
        print('There are', len(albums), 'in this page, getting next page', page)

        next_page = resp_json['paging']['next']
        resp = requests.get(next_page, params={'limit': 500})
        resp_json = resp.json()
        with open(f'albums/response_{page}.json', 'w') as my_file:
            json.dump(resp_json, my_file, indent=2)

        albums = resp_json['data']
        all_albums.extend(albums)

    return all_albums


if __name__ == "__main__":
    albums = get_all_albums()
    # FB has rate limit for application, cache the data for later use.
    with open('albums/my_albums.json', 'w') as my_file:
        json.dump(albums, my_file, indent=2)