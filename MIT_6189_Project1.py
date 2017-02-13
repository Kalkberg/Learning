# -*- coding: utf-8 -*-
"""


MIT Open Courseware 6.189, Project 1 Hangman

Pig latin

@author: Kalkberg
"""

def alltrue(some_list, valtest):
    out = None
    for val in some_list:
        if val < valtest:
            out = True
        else:
            out = False
            break
    return out

def onetrue(some_list, valtest):
    out = None
    for val in some_list:
        if val < valtest:
            out = True
            break
        else:
            out = False
    return out

# Import statements: DO NOT delete these! DO NOT write code above this!
from random import randrange
from string import *

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
# Import hangman words

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print ("  ", len(wordlist), "words loaded.")
    print ('Enter play_hangman() to play a game of hangman!')
    return wordlist

# actually load the dictionary of words and point to it with 
# the words_dict variable so that it can be accessed from anywhere
# in the program
words_dict = load_words()


# Run get_word() within your program to generate a random secret word
# by using a line like this within your program:
# secret_word = get_word()

def get_word():
    """
    Returns a random word from the word list
    """
    word=words_dict[randrange(0,len(words_dict))]
    return word

# end of helper code
# -----------------------------------


# CONSTANTS
MAX_GUESSES = 6

# GLOBAL VARIABLES 
secret_word = 'claptrap' 
letters_guessed = []

# From part 3b:
def word_guessed():
    '''
    Returns True if the player has successfully guessed the word,
    and False otherwise.
    '''
    global secret_word
    global letters_guessed

    ####### YOUR CODE HERE ######
    out = None
    for i in range(0,len(secret_word)-1):
        if secret_word[i] in letters_guessed:
            out = True
        else:
            out = False
            break
    return out

def print_guessed():
    '''
    Prints out the characters you have guessed in the secret word so far
    '''
    global secret_word
    global letters_guessed
    
    ####### YOUR CODE HERE ######
    out = ''
    for i in range(0,len(secret_word)-1):
        if secret_word[i] in letters_guessed:
            out += secret_word[i]
        else:
            out += '-'
    print(out)

def play_hangman():
    # Actually play the hangman game
    global secret_word
    global letters_guessed
    global MAX_GUESSES
    global words_dict
    
    # Put the mistakes_made variable here, since you'll only use it in this function
    mistakes_made = 0

    # Update secret_word. Don't uncomment this line until you get to Step 8.
    # secret_word  = get_word()

    ####### YOUR CODE HERE ######
    guesses = 0
    
    while (guesses < MAX_GUESSES+1):
        print('%s guesses left!'%(MAX_GUESSES-guesses))
        print_guessed()
        guess_let = input('Print the letter you want to guess: ')
        guess_let.lower()
        
        # Check if letter has been guessed
        if guess_let in letters_guessed:
            print('Letter already guessed! Try another one.')
        else:
            letters_guessed += guess_let
            # Check if the letter is in the word
            if guess_let in secret_word:
                print('Got one!')
                
            else:
                print('Sorry, that letter is not in the word')
                mistakes_made
        
        
    return None