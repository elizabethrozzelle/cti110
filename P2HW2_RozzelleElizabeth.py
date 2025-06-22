# Elizabeth Rozzelle
# Date: June 22, 2025
# Assignment Name: P2HW2
# Brief description of program: This program asks the user to enter grades for 6 modules, stores them in a list,and then displays the lowest, highest, sum, and average of the grades.

# Pseudocode:
# 1. Ask the user to enter a grade for each of the 6 modules (convert to float)
# 2. Store all the grades in a list called grades
# 3. Use built-in functions to calculate:
#    - the lowest grade
#    - the highest grade
#    - the sum of grades
#    - the average (sum divided by number of items)
# 4. Display results using formatting so values align as shown in the sample image

# Collect grades from user
grade1 = float(input("Enter grade for Module 1: "))
grade2 = float(input("Enter grade for Module 2: "))
grade3 = float(input("Enter grade for Module 3: "))
grade4 = float(input("Enter grade for Module 4: "))
grade5 = float(input("Enter grade for Module 5: "))
grade6 = float(input("Enter grade for Module 6: "))

# Store grades in a list
grades = [grade1, grade2, grade3, grade4, grade5, grade6]

# Perform calculations
lowest = min(grades)
highest = max(grades)
total = sum(grades)
average = total / len(grades)

# Display results with formatting
print("\n------------Results------------")
print(f"Lowest Grade:       {lowest}")
print(f"Highest Grade:      {highest}")
print(f"Sum of Grades:      {total}")
print(f"Average:            {average:.2f}")
print("--------------------------------")
