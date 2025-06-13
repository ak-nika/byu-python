"""
Author: Akingbayi Ojo
Purpose: To generate a clever story
"""

import random

print("Please enter the following:\n")

# Get the values needed for the story
adjective = input("adjective: ")
animal = input("animal: ")
verb1 = input("verb: ")
exclamation = input("exclamation: ")
verb2 = input("verb: ")
verb3 = input("verb: ")
# Additional values
object = input("object: ")
action = input("action: ")

# Add random event
random_event = random.choice(
    [
        "it started raining cupcakes",
        "it hit the road",
        "a pig flew by",
        "a snail suddenly jumped on me",
    ]
)

# Print the story
print("\nYour story is:\n")

print(
    f'The other day, I was really in trouble. It all started when I saw a very {adjective} {animal} {verb1} down the hallway. "{exclamation.capitalize()}!" I yelled. But all I could think to do was to {verb2} over and over. Then suddenly, {random_event}. Miraculously, that caused it to stop, but not before it tried to {verb3} right in front of my family {object}. I was so shocked that I decided to {action}. It truly was a day I would not forget.'
)
