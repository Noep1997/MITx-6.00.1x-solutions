"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
HKS Python Pilot Program -- Summer 2018
Philippe Noël
Problem Set 5 - Problem 3
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object

        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        # inherit from Message, self.message_text and self.valid_words are
        # already dealt by by calling __init__ (see Message class)
        Message.__init__(self, text)

    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value
        for decrypting it.

        Note: if multiple shifts are  equally good such that they all create
        the maximum number of you may choose any of those shifts (and their
        corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''
        best_shift, best_number_words = 0, 0
        best_message = ''
        # 26 comes from 26 letters in the alphabet (possible shifts 0 to 25)
        for shift in range(26):
            # find potential words in message by shifting it and splitting into words
            message = self.apply_shift(shift)
            words = message.split()
            # list comprehension to loop over all "words" and see if they're real words
            num_real_words = sum([is_word(self.valid_words, word) for word in words])
            # update our counters if we found a better message
            if num_real_words > best_number_words:
                best_shift, best_number_words = shift, num_real_words
                best_message = message
        # render success
        return (best_shift, best_message)
