from simple_image_download import simple_image_download as sp
import os

def generate_images(keywords, img_count, stored_dir, response_dir):
    response = sp.simple_image_download

    # keywords = "vehicles with license plate"
    # img_count = 50

    response().download(keywords=keywords, limit=img_count)

    ### move files to mydatasets_train ###
    allfiles = os.listdir(stored_dir)
    allfiles_r = os.listdir(response_dir)

    for p in allfiles_r: #remove previous files
        file_path = os.path.join(response_dir, p)
        os.remove(file_path)



    for p in allfiles:
        file_path = os.path.join(stored_dir, p)
        re_file_path = os.path.join(response_dir, p)
        os.rename(file_path, re_file_path)

