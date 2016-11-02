# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 15:09:28 2016

@author: pyakovlev
"""

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-c', '--course')
parser.add_argument('-t', '--title')
parser.add_argument('-n', '--name',) 
parser.add_argument('-s', '--school', default='My U')

args = parser.parse_args()