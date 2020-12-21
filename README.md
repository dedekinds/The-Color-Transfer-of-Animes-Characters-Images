# The Color Transfer of Animes Characters' Images：Pokémon Fusion Example

The final project of Advance Machine Learning course in Tsinghua University. Two contributors come from Tsinghua University
[@dedekinds](https://github.com/dedekinds) and Northwestern University, U.S. [@wuyujack](https://wuyujack.github.io/). This project aims to improve the images' quality after color transferring in low quality pictures. You can refer to the `Data` section to learn more about our test images.

## License
*MIT license*

## Setup
### Dependencies
* [Tensorflow](https://www.tensorflow.org/)
* [Numpy](www.numpy.org/)
* [Pillow](https://pypi.python.org/pypi/Pillow/)
* [Scipy](https://www.scipy.org/)
* [PyCUDA](https://pypi.python.org/pypi/pycuda) (used in smooth local affine, tested on CUDA 9.0)
* [ImageMagick](http://www.imagemagick.org/script/index.php)
* Ubuntu 17.10
### Download the VGG-19 model weights
The VGG-19 model of tensorflow is adopted from [VGG Tensorflow](https://github.com/machrisaa/tensorflow-vgg) with few modifications on the class interface. The VGG-19 model weights is stored as .npy file and could be download from [Google Drive](https://drive.google.com/file/d/0BxvKyd83BJjYY01PYi1XQjB5R0E/view?usp=sharing) or [BaiduYun Pan](https://pan.baidu.com/s/1o9weflK). After downloading, copy the weight file to the **./project/vgg19** directory


## Data
You can make a easy Web crawler to get the orginal low quality Pokémon dataset without fusion in following websites: 
1. http://pokefusion.japeal.com/
2. https://wiki.52poke.com

We also provide the GEN1 to GEN4 [Pokémon Fusion Dataset](https://pan.baidu.com/s/16MHDxSUzexAKax46zhb0GQ). The`GEN` here is the abbreviation of generation of Pokémon. Actually GEN5 is already existed in http://pokefusion.japeal.com/ but we did not crawl down the Pokémon of this generation.

## Install ImageMagick
First you need to install the ImageMagick, you can type 
```
sudo apt-get install ImageMagick
```
in Linux Terminal. This software is used to extracts the alpha channel from the PNG images (your content and style images). The covert code is already included in the `base_model.py` file.

## Usage
### Baseline Model 
To generate the result of baseline model, you can type
```
python base_model.py
```

in the Terminal and generate the deep-photo-style model's result, which is the baseline model to be compared with our work. You can find the last_result.jpg in the same path, as well as all the result images of each iteration. The default size of iteration is 1000.


If you want to modify the iteration size, you can change the parameter `—save_iter` in `deep_photostyle.py`. You can also modify the `Weight Options` parameter to change the weight of different loss.

### Our work: Pre-coloring model
In order to improve the worse performance in color transfer when you use low quality content picture or/and style picture in the baseline model, we propose an enhancement method: the Pre-coloring model. Here is the usage:

You can type 
```
python get_pre_coloring.py
```
in the Terminal and find the pre_result.jpg in `/examples/style`. If you think the result image does not satisfy your requirement, you can rerun again the same command until you get a good enough pre-coloring result. Since in most cases, the K-means Algorithm can not converge, so each time when you run the command above, you will get different pre-coloring result, that's the beauty of art generation :) We present some interesting results of different pre-coloring when you use different style picture. The picture on the left-most is the orginal picture.

![image](https://github.com/dedekinds/havefun/blob/master/image/yrs.jpg)

You can also modify the `n_clusters` parameter in `get_pre_coloring.py` and this parameter will change the size of color cluster in your content and style image in pre-color procedure and finally change our pre-coloring result.

When you complete the pre-coloring step, you can consequently type 
```
python pre_color_model.py
```
in your Terminal and get our enhancement result.


## Result
Here are illustration of our work and performance comparision between our work and the baseline model:

![image](https://github.com/dedekinds/havefun/blob/master/image/tkl.png)
As the picture shown above, with our pre-coloring enhancement, the picture is becoming much more clear when the iteration size is increasing. 
![image](https://github.com/dedekinds/havefun/blob/master/image/db.png)

Here is the comparsion with and without our pre-coloring enhancement before color transfer shown above. Although the result of Luan's CVPR17 paper is incredible in high quality and larger pixel picture's color and style transfer, our enhancement are much better when you are using low quality and smaller pixel images in content and/or style section.

We also present the performance of our works when you want to conduct color transfer in a dynamic feature, such as gif, shown as following. On the left is our result with pre-coloring and the gif on the right is the orginal gif.

![image](https://github.com/dedekinds/havefun/blob/master/image/lymgif.gif)
![image](https://github.com/dedekinds/havefun/blob/master/image/rapidash.gif)

Here are some funny results after pre-coloring enhancement, just have fun :)
![image](https://github.com/dedekinds/havefun/blob/master/image/yb.png)

![image](https://github.com/dedekinds/havefun/blob/master/image/tkllogo.png)
## Acknowledgement

* The baseline style transfer model implementation and the VGG-19 model weights of our project is totally based on the [LouieYang's](https://github.com/LouieYang/deep-photo-styletransfer-tf) deep-photo-styletransfer-tf project. The style transfer 
model implemented in [Yang's](https://github.com/LouieYang/deep-photo-styletransfer-tf) project is based on the paper "Deep Photo Style Transfer": https://arxiv.org/abs/1703.07511. You can also refer to this paper's author, [Fujun Luan's](https://github.com/luanfujun/deep-photo-styletransfer) github to learn more about the original implementation of the paper.


## Contact 
Please feel free to contact us if there are any problems: Mingfu Liang(mingfuliang2020@u.northwestern.edu) or Zhongzhan Huang(zhongzhanhuang@foxmail.com)
