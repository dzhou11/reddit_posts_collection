import argparse
import json
import requests
import pandas

def load_data(filename):
	import datetime
	import re
	with open(filename, 'r') as content_file:
		content = content_file.readlines()
	content = [w.replace('title_text', 'title') for w in content]
	new=[]
	for w in content:
		if 'title' in w:
			if (re.search(r'\{((.*)\:.*\,)*((.*)\:.*[^,])(}\\n|})$', w)) :
				w=json.loads(w)
				try:
					t=datetime.datetime.strptime(w['createdAt'], "%Y-%m-%dT%H:%M:%S%z")
				except:
					continue
				utc_time_value = t - t.utcoffset()
				utc_dt = utc_time_value.replace(tzinfo=datetime.timezone.utc)
				w['createdAt']=utc_dt.strftime('%Y-%m-%dT%H:%M:%S%z')
				new.append(w)
	return new	
