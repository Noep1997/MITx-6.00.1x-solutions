"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
HKS Python Pilot Program -- Summer 2018
Philippe Noël
Problem Set 2 - Problem 1
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# constants
number_of_months = 12
monthly_IR = 1 + annualInterestRate / 12.0
# loop over all months and increment balance accorind to IR on balance left
for i in range(number_of_months):
    month_min_payment = monthlyPaymentRate * balance
    balance = (balance - month_min_payment) * monthly_IR
# output
print("Remaining balance: ", round(balance, 2))
