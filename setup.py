import os
from distutils.core import setup

with open('requirement.txt') as f:
    required = f.read().splitlines()


setup(
    name='time_series_transform',
    version='0.0.2',
    description = 'A data preprocessing package for time series data. It provides tools for machine learing and deep learning.It also has subsection specialized in stock.',
    packages=[
        'time_series_transform',
        'time_series_transform/transform_core_api',
        'time_series_transform/stock_transform',
        'time_series_transform/test',
        ],
    license='MIT',
    author_email = 'kuanlun.chiang@outlook.com',
    url = 'https://github.com/allen-chiang/Time-Series-Transformer',
    download_url ='https://github.com/allen-chiang/Time-Series-Transformer/archive/0.0.2.tar.gz',
    keywords = ['time series','stock', 'machine learning', 'deep learning'],
    install_requires = required,
    author = 'KuanLun Chiang KuanYu Chiang',
    # long_description=open('README.rst').read(),
    classifiers=[
    'Intended Audience :: Science/Research',
    'Intended Audience :: Developers',      
    'Programming Language :: Python',
    'Topic :: Software Development',
    'Topic :: Scientific/Engineering',
    'License :: OSI Approved :: MIT License', 
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
  ],
)
