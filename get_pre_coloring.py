from PIL import Image
import numpy as np
import os
from sklearn.cluster import KMeans
import collections

n_clusters=8 
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
os.system('convert -alpha Extract -type optimize -strip -quality 60 +dither pre_color_context.png pre_color_context_mask.png')
os.system('mv pre_color_context_mask.png '+PATH+'/examples/segmentation')

#create style_segementation and move it to /segmentation
os.chdir(PATH+'/READY')
os.system('convert -alpha Extract -type optimize -strip -quality 60 +dither pre_color_style.png pre_color_style_mask.png')
os.system('mv pre_color_style_mask.png '+PATH+'/examples/segmentation')


#########################################
#convert type
os.chdir(PATH+'/READY')
os.system('convert pre_color_context.png pre_color_context.jpg')#convert to pre-jpg first 
os.system('convert pre_color_style.png pre_color_style.jpg')#it can avoid some trouble from the type of png

context = png2jpg_background_white(PNG = 'pre_color_context.jpg',SEG = 'pre_color_context_mask.png' )
context.save('pre_color_context.jpg')
os.system('mv pre_color_context.jpg '+PATH+'/examples/input/')

style = png2jpg_background_white(PNG = 'pre_color_style.jpg',SEG = 'pre_color_style_mask.png' )
style.save('pre_color_style.jpg')
os.system('mv pre_color_style.jpg '+PATH+'/examples/style/')

#rotate and flop
os.chdir(PATH+'/examples/input')
rot_flop('pre_color_context.jpg')

os.chdir(PATH+'/examples/style')
rot_flop('pre_color_style.jpg')




###########################################
#pre_coloring
os.chdir(PATH)
INPUT=np.array(Image.open(PATH+'/examples/input/pre_color_context.jpg'))
OUTPUT=np.array(Image.open(PATH+'/examples/style/pre_color_style.jpg'))

#for context
INPUT_temp = INPUT.reshape(-1,3)
est = KMeans(n_clusters=n_clusters)
est.fit(INPUT_temp)
labels = est.labels_

INPUT_centers = est.cluster_centers_
INPUT_label_nums = collections.Counter(labels)
INPUT_labels = est.labels_


#for style
OUPUT_temp = OUTPUT.reshape(-1,3)
est = KMeans(n_clusters=n_clusters)
est.fit(OUPUT_temp)
labels = est.labels_

OUTPUT_centers = est.cluster_centers_
OUTPUT_label_nums = collections.Counter(labels)
OUTPUT_labels = est.labels_





#create a one-one mapping from INPUT_centers to OUTPUT_centers
#it is a easy mapping below, you can make a more effective mapping 


#####
#warning: actually, it is not good for using k-means which usually do not converge! As this result, the coloring result is usually different.
#####
h = INPUT.shape[0]
w = INPUT.shape[1]

new_input = Image.new("RGB",(h,w))
INPUT_labels = INPUT_labels.reshape(h,w)

for i in range (0,h):
    for j in range (0,w):
        temp = INPUT_labels[i][j]
        r = int(OUTPUT_centers[temp][0])
        g = int(OUTPUT_centers[temp][1])
        b = int(OUTPUT_centers[temp][2])
        new_input.putpixel([i,j],(r,g,b))
            

os.chdir(PATH+'/examples/style')
new_input.save('pre_result.jpg')
rot_flop('pre_result.jpg')






