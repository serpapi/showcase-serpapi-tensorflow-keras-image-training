# Tensorflow / Keras training a network to recognize
#  Apple logo versus a real Apple fruit.
#
# For more details see: README.md
#  * README
#  * [Keras documentation](https://www.tensorflow.org/guide/keras)
#
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten
import sys

print(tf.VERSION)
print(tf.keras.__version__)

IMAGE_HEIGHT = 200
IMAGE_WIDTH  = 200

# image data generator
gen = ImageDataGenerator(
	rotation_range=0,
	width_shift_range=0.2,
	height_shift_range=0.2,
	horizontal_flip=False
	)

# train generator
print("load images for training")
train_generator = gen.flow_from_directory(
        'data/train',
        target_size=(IMAGE_HEIGHT,IMAGE_WIDTH),
        batch_size=10,
        class_mode='binary')

# validation data
print("load images for validation")
validation_generator = gen.flow_from_directory(
        'data/validation',
        target_size=(IMAGE_HEIGHT,IMAGE_WIDTH),
        batch_size=10,
        class_mode='binary')

# basic model sequential
#  it was not refine in any way.
model = Sequential()
model.add(Flatten(input_shape=(IMAGE_HEIGHT,IMAGE_WIDTH,3)))
model.add(Dense(32, activation='relu'))
model.add(Dense(3, activation='softmax'))
model.compile(optimizer=tf.train.AdamOptimizer(1),
        loss='sparse_categorical_crossentropy',
        metrics=['accuracy'])

# show model
print("run fit generator")

# now we can use our generator in model fit method
model.fit_generator(
        train_generator,
	validation_data=validation_generator,
        epochs=1)

print "model trained"
print "Note: the validation set accuracy is around 50%"
print " which is terrible. You need a lot images."
print " You probably need to download and manually classify around 10k images for a good results."
print " So, you need to create an account with SerpAPI to download more images."
print ">> https://serpapi.com"

# when you're real model is ready
#
# Save entire model to a HDF5 file
#model.save('apple_model.h5')

# Recreate the exact same model, including weights and optimizer.
#model = tf.keras.models.load_model('apple_model.h5')

print("done")
sys.exit(0)