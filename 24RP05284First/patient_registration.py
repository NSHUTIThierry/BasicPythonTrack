# Hospital Patient Registration
# RP-Tumba College
# Student: NSHUTI Thierry
# Registration Number: 24RP05284

# Declare patient information using appropriate data types
patient_name = "Jean Claude"       # String
age = 32                           # Integer
body_temperature = 37.2            # Float
patient_admitted = True            # Boolean
telephone_number = "0781234567"    # String

# Display patient information
print("===== PATIENT REGISTRATION =====")
print("Patient Name:", patient_name)
print("Age:", age)
print("Body Temperature:", body_temperature)
print("Patient Admitted:", patient_admitted)
print("Telephone Number:", telephone_number)

# Display the data type of each variable
print("\n===== DATA TYPES =====")
print("Patient Name:", type(patient_name))
print("Age:", type(age))
print("Body Temperature:", type(body_temperature))
print("Patient Admitted:", type(patient_admitted))
print("Telephone Number:", type(telephone_number))

# Explanation: A telephone number should be stored as a string rather than an integer
# because:
# 1. Phone numbers can start with leading zeros (e.g., 0781234567), which would be
#    lost if stored as an integer.
# 2. Phone numbers may contain special characters like +, -, (, ), or spaces.
# 3. Phone numbers are not used for mathematical operations (no addition, subtraction, etc.)
# 4. String storage preserves the exact format as entered by the user.
