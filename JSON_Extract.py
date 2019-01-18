# -*- coding: utf-8 -*-
"""
Extracts data from a GeoJSON file

@author: Kalkberg
"""

import requests

countries = requests.get('https://d2ad6b4ur7yvpq.cloudfront.net/naturalearth-3.3.0/ne_110m_admin_0_countries.geojson').json()

names = [[],[],[]]

for i in range(len(countries['features'])):
    names[0].append(countries['features'][i]['properties']['name'])
    names[1].append(countries['features'][i]['geometry']['coordinates'])

[x for len(countries['features']) in countries['features'][x]['properties']['name']]