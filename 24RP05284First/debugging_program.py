# Program to display student examination results
# RP-Tumba College
# Student: NSHUTI Thierry
# Registration Number: 24RP05284

# Three errors in the original program:
# 1. Missing colon (:) after 'else' statement
# 2. Incorrect indentation for print statements inside if/else blocks
# 3. Missing indentation for the 'else' block print statement

student_name = "FNAME"
marks = 85

print("Student:", student_name)

if marks >= 50:
    print("Passed")
else:
    print("Failed")

# Explanation: Indentation is important in Python because it defines the scope/block of code
# that belongs to control structures (if, else, loops, functions). Unlike other languages
# that use braces {}, Python uses whitespace indentation to determine which statements
# are part of a block. Incorrect indentation leads to IndentationError or logical errors.

# Expected output:
# Student: FNAME
# Passed
