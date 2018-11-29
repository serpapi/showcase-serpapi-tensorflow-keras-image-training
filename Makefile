# Makefile automate run and install
#

# setup docker
#
all: install run

# Install dependency
install:
	docker pull tensorflow/tensorflow
	mkdir -p data

# Run docker instance for testing
# TODO Remove local network
run:
	docker run -it --rm -v ${PWD}/.:/app -w /app tensorflow/tensorflow make build

debug:
	docker run -it --rm -v ${PWD}/.:/app -w /app tensorflow/tensorflow bash

# run all steps
#
build: dep fetch classify train

# install dependency
dep:
	pip install wget
	pip install google-search-results
	apt-get update && apt-get install -y file

# fetch images from SerpApi
#  and download images from original source
fetch:
	mkdir -p data
	python fetch.py

# Image classify using regular expression.
#  you need to revisit this method dependending on the problem.
classify:
	mkdir -p data/train/fruit
	mkdir -p data/train/brand
	mkdir -p data/validation/brand
	mkdir -p data/validation/fruit
	@echo "remove HTML files"
	file data/* | egrep -v "JPEG\simage|PNG\simage|directory" | cut -d':' -f1 | xargs -I {} rm "{}" 
	@echo "unrelated files"
	file data/* | egrep -i "headphone|og.png|MMEF|merlin|tile|macbook|acastro|cover|ac-video|USB|ipad|car|z0uk|macmini|MacFeature|watch|Apple_Park|51m3-nQ8WhL|ceotmic|ios11|ios12" | cut -d':' -f1 | xargs rm
	@echo "copy apple logo files"
	find data/ -maxdepth 1 -type f | egrep -i "logo|iphone|event|bosnia|cover|unnamed|CN067|Product|105146643|Security" | xargs -I {} mv {} data/train/brand
	@echo "copy fruit images"
	find data/ -maxdepth 1 -type f | grep -v "directory" | xargs -I {} mv {} data/train/fruit
	@echo "create validation set"
	cp data/train/fruit/a1.jpg data/validation/fruit
	cp data/train/brand/knowledge_graph_logo.png data/validation/brand

# Train a simple model using Keras / tensorflow
#  This keras model is trained using Keras ImageDataGenerator
#  which allows to easy resize image, pad, handle multi-color images...
#
train:
	python train.py

