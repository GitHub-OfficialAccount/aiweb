from detectron2.utils.logger import setup_logger

setup_logger()

from detectron2.data.datasets import register_coco_instances
from detectron2.engine import DefaultTrainer

import os
import pickle

from mydatasets_utils import *

config_file_path = "COCO-Detection/faster_rcnn_R_50_FPN_3x.yaml"
checkpoint_url = "COCO-Detection/faster_rcnn_R_50_FPN_3x.yaml"

output_dir = "./output/object_detection"
num_classes = 1

device = "cpu" #or cuda

# path = os.getcwd() ##for django
path = os.path.abspath('detectron_aiweb')

train_dataset_name = "RBC_train"
train_images_path =  os.path.join(path,"mydatasets_train")
train_json_annot_path = os.path.join(path,"mydatasets_train.json")
assert os.path.exists(train_images_path)
assert os.path.exists(train_json_annot_path)

test_dataset_name = "RBC_test"
test_images_path = os.path.join(path,"mydatasets_test")
test_json_annot_path = os.path.join(path,"mydatasets_test.json")
assert os.path.exists(test_images_path)
assert os.path.exists(test_json_annot_path)

#############################
register_coco_instances(
    name=train_dataset_name,
    metadata={},
    json_file=train_json_annot_path,
    image_root=train_images_path)

register_coco_instances(
    name=test_dataset_name,
    metadata={},
    json_file=test_json_annot_path,
    image_root=test_images_path)

plot_samples(dataset_name=train_dataset_name, n=2)