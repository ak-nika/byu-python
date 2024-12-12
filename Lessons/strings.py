# Get the user's first and last names
first_name = input("What is your first name? ")
last_name = input("What is your last name? ")

print(f"Your name is {last_name.title()}, {first_name.title()} {last_name.title()}.")

# Favourite colour
# Set a variable to store the value the user inputs
colour = input("What is your favourite colour? ")

# Print the user's input
print("Your favourite colour is")
print(colour)
# OR
# print("Your favourite colour is", colour)

# ID Generator
"""
Author: Akingbayi Ojo

Purpose: To generate an ID card
"""

print("Please enter the following information: \n")

# Get the user's information
first_name = input("First name: ")
last_name = input("Last name: ")
email = input("Email address: ")
number = input("Phone number: ")
job = input("Job title: ")
id_number = input("ID number: ")

# Stretch Challenge
hair = input("Hair color: ")
eye = input("Eye color: ")
month = input("What month did you start? ")
training = input("Have you completed your training?(Yes/No) ")

# Display the user's ID card
print("\nThe ID Card is:")
print("-------------------------------------------------")
print(f"{last_name.upper()}, {first_name.title()}")
print(job.title())
print(f"ID: {id_number}\n")

print(email.lower())
print(number)

# Stretch Challenge
print(f"\n{'Hair: ' + hair.title():<15} Eye: {eye.title()}")
print(f"{'Month: ' + month.title():<15} Training: {training.title()}")
print("-------------------------------------------------")