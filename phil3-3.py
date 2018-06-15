"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
HKS Python Pilot Program -- Summer 2018
Philippe Noël
Problem Set 3 - Problem 3
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
import string

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    letters_available = '' # initialize empty string
    for letter in string.ascii_lowercase:
        if letter not in lettersGuessed:
            letters_available += letter
    return letters_available
