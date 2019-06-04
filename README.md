# README

This python package contains a 3D U-Net algorithm (a type of deep learning convolutional neural network based on [Ronneberger et al., 2015](https://arxiv.org/abs/1505.04597)) for the segmentation of voxelwise medical imaging data. It is geared toward the [BraTS 2018](https://www.med.upenn.edu/sbia/brats2018.html) glioma brain tumor dataset, although the underlying network is broadly applicable to other voxelwise multi input channel and multi output class applications. It is implemented in the `mxnet` deep learning framework.

## Install

1. Make sure a version of [`mxnet`](https://mxnet.incubator.apache.org/versions/master/install/) is installed with GPU support. For example:

    ```bash
    pip install mxnet-cu92mkl
    ``` 

1. Download this repository, either with `git clone <URL>` (where `<URL>` is the git repository URL) or by clicking the download link in the git web interface.

1. Install the companion python module. From the command line:
    ```
    cd /path/to/unet_brats/
    pip install .
    ```
    Alternatively, install directly from the git repository like:

    ```bash
    pip install git+<URL>
    ```

## Usage

Example Jupyter notebooks for training and testing/inference are included in the [notebooks](notebooks) directory.

## Performance

This project aims to create a good implementation of a simple "vanilla" U-Net, which may be used as a basic foundation for more complex analyses. Nevertheless, despite the focus on simplicity, it achieves competitive performance out-of-the-box, for example achieving top 10 results in whole tumor segmentation at the time of this writing. From the [BraTS 2018 Leaderboard](https://www.cbica.upenn.edu/BraTS18/lboardValidation.html):

| Team         | Dice_ET | Dice_WT | Dice_TC |
| ---          | ---     | ---     | ---     |
| Dep_Rad_UCSF | 0.78829 | 0.90918 | 0.84132 |

## Example output

![](https://user-images.githubusercontent.com/473295/58853174-d775b300-8688-11e9-9a33-6ee4444d3c20.png)
