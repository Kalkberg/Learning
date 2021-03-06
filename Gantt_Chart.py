# -*- coding: utf-8 -*-
"""
Gantt chart with plotly. Currently written for proposed EPSCoR grant.

@author: Kalkberg
"""

#import plotly.plotly as py
#import plotly
#import plotly.figure_factory as ff
#
df = [dict(Task="Field Planning", Start='2019-01-01', Finish='2019-02-01', Resource='PI & Student'),
      dict(Task="Trenching", Start='2019-05-01', Finish='2019-07-01', Resource='PI & Student'),
      dict(Task="CRN Sampling", Start='2019-07-01', Finish='2019-08-01', Resource='PI & Student'),
      dict(Task="Sample Preparation", Start='2019-08-01', Finish='2019-08-15', Resource='Student'),
      dict(Task="Sample Analysis", Start='2019-08-15', Finish='2020-01-01', Resource='Contractor'),
      dict(Task="Data Analysis", Start='2020-01-01', Finish='2020-02-01', Resource='PI & Student'),
      dict(Task="Data Interpertation", Start='2020-02-01', Finish='2020-05-01', Resource='PI & Student'),
      dict(Task="Workshop Planning", Start='2020-01-01', Finish='2020-03-01', Resource='PI'),
      dict(Task="UGS Workshop", Start='2019-02-01', Finish='2019-02-15', Resource='PI'),
      dict(Task="UGS Workshop", Start='2020-02-01', Finish='2020-02-15', Resource='PI & Student'),
      dict(Task="Conference", Start='2020-11-01', Finish='2020-12-01', Resource='PI & Student'),
      dict(Task="Senior Thesis", Start='2020-09-01', Finish='2021-05-01', Resource='Student'),
      dict(Task="Manuscript Prep", Start='2020-09-01', Finish='2021-05-01', Resource='PI & Student'),]
##
#colors = {'PI':'rgb(255,0,0)','Student':'rgb(0,0,255)',
#          'PI & Student':'rgb(255,0,255)','Contractor':'rgb(255,255,0)'}
#
#fig = ff.create_gantt(df, colors=colors, index_col='Resource', show_colorbar=True, group_tasks=True)
#plotly.offline.plot(fig, filename='gantt-use-a-pandas-dataframe')

from bokeh.plotting import figure, show, output_notebook, output_file
from bokeh.models import ColumnDataSource, Range1d
from bokeh.models.tools import HoverTool
from datetime import datetime
from bokeh.charts import Bar
output_notebook()
#output_file('GanntChart.html') #use this to create a standalone html file to send to others
import pandas as ps

DF=ps.DataFrame(columns=['Item','Start','End','Color'])
Items=[
    ['Contract Review & Award','2015-7-22','2015-8-7','red'],
    ['Submit SOW','2015-8-10','2015-8-14','gray'],
    ['Initial Field Study','2015-8-17','2015-8-21','gray'],
    ['Topographic Procesing','2015-9-1','2016-6-1','gray'],
    ['Init. Hydrodynamic Modeling','2016-1-2','2016-3-15','gray'],
    ['Prepare Suitability Curves','2016-2-1','2016-3-1','gray'],
    ['Improvement Conceptual Designs','2016-5-1','2016-6-1','gray'],
    ['Retrieve Water Level Data','2016-8-15','2016-9-15','gray'],
    ['Finalize Hydrodynamic Models','2016-9-15','2016-10-15','gray'],
    ['Determine Passability','2016-9-15','2016-10-1','gray'],
    ['Finalize Improvement Concepts','2016-10-1','2016-10-31','gray'],
    ['Stakeholder Meeting','2016-10-20','2016-10-21','blue'],
    ['Completion of Project','2016-11-1','2016-11-30','red']
    ] #first items on bottom

for i,Dat in enumerate(Items[::-1]):
    DF.loc[i]=Dat

#convert strings to datetime fields:
DF['Start_dt']=ps.to_datetime(DF.Start)
DF['End_dt']=ps.to_datetime(DF.End)


G=figure(title='Project Schedule',x_axis_type='datetime',width=800,height=400,y_range=DF.Item.tolist(),
        x_range=Range1d(DF.Start_dt.min(),DF.End_dt.max()), tools='save')

hover=HoverTool(tooltips="Task: @Item<br>\
Start: @Start<br>\
End: @End")
G.add_tools(hover)

DF['ID']=DF.index+0.8
DF['ID1']=DF.index+1.2
CDS=ColumnDataSource(DF)
G.quad(left='Start_dt', right='End_dt', bottom='ID', top='ID1',source=CDS,color="Color")
#G.rect(,"Item",source=CDS)
show(G)