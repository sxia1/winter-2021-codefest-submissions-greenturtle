from urllib.request import urlopen
from bs4 import BeautifulSoup as soup
import re
import dropbox
import csv
import time

KEY=""

def getcategories(memeLink, dbx):
	folders = []
	category_urls = []
	#categoryNames = []
	client = urlopen(memeLink)
	wholeHtml = client.read()
	souped = soup(wholeHtml, "html.parser")
	tb = souped.findAll("tbody", {"class":"entry-grid-body infinite"})
	trList = tb[0].findAll("tr")
	tds = []
	for i in trList:
		tds.append(i.findAll("td"))
	for each in tds:
		for i in each:
			try:
				i["colspan"]
			except KeyError:
				category_urls.append('https://knowyourmeme.com' + i.a["href"] + '/photos/sort/views')
				folders.append(i.a["href"])
				print(i.a["href"])
				#categoryNames.append(i.img["alt"])
	dbx.files_create_folder_batch(folders)
	return (folders, category_urls)

def getcategoryimages(category_url, folder, dbx, start=1, increment=5):
	print("\n")
	print(folder)
	for n in range(start, start+increment):
		client = urlopen(category_url + "/page/" + str(n))
		wholeHtml = client.read()
		souped = soup(wholeHtml, "html.parser")
		images = souped.findAll("div", {"class":"item"})
		
		# skip to next page if no images (avoid waiting 5s for blank pages)
		if len(images) == 0: 
			print("no images, continuing...")
			continue

		#upload all images to dropbox

		print("page {}, sleeping for 5s before uploading {} images".format(n, len(images)))
		time.sleep(5)

		for i in images:
			url = i.img["data-src"]
			filename = url.split("/")
			filename = filename[len(filename)-1]
			#filter out gifs
			if not url.endswith("gif") and not filename.startswith("long"):
				url = url.replace("masonry", "newsfeed")
				print(filename)

				try: 
					dbx.files_save_url(folder+"/"+filename, url)
					
				except Exception as e:
					print(e)

	print("\nfinished {}, sleeping for 15s".format(folder))
	time.sleep(15)

def driver(KEY):
	memeLink = "https://knowyourmeme.com/memes/popular/page/2"
	dbx = dropbox.Dropbox(KEY)
	result = getcategories(memeLink, dbx)
	folders = result[0]
	category_urls = result[1]
	for x in range(len(category_urls)-1):
		getcategoryimages(category_urls[x], folders[x], dbx, start=1, increment=5)

if __name__ == "__main__":
    driver(KEY)


