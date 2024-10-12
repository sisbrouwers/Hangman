# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 16:14:41 2024

@author: sofie
"""

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

strikes = 0
solution = "-" * len(word)

print(solution)

while strikes < 6:
    letter = input("Guess a letter: ")
    correct = False
    
    for i in range(0, len(word)):
        if (letter[0].lower() == word[i].lower() and solution[i] == "-"):
            solution = solution[:i] + word[i] + solution[i + 1:]
            correct = True
    
    if (correct == False):
        strikes += 1
    
    print(HANGMAN_PICS[strikes])
    print(solution)
    
    if word == solution:
        print("You won!")
        break
    
if (strikes == 6):
    print("You lost...")
    
            