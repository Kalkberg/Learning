# -*- coding: utf-8 -*-
"""
MIT Open Courseware 6.189, Homework 1, Exercise 1.7

Pig latin

@Kalkberg
"""

word = input('Input word to translate to pig latin: ')

vowels = ['a','e','i','o','u']

pigword = ''

if word[0] in vowels:
    pigword = word + 'hay' 
else:
    pigword = word[1:] + 'ay'

print(pigword)

for i in range(1,2)):
    for i 
