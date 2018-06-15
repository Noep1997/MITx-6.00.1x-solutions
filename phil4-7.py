"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
HKS Python Pilot Program -- Summer 2018
Philippe Noël
Problem Set 4 - Problem 7
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.

    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.
          But if no hand was played, output "You have not played a hand yet.
          Please play a new hand first!"

        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    wordList: list (string)
    """
    # bool condition to track whether we're still playing or not
    playing = True
    no_previous_hand = True # to know whether a previous hand was played or not
    while playing:
        # get user action
        action = input("Enter n to deal a new hand, r to replay the last hand, or e to end game: ")
        # dealing new hand
        if action == 'n':
            no_previous_hand = False # we will have played at least 1 hand
            hand = dealHand(HAND_SIZE)
            while playing:
                # we now check if user or computer plays
                player = input("Enter u to have yourself play, c to have the computer play: ")
                # player plays
                if player == 'u':
                    playHand(hand, wordList, HAND_SIZE)
                    break
                # computer plays
                elif player =='c':
                    compPlayHand(hand, wordList, HAND_SIZE)
                    break
                # invalid command, retry
                else:
                    print("Invalid command.") # no break here so it reprompts
        # call to replay the last hand
        elif action == 'r':
            # check if it's the first hand
            if no_previous_hand:
                print("You have not played a hand yet. Please play a new hand first!")
            else:
                # there is a previous hand, so play it
                while playing:
                    # we now check if user or computer plays
                    player = input("Enter u to have yourself play, c to have the computer play: ")
                    # player plays
                    if player == 'u':
                        playHand(hand, wordList, HAND_SIZE)
                        break
                    # computer plays
                    elif player =='c':
                        compPlayHand(hand, wordList, HAND_SIZE)
                        break
                    # invalid command, retry
                    else:
                        print("Invalid command.") # no break here so it reprompts
        # call for exiting the game
        elif action == 'e':
            playing = False
        # call for invaliad command (not n, r or e)
        else:
            print("Invalid command.")
