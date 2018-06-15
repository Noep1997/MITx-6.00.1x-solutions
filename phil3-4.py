"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
HKS Python Pilot Program -- Summer 2018
Philippe Noël
Problem Set 3 - Problem 4
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

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

    # play the rounds
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
