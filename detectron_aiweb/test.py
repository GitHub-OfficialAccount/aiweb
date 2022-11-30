import cv2, os

file_detectron2 = os.path.abspath('detectron2')
file_images = os.path.join(file_detectron2, 'images')
file_image = os.path.join(file_images, 'sheep.jpg')
print(file_image)

image = cv2.imread(file_image)
cv2.imshow('image',image)

cv2.waitKey(0)
cv2.destroyAllWindows()