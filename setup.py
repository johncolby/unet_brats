from setuptools import setup

setup(
    name='unet_brats',
    version='0.1.0',
    url='https://github.com/johncolby/unet_brats',
    author='John Colby',
    author_email='john.b.colby@gmail.com',
    description='U-Net segmentation for BraTS 2018 in mxnet',
    packages=['unet_brats'],
    install_requires=['mxboard',
                      'numpy',
                      'nibabel',
                      #'mxnet',
                      'gluoncv',
                      'numpy',
                      'transforms3d',
                      'tqdm',
                      'rpy2',
                      'ipykernel',
                      'ipywidgets'],
)