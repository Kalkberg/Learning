# -*- coding: utf-8 -*-
"""
Script for cutting up a batch of grd files using gmt

@author: Kalkberg
"""

import os
import glob
import shutil

cut_area = '800/5644/1000/25000'
wrk_dir = '/home/pyakovlev/INSAR/Virginia_City/'

os.chdir(wrk_dir)

# Find files to change
corr_files = glob.glob('corr*.grd')
phase_files = glob.glob('phase*.grd')

# Make backup grid files then cut
for i in range(0,len(corr_files)):
    shutil.copy(corr_files[i], corr_files[i][:-4]+'_backup.grd')
    os.system('gmt grdcut '+corr_files[i]+' -G'+corr_files[i]+' -R'+cut_area)
    shutil.copy(phase_files[i], phase_files[i][:-4]+'_backup.grd')
    os.system('gmt grdcut '+phase_files[i]+' -G'+phase_files[i]+' -R'+cut_area)
    