"""
Author: Akingbayi Ojo
Purpose: To guess a hidden word
Creativity: The word is selected at random from a list and a user can add the number of attempts they would like to guess the word
"""
import random

print("Welcome to the Wordle game!")
print("You have to guess today's word\n")

word_list = ["temple", "moroni", "nephi", "joseph", "church", "aaron", "moses", "alma"]
word = random.choice(word_list)
guess = ""
guess_count = 0
available_guess = int(input("How many attempts would you like? "))

while word.lower() != guess.lower():
    # Check if the user has run out of guesses
    if available_guess <= 0:
        print(f"\nYou ran out of guesses! The word was: {word}")
        break

    if not guess:
        # Display the number of letters (hint) before the first guess
        print("Your hint is:", "_ " * len(word))
    elif len(word) != len(guess):
        # Check if the guess and the word are the same length
        print("Sorry, the guess must have the same number of letters as the secret word.")
    else:
        # Attempt to display the hint
        print("\nYour hint is: ", end="")
        # Give hints based on the current guess
        for index in range(len(word)):
            if index < len(guess) and guess[index].lower() == word[index].lower():
                # Correct letter at correct position
                print(f"{guess[index].upper()} ", end="")  
            elif index < len(guess) and guess[index].lower() in word.lower():
                # Correct letter but wrong position
                print(f"{guess[index].lower()} ", end="")
            else:
                # Incorrect or missing letter
                print("_ ", end="") 
    
    # Display the number of guesses left
    print(f"\nYou have {available_guess} guess(es) left")

    # Get the next guess
    guess = input("\nWhat is your guess? ")
    
    # Increase the number of guesses made
    guess_count += 1
    
    if guess.lower() != word.lower():
        # Check if the guess is correct
        print("Wrong! Try again.")
        
        # Reduce the number of available guesses
        available_guess -= 1
    elif guess.lower() == word.lower():
        # Check if the guess is correct
        print("\nCorrect!")
        print(f"You guessed the word {word.capitalize()} in {guess_count} guesses.")
        break