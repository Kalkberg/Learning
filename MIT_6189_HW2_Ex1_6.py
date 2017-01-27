# -*- coding: utf-8 -*-
"""
MIT Open Courseware 6.189, Homework 1, Exercise 1.7

Nims/Stones game

@param pile: Number of stones to start with
@param max_stones: Maximum number of stones one can take in a turn

@Kalkberg
"""
def stones(pile, max_stones):  
    print('%s stones in the pile. Players can take up to %s stones'
          %(pile, max_stones))
    
    # Counters
    turn = 1 # Whose turn it is
    
    
    def take_stones(pile):
        take = 0 # Number of stones to take
        # Get input and check if input is valid
        while take == 0: 
            take = input('Player %s: '
                         'How many stones would you like to take? ' %turn)
            if (take.isdigit() == False  
                or int(take) < 1
                or int(take) > max_stones):
                print('Wrong input! '  
                      'Number of stones can only be a positive interger '
                      'between 1 and %s!' %max_stones)
                take = 0 # reset counter so that while statement is still true
            if int(take) > pile:
                print('Not enough stones in the pile! Take fewer!')
                take = 0
        return int(take)
    
    while pile > 0:
        while turn == 1:
            take_no = take_stones(pile) # Get input on number of stones to take
            # Remove stones from pile and make it the next player's turn
            pile -= take_no
            print('%s stones left in the pile!' %pile)
            turn += 1
        if pile <1:
            break
        while turn == 2:
            take_no = take_stones(pile)
            # Remove stones from pile and make it the next player's turn
            pile -= take_no
            print('%s stones left in pile!' %pile)
            turn -= 1
    
    # Evaluate winner
    if turn == 1:
        winner = 2
    if turn == 2:
        winner = 1
    
    # Print who won. Note the turn counter will be evaluated as the OTHER player!
    print('Game over! Player %s wins!' %winner)