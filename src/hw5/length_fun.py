import json
import argparse

def load_json(fname):
	content=[]
	with open(fname, 'r') as content_file:
		for jsonObj in content_file:
			Dict = json.loads(jsonObj)
			content.append(Dict)
		#content = json.load(content_file)
	return content
def get_len(dic):
	return len(dic['data']['title'])
def avg_title(posts):
	acc=0
	for dic in posts:
		acc+=get_len(dic)
	return acc/len(posts)
