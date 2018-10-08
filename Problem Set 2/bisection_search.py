# Implementing the same problem in a more efficient way using bisection search

outstandingBalance = balance
monthlyInterestRate = annualInterestRate/12.0
low = balance/12
high = (balance * ((1 + monthlyInterestRate) ** 12)) / 12.0
guess = round((low + high)/2, 2)

while True:
    for month in range(1, 13):
        mon_unpaid_bal = outstandingBalance - guess
        interest = monthlyInterestRate * mon_unpaid_bal
        outstandingBalance = round(mon_unpaid_bal + interest, 2)

    if 0 <= abs(outstandingBalance) <= 0.1:
        break

    if outstandingBalance < 0:
        high = guess
    else:
        low = guess
    guess = round((low + high)/2, 2)
    outstandingBalance = balance

print("Lowest Payment : {}".format(guess))
