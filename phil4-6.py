"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
HKS Python Pilot Program -- Summer 2018
Philippe Noël
Problem Set 4 - Problem 6
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.

    1) Asks the user to input 'n' or 'r' or 'e'.
      * If the user inputs 'n', let the user play a new (random) hand.
      * If the user inputs 'r', let the user play the last hand again.
      * If the user inputs 'e', exit the game.
      * If the user inputs anything else, tell them their input was invalid.

    2) When done playing the hand, repeat from step 1
    """
    # bool condition to track whether we're still playing or not
    playing = True
    while playing:
        # get user action
        action = input("Enter n to deal a new hand, r to replay the last hand, or e to end game: ")
        # dealing new hand
        if action == 'n':
            # deal a new hand and play it, no exception possible here
            hand = dealHand(HAND_SIZE)
            playHand(hand, wordList, HAND_SIZE)
        # call to replay the last hand
        elif action == 'r':
            # potential exception here if there was no last hand
            try:
                playHand(hand, wordList, HAND_SIZE)
            except:
                # this will trigger if there is no "hand" yet
                print("You have not played a hand yet. Please play a new hand first!")
        # call for exiting the game
        elif action == 'e':
            playing = False
        # call for invaliad command (not n, r or e)
        else:
            print("Invalid command.")
