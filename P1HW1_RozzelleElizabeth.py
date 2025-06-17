# Elizabeth Rozzelle
# June 16, 2025
# P1HW1
# This program asks the user for a base and exponent, calculates the power,
# then asks for three integers, sums the first two, subtracts the third,
# and displays all results with formatted output.

# Get base and exponent from user
base = int(input("Enter an integer base: "))
exponent = int(input("Enter an integer exponent: "))

# Calculate power
power_result = base ** exponent

# Print the power statement
print()
print(f"{base} to the power of {exponent} is {power_result}!!!")
print()

# Get three integers from user
num1 = int(input("Enter first integer: "))
num2 = int(input("Enter second integer: "))
num3 = int(input("Enter third integer: "))

# Calculate sum and difference
sum_result = num1 + num2
final_result = sum_result - num3

# Print the sum and subtraction statement
print()
print(f"({num1} + {num2}) - {num3} = {final_result}!!!")

input()
