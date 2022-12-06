from detectron2.engine import DefaultPredictor

import os
import pickle

from mydatasets_utils import *

path = os.getcwd()

cfg_save_path = os.path.join(path,'OD_cfg.pickle')

with open(cfg_save_path, 'rb') as f:
    cfg = pickle.load(f)

cfg.MODEL.WEIGHTS = os.path.join(cfg.OUTPUT_DIR, "model_final.pth")
cfg.MODEL.ROI_HEADS.SCORE_THRESH_TEST = 0.5

predictor = DefaultPredictor(cfg)

test_dataset_name = "RBC_test"
test_images_path = os.path.join(path,"mydatasets_test")

assert os.path.exists(test_images_path)

image_name = "BloodImage_00038_jpg.rf.ffa23e4b5b55b523367f332af726eae8.jpg" #to be filled in
image_path = os.path.join(test_images_path,image_name)
video_path = '' #to be filled in

on_image(image_path, predictor)
# onvideo(video_path, predictor)
