"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
HKS Python Pilot Program -- Summer 2018
Philippe Noël
Problem Set 4 - Problem 2
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def updateHand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it.

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)
    returns: dictionary (string -> int)
    """
    # make a copy since we don't want to modify the original hand
    hand_copy = hand.copy()
    for letter in word:
        # we assume the word is only made of letters in hand
        hand_copy[letter] -= 1
        # remove instead of displaying 0 if no letters left
        if hand_copy[letter] == 0:
            del hand_copy[letter]
    # render success
    return hand_copy
