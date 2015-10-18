#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name='amestatus',
    version='0.1.1',
    description="Status page integration toolkit, lightweight and flexy",
    long_description=open('README.md').read(),
    author="Ametiste-OSS",
    author_email='masted@gmail.com',
    url='https://github.com/ametiste-oss/ame-status',
    license='MIT',
    install_requires=[],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
)
