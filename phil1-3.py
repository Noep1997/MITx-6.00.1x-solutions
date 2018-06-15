"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
HKS Python Pilot Program -- Summer 2018
Philippe Noël
Problem Set 1 - Problem 3
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# initialize vars
curr_longest, curr_string = '', ''
# loop over string
for letter in s:
    # if no current string or letter in alphaetical order we add to curr
    if curr_string == '' or letter >= curr_string[-1]:
        curr_string += letter
    # we end the alphabetical order string
    else:
        # update longest string if this one is longer
        if len(curr_string) > len(curr_longest):
            curr_longest = curr_string
        # reset the current string
        curr_string = letter
# final check to see if final part of the s is longer
if len(curr_string) > len(curr_longest):
    curr_longest = curr_string
# output
print("Longest substring in alphabetical order is: ", curr_longest)
