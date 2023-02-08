#!/usr/bin/env python3
# indexes SD test image folders and copies the grid images to the appropriate folders.
# Version 1.0

# resources :
# https://stackoverflow.com/questions/3925096/how-to-get-only-the-last-part-of-a-path-in-python


import os
import shutil
import sys
from glob import glob

# get current directory
base_dir = os.getcwd()
# base_dir = '/Volumes/EXT SSD 4TB/Stable-Diffusion/Models/!My Trained Models/1.5 Trained Models/joepenna_repo/gulsah_22img/Test Images'
base_dir += '/test'

print("dir = " + base_dir)

# =================================================================================================
# 1. RENAME
# =================================================================================================
search_pattern = base_dir + '/*/'
folder_list = glob(f'{search_pattern}', recursive=False)

for folderpath in folder_list:
    # get the last part of the path
    foldername = os.path.basename(os.path.normpath(folderpath))
    # print(foldername)

    # delete 3), 10), 14), 16)
    if foldername.startswith('3)'):
        shutil.rmtree(folderpath)

    elif foldername.startswith('10)'):
        shutil.rmtree(folderpath)

    elif foldername.startswith('14)'):
        shutil.rmtree(folderpath)

    elif foldername.startswith('16)'):
        shutil.rmtree(folderpath)

# now rename the other folders
# rebuild list
folder_list2 = glob(f'{search_pattern}', recursive=False)

for folderpath in folder_list2:
    foldername = os.path.basename(os.path.normpath(folderpath))
    if foldername.startswith('4)'):
        print(base_dir)
        print(foldername)
        print()