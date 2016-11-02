# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 10:29:33 2016

Simple script to generate a PDF file of a table

@author: pyakovlev
"""
from argparse import Namespace
import os
import subprocess

a=1
b=2
c=3
d=4
e=5
f=6
g=7
h=8
i=9
j=10
k=11
l=12
m=13
n=14
o=15
p=16

args=Namespace(a=a, b=b, c=c, d=d, e=e, f=f, g=g, h=h, i=i, j=j, k=k, l=l, m=m,
               n=n, o=o, p=p)

content = r'''\documentclass[english]{article}
\usepackage[latin9]{inputenc}
\makeatletter
\providecommand{\tabularnewline}{\\}
\makeatother
\usepackage{babel}
\begin{document}
\begin{tabular}{|c|c|c|c|c|c|}
\cline{2-6} 
\multicolumn{1}{c|}{} & b & c & d & e & f\tabularnewline
\hline 
w & %(a)s & %(b)s & %(c)s & %(d)s & unit1\tabularnewline
\hline 
x & %(e)s & %(f)s & %(g)s & %(h)s & unit2\tabularnewline
\hline 
y & %(i)s & %(j)s & %(k)s & %(l)s & unit3\tabularnewline
\hline 
z & %(m)s & %(n)s & %(o)s & %(p)s & unit4\tabularnewline
\hline 
\end{tabular}
\end{document}
 '''

with open('table.tex','w') as f:
    f.write(content%args.__dict__)
    
cmd = [r'C:\Program Files (x86)\MiKTeX 2.9\miktex\bin\pdflatex.exe',
       '-interaction', 'nonstopmode', 'table.tex']
proc = subprocess.Popen(cmd)
proc.communicate()

retcode = proc.returncode
if not retcode == 0:
    os.unlink('table.pdf')
    raise ValueError('Error {} executing command: {}'.format(retcode, ' '.join(cmd))) 

os.unlink('table.tex')
os.unlink('table.log')
os.unlink('table.aux')