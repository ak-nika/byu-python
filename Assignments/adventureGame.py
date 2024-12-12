"""
Author: Akingbayi Ojo
Purpose: To create a text based adventure game.
Creativity: The user can select what type of adventure they would like to go through. In the sci-fi adventure, there is a secret option and in the horror, there is a sanity meter.
"""
import random

print("Welcome to my adventure game.")
print("Select what type of adventure you would like to go through.")
adventure = input("FANTASY, SCI-FI, or HORROR? ").strip()

if adventure.lower() == "fantasy":
    print("\nWelcome to the FANTASY game.")
    print("You are a knight on a quest to rescue the princess from a dragon. You are at the entrance of a dark cave.")

    choice = input("Do you want to go ENTER, SEARCH or GO BACK? ").strip()

    if choice.lower() == "enter":
        print("\nYou entered the cave.")
        print("You hear the sleeping dragon's breathing in the distance.")
        choice1 = input("Do you DRAW your sword to attack, use MAGIC to hide yourself, or SNEAK around quietly? ")

        if choice1.lower() == "draw":
            print("\nYou drew your sword.")
            print("The dragon wakes up and you prepare for a battle.")
            choice2 = input("Do you ATTACK, DEFEND, or RUN? ").strip()

            if choice2.lower() == "attack":
                print("\nYou attacked the dragon.")
                print("You enter a fierce battle and defeat the dragon.")
                print("The princess is saved!!")
                print("YOU WIN!!")
            elif choice2.lower() == "defend":
                print("\nYou defended yourself.")
                print("The dragon uses its fire breath and burns you alive.")
                print("You die.")
            elif choice2.lower() == "run":
                print("\nYou ran away from the dragon.")
                print("You are attacked by the dragon and die.")
            else:
                print("\nInvalid option. You are attacked by the dragon and die.")
        elif choice1.lower() == "magic":
            print("\nYou used magic.")
            print("You turn invisible and the dragon remains asleep.")
            choice2 = input("Do you FREE the princess first, STEAL the dragon's treasure, or ENCHANT the dragon's magic? ").strip()

            if choice2.lower() == "free":
                print("\nYou free the princess.")
                print("YOU WIN!!")
            elif choice2.lower() == "steal":
                print("\nYou stole the dragon's treasure and run away.")
                print("The villagers find out and attack you.")
                print("You die.")
            elif choice2.lower() == "enchant":
                print("\nYou attempt enchant the dragon")
                print("You don't have enough magic for something that size.")
                print("The dragon wakes up and you die.")
            else:
                print("\nInvalid option. The dragon wakes up and you are attacked by the dragon and die.")
        elif choice1.lower() == "sneak":
            print("\nYou snuck around the dragon's cave.")
            print("The ground beneath you starts to shake.")
            print("You notice a tree near you.")
            choice2 = input("Do you CONTINUE sneaking, CLIMB the tree, or turn BACK? ").strip()

            if choice2.lower() == "continue":
                print("\nYou continued sneaking.")
                print("The dragon wakes up and you prepare for a battle.")
                choice3 = input("Do you ATTACK, DEFEND, or RUN? ").strip()

                if choice3.lower() == "attack":
                    print("\nYou attacked the dragon.")
                    print("You enter a fierce battle and defeat the dragon.")
                    print("The princess is saved!!")
                    print("YOU WIN!!")
                elif choice3.lower() == "defend":
                    print("\nYou defended yourself.")
                    print("The dragon uses its fire breath and burns you alive.")
                    print("You die.")
                elif choice3.lower() == "run":
                    print("\nYou ran away from the dragon.")
                    print("You are attacked by the dragon and die.")
                else:
                    print("\nInvalid option. You are attacked by the dragon and die.")
            elif choice2.lower() == "climb":
                print("\nYou climbed the tree.")
                print("The dragon hears you and wakes up.")
                print("You are attacked by the dragon and die.")
            elif choice2.lower() == "back":
                print("\nYou turned back.")
                print("The dragon wakes up and attacks you.")
                print("You don't have enough time to react and you die.")
        else:
            print("\nInvalid option. You are attacked by the dragon and die.")
    elif choice.lower() == "search":
        print("\nYou searched the area and found a secret passage to the dragon's treasure.")
        choice1 = input("Do you ENTER the passage, GO BACK or CONTINUE searching? ").strip()

        if choice1.lower() == "enter":
            print("\nYou entered the passage.")
            print("The dragon wakes up and you prepare for a battle.")
            choice2 = input("Do you ATTACK, DEFEND, or RUN? ").strip()

            if choice2.lower() == "attack":
                print("\nYou attacked the dragon.")
                print("You enter a fierce battle and defeat the dragon.")
                print("The princess is saved!!")
                print("YOU WIN!!")
            elif choice2.lower() == "defend":
                print("\nYou defended yourself.")
                print("The dragon uses its fire breath and burns you alive.")
                print("You die.")
            elif choice2.lower() == "run":
                print("\nYou ran away from the dragon.")
                print("You are attacked by the dragon and die.")
            else:
                print("\nInvalid option. You are attacked by the dragon and die.")
        elif choice1.lower() == "back":
            print("\nYou went back.")
            print("The dragon wakes up and attacks you.")
            print("You don't have enough time to react and you die.")
        elif choice1.lower() == "continue":
            print("\nYou continued searching.")
            print("The dragon senses you and wakes up.")
            choice2 = input("Do you ATTACK, DEFEND, or RUN? ").strip()

            if choice2.lower() == "attack":
                print("\nYou attacked the dragon.")
                print("You enter a fierce battle and defeat the dragon.")
                print("The princess is saved!!")
                print("YOU WIN!!")
            elif choice2.lower() == "defend":
                print("\nYou defended yourself.")
                print("The dragon uses its fire breath and burns you alive.")
                print("You die.")
            elif choice2.lower() == "run":
                print("\nYou ran away from the dragon.")
                print("You are attacked by the dragon and die.")
            else:
                print("\nInvalid option. You are attacked by the dragon and die.")
        else:
            print("\nInvalid option. You are attacked by the dragon and die.")
    elif choice.lower() == "go back":
        print("\nYou left the dragon's cave.")
        print("The princess dies and you are blamed for it.")
        print("You are killed by the villagers.")
    else:
        print("\nInvalid option.")
        print("You wake up the dragon and are attacked by it at the entrance.")
        print("You are killed by the dragon.")
elif adventure.lower() == "sci-fi":
    print("\nWelcome to the SCI-FI game.")
    print("You have crash landed on an alien unknown alien planet. You need to find resources to repair your ship.")
    choice1 = input("Do you EXPLORE the planet, SEARCH for resources, or WAIT? ").strip()

    if choice1.lower() == "explore":
        print("\nYou explored the planet.")
        print("You entered a dense alien jungle. You see some strange creatures.")
        choice2 = input("Do you OBSERVE them, FLEE back to your ship, or ATTACK them? ").strip()

        if choice2.lower() == "observe":
            print("\nYou observed the creatures.")
            choice3 = input("Do you MIMIC them, FLEE back to your ship, or WAIT? ").strip()

            if choice3.lower() == "mimic":
                print("\nYou mimicked the creatures.")
                print("You were able to communicate with them.")
                print("They take you to where valuable resources are.")
                print("You find the resources to repair your ship.")
            elif choice3.lower() == "flee":
                print("\nYou fled back to your ship.")
                print("The creatures noticed you and followed you.")
                print("You notice and run faster.")
                print("The creatures reach you and attacked you.")
                print("You died.")
            elif choice3.lower() == "wait":
                print("\nYou waited.")
                print("The creatures notice you and became hostile to you.")
                print("They attacked you and you die.")
            else:
                print("\nInvalid option. The creatures attacked you.")
                print("You died.")
        elif choice2.lower() == "flee":
            print("\nYou fled back to your ship.")
            print("The creatures noticed you and followed you.")
            print("You notice and run faster.")
            print("You fall into a ditch.")
            choice3 = input("Do you WAIT to be rescued, or do you CLIMB out? ").strip()

            if choice3.lower() == "wait":
                print("\nYou waited to be rescued.")
                print("You are rescued by a nice alien.")
                print("You find the resources to repair your ship and repair your ship.")
            elif choice3.lower() == "climb":
                print("\nYou climbed out of the ditch.")
                print("The creatures attacked you.")
                print("You died.")
        elif choice2.lower() == "attack":
            print("\nYou attacked the creatures.")
            print("They attacked you back.")
            print("You died.")
        else:
            print("\nInvalid option. The creatures attacked you.")
            print("You die.")
    elif choice1.lower() == "search":
        print("\nYou searched the area and found an alien civilization.")
        choice2 = input("Do you ENTER the civilization, RETURN to your ship, or CONTINUE searching? ").strip()

        if choice2.lower() == "enter":
            print("\nYou entered the civilizations.")
            print("You find advanced technology.")
            choice3 = input("Do you TAKE the technology, LEAVE it and return to your ship, or CONTINUE searching? ").strip()

            if choice3.lower() == "take":
                print("\nYou took the technology.")
                print("You repaired your ship.")
            elif choice3.lower() == "leave":
                print("\nYou left the technology and returned to your ship.")
                print("You were unable to repair your ship.")
                print("You remain stranded and died.")
            elif choice3.lower() == "continue":
                print("\nYou continued searching and found nothing.")
                print("You remain stranded and died.")
            else:
                print("\nInvalid option. You remain stranded.")
                print("You die.")
        elif choice2.lower() == "return":
            print("\nYou returned to your ship.")
            print("You waited for help but no one came to help.")
            print("You died.")
        elif choice2.lower() == "continue":
            print("\nYou continued searching and found nothing.")
            print("You remain stranded and died.")
        else:
            print("\nInvalid option. You remain stranded.")
            print("You die.")
    elif choice1.lower() == "wait":
        print("\nYou waited for a while.")
        print("No one came for you.")
        print("You starved to death.")
    elif choice1.lower() == "investigate":
        print("\nCongratulations for finding the secret option!!")
        print("You investigated the planet.")
        print("You found a spaceship and entered the spaceship.")
        print("A pass code is required to enter.")
        pass_code = int(input("Enter the pass code (hint: The pass code is a 4 digit number): ").strip())

        if pass_code == 1234:
            print("\nYou entered the spaceship.")
            print("You found a spaceship and repaired your ship.")
            print("YOU WIN!!")
        else:
            print("\nWrong pass code. The spaceship triggered an alarm and blew up.")
            print("You died.")
    else:
        print("\nInvalid option. You found a spaceship and repaired your ship.")
elif adventure.lower() == "horror":
    sanity = 100
    print("\nWelcome to the HORROR game.")
    print("You are a detective asked to investigate a mysterious mansion that is said to be haunted.")
    choice = input("Do you ENTER the mansion, CHECK the grounds, or LEAVE? ").strip()

    if choice.lower() == "enter":
        sanity -= random.randint(1, 20)
        print("\nYou entered the mansion and feel a cold chill down your spine. The air is thick and dreary.")
        choice1 = input("Do you investigate the ATTIC, BASEMENT, or LIVING ROOM? ").strip()

        if choice1.lower() == "attic":
            sanity -= random.randint(5, 10)
            print("\nYou entered the attic and see strange symbols on the floor.")
            choice2 = input("Do you INVESTIGATE the symbols, STAND in the circle, or LEAVE? ").strip()

            if choice2.lower() == "investigate":
                sanity -= random.randint(20, 50)
                print("\nYou investigated the symbols.")

                if sanity < 40:
                    print("\nYou see the symbols and run insane.")
                else:
                    print("You investigate the symbols and a monster appears.")
                    print("It drags you into the circle.")
            elif choice2.lower() == "stand":
                sanity -= random.randint(20, 50)

                if sanity < 50:
                    print("\nDue to the effect of the symbols, you run insane.")
                else:
                    print("\nThe circle activates and traps you inside.")
                    print("You remain in trapped and eventually die in the circle.")
            elif choice2.lower() == "leave":
                print("\nYou leave quickly and luckily, you escape the monsters form the symbols")
                print("You make it out alive...")
            else:
                print("\nInvalid option. You get trapped in the attic and die.")
        elif choice1.lower() == "basement":
            sanity -= random.randint(5, 10)

            print("\nYou entered the basement.")
            print("You hear faint whispers from the basement.")
            choice2 = input("Do you CALL out, remain SILENT, or LEAVE? ").strip()

            if choice2.lower() == "call":
                sanity -= random.randint(10, 20)

                if sanity < 50:
                    print("\nThe whisper grows louder.")
                    print("You can't take it anymore and run out of the mansion but something follows...")
                else:
                    print("\nYou manage to stay calm but the basement door suddenly shuts.")
                    print("You are trapped in the basement and eventually die.")
            elif choice2.lower() == "remain":
                print("\nYou manage to stay calm and avoid any confrontation from spirits.")
                print("You find a back door and leave the mansion.")
            elif choice2.lower() == "leave":
                print("\nYou try to leave but the basement door suddenly shuts.")
                print("You are trapped in the basement and eventually die.")
            else:
                print("\nInvalid option. The spirits claim you and you die.")
        elif choice1.lower() == "living room":
            sanity -= random.randint(10, 40)

            print("\nYou entered the living room.")
            print("You see a painting.")
            choice2 = input("Do you INVESTIGATE it, IGNORE it, or TAKE it?").strip()

            if choice2.lower() == "investigate":
                sanity -= random.randint(10, 40)

                if sanity < 50:
                    print("\nAs you approach the painting, you begin to see illusions.")
                    print("You eventually go insane and run out of the mansion a mad man.")
                else:
                    print("\nYou investigate the painting and find a ghost.")
                    print("The ghost attacks you and you die.")
            elif choice2.lower() == "ignore":
                print("\nYou ignore the painting and see noting.")
                print("You leave the mansion peacefully.")
            elif choice2.lower() == "take":
                sanity -= random.randint(20, 45)

                if sanity < 50:
                    print("\nAs you touch the painting, your environment starts to change and you feel... different")
                    print("Turns out you're insane now :)")
                else:
                    print("\nAs you touch the painting, you are attacked by ghosts")
                    print("You die")
            else:
                print("\nInvalid option. You see ghosts.")
                print("They attack you and you die.")
        else:
            print("\nInvalid option. You found a ghost and died.")
    elif choice.lower() == "check":
        print("\nYou checked the grounds.")
        print("You notice a graveyard behind the mansion.")
        choice1 = input("Do you ENTER the graveyard, RETURN to the entrance, or LEAVE the mansion? ")

        if choice1.lower() == "enter":
            print("\nYou enter the graveyard and notice a thick fog")
            choice2 = input("Do you ENTER the fog, TURN back to the entrance, or LEAVE? ").strip()

            if choice2.lower() == "enter":
                print("\nYou entered the fog.")
                print("You found some ancient text. This text solves the mystery of the mansion.")
                print("YOU WIN!!")
            elif choice2.lower() == "turn":
                print("\nYou turned back to the entrance.")
                print("You hear a strange noise. The mansion has claimed another victim. You lose.")
            elif choice2.lower() == "leave":
                print("COWARD.")
                print("You try to leave but are attacked by ghosts and die like a coward :)")
            else:
                print("\nInvalid option. You get attacked by ghosts and die.")
        elif choice1.lower() == "return":
            print("\nYou turn back and return to the mansion.")
            print("You hear a strange noise. The mansion has claimed another victim. You lose.")
        elif choice1.lower() == "leave":
            print("COWARD.")
            print("You try to leave but are attacked by ghosts and die like a coward :)")
        else:
            print("\nInvalid option. You get attacked by ghosts and die.")
    elif choice.lower() == "leave":
        print("\nYou left the building.")
        print("COWARD")
        print("You found a ghost and died.")
    else:
        print("\nInvalid option. You found a ghost and died.")
else:
    print("Invalid input. Please enter either FANTASY, SCI-FI, or HORROR.")

print("\nTHE END")