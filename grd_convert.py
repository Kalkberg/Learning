# -*- coding: utf-8 -*-
"""
Helper script for taking velocity files produced by GMT5SAR, and generating
NetCDF grids with lat/long coordinates

Note: Only works if image footprints are the same

@author: Kallberg
"""
import os
import shutil
import glob

wrk_dir = '/home/pyakovlev/INSAR/Virginia_City/'

os.chdir(wrk_dir)

# Convert veolocity file
shutil.move('vel.grd',wrk_dir+'/topo/')
os.chdir(wrk_dir+'topo')
os.system('proj_ra2ll.csh trans.dat vel.grd vel_ll.grd')
os.system('grdconvert -fg vel_ll.grd vel_ll.nc')

# Find and convert all disp files
os.chdir(wrk_dir)
disps = glob.glob('disp*.grd')

# Make backup grid files then cut
for i in range(0,len(disps)):
    shutil.move(disps[i],wrk_dir+'/topo/')
    os.chdir(wrk_dir+'topo')
    os.system('proj_ra2ll.csh trans.dat ' + disps[i] + ' ' + disps[i][:-4] + '_ll.grd')
    os.system('grdconvert -fg ' + disps[i][:-4] + '_ll.grd '+ disps[i][:-4] + '_ll.nc')
    os.chdir(wrk_dir)
    
