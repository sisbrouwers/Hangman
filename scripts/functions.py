# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 21:01:07 2024

@author: sofie
"""

def create_solution(word):
    return "-" * len(word)
    
def update_solution(letter, word, solution):
    """
    Updates the solution if the provided letter is a part of the hidden word
    and returns the updated solution.
    
    Parameters
    ----------
    letter : This represents a guessed letter input by the player. Each guessed letter is checked against the word, and if it’s correct, the update_solution function replaces the appropriate dashes in the solution with the guessed letter
    word : This represents the word to be guessed in the Hangman game. It is collected from user input, and it serves as the hidden word that the player will try to guess.
    solution : This represents the current state of the guessed word, initially displayed as a series of dashes that match the length of the word. The function create_solution initializes solution to dashes, and each correct guess reveals part of this solution

    """
    for i in range(0, len(word)):
        if (letter[0].lower() == word[i].lower() and solution[i] == "-"):
            solution = solution[:i] + word[i] + solution[i + 1:]
    return solution

def test_correct_solution():
    word = "Anaconda"
    letter = "a"
    solution = create_solution(word)
    
    new_solution = update_solution(letter, word, solution)
    assert new_solution == "A-a----a"