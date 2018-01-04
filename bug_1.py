from urllib.request import urlopen
from urllib.request import Request
import urllib.error
import json

def download(url,user_agent='wswp',num_retries=2):
	print("Downloading:"+url)
	headers = {'User-agent':user_agent}
	request = Request(url,headers=headers)
	
	try:
		html = urlopen(request).read()
	except urllib.error.URLError as e:
		print("Downloading Error:"+e.reason)
		html = None
		if num_retries > 0:
			if getattr(e,'code',None) and 500 <= e.code < 600:
				return download(url,num_retries-1)
	return html
	
	
				
url_name = input("url:")

with open("lala2.html",'w') as fw:
	fw.write(download(url_name).decode("utf-8"))
