import argparse
import json
import requests
import pandas

from hw5.clean_fun import *
#def load_data(filename):
#	import datetime
#	import re
#	with open(filename, 'r') as content_file:
#		content = content_file.readlines()
#	content = [w.replace('title_text', 'title') for w in content]
#	new=[]
#	for w in content:
#		if 'title' in w:
#			if (re.search(r'\{((.*)\:.*\,)*((.*)\:.*[^,])(}\\n|})$', w)) :
#				w=json.loads(w)
#				try:
#					t=datetime.datetime.strptime(w['createdAt'], "%Y-%m-%dT%H:%M:%S%z")
#				except:
#					continue
#				utc_time_value = t - t.utcoffset()
#				utc_dt = utc_time_value.replace(tzinfo=datetime.timezone.utc)
#				w['createdAt']=str(utc_dt)
#				new.append(w)
#	return new	


def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('-i',help='the input file')
	parser.add_argument('-o',help='the output file')
	

	args=parser.parse_args()
	
	inputfile=args.i
	outputfile=args.o	
	try:
		posts=load_data(inputfile)
	except:
		print("Cannot find the input file, please check the format:'python3 clean.py -i <input_file> -o <output_file>'")
	try:
		with open(outputfile, 'w') as fp:
			fp.write(
			#'[' +
			'\n'.join(json.dumps(i) for i in posts) #+
			#']\n'
			)

	except:
		print("please call this script with format 'python3 clean.py -i <input_file> -o <output_file>'")
if __name__== '__main__':
	main()
