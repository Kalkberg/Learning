# -*- coding: utf-8 -*-
"""
Uses arcpy to reproject all rasters in a directory

Licence:
This work is licensed under the Creative Commons Attribution 4.0 
International License. To view a copy of this license, 
visit http://creativecommons.org/licenses/by/4.0/ or send a letter to 
Creative Commons, PO Box 1866, Mountain View, CA 94042, USA.

@author: Kalkberg
"""

import arcpy
import os
import glob

workdir = 'D:\\Yakovlev\\Google Drive\\MBMG_GIS\\Images\\DigitalGlobe\\ElkPark\\'
filetype = '.tif'
os.chdir(workdir)
rasters = glob.glob('*'+filetype)

for i in range(0,len(rasters)):
    # Copy the raster to a temp file
    Raster = rasters[i]
    InputRaster = rasters[i][0:-4]+'_temp'+filetype
    os.rename(Raster,InputRaster)
    
    # Project raster to a new file with same name as original
    OutputRaster = Raster # projection set to WGS84 to Montana State Plane
    arcpy.ProjectRaster_management(workdir+InputRaster,workdir+OutputRaster,  "PROJCS['NAD_1983_StatePlane_Montana_FIPS_2500',GEOGCS['GCS_North_American_1983',DATUM['D_North_American_1983',SPHEROID['GRS_1980',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Lambert_Conformal_Conic'],PARAMETER['False_Easting',600000.0],PARAMETER['False_Northing',0.0],PARAMETER['Central_Meridian',-109.5],PARAMETER['Standard_Parallel_1',45.0],PARAMETER['Standard_Parallel_2',49.0],PARAMETER['Latitude_Of_Origin',44.25],UNIT['Meter',1.0]]", "NEAREST", "0.432773465057994 0.432799879454038", "WGS_1984_(ITRF00)_To_NAD_1983", "", "GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]]")
    # UTM to Montana Stateplane project
    # "PROJCS['NAD_1983_StatePlane_Montana_FIPS_2500',GEOGCS['GCS_North_American_1983',DATUM['D_North_American_1983',SPHEROID['GRS_1980',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Lambert_Conformal_Conic'],PARAMETER['False_Easting',600000.0],PARAMETER['False_Northing',0.0],PARAMETER['Central_Meridian',-109.5],PARAMETER['Standard_Parallel_1',45.0],PARAMETER['Standard_Parallel_2',49.0],PARAMETER['Latitude_Of_Origin',44.25],UNIT['Meter',1.0]]", "NEAREST", "1 1", "WGS_1984_(ITRF00)_To_NAD_1983", "", "PROJCS['WGS_1984_Web_Mercator_Auxiliary_Sphere',GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Mercator_Auxiliary_Sphere'],PARAMETER['False_Easting',0.0],PARAMETER['False_Northing',0.0],PARAMETER['Central_Meridian',0.0],PARAMETER['Standard_Parallel_1',0.0],PARAMETER['Auxiliary_Sphere_Type',0.0],UNIT['Meter',1.0]]")

    # Delete original file
    os.remove(InputRaster)
