"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
HKS Python Pilot Program -- Summer 2018
Philippe Noël
Problem Set 1 - Problem 2
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# initialize vars
num_bobs = 0
s_len = len(s)
# loop over s, looking for 'bob'
for i in range(s_len - 2):
    if s[i:i + 3] == 'bob':
        num_bobs += 1
# output
print("Number of times bob occurs is: ", num_bobs)
