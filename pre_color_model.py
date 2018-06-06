import os
from PIL import Image
import numpy as np

PATH = os.getcwd()
def rot_flop(filename):
    os.system('convert -rotate 90 '+filename+' '+filename)
    os.system('convert -flop '+filename+' '+filename)


#training
os.chdir(PATH)
os.system('python deep_photostyle.py --content_image_path ./examples/input/pre_color_context.jpg --style_image_path ./examples/style/pre_result.jpg --content_seg_path ./examples/segmentation/pre_color_context_mask.png --style_seg_path ./examples/segmentation/pre_color_context_mask.png --style_option 2')


#Clipping
os.chdir(PATH)
INPUT=np.array(Image.open('best_temp.png'))
os.chdir(PATH+'/examples/segmentation')
seg = np.array(Image.open('pre_color_context_mask.png'))

h = INPUT.shape[0]
w = INPUT.shape[1]
print(h,w)

new = Image.new("RGB",(h,w))
for i in range(0,h):
    for j in range(0,w):
        if seg[i][j]:
            new.putpixel([i,j],(INPUT[i,j,0],INPUT[i,j,1],INPUT[i,j,2]))
        else:
            new.putpixel([i,j],(255,255,255))

os.chdir(PATH)
new.save('pre_last_result.jpg')
rot_flop('pre_last_result.jpg')
