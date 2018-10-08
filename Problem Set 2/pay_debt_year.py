# Write a program to calculate the credit card balance after one year if a person only pays the minimum monthly
# payment required by the credit card company each month.
# For each month, calculate statements on the monthly payment and remaining balance. At the end of 12 months,
# print out the remaining balance.

# A summary of the required math is found below:
#
# Monthly interest rate= (Annual interest rate) / 12.0
# Minimum monthly payment = (Minimum monthly payment rate) x (Previous balance)
# Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
# Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)


for month in range(1, 13):
    mon_min_amt = monthlyPaymentRate * balance
    mon_unpaid_bal = balance - mon_min_amt
    interest = (annualInterestRate / 12) * mon_unpaid_bal

    balance = mon_unpaid_bal + interest

print("Remaining balance : {}".format(round(balance, 2)))

