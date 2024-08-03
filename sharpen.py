import cv2
import numpy as np
import os

def sharpen(images_folder, output_folder):
    try:
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)
    except OSError:
        print('Error creating {} directory.'.format(output_folder))

    image_files = os.listdir(images_folder)
    
    for image_file in image_files:
        image_path = images_folder + '/' + image_file
        image = cv2.imread(image_path)
        kernel = np.array([[0,-1,0],[-1,5,-1],[0,-1,0]])
        image_sharp = cv2.filter2D(src=image, ddepth=-1, kernel=kernel)
        output_file = output_folder + '/' + image_file
        cv2.imwrite(output_file, image_sharp)
        print('Sharpened image ' + output_file + 'has been written to folder ' + output_folder)
