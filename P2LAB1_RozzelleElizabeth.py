# Elizabeth Rozzelle
# Date: June 20, 2025
# Assignment Name: P2LAB1
# Description: This program prompts the user to enter the radius of a circle. It calculates and displays the circle's diameter, circumference, and area using standard mathematical formulas and formatted output.

# Prompt user for the radius of the circle
radius = float(input("What is the radius of the circle? "))

# Calculate circle properties
diameter = 2 * radius
circumference = 2 * 3.141592653589793 * radius  # Using π ≈ 3.14159
area = 3.141592653589793 * radius ** 2

# Output results with appropriate formatting
print("\nThe diameter of the circle is", format(diameter, ".1f"))
print("The circumference of the circle is", format(circumference, ".2f"))
print("The area of the circle is", format(area, ".3f"))
