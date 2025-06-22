# Elizabeth Rozzelle
# Date: June 20, 2025
# Assignment Name: P2LAB2
# A brief description of the project:
# This program lets the user choose a car, shows its MPG, and calculates how much gas is needed to drive a number of miles.

# Create the dictionary
vehicle_mpg = {
    "Camaro": 18.21,
    "Prius": 52.36,
    "Model S": 110,
    "Silverado": 26
}

# Store the keys in a variable and print it
keys = vehicle_mpg.keys()
print(keys)

# Prompt user for a vehicle name (must match a key)
vehicle = input("Enter a vehicle to see its mpg: ")

# Display the MPG for the chosen vehicle
mpg = vehicle_mpg[vehicle]
print(f"\nThe {vehicle} gets {mpg} mpg.")

# Prompt for number of miles to drive
miles = float(input(f"\nHow many miles will you drive the {vehicle}? "))

# Calculate gallons needed
gallons = miles / mpg

# Display gallons needed, rounded to 2 decimal places
print(f"\n{gallons:.2f} gallon(s) of gas are needed to drive the {vehicle} {miles} miles.")
