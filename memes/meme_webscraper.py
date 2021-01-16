from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup as soup
import os
import re

def getcategories(memeLink):
	client = urlopen(memeLink)
	wholeHtml = client.read()
	souped = soup(wholeHtml, "html.parser")
	tb = souped.findAll("tbody", {"class":"entry-grid-body infinite"})
	trList = tb[0].findAll("tr")
	tds = []
	for i in trList:
		tds.append(i.findAll("td"))
	with open('categories.csv', 'a') as f:
		for each in tds:
			for i in each:
				try:
					i["colspan"]
				except KeyError:
					f.write(i.a["href"] + "\n")
					#print(i.a["href"])
	f.close()

def getcategoryimages(category_url, folder, page):
	print("\n")
	print(folder)
	client = urlopen(category_url + "/page/" + str(page))
	wholeHtml = client.read()
	souped = soup(wholeHtml, "html.parser")
	images = souped.findAll("div", {"class":"item"})
	
	# skip to next page if no images (avoid waiting 5s for blank pages)
	if len(images) == 0: 
		return
	
	for i in images:
		url = i.img["data-src"]
		print(url)
		filename = url.split("/")
		filename = filename[len(filename)-1]
		#filter out gifs
		if not url.endswith(("gif", "jpg_large")) and not filename.startswith(("long", "spoiler")) and "." in filename:
			url = url.replace("masonry", "newsfeed")
			urlretrieve(url, folder+"/"+filename)
			print(filename)

def driver():
	'''
	for x in range(55):
		memeLink = "https://knowyourmeme.com/categories/meme/page/"+str(x+1)+"?sort=images"
		getcategories(memeLink, dbx)
	'''
	with open('x.csv', 'r') as f:
		for line in f:
			folder = line.rstrip()
			category_url = "https://knowyourmeme.com/memes/" + folder + "/photos/sort/views"
			print(category_url)
			os.mkdir(folder)
			for i in range(1, 6):
				getcategoryimages(category_url, folder, i)

if __name__ == "__main__":
    driver()
