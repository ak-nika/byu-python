"""
Author: Akingbayi Ojo
Purpose: To create a shopping cart
Creativity: The user can determine the quantity of a particular product they want and the amount is aligned whenever the user views their cart.
"""

print("Welcome to the Shopping Cart Program!")
items = []
prices = []
quantities = []
action = None

while action != 5:
    print("\nPlease select one of the following:")
    print("1. Add item")
    print("2. View cart")
    print("3. Remove item")
    print("4. Compute total")
    print("5. Quit")

    action = int(input("Please enter an action: "))

    if action == 1:
        new_item = input("\nWhat item would you like to add? ")
        new_price = float(input(f"What is the price of '{new_item.capitalize()}'? $"))
        new_quantity = int(input("How many units do you want to order? "))

        items.append(new_item.capitalize())
        prices.append(new_price)
        quantities.append(new_quantity)

        print(f"'{new_item.capitalize()}' has been added to the cart.")
    elif action == 2:
        print("\nThe contents of your shopping cart are:")

        for i in range(len(items)):
            print(f"{i + 1}. {items[i]:<10} ${prices[i]:.2f} x {quantities[i]}")
    elif action == 3:
        print("\nThe contents of your shopping cart are:")

        for i in range(len(items)):
            print(f"{i + 1}. {items[i]:<10} ${prices[i]:.2f} x {quantities[i]}")

        remove = int(input("\nWhich item would you like to remove? "))

        if remove < len(items) and remove > 0:
            items.pop(remove - 1)
            prices.pop(remove - 1)
            quantities.pop(remove - 1)

            print("Item removed")
        else:
            print(
                f"Sorry, that is not a valid item number. Please enter a number between 1 and {len(items)}"
            )
    elif action == 4:
        total = 0

        for i in range(len(prices)):
            subtotal = prices[i] * quantities[i]

            total += subtotal

        print(f"\nThe total price of the items in the shopping cart is ${total:.2f}.")
    elif action == 5:
        print("\nThank you. Goodbye!")
    else:
        print("\nInvalid input. Please enter a number between 1 and 5.")
