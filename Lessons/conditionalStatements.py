# Conditional Statements

# Number checker and favourite animal checker
# Number checker
# num1 = int(input("What is the first number? "))
# num2 = int(input("What is the second number? "))

# if num1 > num2:
#     print("The first number is greater")
# else:
#     print("The first number is not greater")

# if num1 == num2:
#     print("The numbers are equal")
# else:
#     print("The numbers are not equal")

# if num1 < num2:
#     print("The second number is greater")
# else:
#     print("The second number is not greater")

# # Favourite animal checker
# animal = input("\nWhat is your favorite animal? ")

# if animal.lower() == "lion":
#     print("That is my favourite animal too!")
# else:
#     print("That is not my favourite animal")

# Complex conditions
# Qualifying for a loan
# print("Welcome to our Loan program.")
# print("Please rate the following on a scale of 1 - 10 so we can determine if you qualify for a loan\n")

# loan = int(input("How large is the loan? "))
# credit = int(input("How good is your credit history? "))
# income = int(input("How high is your income? "))
# down_payment = int(input("How large is your down payment? "))
# can_qualify = False

# if loan >= 5:
#     if credit >= 7 and income >= 7:
#         can_qualify = True
#     elif credit >= 7 or income >=7:
#         if down_payment >= 5:
#             can_qualify = True
#         else:
#             can_qualify = False
#     else:
#         can_qualify = False
# else:
#     if credit < 4:
#         can_qualify = False
#     else:
#         if income >= 7 or down_payment >= 7:
#             can_qualify = True
#         elif income >= 7 and down_payment >= 7:
#             can_qualify = True
#         else:
#             can_qualify = False
        
# if can_qualify:
#     print("\nCongratulations!! You qualify for a loan.")
# else:
#     print("\nSorry, you do not qualify for a loan")