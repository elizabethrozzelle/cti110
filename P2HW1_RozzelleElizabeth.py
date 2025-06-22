# Elizabeth Rozzelle
# Date: June 21, 2025
# Assignment Name: P2HW1
# A brief description of the project:
# This program asks for a travel budget and expenses, then calculates and displays the remaining balance. Output is formatted in aligned columns.

# Get user input and convert to appropriate types
budget = float(input("Enter Budget: "))
destination = input("Enter your travel destination: ")
gas = float(input("How much do you think you will spend on gas? "))
hotel = float(input("Approximately, how much will you need for accommodation/hotel? "))
food = float(input("Last, how much do you need for food? "))

# Calculate remaining balance
total_expenses = gas + hotel + food
balance = budget - total_expenses

# Display results
print("\n------------Travel Expenses-------------")
print(f"{'Location:':20} {destination}")
print(f"{'Initial Budget:':20} ${budget:.2f}")
print(f"{'Fuel:':20} ${gas:.2f}")
print(f"{'Accommodation:':20} ${hotel:.2f}")
print(f"{'Food:':20} ${food:.2f}")
print("----------------------------------------")
print(f"{'Remaining Balance:':20} ${balance:.2f}")
