# Electricity Billing System
# RP-Tumba College
# Student: NSHUTI Thierry
# Registration Number: 24RP05284

# Get the number of electricity units consumed from the user
units = float(input("Enter electricity units consumed: "))

# Declare the assumed price per unit (250 RWF per unit)
rate_per_unit = 250

# Calculate the estimated electricity bill by multiplying units by rate
total_cost = units * rate_per_unit

# Display the billing report showing units, rate, and total estimated bill
print("\n===== ELECTRICITY BILL =====")
print("Units consumed:", units)
print("Rate per unit:", rate_per_unit, "RWF")
print("Total estimated bill:", total_cost, "RWF")
