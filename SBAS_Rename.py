# -*- coding: utf-8 -*-
"""
Helper script to renames GMT5SAR files for SBAS after making a stack of 
interferograms

Licence:
This work is licensed under the Creative Commons Attribution 4.0 
International License. To view a copy of this license, 
visit http://creativecommons.org/licenses/by/4.0/ or send a letter to 
Creative Commons, PO Box 1866, Mountain View, CA 94042, USA.

@author: Kalkberg
"""

import sys
import os
import glob
import shutil

# Create function describing usage and terminating program for errors
def error():
    print("Usage: python3 SBAS_Rename.py working_dir")
    sys.exit()

# Check number of arguments and import, if not one, return error
if len(sys.argv) == 2:
    # Import directory to work on and satellite type from input arguments
    workdir = sys.argv[1]
    print("Current working directory is set to %s" % workdir)
else:
    print("Error: Wrong number of input arguments!")
    error()   

#workdir = '/home/pyakovlev/INSAR/Virginia_City'

# Move to folder of interferograms
os.chdir(workdir+'/intf/')
dirs = os.listdir('.')

for i in range(0,len(dirs)):
    os.chdir(dirs[i])
    files = glob.glob('*.LED')
    shutil.copy('corr.grd',
                workdir+'corr_'+files[0][:-4]+'_'+files[1][0:-4]+'.grd')
    shutil.copy('unwrap.grd',
                workdir+'unwrap_'+files[0][:-4]+'_'+files[1][0:-4]+'.grd')
    shutil.copy('phase.grd',
                workdir+'phase_'+files[0][:-4]+'_'+files[1][0:-4]+'.grd')
    os.chdir('..')
