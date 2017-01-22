# -*- coding: utf-8 -*-
"""
MIT Open Courseware 6.189, Homework 1, Optional Exercise 1

Zeller's Algorithm

@Kalkberg
"""

date = '0'

# Get input and make sure it's not wonky.
while (int(date) <= 0 and len(date) != 6):
    date = input('Enter date in DDMMYYYY format: ')
    if (int(date) <= 0 and len(date) != 6):
        print('Unknown format!')
    if (int(date[0:2]) < 1 or int(date[0:2]) > 31):
        print ('Valid days can only be between 1 and 31!')
    if (int(date[2:4]) < 1 or int(date[2:4]) > 12):
        print ('Valid months can only be between 1 and 12!')


Day = int(date[0:2])
Month = int(date[2:4])
Century = int(date[4:6])
Year = int(date[6:8])

if Month < 3:
    Year -= 1
    Month += 10
else:
    Month -= 2

W = (13*Month - 1) / 5
X = Year / 4
Y = Century / 4
Z = W + X + Y + Day + Year - 2*Century
R = int(Z%7)

if R < 0:
    R +=7

if R == 0:
    print('This is a Sunday')
elif R == 1:
    print('This is a Monday')
elif R == 2:
    print('This is a Tuesday')
elif R == 3:
    print('This is a Wednesday')
elif R == 4:
    print('This is a Thursday')
elif R == 5:
    print('This is a Friday')
elif R == 6:
    print('This is a Saturday')