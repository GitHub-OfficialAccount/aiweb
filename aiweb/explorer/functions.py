import os

path = os.getcwd()
parent_path = os.path.dirname(path)

### add detectron path ###
import sys
detectron_path = os.path.join(parent_path,'detectron_aiweb')
assert os.path.exists(detectron_path)
sys.path.append(detectron_path)

from main import detect
from mydatasets_generation import generate_images

generate_images_path = os.path.join(detectron_path, 'mydatasets_train')

def get_stored_dir(keywords):
    stored_dir = os.path.join(path,'simple_images',keywords)
    return stored_dir