import splitfolders

import os

os.makedirs('./dataset')
os.makedirs('./dataset/train')
os.makedirs('./dataset/val')



splitfolders.ratio('./nd/', output='./dataset', seed=1337, ratio=(0.75, 0.25))