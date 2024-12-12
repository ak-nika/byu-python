# Lists in python

# REGULAR LISTS
# Ask the user for their friends name and display them all at the end
# friends = []
# new_friend = ""

# while new_friend.lower() != "end":
#     new_friend = input("Type the name of a friend: ")
    
#     if new_friend.lower() == "end":
#         break
#     else:
#         friends.append(new_friend)

# print("\nYour friends are:")
# for friend in friends:
#     print(friend)

# LISTS WITH INDEXES
# A shopping cart that can change an item
# items = []
# new_item = ""

# print("Please enter the items of the shopping list (type: quit to finish): ")

# while new_item != "quit":
#     new_item = input("Item: ")
    
#     if new_item.lower() != "quit":
#         items.append(new_item)

# print("\nThe shopping list is:")
# for item in items:
#     print(item)

# print("\nThe shopping list with indexes is:")
# for i in range(len(items)):
#     print(f"{i}. {items[i]}")
    
# change_index = int(input("\nWhich item would you like to change? "))
# change_item = input("What would you like to change it to? ")

# items[change_index] = change_item

# print("\nThe shopping list with indexes is:")
# for i in range(len(items)):
#     print(f"{i}. {items[i]}")

x = 5

x =+ 1

print(x)