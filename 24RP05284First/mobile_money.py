# Mobile Money Transaction Record
# RP-Tumba College
# Student: NSHUTI Thierry
# Registration Number: 24RP05284

# Collect transaction details from the keyboard
customer_name = input("Enter customer name: ")
initial_balance = float(input("Enter initial balance (RWF): "))
withdrawal_amount = float(input("Enter withdrawal amount (RWF): "))

# Assume a fixed transaction fee
transaction_fee = 500

# Calculate the remaining account balance after withdrawal and fee
remaining_balance = initial_balance - withdrawal_amount - transaction_fee

# Display the transaction summary
print("\n===== MOBILE MONEY TRANSACTION =====")
print("Customer Name:", customer_name)
print("Initial Balance:", initial_balance, "RWF")
print("Withdrawal Amount:", withdrawal_amount, "RWF")
print("Transaction Fee:", transaction_fee, "RWF")
print("Remaining Balance:", remaining_balance, "RWF")
