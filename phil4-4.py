"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
HKS Python Pilot Program -- Summer 2018
Philippe Noël
Problem Set 4 - Problem 4
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def calculateHandlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.

    hand: dictionary (string int)
    returns: integer
    """
    return sum(hand.values())
