# Make a video from images

from conf import SAMPLE_INPUTS, SAMPLE_OUTPUTS
import os 
from moviepy.editor import * # or ImageSequenceClip and ImageClip
from PIL import Image

thumbnail_dir = os.path.join(SAMPLE_OUTPUTS, 'thumbnails')
thumbnail_per_second_dir = os.path.join(SAMPLE_OUTPUTS, 'thumbnails-per-second')
thumbnail_per_frame_dir = os.path.join(SAMPLE_OUTPUTS, 'thumbnails-per-frame')
thumbnail_per_half_second_dir = os.path.join(SAMPLE_OUTPUTS, 'thumbnails-per-half_second')
output_video = os.path.join(SAMPLE_OUTPUTS, 'thumbs.mp4')

this_dir = os.listdir(thumbnail_dir)
filepaths = [os.path.join(thumbnail_dir, fname) for fname in this_dir if fname.endswith('jpg')] # we can do it the normal way next line
# filepaths = []
# for fname in this_dir:
#     if fname.endswith('jpg'):
#         path = os.path.join(thumbnail_dir, fname)
#         filepaths.append(path)

#print(filepaths)
# clip = ImageSequenceClip(filepaths, fps=1)
# clip.write_videofile(output_video)

# better methods on how to go throw an entire directory using method call walk()
# this now give us a dirctory full of key value pair that are coming from the name of the file itself
directory = {}

for root, dirs, files in os.walk(thumbnail_per_second_dir):
    for fname in files:
        filepath = os.path.join(root, fname)
        try:
            key =  float(fname.replace('.jpg', ''))
        except:
            key = None
        if key != None:
            directory[key] = filepath
# this will make the frames in the video in an order thats based on how i named them 
new_path = []
for k in sorted(directory.keys()):
    #print(k)
    filepath = directory[k]
    new_path.append(filepath)

# clip = ImageSequenceClip(new_path, fps=10)
# clip.write_videofile(output_video)
my_clips = []
for path in list(new_path):
    frame = ImageClip(path)
    #print(dir(frame)) # gives me all the methods available in frame
    my_clips.append(frame.img) # .img is one of the methods available in frame
    #print(frame.img) # numpy array 

clip = ImageSequenceClip(my_clips, fps=22)
clip.write_videofile(output_video)