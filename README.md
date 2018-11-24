# Showcase SerpAPI Tensorflow / Keras image training 

SerpAPI enables images search using "Google Image".
The Google results are converted into normalized JSON responses 
 that's easy to process in any programming language.
see: https://serpapi.com/images-results

In this show case, we follow the latest documentation from keras 2.1.6 / tensorflow 1.12.0.
https://www.tensorflow.org/guide/keras

We provided two ways to run this tutorial.
 1. Docker based image provided by Tensorflow team
 2. Run tensorflow 1.12 in your environment 

The overal flow is the following:
 * Fetch data from SerpAPI 
 * Download all the original image directly from the source.
 * Classify the image by moving them into directories or removing some (data/train/<class>)
 * Train the model 
 * Analyze accuracy using a small validation set

We are going to train a machine learning model based Tensorflow and Keras to recognize
  Apple logo/brand versus a real Apple fruit.

Requirements
---

 1. Docker installed
 2. make command

Or

 1. Tensorflow 1.12 with Keras enabled
 2. Python 2.7
 3. make

## How to run this ?
### With Docker 
Run the command
```bash
$> make 
```

### Without Docker
Run the command

```bash
$> make build
```

## Conclusion

This model is not realistic because it achieves only 50% accuracy with less than 300images.
You probably need to pull around 10k images to get a good results.
Also, you might need multiple query like: 
 * Apple Logo
 * Apple fuit
This will save time when manually classifying the apple.


In order to get more images, you need to register with SerpAPI.com.
You will need to pick a plan matching the number of images required.
The service returns 300 images per 1 search.

## Note
 1. We are using Python as a programming language but SerpAPI support many more languages.
 2. Usefull documentation: https://keras.io/getting-started/sequential-model-guide/
 3. Around 10% of the images returned by Google are very difficult to be post process with Keras. So you might need to delete them. The command line tool "file" helps to find the bad images

