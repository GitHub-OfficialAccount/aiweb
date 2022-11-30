from Detector import *

detector = Detector()

#get image path
import cv2, os
file_detectron2 = os.path.abspath('detectron2')
file_images = os.path.join(file_detectron2, 'images')
file_image = os.path.join(file_images, 'sheep.jpg')

detector.onImage(file_image)