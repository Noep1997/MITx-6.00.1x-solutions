"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
HKS Python Pilot Program -- Summer 2018
Philippe Noël
Problem Set 2 - Problem 3
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# constants
number_of_months = 12
monthly_IR = 1 + annualInterestRate / 12.0
lower_bound = balance / 12.0
upper_bound = round(balance * (monthly_IR ** 12) / 12.0, 2)
tmp_balance = balance # keep track of actual balance over iterations

# initialize vars
midpoint = 0

# bisection search
while upper_bound - lower_bound > 0.01:
    midpoint = (lower_bound + upper_bound) / 2.0
    balance = tmp_balance
    # check the remaining balance
    for i in range(number_of_months):
        balance = (balance - midpoint) * monthly_IR
    if balance > 0:
        # our monthly pay is too low, so next iteration should have it as
        # the lowerbound (cuz anything lower will be too low too)
        lower_bound = midpoint
    else:
        # our monthly pay is too high, so next iteration should have it as
        # the upperbound (cuz anything higher will be too high too)
        upper_bound = midpoint

# output
print("Lowest Payment: ", round(midpoint, 2))
