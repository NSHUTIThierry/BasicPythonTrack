# Student Examination Results
# RP-Tumba College
# Student: NSHUTI Thierry
# Registration Number: 24RP05284

# Declare marks for three modules
python_marks = 85
database_marks = 78
networking_marks = 92

# Calculate total marks
total_marks = python_marks + database_marks + networking_marks

# Calculate average marks
average_marks = total_marks / 3

# Convert the average to a string
average_string = str(average_marks)

# Display the examination results
print("===== STUDENT EXAMINATION RESULTS =====")
print("Python Programming:", python_marks)
print("Database Management:", database_marks)
print("Computer Networking:", networking_marks)
print("Total Marks:", total_marks)
print("Average Marks: " + average_string)

# Display the data types
print("\n===== DATA TYPES =====")
print("Total Marks:", type(total_marks))
print("Average Marks:", type(average_marks))
print("Converted Average:", type(average_string))
