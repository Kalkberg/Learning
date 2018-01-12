# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 14:55:04 2018

@author: pyakovlev
"""

import pandas as pandas
import seaborn as sbrn

Rocks = pandas.read_csv('Tibet_Volc_for_plotting8csv.csv')

Rocks['Age_Ma']=Rocks['Age_Ma'].apply(pandas.to_numeric, errors='coerce')

LhasaYoung = Rocks[(Rocks['Zone']=='South')&(Rocks['Age_Ma']<46)&(Rocks['Type']=='Extrusive')]
BadFe=LhasaYoung[LhasaYoung['FeO_t_calc']>8]
BadP=LhasaYoung[LhasaYoung['P2O5']<0.1]

sbrn.regplot(x=LhasaYoung['MgO'],y=LhasaYoung['FeO_t_calc'], fit_reg=False)