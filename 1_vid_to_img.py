from conf import SAMPLE_INPUTS, SAMPLE_OUTPUTS
import os 
from moviepy.editor import * # or VideoFileClip
from PIL import Image
source_path = os.path.join(SAMPLE_INPUTS, 'sample.mp4')
thumbnail_dir = os.path.join(SAMPLE_OUTPUTS, 'thumbnails')
thumbnail_per_second_dir = os.path.join(SAMPLE_OUTPUTS, 'thumbnails-per-second')
thumbnail_per_frame_dir = os.path.join(SAMPLE_OUTPUTS, 'thumbnails-per-frame')
thumbnail_per_half_second_dir = os.path.join(SAMPLE_OUTPUTS, 'thumbnails-per-half_second')
os.makedirs(thumbnail_dir, exist_ok = True)
os.makedirs(thumbnail_per_second_dir, exist_ok = True)
os.makedirs(thumbnail_per_frame_dir, exist_ok = True)
os.makedirs(thumbnail_per_half_second_dir, exist_ok = True)

clip = VideoFileClip(source_path)
print(clip.reader.fps) # frame per second
print(clip.reader.nframes) # number of frame in the video 
print(clip.duration) # duration of the clip 

duration = clip.duration
max_duration = int(duration + 1)

# every second we create a thumbnail 
for i in range(0, max_duration): # + 1 is to include the last second
    new_img_path = os.path.join(thumbnail_dir, f'{i}.jpg')
    #print(f'frame at {i} seconds saved at {new_img_path}')
    frame = clip.get_frame(i)
    #print(frame) # this wil print the np.array of the img #inference can be used in machine learning or we can use pillow to let it convert array to img 
    new_img = Image.fromarray(frame)
    new_img.save(new_img_path)

# every second we create an img more efficient way
fps = clip.reader.fps
nframes = clip.reader.nframes
seconds = nframes / (fps * 1.0) # number of seconds inside the clip 
for frame_index, frame in enumerate(clip.iter_frames()): # + 1 is to include the last second
    if frame_index % fps == 0:
        current_ms = int((frame_index / fps))
        new_img_path = os.path.join(thumbnail_per_second_dir, f'{current_ms}.jpg')
        #print(f'frame at {i} seconds saved at {new_img_path}')
        #print(frame) # this wil print the np.array of the img #inference can be used in machine learning or we can use pillow to let it convert array to img 
        new_img = Image.fromarray(frame)
        new_img.save(new_img_path) 

# every half a second we create a img
for frame_index, frame in enumerate(clip.iter_frames()): # + 1 is to include the last second
    fphs = int(fps/2.0)
    if frame_index % fphs == 0:
        current_ms = int((frame_index / fps) * 1000)
        new_img_path = os.path.join(thumbnail_per_half_second_dir, f'{current_ms}.jpg')
        #print(f'frame at {i} seconds saved at {new_img_path}')
        #print(frame) # this wil print the np.array of the img #inference can be used in machine learning or we can use pillow to let it convert array to img 
        new_img = Image.fromarray(frame)
        new_img.save(new_img_path) 


# every frame we create a thumbnail
for i, frame in enumerate(clip.iter_frames()): # + 1 is to include the last second
    new_img_path = os.path.join(thumbnail_per_frame_dir, f'{i}.jpg')
    #print(f'frame at {i} seconds saved at {new_img_path}')
    #print(frame) # this wil print the np.array of the img #inference can be used in machine learning or we can use pillow to let it convert array to img 
    new_img = Image.fromarray(frame)
    new_img.save(new_img_path) 