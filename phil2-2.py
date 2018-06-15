"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
HKS Python Pilot Program -- Summer 2018
Philippe Noël
Problem Set 2 - Problem 2
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# constants
number_of_months = 12
monthly_IR = 1 + annualInterestRate / 12.0

# initialize vars
min_monthly_pay = 0
tmp_balance = balance # keep track of actual balance over iterations

# increase minimum monthly payment until there is no balance left
while balance > 0:
    # monthly payment must be a multiple of 10$ so we iterate incrementing by 10
    min_monthly_pay += 10
    balance = tmp_balance # reset balance her for new iteration
    # check the remaining balance, do that until there is none
    for i in range(number_of_months):
        balance = (balance - min_monthly_pay) * monthly_IR

# output
print("Lowest Payment: ", min_monthly_pay)
