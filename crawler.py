#Author: john@johnwesly.net

# import urllib on Python3
import urllib.parse
import urllib.request
from bs4 import BeautifulSoup

url = "http://www.boston.com"

urls = [url] #stack of urls
visited = [url] #historic record of urls

f = open('visited.txt','w')
while len(urls) > 0:
	try:
		htmltext = urllib.request.urlopen(urls[0]).read()
		decodedurl = urllib.parse.unquote(urls[0])			
		visited.append(decodedurl)
		print("==============> {} " . format(len(visited)))
		f.write("===========================================\n")
		f.write(decodedurl+'\n')
		f.write("===========================================\n")
	except:
		print(urls[0])
	soup = BeautifulSoup(htmltext, "html.parser")

	urls.pop(0)
	print(len(urls))

	for tag in soup.findAll('a',href=True):
		tag['href'] = urllib.parse.urljoin(url,tag['href'])
		if url not in tag['href'] and tag['href'] not in visited:
			urls.append(tag['href'])	
			decodedurl = urllib.parse.unquote(tag['href'])	
			f.write(decodedurl+'\n')

f.close()