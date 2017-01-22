# -*- coding: utf-8 -*-
"""
MIT Open Courseware 6.189, Homework 1, Exercise 1.7

Rock Paper Scisors

@Kalkberg
"""

def input_check(data):
    if (data != 'rock' and data != 'scissors' and data != 'paper'):
        print('This is not a valid object selection')

p1 = input('Player 1? ')
input_check(p1)
p2 = input('Player 2? ')
input_check(p2)

if p1 == 'rock':
    if p2 == 'rock':
        print('Tie')
    elif p2 == 'scissors':
        print('Player 1 wins')
    elif p2 == 'paper':
        print('Player 2 wins')

if p1 == 'paper':
    if p2 == 'rock':
        print('Player 1 wins')
    elif p2 == 'scissors':
        print('Player 2 wins')
    elif p2 == 'paper':
        print('Tie')

if p1 == 'scisors':
    if p2 == 'rock':
        print('Player 2 wins')
    elif p2 == 'scissors':
        print('Tie')
    elif p2 == 'paper':
        print('Player 1 wins')