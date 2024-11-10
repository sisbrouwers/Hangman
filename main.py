# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 16:14:41 2024

@author: sofie
"""

from scripts.functions import create_solution, update_solution

HANGMAN_PICS = ['''
 +---+
     |
     |
     |
    ===''', '''
 +---+
 O   |
     |
     |
    ===''', '''
 +---+
 O   |
 |   |
     |
    ===''', '''
 +---+
 O   |
/|   |
     |
    ===''', '''
 +---+
 O   |
/|\  |
     |
    ===''', '''
 +---+
 O   |
/|\  |
/    |
    ===''', '''
 +---+
 O   |
/|\  |
/ \  |
    ===''']

    
word = input("Enter a word: ")
solution = create_solution(word)

strikes = 0

print(solution)

while strikes < 6:
    letter = input("Guess a letter: ")
    new_solution = update_solution(letter, word, solution)
    
    if (new_solution == solution):
        strikes += 1
    
    solution = new_solution
    
    print(HANGMAN_PICS[strikes])
    print(solution)
    
    if word == solution:
        print("You won!")
        break
    
if (strikes == 6):
    print("You lost...")