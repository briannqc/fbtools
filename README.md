# About

If you have been using Facebook for years like me, you have probably posted many many posts. You wish Facebook
has a magic `Change all my posts' privacy to ONLY ME` button. Unfortunately, Mark and his team will never
give us such button and kill themselves.

This tool helps you download your facebook feeds and albums, filter out non-only-me (such as public, friends and
custom) posts, it then iterates these posts, gives you a chance to review your 'abandoned' posts. You can either
delete your posts, make them 'Only Me' or simply leave them there if you want to.

# TODO
This oversimplified tool is not fully automated yet, I couldn't find any API to change post's privacy programmatically.

# Usage
## Generate Access Token

**Prerequisite** You must be a Facebook developer first, but it just takes you a few clicks to become a FB developer.

To generate an access token, you can go to [Graph API Explorer](https://developers.facebook.com/tools/explorer/).
Your token should have `users_posts` and `users_photos` permission.

Once you have your access token, you should set it to `ACCESS_TOKEN` environment variable:

```shell
export ACCESS_TOKEN=EAACipnvwd*********************yRJRZAn6Uksx
```

## Download your data
Facebook set rate limit for every app, you should better download your data offline first. The offline data will also
save you time.

```shell
# Download posts
python3 get_all_feeds.py

# Download albums
python3 get_all_albums.py

# Process your data
python3 main.py
```
