#Files in python
# Read a file and print each line
# with open("C:\\Users\\aking\\OneDrive\\Documents\\BYU Pathway\\Python\\Lessons\\books.txt") as file:
#     for line in file:
#         print(line.strip())

# Loop splitting
# people = [
#     "Stephanie 36",
#     "John 29",
#     "Emily 24",
#     "Gretchen 54",
#     "Noah 12",
#     "Penelope 32",
#     "Michael 2",
#     "Jacob 10"
# ]
# youngest_age = 9999
# youngest_person = ""

# for person in people:
#     name, age = person.split()
#     age = int(age)
#     if age < youngest_age:
#         youngest_age = age
#         youngest_person = name

# print(f"The youngest person is {youngest_person} who is {youngest_age} years old.")

line = "     text"

line.strip()

print(line)