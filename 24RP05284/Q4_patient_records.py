"""
Question 4: Hospital Patient Record Management

The outer dictionary uses patient IDs as unique keys. Each value is another
dictionary containing the patient's name, age, and temperature.
"""

patients = {
    "P001": {"name": "Jean", "age": 25, "temperature": 36.7},
    "P002": {"name": "Amina", "age": 34, "temperature": 37.0},
    "P003": {"name": "Peter", "age": 12, "temperature": 36.5},
    "P004": {"name": "Claudine", "age": 45, "temperature": 38.1},
    "P005": {"name": "Eric", "age": 8, "temperature": 37.2}
}


def search_patient():
    patient_id = input("Enter patient ID to search: ").strip().upper()
    if patient_id in patients:
        print("Patient found:")
        print(f"ID: {patient_id}")
        for field, value in patients[patient_id].items():
            print(f"{field.capitalize()}: {value}")
    else:
        print("No patient found with that ID.")


def update_temperature():
    patient_id = input("Enter patient ID to update: ").strip().upper()
    if patient_id not in patients:
        print("Patient ID not found.")
        return

    try:
        new_temperature = float(input("Enter new temperature in C: "))
        if not 30 <= new_temperature <= 45:
            print("Invalid temperature. Enter a value from 30 C to 45 C.")
            return
        patients[patient_id]["temperature"] = new_temperature
        print("Patient temperature updated successfully.")
    except ValueError:
        print("Invalid input. Temperature must be numeric.")


def register_patient():
    patient_id = input("Enter new unique patient ID: ").strip().upper()
    if not patient_id:
        print("Patient ID cannot be empty.")
    elif patient_id in patients:
        print("Registration rejected: this patient ID already exists.")
        return

    name = input("Enter patient name: ").strip()
    try:
        age = int(input("Enter patient age in years: "))
        temperature = float(input("Enter patient temperature in C: "))
        if not name:
            print("Name cannot be empty.")
        elif age < 0 or age > 130:
            print("Invalid age. Enter an age from 0 to 130.")
        elif not 30 <= temperature <= 45:
            print("Invalid temperature. Enter a value from 30 C to 45 C.")
        else:
            patients[patient_id] = {
                "name": name,
                "age": age,
                "temperature": temperature
            }
            print("Patient registered successfully.")
    except ValueError:
        print("Invalid age or temperature. Please enter numeric values.")


while True:
    print("\n========== PATIENT RECORD MENU ==========")
    print("1. Search for a patient")
    print("2. Update patient temperature")
    print("3. Register a new patient")
    print("4. Display all patients")
    print("5. Exit")

    choice = input("Choose an option (1-5): ").strip()

    if choice == "1":
        search_patient()
    elif choice == "2":
        update_temperature()
    elif choice == "3":
        register_patient()
    elif choice == "4":
        for patient_id, details in patients.items():
            print(patient_id, details)
    elif choice == "5":
        print("Exiting patient record system.")
        break
    else:
        print("Invalid choice. Select a number from 1 to 5.")
