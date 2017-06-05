# -*- coding: utf-8 -*-
"""
Simple script to browse an FTP website, and download some files.
Currently set to the Montana Cadastral website

@author: Kalkberg
"""

import os
from ftplib import FTP
import zipfile
import glob

# Input arguments
downloaddir = 'D:\\'
destdir = 'Cadastral3'
ftpsite = 'ftp.geoinfo.msl.mt.gov'
filepath = 'Data/Spatial/MSDI/Cadastral/Parcels/'

# Create folder structure in destination directory
os.chdir(downloaddir)
os.makedirs(destdir)
os.chdir(destdir)

# Got to needed directory
host = FTP(ftpsite)
host.login() # log in as anonymus
host.cwd(filepath)
dirs = host.nlst()

# Download files
for i in range(0,len(dirs)):
    host.cwd(dirs[i])
    host.retrbinary('RETR ' + dirs[i]+'OwnerParcel_shp.zip',
                    open(dirs[i]+'OwnerParcel_shp.zip','wb').write)
    host.cwd('..')