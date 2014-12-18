from bs4 import BeautifulSoup
from urllib.request import urlopen

invalids = ['#', '.ogg', '/wiki/Help:']

def first_valid(par_links):
	for elem in par_links:
		link = elem['href']
		if link[0] in invalids or link[-4:] in invalids or link[:11] in invalids :
			continue
		else:
			extracted_link = link
			print(extracted_link[6:])
			return extracted_link
	return ""



def first_link(source_url):
	source_content = urlopen(source_url)
	source_html = source_content.read()
	soup = BeautifulSoup(source_html)

	''' 
	Creates list of all paragraphs on page, and searches each one for links.
	First link encountered is stored into extracted_link and break out of loop.
	First link cannot being with '#' (wiki internal citation)
	'''
	extracted_link = ""
	abstract = soup.find("div", {"class" : "mw-content-ltr"})
	for div in abstract.find_all("div"):
		div.clear()
	abstract = soup.find_all('p') 			
	for par in abstract:
		par_links = par.find_all('a', href = True)
		extracted_link = first_valid(par_links)
		if extracted_link:
			break

	''' 
	Build full link and return
	'''
	if not extracted_link:
		print("NO LINK FOUND")
	else:	
		source_url = "http://en.wikipedia.org" + extracted_link
		return source_url



working_url = input("Enter link to a valid wikipedia article: ")
while (working_url != "http://en.wikipedia.org/wiki/Philosophy"):
	working_url = first_link(working_url)
	print("**", working_url,"\n")
