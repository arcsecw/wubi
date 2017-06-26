#!/usr/bin/env python
# -*- coding: utf-8 -*-

from io import open

from setuptools import setup

setup(
    name='wubi',
    version='0.0.1',
    description='Translate chinese chars to wubi',
    author='arcsecw',
    author_email='tob-wang@qq.com',
    packages=['wubi',],
    package_data={
        '': ['LICENSE'],
        'wubi': ['wubi.cPickle'], },
    entry_points={"console_scripts": ["wubi = wubi.cmd:wubi", ]},
    url='https://github.com/arcsecw/wubi',
    license="BSD",
    long_description=open('README.rst', encoding='utf-8').read(),
    classifiers=[
        "Topic :: Software Development",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
    ]
)
