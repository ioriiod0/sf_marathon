# -*- coding: utf-8 -*-
# @Author: ioriiod0
# @Date:   2016-12-23 10:15:33
# @Last Modified by:   ioriiod0
# @Last Modified time: 2016-12-23 12:31:58

import sys
from setuptools import setup, find_packages

__title__ = 'sf_marathon'
__author__ = 'gao lei'
__email__ = 'ioriiod0@gmail.com'
__version__ = '0.0.1'

setup(name=__title__,
        version=__version__,
        author=__author__,
        author_email=__email__,
        install_requires=[
        ],
        package_dir={'': 'lib'},
        packages=find_packages('lib'),
        cmdclass={},
        zip_safe=False
        )