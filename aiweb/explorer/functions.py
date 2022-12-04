import os

path = os.getcwd()
parent_path = os.path.dirname(path)

### add detectron path ###
import sys
detectron_path = os.path.join(parent_path,'detectron_aiweb')
assert os.path.exists(detectron_path)
sys.path.append(detectron_path)

### NOT AN ERROR ###
from main import detect
### NOT AN ERROR ###