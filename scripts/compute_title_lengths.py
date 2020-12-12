import json
import argparse
from hw5.length_fun import *
#def load_json(fname):
#	content=[]
#	with open(fname, 'r') as content_file:
#		for jsonObj in content_file:
#			Dict = json.loads(jsonObj)
#			content.append(Dict)
#		#content = json.load(content_file)
#	return content
#def get_len(dic):
#	return len(dic['data']['title'])
#def avg_title(posts):
#	acc=0
#	for dic in posts:
#		acc+=get_len(dic)
#	return acc/len(posts)
	
def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('file',help='the .json file you want to compute title length.')
	args=parser.parse_args()
	
	posts=load_json(args.file)
	r=avg_title(posts)
	print(r)
	return r

if __name__== '__main__':
	main()
