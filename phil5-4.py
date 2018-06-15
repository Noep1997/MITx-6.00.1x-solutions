"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
HKS Python Pilot Program -- Summer 2018
Philippe Noël
Problem Set 5 - Problem 4
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def decrypt_story():
    ''' Decrypts the message found in story.txt '''
    # get_story_String is helper function found in ps6.py to get the story
    return CiphertextMessage(get_story_string()).decrypt_message()
