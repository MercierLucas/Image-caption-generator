from utils import ProgressBar

import os
from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras import Model


def load_images(path,preprocessor=None,limit=None,):
  images = []
  images_id = next(os.walk(path))[2]
  size = limit if limit != None else len(images_id)
  print(f"Loading {size} images")

  prog = ProgressBar(100,size)

  for id in range(size):
    name = images_id[id]

    filename = path + "/" + name
    image = load_img(filename,target_size=(224,224))
    image = img_to_array(image)
    image = image.reshape((1, image.shape[0], image.shape[1], image.shape[2]))

    if preprocessor != None:
      image = preprocessor.preprocess_input(image)

    image_id = name.split('.')[0]
    images.append([image_id,image])

    prog.update(id)
    
  print("Loading complete")
  return images


def extract_features(images,model):
  features = dict()
  count = 0
  prog = ProgressBar(100,len(images))

  for id,image in images:
    feature = model.predict(image,verbose=0)
    features[id] = feature
    count +=1
    prog.update(count)

  return features