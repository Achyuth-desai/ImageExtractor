import cv2
import os
from sharpen import sharpen

def extract(video_file, output_folder):
    frameRate = 0.05
    frameCount = 0
    width = 200
    height = 200
    cam = cv2.VideoCapture(video_file)
    try:
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

    except OSError:
        print('Error creating {} directory'.format(output_folder))

    while True:
        ret, frame = cam.read()

        if not ret:
            break

        frameCount += 1
        if frameCount % int(cam.get(5) / frameRate) == 0:
            frame = cv2.resize(frame, (width, height))
            output_file = output_folder + '/frame' + str(frameCount) + '.jpg'
            cv2.imwrite(output_file, frame)
            print("Frame {} has been written to the data folder as {}.".format(frameCount, output_file))

    cam.release()
    cv2.destroyAllWindows()
