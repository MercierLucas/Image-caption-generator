import os
import string
from utils import ProgressBar

from IPython.display import clear_output

def load_text(filename,mode='r'):
  file = open(filename,mode)
  text = file.read()
  file.close()
  return text



def remove_chars(text,chars):
  for char in chars:
    text = text.replace(char,"")
  return text

def text_cleaner(text):
  text = remove_chars(text,string.punctuation)
  text = text.lower()
  if len(text.split()) > 0:
    text = " ".join([word for word in text.split() if len(word)>1])
    text = " ".join([word for word in text.split() if word.isalpha()])
  return text


def extract_description(file,output_file_name):
  result = []

  for line in file.split('\n'):
    if len(line) < 2 : continue

    line = line.split()
    infos = line[0].split("#")
    id = infos[0].split('.')[0]
    desc = " ".join(line[1:])
    desc = text_cleaner(desc)

    result.append(id+" "+desc)
    

  result = '\n'.join(result)
  output_file = open(output_file_name,'w')
  output_file.write(result)
  output_file.close()
  print(f"Description saved to file {output_file_name} success.")



