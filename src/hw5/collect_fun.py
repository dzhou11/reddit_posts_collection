import json
import requests
import pandas
import os.path as osp
s1=["funny", "AskReddit", "gaming", "aww", "pics", "Music", "science", "worldnews", "videos", "todayilearned"]
s2=['AskReddit', 'memes', 'politics', 'nfl', 'nba', 'wallstreetbets', 'teenagers', 'PublicFreakout', 'leagueoflegends','unpopularopinion']

script_dir=osp.dirname(__file__)
def get_posts(names):  # only get posts, dont write
	num=100
	posts=[]
	#name="funny"
	for name in names:
		data= requests.get(f'http://api.reddit.com/r/{name}/new?limit={num}',
					 headers={'User-Agent' : 'windows: requests (by /u/druths)'})
		content=data.json()['data']['children']
		posts.extend(content)
	return posts
