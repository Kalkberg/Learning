# -*- coding: utf-8 -*-
"""
MIT Open Courseware 6.189, Homework 1, Optional Exercise 2

Secret Messages

@Kalkberg
"""
# Have user put in data
input_phrase = input('Enter Phrase to be encoded: ')
shift = int(input('Enter shift value: '))

encoded_phrase = ''

for i in range(0, len(input_phrase)):
    if input_phrase[i].isalpha() == True:
        if input_phrase[i].istitle() == True:
            original_value = ord(input_phrase[i]) - 64
            encoded_value = (original_value + shift)%26 + 64
        else:
            original_value = ord(input_phrase[i]) - 96
            encoded_value = (original_value + shift)%26 + 96
        encoded_phrase += chr(encoded_value)
    else:
        encoded_phrase += input_phrase[i]
        
print(encoded_phrase)