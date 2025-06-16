#Elizabeth Rozzelle
#June 16, 2025
#P1HW2
#This program asks the user to enter their travel budget, destination, and how much they will spend on food, gas, and hotel. It then shows the remaining balance after the expenses are subtracted from the budget.

#Pseudocode:
# 1. Prompt the user to enter the budget.
# 2. Prompt the user to enter travel destination.
# 3. Ask for expected cost of gas.
# 4. Ask for expected cost of accomodation.
# 5. Ask for expected cost of food.
# 6. Add all expenses together
# 7. Subtract expenses from budget to get remaining balance
# 8. Print out all the info nicely

budget = float(input("Enter Budget: "))
destination = input("Enter your travel destination: ")

gas = float(input("How much do you think you will spend on gas? "))
hotel = float(input("Approximately, how much will you need for accommodation/hotel? "))
food = float(input("Last, how much do you need for food? "))

# Calculating total expenses
total_expenses = gas + hotel + food

# Calculating what's left after spending
remaining_balance = budget - total_expenses

# Displaying the results
print()
print("------------ Travel Expenses ------------")
print("Location:", destination)
print("Initial Budget: $" + str(budget))
print()

print("Fuel: $" + str(gas))
print("Accommodation: $" + str(hotel))
print("Food: $" + str(food))
print()

print("Remaining Balance: $" + str(remaining_balance))
