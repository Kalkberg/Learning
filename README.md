# Learning
Scripts generated while learning Python. In rare cases, actually useful for something.
All files in this repository are licensed under the Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License, unless noted otherwise. 
To view a copy of this license, visit http://creativecommons.org/licenses/by-nc-nd/4.0/ 
or send a letter to Creative Commons, PO Box 1866, Mountain View, CA 94042, USA.

args_parser.py - Learned how to parse input arguments.

beachball.py - Makes a KMZ of moment tensor solutions from input csv of earthquake data. Currently configured for the Montana Regional Seismic Network.

ColorRamp.py - Learned how to make custom color ramps. Code mainly sourced from StackOverflow answer linked in code.

extract_sar.py - Takes ENVI or ERS SAR data obtained from WinSAR, extracts, and renames files for use in WIN5SAR.

Field_Trip_KMZ.py - Takes a csv of lats, longs, point names, and point descriptions and makes a KMZ of the points and metadata. Currently formatted to produce field trips for the Tobacco Root Gelogical Society.

grd_cut.py - Cuts .grd files using GMT

grd_convert - Helper script for taking velocity files produced by GMT5SAR, and generating
NetCDF grids with lat/long coordinates

Grid_Map.py - Takes a set of points with values at lat and long coordinates and creates a map in the region of interest.

MIT_6189* - *Scripts written while working through MIT's open courseware for course 6.189 - A gentle introduction to Python

MomentTensor - Convert strike, dip, and rake to harvard moment tensor solution. Not working.

netCDF_Plot.py - Plots netCDF data. Currently configured to plot dynamic topography derived from Molnar et al., 2015

pdf_writer.py - Learned how to make a table from a bunch of data in LaTeX and ouput it to a PDF.

plotting.py - Learned how to make and save basic plots to PDF format.

Plot_Anim.py - Takes a csv of age, lat, and long data and makes an animation with a geographic basemap.

Plot_Anim_Hexbin.py - Same as Plot_Anim but makes hexbins of data. Implementation is different as hexbin is not iterable for matplotlib's animation toolbox. Instead prints each frame and combines them into a movie using the moviepy library.

Plot_Anim_Hexbin_median_Val.py - Same as Plot_Anim_Hexbin but calculates median value in each hexbin.

Point_Poly.py - Takes a list of polygons, and a list of data with min/max ages, and lat/long data. Then estimates requency of samples in each polygon.

PTBAxes.py - obtain P, T, and B axes orientations from strike, dip and rake data.

SBAS_Rename.py - Helper script to renames GMT5SAR files for SBAS after making a stack of interferograms.
