# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 21:49:31 2020

@author: harin
"""

import os

imdir = 'images'
if not os.path.isdir(imdir):
    os.mkdir(imdir)

flower_folders = [folder for folder in os.listdir('.')]

n = 0
for folder in flower_folders:
    for imfile in os.scandir(folder):
        os.rename(imfile.path, os.path.join(imdir, '{:06}.png'.format(n)))
        n += 1