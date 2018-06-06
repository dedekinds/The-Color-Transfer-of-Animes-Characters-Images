# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 10:29:21 2018

@author: dedekinds
"""
import os
from PIL import Image
import numpy as np

PATH = os.getcwd()

def png2jpg_background_white(PNG,SEG):
    os.chdir(PATH+'/READY')
    INPUT=np.array(Image.open(PNG))
    os.chdir(PATH+'/examples/segmentation')
    seg = np.array(Image.open(SEG))
    h = INPUT.shape[0]
    w = INPUT.shape[1]
    
    new = Image.new("RGB",(h,w))
    for i in range(0,h):
        for j in range(0,w):
            if seg[i][j]:
                new.putpixel([i,j],(INPUT[i,j,0],INPUT[i,j,1],INPUT[i,j,2]))
            else:
                new.putpixel([i,j],(255,255,255))
    return new

def rot_flop(filename):
    os.system('convert -rotate 90 '+filename+' '+filename)
    os.system('convert -flop '+filename+' '+filename)



#create context_segementation and move it to /segmentation
os.chdir(PATH+'/READY')
os.system('convert -alpha Extract -type optimize -strip -quality 60 +dither base_context.png base_context_mask.png')
os.system('mv base_context_mask.png '+PATH+'/examples/segmentation')

#create style_segementation and move it to /segmentation
os.chdir(PATH+'/READY')
os.system('convert -alpha Extract -type optimize -strip -quality 60 +dither base_style.png base_style_mask.png')
os.system('mv base_style_mask.png '+PATH+'/examples/segmentation')


#########################################
#convert type
os.chdir(PATH+'/READY')
os.system('convert base_context.png base_context.jpg')#convert to pre-jpg first 
os.system('convert base_style.png base_style.jpg')#it can avoid some trouble from the type of png

context = png2jpg_background_white(PNG = 'base_context.jpg',SEG = 'base_context_mask.png' )
context.save('base_context.jpg')
os.system('mv base_context.jpg '+PATH+'/examples/input/')

style = png2jpg_background_white(PNG = 'base_style.jpg',SEG = 'base_style_mask.png' )
style.save('base_style.jpg')
os.system('mv base_style.jpg '+PATH+'/examples/style/')

#rotate and flop
os.chdir(PATH+'/examples/input')
rot_flop('base_context.jpg')

os.chdir(PATH+'/examples/style')
rot_flop('base_style.jpg')



#begin training 
os.chdir(PATH)
os.system('python deep_photostyle.py --content_image_path ./examples/input/base_context.jpg --style_image_path ./examples/style/base_style.jpg --content_seg_path ./examples/segmentation/base_context_mask.png --style_seg_path ./examples/segmentation/base_style_mask.png --style_option 2')

#Clipping
os.chdir(PATH)
INPUT=np.array(Image.open('best_temp.png'))
os.chdir(PATH+'/examples/segmentation')
seg = np.array(Image.open('base_context_mask.png'))

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
new.save('last_result.jpg')
rot_flop('last_result.jpg')
