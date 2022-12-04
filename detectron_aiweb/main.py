from Detector import *
import os

def detect(image): #used for django app
    detector = Detector()
    ### the following path is done based on explorer/views.py ###
    ### eg. sys.path should return the path of views.py rather than this file ###
    path = os.getcwd()
    parent_path = os.path.dirname(path)
    detectron_path = os.path.join(parent_path,'detectron_aiweb')

    assert os.path.exists(detectron_path)

    path_image = os.path.join(detectron_path,'images',image)
    
    assert os.path.exists(path_image)
    
    output = detector.getImage(path_image)

    return output.get_image()[:,:,::-1]


### USE THIS FOR TESTING IN VSCODE ###
def detect_for_python(image): 
    detector = Detector()

    import os
    #get image path
    path_detectron2 = os.path.abspath('detectron_aiweb')
    path_image = os.path.join(path_detectron2,'images',image)

    detector.showImage(path_image)