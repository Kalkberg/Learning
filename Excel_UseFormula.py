# -*- coding: utf-8 -*-
"""
Puts values into a spreadsheet and takes out calculated values and plot result

@author: Kalkberg
"""

import win32com.client as win32
import numpy as np
import matplotlib.pyplot as plot

excel = win32.Dispatch('Excel.Application')
wb = excel.Workbooks.Open(r'D:\Github\Learning\Test_Sheet.xlsx')
ws = wb.Worksheets('Sheet1')
ws.EnableCalculation = True
ws.Calculate()

x = np.linspace(0,10,11)
y = np.zeros(11)

for i in range(len(x)):
    ws.Cells(1,2).Value=x[i]
    ws.Calculate()
    y[i]=ws.Cells(3,2).Value

# release resources
ws = None
wb = None
excel = None

plot.plot(x,y, 'ko')
