from extract import extract
from sharpen import sharpen
from superRes import super_res

video_files = ['CD1.mp4', 'CD2.mp4', 'CD3.mp4']

for video_file in video_files:
    frame_extract_folder += 'Extracts_' + video_file
    superRes_extract_folder += 'Improved_' + video_file
    output_folder += 'Images_' + video_file
    extract(video_file=video_file, output_folder=frame_extract_folder)
    print('EXTRACTION OF {} FILE IS COMPLETE. NOW RUNNING SUPER_RES TO IMPROVE THE RESOLUTION USING EDSR.'.format(video_file))
    super_res(image_folder=frame_extract_folder, output_folder=superRes_extract_folder)
    print('SCALING OF EXTRACTED IMAGES IS COMPLETED. NOW RUNNING SHARPEN TO SHARPEN THE IMPROVED IMAGES.')
    sharpen(images_folder=superRes_extract_folder, output_folder=output_folder)
    print('FINAL IMAGES HAVE BEEN STORED TO FOLDER {}'.format(output_folder))
    print('################ COMPLETE #####################')
