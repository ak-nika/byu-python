# Guessing game
import random

number = random.randint(1, 100)
guess = -1
guess_count = 0

while guess != number:
    guess = int(input("What is your guess? "))
    
    guess_count += 1

    if guess > number:
        print("Lower")
    elif guess < number:
        print("Higher")
    elif guess == number:
        print("\nYou guessed it right")
        print(f"You guessed it in {guess_count} tries.")
        
        play = input("Do you want to play again?(Yes/No) ")
        
        if play.lower() == "yes":
            number = random.randint(1, 100)
            guess_count = 0
            continue
        else:
            break