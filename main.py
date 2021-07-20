import json
import numpy as np
import webbrowser as wb
import pylab as pl
import pandas as pd
from dateutil.parser import parse
import pytz
from collections import Counter


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


def stat():
    posts = {}
    with open('feeds/my_posts.json', 'r') as my_file:
        posts = json.load(my_file)
    
    vnt = pytz.timezone('Asia/ho_chi_minh')
    def created_time_of(post):
        time_str = post['created_time']
        time = parse(time_str)
        time_vnt = time.astimezone(vnt)
        return (time_vnt.year, time_vnt.hour)

    created_time = list(map(lambda p: created_time_of(p), posts))
    counter = Counter(created_time)
    activities = [[key, counter[key]] for key in counter]
    activities = dict((v[0], v[1]) for v in activities)
    
    fulfilled_activivites = []
    for y in range(2010, 2022):
        for h in range(0, 24):
            feed = 0
            if (y, h) in activities:
                feed = activities[(y, h)]
            fulfilled_activivites.append((y, h, feed))

    year = list(map(lambda t: t[0], fulfilled_activivites))
    hour = list(map(lambda t: t[1], fulfilled_activivites))
    activity = list(map(lambda t: t[2], fulfilled_activivites))
    df = pd.DataFrame({"Hour": hour, "Year": year, "Activity": activity})

    # reshape the data and plot it
    df2 = df.pivot(columns="Year", index="Hour", values="Activity")
    df2.fillna(0, inplace=True)
    print(df2)

    Hour, Year = np.mgrid[:df2.shape[0]+1, :df2.shape[1]+1]
    _, ax = pl.subplots(figsize=(12, 4))
    ax.set_aspect("equal")

    ax.set_yticks(np.arange(len(df2.columns))+0.5)
    ax.set_yticklabels(df2.columns)
    ax.set_xticks(np.arange(len(df2.index))+0.5)
    ax.set_xticklabels(df2.index)

    pl.pcolormesh(Hour, Year, df2.values, cmap="Greens", edgecolor="w", vmin=0, vmax=30)
    pl.show()


if __name__ == "__main__":
    # process_feeds()
    # process_albums()
    stat()
