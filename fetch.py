#!/usr/bin/env python
#
# Fetch image usign SerpApi
#
from lib.google_search_results import GoogleSearchResults
import requests
import json
import wget
import os

# search images with SerpApi
#  the search on the keyword: apple is free of charge 
#   but any keyword required an api_key.
#
def get_batch(pageNumber):
    params = {
        "q" : "apple",
        "location" : "Dallas",
        "hl" : "en",
        "gl" : "us",
        #"google_domain" : "google.com",
        "api_key" : "demo",
        "tbm" : "isch",
        "ijn": pageNumber,
        "source": "test"
    }

    # TODO Switch to production
    query = GoogleSearchResults(params)
    data = query.get_dictionary()
    print(data)

    # extract link
    links = []
    for item in data['images_results']:
        print(item)
        links.append(item['original'])
    return links

# collect multiple batch
links = []
links += get_batch(0)
# need

# download images
print "download images"
for link in links:
	try:
		wget.download(link, 'data/')
		print("+")
	except:
		pass

# Let's classify our images into two groups
#  1- Apple Brand
#  2- Apple Fruit
# $> make classify

# Then we are ready to train the model
# $> make train
