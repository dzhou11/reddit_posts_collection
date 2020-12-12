import json
import requests
import pandas
import os.path as osp
from hw5.collect_fun import *
s1=["funny", "AskReddit", "gaming", "aww", "pics", "Music", "science", "worldnews", "videos", "todayilearned"]
s2=['AskReddit', 'memes', 'politics', 'nfl', 'nba', 'wallstreetbets', 'teenagers', 'PublicFreakout', 'leagueoflegends','unpopularopinion']

script_dir=osp.dirname(__file__)
#def get_posts(names):  # only get posts, dont write
#	num=100
#	posts=[]
	#name="funny"
#	for name in names:
#		data= requests.get(
#		content=data.json()['data']['children']
#		posts.extend(content)	
#	return posts
def main():
	sample1=get_posts(s1)
	sample2=get_posts(s2)
	
	path1=osp.join(script_dir,'..','data','sample1.json')
	path2=osp.join(script_dir,'..','data','sample2.json')
	with open(path1, 'w') as fp:
		fp.write(
		#'[' +
		'\n'.join(json.dumps(i) for i in sample1) # +
		#']\n'
		)
	with open(path2, 'w') as fp:
		fp.write(
		#'[' +
		'\n'.join(json.dumps(i) for i in sample2) # +
		#']\n'
		)
if __name__== '__main__':
	main()
