# Quality Enhancement of Color Transfer Between Low and High Quality Pictures

The final project of Advance Machine Learning course in Tsinghua University. Two contributors come from Tsinghua University
and Northwestern University, U.S.. 

## Disclaimer
*MIT license*

## Setup
### Dependencies
* [Tensorflow](https://www.tensorflow.org/)
* [Numpy](www.numpy.org/)
* [Pillow](https://pypi.python.org/pypi/Pillow/)
* [Scipy](https://www.scipy.org/)
* [PyCUDA](https://pypi.python.org/pypi/pycuda) (used in smooth local affine, tested on CUDA 9.0)
* [ImageMagick](http://www.imagemagick.org/script/index.php)

### Download the VGG-19 model weights
The VGG-19 model of tensorflow is adopted from [VGG Tensorflow](https://github.com/machrisaa/tensorflow-vgg) with few modifications on the class interface. The VGG-19 model weights is stored as .npy file and could be download from [Google Drive](https://drive.google.com/file/d/0BxvKyd83BJjYY01PYi1XQjB5R0E/view?usp=sharing) or [BaiduYun Pan](https://pan.baidu.com/s/1o9weflK). After downloading, copy the weight file to the **./project/vgg19** directory

## Acknowledgement

* The baseline style transfer model of our project is based on the [LouieYang's](https://github.com/LouieYang/deep-photo-styletransfer-tf) deep-photo-styletransfer-tf project.

