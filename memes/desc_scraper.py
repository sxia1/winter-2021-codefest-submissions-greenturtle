from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup as soup
import os
import re
import json

def getcategoryimages(dct, category_url, folder):
	print(folder)
	client = urlopen(category_url)
	wholeHtml = client.read()
	souped = soup(wholeHtml, "html.parser")
	# name = souped.findAll("meta", {"property":"og:title"}) # gave me a bunch of random shit 
	# name = souped.findAll("title") # good alternative 
	name = souped.title.string
	name = name.replace("Know Your Meme","").replace("|","").strip()
	description = souped.findAll("meta", {"name":"description"})
	# print(name)
	# print(description[0]['content'])

	dct[folder]={"name": name, "description": description[0]['content']}

	with open('categories.csv', 'a') as f:
		f.write(folder + "\t" + name + "\t" + description[0]['content'] + "\n")
	f.close()

	## print(folder, dct[folder])


def driver():

	dct = {}

	with open('x.csv', 'r') as f:
		for line in f:
			folder = line.rstrip()
			category_url = "https://knowyourmeme.com/memes/" + folder # + "/photos/sort/views"
			print("\n")
			print(category_url)
			getcategoryimages(dct, category_url, folder)

	with open('categories.json', 'w') as f:
		json.dump(dct, f)

	
if __name__ == "__main__":
	driver()
