from detectron2.utils.logger import setup_logger

setup_logger()

from detectron2.data.datasets import register_coco_instances
from detectron2.engine import DefaultTrainer

import os
import pickle

from mydatasets_utils import *

config_file_path = "COCO-Detection/faster_rcnn_R_50_FPN_3x.yaml"
checkpoint_url = "COCO-Detection/faster_rcnn_R_50_FPN_3x.yaml"

path = os.getcwd()

output_dir = os.path.join(path, "mydatasets_output/object_detection")

num_classes = 3 #depends on how many types of object are being identified

device = "cpu" #or cuda

train_dataset_name = "RBC_train"
train_images_path =  os.path.join(path,"mydatasets_train")
train_json_annot_path = os.path.join(path,"mydatasets_train.json")

test_dataset_name = "RBC_test"
test_images_path = os.path.join(path,"mydatasets_test")
test_json_annot_path = os.path.join(path,"mydatasets_test.json")

assert os.path.exists(train_images_path)
assert os.path.exists(train_json_annot_path)
assert os.path.exists(test_images_path)
assert os.path.exists(test_json_annot_path)

cfg_save_path = os.path.join(path,"OD_cfg.pickle")

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

# plot_samples(dataset_name=train_dataset_name, n=2)

##########################

def main():
    cfg = get_train_cfg(config_file_path, checkpoint_url, train_dataset_name, test_dataset_name, num_classes, device, output_dir)

    with open(cfg_save_path,'wb') as f: #'wb': write in binary mode
        pickle.dump(cfg, f, protocol=pickle.HIGHEST_PROTOCOL)

    os.makedirs(cfg.OUTPUT_DIR, exist_ok=True)

    trainer = DefaultTrainer(cfg)
    trainer.resume_or_load(resume=False)

    trainer.train()

if __name__ == '__main__':
    main()

### the smaller loss, the higher accuracy
# 0.00: Perfect; <0.02: Great; <0.05: Good
# total_loss: This is a weighted sum of the following individual losses calculated during the iteration. By default, the weights are all one.
# loss_cls: Classification loss in the ROI head. Measures the loss for box classification, i.e., how good the model is at labelling a predicted box with the correct class.
# loss_box_reg: Localisation loss in the ROI head. Measures the loss for box localisation (predicted location vs true location).
# loss_rpn_cls: Classification loss in the Region Proposal Network. Measures the "objectness" loss, i.e., how good the RPN is at labelling the anchor boxes as foreground or background.
# loss_rpn_loc: Localisation loss in the Region Proposal Network. Measures the loss for localisation of the predicted regions in the RPN.
# loss_mask: Mask loss in the Mask head. Measures how "correct" the predicted binary masks are.
# time: Time taken by the iteration.
# data_time: Time taken by the dataloader in that iteration.
# lr: The learning rate in that iteration.
# max_mem: Maximum GPU memory occupied by tensors in bytes.