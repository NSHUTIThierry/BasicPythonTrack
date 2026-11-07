"""
Question 3: College Student Performance Analysis

A dictionary is suitable because each student name is associated with one mark.
It supports easy lookup and updating without removing other students' records.
"""

students = {
    "Alice": 85,
    "Eric": 72,
    "Diane": 91,
    "Patrick": 48,
    "Aline": 76
}

marks = list(students.values())
average = sum(marks) / len(marks)

print("========== STUDENT PERFORMANCE ==========")
print(f"Class average: {average:.2f}")
print(f"Highest mark: {max(marks)} ({max(students, key=students.get)})")
print(f"Lowest mark:  {min(marks)} ({min(students, key=students.get)})")

print("\nStudents scoring above the class average:")
for name, mark in students.items():
    if mark > average:
        print(f"{name}: {mark}")

# Update one student's mark while preserving all other records.
name_to_update = input("\nEnter the student name whose mark you want to update (or press Enter to skip): ").strip()

if name_to_update:
    if name_to_update in students:
        try:
            new_mark = float(input(f"Enter the new mark for {name_to_update} (0-100): "))
            if 0 <= new_mark <= 100:
                students[name_to_update] = new_mark
                print(f"{name_to_update}'s mark was updated successfully.")
            else:
                print("Invalid mark. A mark must be between 0 and 100.")
        except ValueError:
            print("Invalid input. Enter a numeric mark.")
    else:
        print("Student not found. No record was changed.")

print("\nStudents in descending order of marks:")
for name, mark in sorted(students.items(), key=lambda item: item[1], reverse=True):
    print(f"{name}: {mark}")
