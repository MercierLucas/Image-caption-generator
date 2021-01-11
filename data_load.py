from pickle import load
from text_preprocessing import load_text

def load_desc_from_file(filename,dataset):
  desc = load_text(filename)
  descriptions = dict()
  for line in desc.split('\n'):
    tokens = line.split()
    image_id = tokens[0]
    image_desc = tokens[1:]
    if image_id in dataset:
      if image_id not in descriptions:
        descriptions[image_id] = []

      image_desc = 'startseq '+' '.join(image_desc)+' endseq'
      descriptions[image_id].append(image_desc)

  return descriptions

# load photo features
def load_photo_features(filename, dataset):
	# load all features
	all_features = load(open(filename, 'rb'))
	# filter features
	features = {k: all_features[k] for k in dataset}
	return features


def load_set(filename):
  images_name = load_text(filename)
  image_set = []
  for image in images_name.split('\n'):
    if len(image) == 0: continue
    image_id = image.split('.')[0]
    image_set.append(image_id)
  
  return image_set