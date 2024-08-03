import cv2
from cv2 import dnn_superres
import os

def super_res(image_folder, output_folder):
    image_files = os.listdir(image_folder)

    try:
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)
    except OSError:
        print('Error creating {} directory'.format(output_folder))

    sr_edsr = dnn_superres.DnnSuperResImpl_create()
    # read the model
    path_EDSR = './models/EDSR_x4.pb'
    sr_edsr.readModel(path_EDSR)

    # set the model and scale
    sr_edsr.setModel('edsr', 4)

    for image_file in image_files:
        path = image_folder + '/' + image_file
        image = cv2.imread(path)
        upscaled_image = sr_edsr.upsample(image)
        output_file = output_folder + '/' + image_file
        cv2.imwrite(output_file, upscaled_image)
        print('File ' + output_file + ' has been written to folder ' + output_folder)
    # if you have cuda support
    # sr_edsr.setPreferableBackend(cv2.dnn.DNN_BACKEND_CUDA)
    # sr_edsr.setPreferableTarget(cv2.dnn.DNN_TARGET_CUDA)


