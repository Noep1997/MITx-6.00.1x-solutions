# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

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


def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # initialize vars
    guesses, mistakes = [], 0
    playing = True # boolean var to keep track of whether the game is still on

    # print the opening game statement
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is %d letters long." % len(secretWord))
    print("-------------")

    while playing:
        # opening message of the current round
        print("You have %i guesses left." % (8 - mistakes))
        print("Available letters: ", getAvailableLetters(guesses))
        # get the letter guess of the user
        guess = (input("Please guess a letter: ")).lower() # lowering

        # first we check if it's a new guess or not
        if guess in guesses:
            print("Oops! You've already guessed that letter: ", getGuessedWord(secretWord, guesses) )
            print("-------------")
        # case where this is a new guess, can either be right or wrong
        else:
            # add new guess to our list
            guesses.append(guess)

            # case where the letter is in the word
            if guess in secretWord:
                print("Good guess: ", getGuessedWord(secretWord, guesses))
            # case where the letter isn't in the word
            else:
                print ("Oops! That letter is not in my word: ", getGuessedWord(secretWord, guesses))
                mistakes += 1 # increment mistake since we only allow 8
            # stupid formatting
            print("-------------")

            # check the state of the game (win/loss)
            if isWordGuessed(secretWord, guesses):
                # user won, switch boolean condition and terminate
                print("Congratulations, you won!")
                playing = False
            # too many mistakes, user lost
            elif mistakes == 8:
                print("Sorry, you ran out of guesses. The word was ", secretWord)
                playing = False


# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
