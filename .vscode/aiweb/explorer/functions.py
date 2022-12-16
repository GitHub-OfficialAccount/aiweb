import os

path = os.getcwd()
parent_path = os.path.dirname(path)

### add detectron path ###
import sys
detectron_path = os.path.join(parent_path,'detectron_aiweb')
assert os.path.exists(detectron_path)
sys.path.append(detectron_path)

from mydatasets_generation import generate_images
from mydatasets_train import main

generate_images_path = os.path.join(detectron_path, 'mydatasets_train')
generate_jsonfile_path = os.path.join(detectron_path, 'mydatasets_train.json')
generate_images_path_test = os.path.join(detectron_path, 'mydatasets_test')
generate_jsonfile_path_test = os.path.join(detectron_path, 'mydatasets_test.json')

def get_stored_dir(keywords):
    stored_dir = os.path.join(path,'simple_images',keywords)
    return stored_dir
try:
    from mydatasets_test import read_img
    def detect(img_path):
        return read_img(img_path)
except: pass
