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

# print("dir = " + base_dir)

# =================================================================================================
# 1. RENAME
# =================================================================================================
search_pattern = base_dir + '/*/'
folder_list = glob(f'{search_pattern}', recursive=False)

num_of_folders = len(folder_list)
if num_of_folders == 19:
    print("Number of folders found = " + str(num_of_folders))
else:
    print("Wrong number of folders found = " + str(num_of_folders) + " Exiting...")

    exit()

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

    # 4 to 3
    if foldername.startswith('4)'):
        print(base_dir)
        print(foldername)
        orig_name = folderpath
        # remove old index number and bracket
        new_name = base_dir + '/3) ' + foldername[3:len(foldername)]
        os.rename(orig_name, new_name)

    elif foldername.startswith('5)'):
        print(base_dir)
        print(foldername)
        orig_name = folderpath
        # remove old index number and bracket
        new_name = base_dir + '/4) ' + foldername[3:len(foldername)]
        os.rename(orig_name, new_name)

    elif foldername.startswith('6)'):
        print(base_dir)
        print(foldername)
        orig_name = folderpath
        # remove old index number and bracket
        new_name = base_dir + '/5) ' + foldername[3:len(foldername)]
        os.rename(orig_name, new_name)

    elif foldername.startswith('7)'):
        print(base_dir)
        print(foldername)
        orig_name = folderpath
        # remove old index number and bracket
        new_name = base_dir + '/6) ' + foldername[3:len(foldername)]
        os.rename(orig_name, new_name)

    elif foldername.startswith('8)'):
        print(base_dir)
        print(foldername)
        orig_name = folderpath
        # remove old index number and bracket
        new_name = base_dir + '/7) ' + foldername[3:len(foldername)]
        os.rename(orig_name, new_name)

    elif foldername.startswith('9)'):
        print(base_dir)
        print(foldername)
        orig_name = folderpath
        # remove old index number and bracket
        new_name = base_dir + '/8) ' + foldername[3:len(foldername)]
        os.rename(orig_name, new_name)

    elif foldername.startswith('11)'):
        print(base_dir)
        print(foldername)
        orig_name = folderpath
        # remove old index number and bracket
        new_name = base_dir + '/9) ' + foldername[3:len(foldername)]
        os.rename(orig_name, new_name)

    elif foldername.startswith('12)'):
        print(base_dir)
        print(foldername)
        orig_name = folderpath
        # remove old index number and bracket
        new_name = base_dir + '/10) ' + foldername[3:len(foldername)]
        os.rename(orig_name, new_name)

    elif foldername.startswith('13)'):
        print(base_dir)
        print(foldername)
        orig_name = folderpath
        # remove old index number and bracket
        new_name = base_dir + '/11) ' + foldername[3:len(foldername)]
        os.rename(orig_name, new_name)

    elif foldername.startswith('15)'):
        print(base_dir)
        print(foldername)
        orig_name = folderpath
        # remove old index number and bracket
        new_name = base_dir + '/12) ' + foldername[3:len(foldername)]
        os.rename(orig_name, new_name)

    elif foldername.startswith('17)'):
        print(base_dir)
        print(foldername)
        orig_name = folderpath
        # remove old index number and bracket
        new_name = base_dir + '/13) ' + foldername[3:len(foldername)]
        os.rename(orig_name, new_name)

    elif foldername.startswith('18)'):
        print(base_dir)
        print(foldername)
        orig_name = folderpath
        # remove old index number and bracket
        new_name = base_dir + '/14) ' + foldername[3:len(foldername)]
        os.rename(orig_name, new_name)

    elif foldername.startswith('19)'):
        print(base_dir)
        print(foldername)
        orig_name = folderpath
        # remove old index number and bracket
        new_name = base_dir + '/15) ' + foldername[3:len(foldername)]
        os.rename(orig_name, new_name)