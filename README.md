# Learning
Scripts generated while learning Python. In rare cases, actually useful for something.

args_parser.py - Learned how to parse input arguments.

beachball.py - Makes a KMZ of moment tensor solutions from input csv of earthquake data. Currently configured for the Montana Regional Seismic Network.

ColorRamp.py - Learned how to make custom color ramps. Code mainly sourced from StackOverflow answer linked in code.

extract_sar.py - Takes ENVI or ERS SAR data obtained from WinSAR, extracts, and renames files for use in WIN5SAR.

MIT_6189* - *Scripts written while working through MIT's open courseware for course 6.189 - A gentle introduction to Python

MomentTensor - Convert strike, dip, and rake to harvard moment tensor solution. Not working.

pdf_writer.py - Learned how to make a table from a bunch of data in LaTeX and ouput it to a PDF.

plotting.py - Learned how to make and save basic plots to PDF format.

Plot_Anim.py - Takes a csv of age, lat, and long data and makes an animation with a geographic basemap.

Plot_Anim_Hexbin.py - Same as Plot_Anim but makes hexbins of data. Implementation is different as hexbin is not iterable for matplotlib's animation toolbox. Uses ffmpeg executable instead. Includes sending a command to ffmpeg which includes user input and is therefore a huge security issue. Since there is no windows version of ffmpeg for python at the moment, there may not be a workaround. 

PTBAxes - obtain P, T, and B axes orientations from strike, dip and rake data.

