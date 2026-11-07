"""
Question 5: Student Scholarship Eligibility System
Fictional rules supplied in the assignment.
"""

try:
    average = float(input("Enter student's average mark (0-100): "))
    attendance = float(input("Enter attendance percentage (0-100): "))

    if not 0 <= average <= 100:
        print("Invalid average. Marks must be between 0 and 100.")
    elif not 0 <= attendance <= 100:
        print("Invalid attendance. Attendance must be between 0% and 100%.")
    elif average >= 85 and attendance >= 90:
        print("FULL SCHOLARSHIP")
        print("Reason: Average is at least 85 and attendance is at least 90%.")
    elif average >= 75 and attendance >= 80:
        print("PARTIAL SCHOLARSHIP")
        print("Reason: Average is at least 75 and attendance is at least 80%.")
    else:
        print("NOT ELIGIBLE")
        reasons = []
        if average < 75:
            reasons.append("average mark is below 75")
        elif average < 85:
            reasons.append("average mark is below 85 for a full scholarship")
        if attendance < 80:
            reasons.append("attendance is below 80%")
        elif attendance < 90:
            reasons.append("attendance is below 90% for a full scholarship")
        print("Reason: " + "; ".join(reasons) + ".")
except ValueError:
    print("Invalid input. Enter numeric values for marks and attendance.")
