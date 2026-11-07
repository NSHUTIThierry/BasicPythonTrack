"""
Question 6: Bank Loan Eligibility Assessment
A customer qualifies only when every stated condition is satisfied.
"""

try:
    age = int(input("Enter customer age in years: "))
    monthly_income = float(input("Enter monthly income (RWF): "))
    years_employed = float(input("Enter years of employment: "))
    defaulted_loan_input = input("Does the customer have an outstanding defaulted loan? (yes/no): ").strip().lower()

    if age < 0:
        print("Invalid age. Age cannot be negative.")
    elif monthly_income < 0:
        print("Invalid income. Monthly income cannot be negative.")
    elif years_employed < 0:
        print("Invalid employment duration. Years worked cannot be negative.")
    elif defaulted_loan_input not in ("yes", "no"):
        print("Invalid response. Enter yes or no.")
    else:
        has_defaulted_loan = defaulted_loan_input == "yes"

        eligible = (
            age >= 21
            and monthly_income >= 200_000
            and years_employed >= 2
            and not has_defaulted_loan
        )

        if eligible:
            print("LOAN SCREENING RESULT: ELIGIBLE")
            print("The customer meets all preliminary requirements.")
        else:
            print("LOAN SCREENING RESULT: NOT ELIGIBLE")
            reasons = []
            if age < 21:
                reasons.append("customer is younger than 21")
            if monthly_income < 200_000:
                reasons.append("monthly income is below 200,000 RWF")
            if years_employed < 2:
                reasons.append("employment duration is less than 2 years")
            if has_defaulted_loan:
                reasons.append("customer has an outstanding defaulted loan")
            print("Reasons: " + "; ".join(reasons) + ".")
except ValueError:
    print("Invalid input. Age, income, and employment duration must be numeric.")
