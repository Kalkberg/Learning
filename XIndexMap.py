# -*- coding: utf-8 -*-
"""
Interactive Map showing custom index of countries

@author: Kalkberg
"""

''' Present an interactive function explorer with slider widgets.
Scrub the sliders to change the properties of the ``sin`` curve, or
type into the title text box to update the title of the plot.
Use the ``bokeh serve`` command to run the example by executing:
    bokeh serve sliders.py
at your command prompt. Then navigate to the URL
    http://localhost:5006/sliders
in your browser.
'''

import numpy as np
import requests
import yaml
import pandas as pd
import cartopy.io.shapereader as shpreader
import shapefile

from bokeh.io import curdoc
from bokeh.layouts import row, widgetbox
from bokeh.models.widgets import Slider, TextInput
from bokeh.plotting import figure
from bokeh.palettes import Viridis6 as palette
from bokeh.models import (
    ColumnDataSource,
    HoverTool,
    LogColorMapper
)


#from bokeh.sampledata.us_counties import data as counties
#from bokeh.sampledata.unemployment import data as unemployment
#
#palette.reverse()
#
##set up data
#counties = {
#    code: county for code, county in counties.items() if county["state"] == "tx"
#}
#
#county_xs = [county["lons"] for county in counties.values()]
#county_ys = [county["lats"] for county in counties.values()]
#
#county_names = [county['name'] for county in counties.values()]
#county_rates = [unemployment[county_id] for county_id in counties]
#color_mapper = LogColorMapper(palette=palette)
#
#source = ColumnDataSource(data=dict(
#    x=county_xs,
#    y=county_ys,
#    name=county_names,
#    rate=county_rates,
#))


CountriesShape = shpreader.natural_earth(resolution='110m',
                    category='cultural', name='admin_0_countries') 
CountryShapes = shapefile.Reader(CountriesShape).shapes()



for country in CountryShapes:
    for point in CountryShapes[country]:
        x = CountryShapes[country].points[point][0]
        y = CountryShapes[country].points[point][1]


# Get json data for countries and put into data frame
countries = requests.get('https://d2ad6b4ur7yvpq.cloudfront.net/naturalearth-3.3.0/ne_110m_admin_0_countries.geojson').json()
countryObject = [[],[],[]]
for country in countries['features']:
    countryObject.append([
       [country['properties']['name']],
       [[x[0] for x in country['geometry']['coordinates'][0]]],
       [[x[1] for x in country['geometry']['coordinates'][0]]],
    ])
df = pd.DataFrame(countryObject)

# Set up plot
TOOLS = "pan,wheel_zoom,reset,hover,save"
plot = figure(
    width = 800, 
    height=400, 
    title='World Countries', 
    x_axis_label='Longitude',
    y_axis_label='Latitude',
)

plot.grid.grid_line_color = None
plot.patches('x', 'y', source=source,
          fill_color={'field': 'rate', 'transform': color_mapper},
          fill_alpha=0.7, line_color="white", line_width=0.5)


## Set up plot
#TOOLS = "pan,wheel_zoom,reset,hover,save"
#plot = figure(
#    title="Texas Unemployment, 2009", tools=TOOLS,
#    x_axis_location=None, y_axis_location=None
#)
#
#plot.grid.grid_line_color = None
#plot.patches('x', 'y', source=source,
#          fill_color={'field': 'rate', 'transform': color_mapper},
#          fill_alpha=0.7, line_color="white", line_width=0.5)

# Set up widgets
text = TextInput(title="title", value='my sine wave')
offset = Slider(title="offset", value=0.0, start=-5.0, end=5.0, step=0.1)
amplitude = Slider(title="amplitude", value=1.0, start=-5.0, end=5.0, step=0.1)
phase = Slider(title="phase", value=0.0, start=0.0, end=2*np.pi)
freq = Slider(title="frequency", value=1.0, start=0.1, end=5.1, step=0.1)

hover = plot.select_one(HoverTool)
hover.point_policy = "follow_mouse"
hover.tooltips = [
    ("Name", "@name"),
    ("Unemployment rate)", "@rate%"),
    ("(Long, Lat)", "($x, $y)"),
]

# Set up callbacks
def update_title(attrname, old, new):
    plot.title.text = text.value

text.on_change('value', update_title)

def update_data(attrname, old, new):

    # Get the current slider values
    a = amplitude.value
    b = offset.value
    w = phase.value
    k = freq.value

    # Generate the new curve
    rates = [i + b for i in county_rates]

    source.data = dict(    
            x=county_xs,
            y=county_ys,
            name=county_names,
            rate=rates,)

for w in [offset]:
    w.on_change('value', update_data)


# Set up layouts and add to document
inputs = widgetbox(text, offset, amplitude, phase, freq)

curdoc().add_root(row(inputs, plot, width=800))
curdoc().title = "Sliders"