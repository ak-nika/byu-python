# Functions in Python
# A function to get message and print different version of the text
# def display_regular(message):
#     print(message)
    
# def display_uppercase(message):
#     print(message.upper())
    
# def display_lowercase(message):
#     print(message.lower())
    
# user_message = input("What is your message? ")

# display_regular(user_message)
# display_uppercase(user_message)
# display_lowercase(user_message)

# Function Practice
import math

def compute_area_square(side):
    area = compute_area_rectangle(side, side)
    return area

def compute_area_rectangle(length, width):
    area = length * width
    return area

def compute_area_circle(radius):
    area = math.pi * radius ** 2
    return area

user_input = ""

while user_input.lower() != "quit":
    user_input = input("What shape would you like to calculate the area of? SQUARE, RECTANGLE, or CIRCLE? ")
    
    if user_input.lower() == "square":
        side = float(input("What is the side of the square? "))
        print(f"The area of the square is {compute_area_square(side):.2f}")
    elif user_input.lower() == "rectangle":
        length = float(input("What is the length of the rectangle? "))
        width = float(input("What is the width of the rectangle? "))
        print(f"The area of the rectangle is {compute_area_rectangle(length, width):.2f}")
    elif user_input.lower() == "circle":
        radius = float(input("What is the radius of the circle? "))
        print(f"The area of the circle is {compute_area_circle(radius):.2f}")
    elif user_input.lower() == "quit":
        print("Goodbye.")
    else:
        print("Invalid input. Please try again.")