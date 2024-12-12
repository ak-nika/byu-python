"""
Author: Akingbayi Ojo

Purpose: To calculate the grade of a student
"""
print("Welcome to the grade calculator")
# num1 = 83
# num2 = 10

# remainder = 83 % 10
# print(remainder)
grade = float(input("\nWhat is your grade percentage? "))

# Part 1
# if grade >= 90:
#     print("Your grade is A")
# elif grade >= 80:
#     print("Your grade is B")
# elif grade >= 70:
#     print("Your grade is C")
# elif grade >= 60:
#     print("Your grade is D")
# else:
#     print("Your grade is F")

# Part 2
# letter = ""

# if grade >= 90:
#     letter = "A"
# elif grade >= 80:
#     letter = "B"
# elif grade >= 70:
#     letter = "C"
# elif grade >= 60:
#     letter = "D"
# else:
#     letter = "F"
    
# Stretch Challenge
letter = ""

if grade >= 90:
    if grade % 10 < 3:
        letter = "A-"
    else:
        letter = "A"
elif grade >= 80:
    if grade % 10 >= 7:
        letter = "B+"
    elif grade % 10 < 3:
        letter = "B-"
    else:
        letter = "B"
elif grade >= 70:
    if grade % 10 >= 7:
        letter = "C+"
    elif grade % 10 < 3:
        letter = "C-"
    else:
        letter = "C"
elif grade >= 60:
    if grade % 10 >= 7:
        letter = "D+"
    elif grade % 10 < 3:
        letter = "D-"
    else:
        letter = "D"
else:
    letter = "F"

print(f"\nYour grade is {letter}")

if grade >= 70:
    print("Congratulations! You have passed the course.")
else:
    print("Sorry, you have failed the course. Try better next time.")

# print(f"\nYour grade is {letter}")