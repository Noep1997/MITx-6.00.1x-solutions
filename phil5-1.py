"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
HKS Python Pilot Program -- Summer 2018
Philippe Noël
Problem Set 5 - Problem 1
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

class Message(object):
    ### DO NOT MODIFY THIS METHOD ###
    def __init__(self, text):
        '''
        Initializes a Message object

        text (string): the message's text

        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words
        '''
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)

    ### DO NOT MODIFY THIS METHOD ###
    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class

        Returns: self.message_text
        '''
        return self.message_text

    ### DO NOT MODIFY THIS METHOD ###
    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class

        Returns: a COPY of self.valid_words
        '''
        return self.valid_words[:]

    def build_shift_dict(self, shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.

        shift (integer): the amount by which to shift every letter of the
        alphabet. 0 <= shift < 26

        Returns: a dictionary mapping a letter (string) to
                 another letter (string).
        '''
        # the dict we're building
        shift_dict = dict()
        # lower case situation, 26 is from number of letters in alphabet (duh)
        # we simply bring back to 0 index for modulo wrapping around alphabet
        for letter in string.ascii_lowercase:
            shift_dict[letter] = chr((ord(letter) - ord('a') + shift) % 26 + ord('a'))
        # upper case situation
        for letter in string.ascii_uppercase:
            shift_dict[letter] = chr((ord(letter) - ord('A') + shift) % 26 + ord('A'))
        # render success
        return shift_dict

    def apply_shift(self, shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift

        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''
        # ciphertext we will build
        ciphertext = ''
        # build our dict with the current shift
        shift_dict = self.build_shift_dict(shift)
        # loop over message and shift it
        for letter in self.get_message_text():
            # if in dictionary (so if it's a letter) we shift it
            if shift_dict.get(letter, 0) != 0:
                ciphertext += shift_dict[letter]
            # if it's not in the dictionary, then it's punctuation or number,
            # stay the same
            else:
                ciphertext += letter
        # render success
        return ciphertext
