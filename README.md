# Quality Enhancement of Color Transfer of Low Quality Pictures：Pokémon Fusion Example

The final project of Advance Machine Learning course in Tsinghua University. Two contributors come from Tsinghua University
and Northwestern University, U.S.. 

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

## Install ImageMagick
First you need to install the ImageMagick, you can type 
```
sudo apt-get install ImageMagick
```
in Linux Terminal. This software is used to extracts the alpha channel from the PNG images (your content and style images). The covert code is already include in the `base_model.py` file.

## Baseline Model 
Then you can type
```
python base_model.py
```

in the Terminal and generate the deep-photo-style model's result, which is the baseline model to be compared with our work. You can find the last_result.jpg in the same path, as well as all the result images of each iteration. The default size of iteration is 1000.


If you want to modify the iteration size, you can change the parameter `—save_iter` in `deep_photostyle.py`. You can also modify the `Weight Options` parameter to change the weight of different loss.

## Our work:Pre-coloring model
In order to improve the worse performance in color transfer when you use low quality content picture or/and style picture in the baseline model, we propose an enhancement method: the Pre-coloring model. Here is the usage:

You can type 
```
python get_pre_coloring.py
```
in the Terminal and find the pre_result.jpg in `/examples/style`. If you think the result image does not satisfy your requirement, you can rerun again the same command until you get a good enough pre-coloring result. Since in most cases, the K-means Algorithm can not converge, so each time when you run the command above, you will get different pre-coloring result, that's the beauty of art generation :)

You can also modify the `n_clusters` parameter in `get_pre_coloring.py` and this parameter will change the size of color cluster in your content and style image in pre-color procedure and finally change our pre-coloring result.

When you complete the pre-coloring step, you can consequently type 
```
python pre_color_model.py
```
in your Terminal and get our enhancement result.

## Acknowledgement

* The baseline style transfer model implementation of our project is totally based on the [LouieYang's](https://github.com/LouieYang/deep-photo-styletransfer-tf) deep-photo-styletransfer-tf project. The style transfer 
model implemented in [Yang's](https://github.com/LouieYang/deep-photo-styletransfer-tf) project is based on the paper "Deep Photo Style Transfer": https://arxiv.org/abs/1703.07511. You can also refer to this paper's author, [Fujun Luan's](https://github.com/luanfujun/deep-photo-styletransfer) github to learn more about the original implementation of the paper.


