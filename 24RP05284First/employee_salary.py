# Employee Salary Management
# RP-Tumba College
# Student: NSHUTI Thierry
# Registration Number: 24RP05284

# Declare employee information and salary components
employee_name = "Jean Claude"
basic_salary = 250000
transport_allowance = 50000
housing_allowance = 30000

# Calculate gross salary by adding basic salary and allowances
gross_salary = basic_salary + transport_allowance + housing_allowance

# Display the salary summary
print("===== EMPLOYEE SALARY SUMMARY =====")
print("Employee Name:", employee_name)
print("Basic Salary:", basic_salary, "RWF")
print("Transport Allowance:", transport_allowance, "RWF")
print("Housing Allowance:", housing_allowance, "RWF")
print("Gross Salary:", gross_salary, "RWF")

# Separate declarations vs multiple assignment:
# Separate declarations (used above): Each variable is declared on its own line.
#   Example:
#       basic_salary = 250000
#       transport_allowance = 50000
#       housing_allowance = 30000
#   Advantage: More readable, easier to add comments for each variable.
#
# Multiple assignment: Assign multiple variables in a single line.
#   Example:
#       basic_salary, transport_allowance, housing_allowance = 250000, 50000, 30000
#   Advantage: Concise, useful when variables are related and initialized together.
