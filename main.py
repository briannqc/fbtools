import json
import numpy as np
import webbrowser as wb


def process_feeds():
    posts = {}
    with open('feeds/my_posts.json', 'r') as my_file:
        posts = json.load(my_file)
    not_self_posts = [x for x in posts if (x['privacy']['value'] != '' and x['privacy']['value'] != 'SELF')]
    with open('feeds/my_not_self_posts.json', 'w') as my_file:
        json.dump(not_self_posts, my_file, indent=2)

    new_size = len(not_self_posts) if len(not_self_posts)%5 == 0 else (len(not_self_posts)//5 + 1) * 5
    not_self_posts_2D = np.resize(not_self_posts, new_size).reshape(-1, 5)
    for window in not_self_posts_2D:
        for p in window:
            wb.open(p['permalink_url'])
        input("Press enter to continue...")


def process_albums():
    albumns = {}
    with open('albums/my_albums.json', 'r') as my_file:
        albumns = json.load(my_file)
    not_self_albums = [x for x in albumns if x['privacy'] != 'custom']
    with open('albums/not_self_albums.json', 'w') as my_file:
        json.dump(not_self_albums, my_file, indent=2)

    new_size = len(not_self_albums) if len(not_self_albums)%5 == 0 else (len(not_self_albums)//5 + 1) * 5
    not_self_albums_2D = np.resize(not_self_albums, new_size).reshape(-1, 5)
    for window in not_self_albums_2D:
        for p in window:
            wb.open(p['link'])
        input("Press enter to continue...")


if __name__ == "__main__":
    process_feeds()
    process_albums()