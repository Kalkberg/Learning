# -*- coding: utf-8 -*-
"""
Reads values from specified cells of a spreadsheet

@author: Kalkberg
"""

import win32com.client as win32

excel = win32.Dispatch('Excel.Application')
wb = excel.Workbooks.Open(r'D:\Github\Learning\Test_Sheet.xlsx')
ws = wb.Worksheets('Sheet1')
#ws.EnableCalculation = True
#ws.Calculate()

val = ws.Cells(2,1).Value
print(val)

# release resources
ws = None
wb = None
excel = None
