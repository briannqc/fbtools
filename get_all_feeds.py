import json
import os
import requests

def get_all_feeds():
    params = {
        'fields': 'message,name,description,created_time,updated_time,from,privacy,permalink_url,link,timeline_visibility,type',
        'access_token': os.environ['ACCESS_TOKEN'],
        'limit': 500
    }
    resp = requests.get('https://graph.facebook.com/v11.0/me/feed', params=params)
    resp_json = resp.json()
    with open('feeds/response_0.json', 'w') as my_file:
            json.dump(resp_json, my_file, indent=2)

    posts = resp.json()['data']
    all_posts = posts
    
    page = 0
    while ('paging' in resp_json) and ('next' in resp_json['paging']):
        page = page + 1
        next_page = resp_json['paging']['next']
        print('There are', len(posts), 'in this page, getting next page', page)
        resp = requests.get(next_page, params={'limit': 500})
        resp_json = resp.json()
        with open(f'feeds/response_{page}.json', 'w') as my_file:
            json.dump(resp_json, my_file, indent=2)

        posts = resp_json['data']
        all_posts.extend(posts)

    return all_posts


if __name__ == "__main__":
    posts = get_all_feeds()
    # FB has rate limit for application, cache the data for later use.
    with open('feeds/my_posts.json', 'w') as my_file:
        json.dump(posts, my_file, indent=2)