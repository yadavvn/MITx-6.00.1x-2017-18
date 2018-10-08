# Now write a program that calculates the minimum fixed monthly payment needed in order pay off a credit card balance
# within 12 months. By a fixed monthly payment, we mean a single number which does not change each month, but instead
# is a constant amount that will be paid each month. In this problem, we will not be dealing with a minimum
# monthly payment rate.

fixedMonAmt = 10
month = 1
outstandingBalance = balance

while outstandingBalance > 0:
    mon_unpaid_bal = outstandingBalance - fixedMonAmt
    interest = (annualInterestRate / 12) * mon_unpaid_bal
    outstandingBalance = mon_unpaid_bal + interest

    month += 1

    if month > 12 and outstandingBalance > 0:
        fixedMonAmt += 10
        outstandingBalance = balance
        month = 1

print("Lowest Payment : {}".format(round(fixedMonAmt, 2)))