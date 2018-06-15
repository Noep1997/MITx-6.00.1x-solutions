"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
HKS Python Pilot Program -- Summer 2018
Philippe Noël
Problem Set 3 - Problem 1
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    for letter in secretWord:
        if letter not in lettersGuessed:
            # if any letter from the word isn't guessed, can return False
            # straight away
            return False
    # all letters were in the array, return True
    return True
