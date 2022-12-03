from Detector import *

detector = Detector()

import os
#get image path
image = 'sheep.jpg'
path_detectron2 = os.path.abspath('detectron_aiweb')
path_image = os.path.join(path_detectron2,'images',image)

detector.onImage(path_image)