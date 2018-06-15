"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
HKS Python Pilot Program -- Summer 2018
Philippe Noël
Problem Set 4 - Problem 1
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def getWordScore(word, n):
    """
    Returns the score for a word. Assumes the word is a valid word.

    The score for a word is the sum of the points for letters in the
    word, multiplied by the length of the word, PLUS 50 points if all n
    letters are used on the first turn.

    Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is
    worth 3, D is worth 2, E is worth 1, and so on (see SCRABBLE_LETTER_VALUES)

    word: string (lowercase letters)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    returns: int >= 0
    """
    # initialize score
    score = 0
    # get the score associated to each letter from the dictionary
    for letter in word:
        score += SCRABBLE_LETTER_VALUES[letter]
    # score of each letter is multiplied by length of word
    score *= len(word)
    # check if all the letters were used
    if len(word) == n:
        score += 50 # 50 bonus points from doing so (from pset spec)
    # render success
    return score
