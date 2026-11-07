"""
Question 2: Smart Agriculture Irrigation System
Validation limits:
- Soil moisture: 0% to 100%
- Temperature: -50 C to 60 C (reasonable general sensor range for this exercise)
"""

try:
    moisture = float(input("Enter soil moisture (0-100%): "))
    temperature = float(input("Enter temperature (-50 to 60 C): "))
    water_available_input = input("Is water available? (yes/no): ").strip().lower()

    if not 0 <= moisture <= 100:
        print("Invalid soil moisture. It must be between 0% and 100%.")
    elif not -50 <= temperature <= 60:
        print("Invalid temperature. It must be between -50 C and 60 C.")
    elif water_available_input not in ("yes", "no"):
        print("Invalid water availability. Enter yes or no.")
    else:
        water_available = water_available_input == "yes"

        if moisture < 30 and temperature > 25 and water_available:
            print("IRRIGATION ACTIVATED: soil is dry, temperature is high, and water is available.")
        else:
            print("IRRIGATION DEACTIVATED.")
            reasons = []
            if moisture >= 30:
                reasons.append("soil moisture is not below 30%")
            if temperature <= 25:
                reasons.append("temperature does not exceed 25 C")
            if not water_available:
                reasons.append("the water tank is empty / water is unavailable")
            print("Reason: " + "; ".join(reasons) + ".")
except ValueError:
    print("Invalid input. Moisture and temperature must be numeric values.")
