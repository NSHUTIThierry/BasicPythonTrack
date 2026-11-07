# Agricultural Production Records
# RP-Tumba College
# Student: NSHUTI Thierry
# Registration Number: 24RP05284

# Declare crop production variables
crop_name = "Irish Potatoes"       # String
quantity_kg = 500                  # Integer
selling_price_per_kg = 800.50      # Float
harvest_sold = True                # Boolean

# Calculate total expected revenue
total_revenue = quantity_kg * selling_price_per_kg

# Display the agricultural record
print("===== AGRICULTURAL PRODUCTION =====")
print("Crop Name:", crop_name)
print("Quantity:", quantity_kg, "kg")
print("Selling Price per Kg:", selling_price_per_kg, "RWF")
print("Harvest Sold:", harvest_sold)
print("Total Expected Revenue:", total_revenue, "RWF")

# Display the data types
print("\n===== DATA TYPES =====")
print("Crop Name:", type(crop_name))
print("Quantity:", type(quantity_kg))
print("Selling Price:", type(selling_price_per_kg))
print("Sales Status:", type(harvest_sold))

# Explanation of data types used:
# Integer (int): Whole numbers without decimal points.
#   Example: quantity_kg = 500 (represents whole kilograms harvested)
# Float (float): Numbers with decimal points (floating-point numbers).
#   Example: selling_price_per_kg = 800.50 (price can have cents/fractional values)
# String (str): Sequence of characters enclosed in quotes.
#   Example: crop_name = "Irish Potatoes" (text data, crop names)
# Boolean (bool): Logical values representing True or False.
#   Example: harvest_sold = True (indicates whether harvest has been sold or not)
