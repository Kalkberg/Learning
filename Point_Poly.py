# -*- coding: utf-8 -*-
"""
Generates a plot of probabilities of point density in a polygon:
    
Input data in csv format:
    PointsFile - List of points with fields: MinAge, MaxAge, Lat, Long
    PolysFile - List of polygons with fields: PolygonNumber, Lat, Long
        Note: Polygon number should be from 0 to n
    PolysName - List of polygon names to associate with numbers
    AgeMin - Minmum age to consider
    AgeMax - Maximum age to consider
    AgeInt - Bin size for plotting
    Output - Stem of name for output data
        
    
Output:
    FigA1 to Fig An - Number of points in polygon n over time
    FigB - All figures A on a single plot

@author: Kalkberg
"""
import numpy as np
import matplotlib.path as path

# Inputs
PointsFile = 'NAM_Volc_Min_Max.csv'
PolysFile = 'Polys.csf'
PolysName = ('Mojave','NV','NVID','NVUT','ORID','ORNV')
AgeMin = 0
AgeMax = 36
AgeInt = 0,5
Output = 'Volc'

# Read in data, cut out headers and redistribute to variables
Points = np.genfromtxt(PointsFile, delimiter=',')
Points = np.delete(Points, (0), axis=0)
PointAgeMin, PointAgeMax, PointLat, PointLong = Points[:,0], Points[:,1], \
                                          Points[:,2], Points[:,3]
Polys = np.genfromtxt(PolysFile, delimiter=',')
Polys = np.delete(Polys, (0), axis=0)
PolyNo, PolyLat, PolyLong = Polys[:,0], Polys[:,1], Polys[:,2]

# Create empty list of points in each polygon
# Columns for each polygon are n=AgeMin, n+1=AgeMax, n+2=Lat, n+3=Long
PointList = np.zeros([0,4*(PolyNo.max()+1)])

# Append points to an array of data for each polygon
for i in range(0,PolyNo.max()):
    Polygon = np.zeros([0,2]) # Empty polygon for next step
    # Create array defining polygon
    for j in range(0, len(PolyNo)):
        if PolyNo == i:
            Polygon = np.append(Polygon,[[PolyLong[j],PolyLat[j]]],axis=0)
    
    PolyPath = path.Path(Polygon) # Create path using matplotlib.path
    PointListPoly = np.zeros([0,4]) # Empty list of points in a set polygon
    
    # Check if points are in the polygon, if so append to list 
    for k in range(0,len(PointLat)):
        if PolyPath.contains_point((PointLong[k],PointLat[k])) == True:
            PointListPoly = np.append(PointListPoly,[[PointAgeMin[k], 
                            PointAgeMax[k], PointLat[k], PointLong[k]]])
    
    # Append to master list of data for each polygon 
    PointList = np.append(PointList,PointListPoly,axis=1)



                                        
                                        
                                                
