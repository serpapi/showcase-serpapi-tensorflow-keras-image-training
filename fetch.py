#!/usr/bin/env python
#
# fetch image from serpapi
#
# TODO need feature to be release in production to enable plugin
#from lib.google_search_results import GoogleSearchResults
import requests
import json
import wget
import os

#import httplib

def get_batch(pageNumber):
    params = {
        "q" : "apple",
        "location" : "Dallas",
        "hl" : "en",
        "gl" : "us",
        #"google_domain" : "google.com",
        #"api_key" : "demo",
        "tbm" : "isch",
        "ijn": pageNumber,
        "source": "test"
    }

    # TODO Switch to production
    # query = GoogleSearchResults(params)
    # data = query.get_dictionary()
    # print(data)

    # search serp API
    rsp = requests.get("http://web:3000/search", params)
    data = json.loads(rsp.text)

    # extract link
    links = []
    for item in data['images_results']:
        print(item)
        links.append(item['original'])
    return links

# collect multiple batch
links = []
links += get_batch(0)

# download images
print "download images"
for link in links:
	try:
		wget.download(link, 'data/')
		print("+")
	except:
		pass

# Delete bad images
#os.remove("data/apple-1024x440.jpg")
#print("all images download in data/")


# Let's train the model now.
# $> make train
