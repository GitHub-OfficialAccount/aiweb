import os,sys

path = os.getcwd()
parent_path = os.path.dirname(path)

### add detectron path ###
detectron_path = os.path.abspath('detectron_aiweb')
assert os.path.exists(detectron_path)
sys.path.append(detectron_path)


### NOT AN ERROR ###
from main import detect
### NOT AN ERROR ###
detect('sheep.jpg')