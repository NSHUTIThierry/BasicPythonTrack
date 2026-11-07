"""
Question 1: Mobile Money Transaction Management System
RP-TUMBA COLLEGE - Python and Fundamentals of AI
"""

initial_balance = 250_000
balance = initial_balance

deposit = 75_000
withdrawal = 80_000
transfer = 45_000
transfer_fee = 1_000

# Assignment operators update the balance after each transaction.
balance += deposit
balance -= withdrawal
balance -= transfer
balance -= transfer_fee

print("========== MOBILE MONEY TRANSACTION SUMMARY ==========")
print(f"Initial balance:       {initial_balance:,.0f} RWF")
print(f"Deposit:              +{deposit:,.0f} RWF")
print(f"Withdrawal:           -{withdrawal:,.0f} RWF")
print(f"Transfer:             -{transfer:,.0f} RWF")
print(f"Transfer fee:         -{transfer_fee:,.0f} RWF")
print(f"Final balance:         {balance:,.0f} RWF")

# Check an additional withdrawal using comparison and logical operators.
try:
    extra_withdrawal = float(input("\nEnter amount for an additional withdrawal (RWF): "))
    if extra_withdrawal <= 0:
        print("Invalid amount. Enter a value greater than zero.")
    elif extra_withdrawal <= balance and balance >= 0:
        balance -= extra_withdrawal
        print(f"Withdrawal successful. New balance: {balance:,.0f} RWF")
    else:
        print("Transaction declined: insufficient funds.")
        print(f"Available balance: {balance:,.0f} RWF")
except ValueError:
    print("Invalid input. Please enter a numeric amount.")
