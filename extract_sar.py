# Script for extracting SAR data obtained from UNAVCO to formats compatible with GMT5SAR
# by Petr Yakovlev, Montana Bureau of Mines & Geology, 2016
# Distributed with the MIT license
#
# Usage:
# python3 extract_sar.py working_dir SAT
# working_dir is the location of the image files to be extracted e.g. /home/user/InSAR
# SAT is set to either ENVI or ERS, and notes data type to be extracted#
#
# Tested on Ubuntu 16.04

# Import modules
import os
import glob
import tarfile
import shutil
import sys

# Create function describing usage and terminating program for errors
def error():
    print("Usage: python3 extract_sar.py working_dir SAT")
    print("Where working_dir is the full path to the image files to be extracted")
    print("e.g. /home/user/InSAR")
    print("SAT is set to either ENVI or ERS, and notes data type to be extracted")
    sys.exit()

# Check number of arguments, if not two, return error
if len(sys.argv)==3:
    print("Current working directory is set to %s" % workdir)
    print("Data type set to %s" % SAT)
else:
    print("Error: Wrong number of input arguments!")
    error()
     
# Import directory to work on and satellite type from input arguments
workdir=sys.argv[1]
SAT=sys.argv[2]

# Move to working directory and read off file list to be worked on
os.chdir('/') # move to root
os.chdir(workdir)
if SAT == 'ERS':
    files=glob.glob('*.gz.tar') # ERS archives end in .gz.tar
elif SAT == 'ENVI':
    files=glob.glob('*.N1') # ENVI archives end in .N1
else: #Terminate program due to wrong input arguments
    print("Error: SAT should be set to ERS or ENVI!")
    error()        

# Create data.in file for WIN5SAR
data=open('data.in','w')

if SAT == 'ERS': # extract and rename files for ERS sat
    for i in range(len(files)):
        print("Working on ERS image %d out of %d..." % (i+1, len(files)))
        tar=tarfile.open(files[i], 'r:gz')
        tar.extractall()
        tar.close
        name=files[i] # extract the actual file name of the repository from the string
        orbit=name[52:57] #figure out orbit name from name of file
        data.write(str(orbit)+'\n') # write orbit name to data file
        shutil.copyfile('DAT_01.001', str(orbit)+'.dat') # create new files with proper extensions
        shutil.copyfile('LEA_01.001', str(orbit)+'.ldr')
        os.rename('DAT_01.001', 'DAT_'+str(orbit)+'.001') # rename extracted files to include orbit number
        os.rename('LEA_01.001', 'LEA_'+str(orbit)+'.001')
else: # copy and rename files for ENVI sat
    for i in range(len(files)):
        print("Working on ENVI image %d out of %d..." % (i+1, len(files)))
        name=files[i] # extract the actual file name of the repository from the string
        orbit=name[49:54] #figure out orbit name from name of file
        data.write(str(orbit)+'\n') # write orbit name to data file
        shutil.copyfile(str(name), str(orbit)+'.baq') # copy file to one with orbit name and .baq extension
    
data.close() # close data.in file
print("All done!")    
