"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
HKS Python Pilot Program -- Summer 2018
Philippe Noël
Problem Set 4 - Problem 3
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.

    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    # word in wordlist
    if word in wordList:
        # check that each letter is in hand
        hand_copy = hand.copy() # copy so we can decrement if many times same letter
        for letter in word:
            if hand_copy.get(letter, 0) == 0:
                return False # letter not in hand or none of this letter left
            else:
                hand_copy[letter] -= 1 # decrement, to check if too many uses of a letter
        return True
    # word not in wordlist
    else:
        return False
