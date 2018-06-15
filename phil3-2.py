"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
HKS Python Pilot Program -- Summer 2018
Philippe Noël
Problem Set 3 - Problem 2
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    word = '' # initialize empty word
    for letter in secretWord:
        # if letter has been guessed, we display it
        if letter in lettersGuessed:
            word += letter
        # if the letter hasn't been guessed, we add an underscore to indicate it
        else:
            word += '_ '
    # render success, full current state of the word is built
    return word
