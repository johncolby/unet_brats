# README

## Modifications for UCSF GK data

- BraTS data are 4 channel; GK data are 2. Modifications were made to the data loaders, dice validation heuristics, etc..
- Number of subjects.
- Directory structure is slightly different. Different file names too.
- Data normalization: BraTS data are identically 0 outside the brain, so can do `means_brain` and `stds_brain`. GK data are not.
- Orientation: BraTS data are in a funny orientation template, which we had to keep for the competition predictions. For GK data, we can just predict in native space.
- Volume dimensions: BraTS are all `[240, 240, 155]`. GK data vary. If I recall correctly, the matrix is always 256×256, but the number of slices vary, data were padded in the slice direction to match. If needed, can adjust the `pad_size_val` further to accommodate other data.

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