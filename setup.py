#!/usr/bin/env python3

'''
Python distutils setup file for Chapter 19 code

Copyright (C) 2019 Simon D. Levy

MIT License
'''

from setuptools import setup

setup (name = 'drlho2e',
    version = '0.1',
    install_requires = ['gym', 'numpy'],
    description = 'Deep-Reinforcement-Learning-Hands-On-Second-Edition',
    packages = ['drlho2e', 'drlho2e.ch19', 'drlho2e.ch19.lib'],
    author='Simon D. Levy',
    author_email='simon.d.levy@gmail.com',
    url='https://github.com/simondlevy/Deep-Reinforcement-Learning-Hands-On-Second-Edition',
    license='MIT',
    platforms='Linux; Windows; OS X'
    )
