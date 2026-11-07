# Local and Global Variables
# RP-Tumba College
# Student: NSHUTI Thierry
# Registration Number: 24RP05284

# Global variables shared by functions
school_name = "RP-Tumba College"
academic_year = "Year 2"


def display_department():
    # Local variables available inside this function
    department_name = "Information Technology"
    student_population = 120

    print("School Name:", school_name)
    print("Department:", department_name)
    print("Student Population:", student_population)


def update_academic_year():
    # Modify the global academic_year variable using 'global' keyword
    global academic_year
    academic_year = "Year 3"


# Call the functions
print("===== DEPARTMENT INFORMATION =====")
display_department()

print("\nAcademic Year Before Update:", academic_year)
update_academic_year()
print("Academic Year After Update:", academic_year)

# Explanation of local vs global variables:
# Global variables (school_name, academic_year): Declared outside functions,
# accessible throughout the program, including inside functions.
# Local variables (department_name, student_population): Declared inside a function,
# only accessible within that function. They are created when the function is called
# and destroyed when the function exits.
# The 'global' keyword in update_academic_year() allows modification of the global
# academic_year variable from within the function.
