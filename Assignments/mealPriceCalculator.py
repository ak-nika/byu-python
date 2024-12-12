"""
Author: Akingbayi Ojo

Purpose: To calculate the price of a meal
Creativity: The user if they want to tip. If they select yes, the amount they would like to tip.
            The amount is then added to the total. If they select no, they continue to the total.
"""

# Get the user's input for the meal
child_meal = float(input("What is the price of a child's meal? $"))
adult_meal = float(input("What is the price of an adult's meal? $"))
child_number = int(input("How many children are there? "))
adult_number = int(input("How many adults are there? "))

# Calculate and display the sub total
sub_total = (child_meal * child_number) + (adult_meal * adult_number)
print(f"\n Subtotal: ${sub_total:.2f}")

# Ask the user for the sales tax rate then calculate and display the sales tax
sales_tax_rate = float(input("\n What is the sales tax rate? "))
sales_tax = sales_tax_rate * sub_total / 100
print(f"Sales tax: ${sales_tax:.2f}")

# Calculate the total by adding the sales tax to the sub total
total = sub_total + sales_tax

# Ask the user if they want to tip
tip = input("\n Would you like to tip? (yes/no) ")

# If the user wants to tip, ask them how much and add it to the total
if (tip.lower() == "yes"):
    tip_amount = float(input("How much would you like to tip? $"))
    total += tip_amount
    print(f"Total: ${total:.2f}")
# If the user does not want to tip, add 0 to the total
else:
    total += 0

# Ask the user for the amount paid and calculate the change
paid = float(input("\n What is the amount paid? $"))
change = paid - total
print(f"Change: ${change:.2f}")