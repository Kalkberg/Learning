# -*- coding: utf-8 -*-
"""
Takes fossil data and plots as vertical bars

@author: Kalkberg
"""

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import pandas

matplotlib.rcParams['pdf.fonttype'] = 'truetype'

data = pandas.read_csv('Glen_Fossils.csv')

fig, ax = plt.subplots(figsize=(9,5))

ax.bar(x=range(len(data.loc[data['Mantle']=='x']['Age Min'])), 
        height=data.loc[data['Mantle']=='x']['Age Max']-data.loc[data['Mantle']=='x']['Age Min'], 
        bottom=data.loc[data['Mantle']=='x']['Age Min'], width=1)

ax.xaxis.set_ticks(range(len(data.loc[data['Mantle']=='x']['Age Min'])))
labels = data.loc[data['Mantle']=='x']['Species'].tolist()
ax.set_xticklabels(labels,rotation='vertical',style='italic')
plt.tight_layout()
plt.title('Mantle Ranch')
plt.savefig('Fossils_Mantle.pdf')
plt.cla()

ax.bar(x=range(len(data.loc[data['Diamond']=='x']['Age Min'])), 
        height=data.loc[data['Diamond']=='x']['Age Max']-data.loc[data['Diamond']=='x']['Age Min'], 
        bottom=data.loc[data['Diamond']=='x']['Age Min'], width=1)

ax.xaxis.set_ticks(range(len(data.loc[data['Diamond']=='x']['Age Min'])))
labels = data.loc[data['Diamond']=='x']['Species'].tolist()
ax.set_xticklabels(labels,rotation='vertical',style='italic')
plt.tight_layout()
plt.title('Diamond Ranch')
plt.savefig('Fossils_Diamond.pdf')
plt.cla()

ax.bar(x=range(len(data.loc[data['MM East']=='x']['Age Min'])), 
        height=data.loc[data['MM East']=='x']['Age Max']-data.loc[data['MM East']=='x']['Age Min'], 
        bottom=data.loc[data['MM East']=='x']['Age Min'], width=1)

ax.xaxis.set_ticks(range(len(data.loc[data['MM East']=='x']['Age Min'])))
labels = data.loc[data['MM East']=='x']['Species'].tolist()
ax.set_xticklabels(labels,rotation='vertical',style='italic')
plt.tight_layout()
plt.title('McCartney East')
plt.savefig('Fossils_MM_East.pdf')

plt.cla()

ax.bar(x=range(len(data.loc[data['MM West']=='x']['Age Min'])), 
        height=data.loc[data['MM West']=='x']['Age Max']-data.loc[data['MM West']=='x']['Age Min'], 
        bottom=data.loc[data['MM West']=='x']['Age Min'], width=1)

ax.xaxis.set_ticks(range(len(data.loc[data['MM West']=='x']['Age Min'])))
labels = data.loc[data['MM West']=='x']['Species'].tolist()
ax.set_xticklabels(labels,rotation='vertical',style='italic')
plt.tight_layout()
plt.title('McCartney West')
plt.savefig('Fossils_MM_West.pdf')
plt.cla()

ax.bar(x=range(len(data['Age Min'])), 
        height=data['Age Max']-data['Age Min'], 
        bottom=data['Age Min'], width=1)

ax.xaxis.set_ticks(range(len(data['Age Min'])))
labels = data['Species'].tolist()
ax.set_xticklabels(labels,rotation=90,style='italic')
plt.tight_layout()
plt.title('All')
plt.savefig('Fossils_All.pdf')