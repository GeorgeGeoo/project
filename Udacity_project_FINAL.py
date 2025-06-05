import random
Villains = ["Orochimaru", "Akatsuki", "Kaguya Ōtsutsuki" ,"Tobi"]
Villain = random.choice(Villains)


heros = ["Naruto Uzumaki", "Kakashi Hatake", "Itachi Uchiha", "Jiraiya"]
hero = random.choice(heros)


powers = ["Rasengan", "Chidori", "Amaterasu", "Summoning Jutsu"]
power = random.choice(powers)


place = "field"
has_power = False
score = 0


def print_pause(message, delay=2):
    # this function prints a message and waits for a specified delay
    import time
    print(message)
    time.sleep(delay)
def capture_input(message, options):
    # this function captures user input and checks if it is in the options list
    choice = ""
    while not (choice in options):
        choice = input(message)
    return choice


def field():
    # this function represents the field where the player starts
    print_pause("you land in a very large field.")
    print_pause("you see a house in the distance.")
    print_pause("and you see a hut nearby.")
    print_pause("press 1 to go to the house.")
    print_pause("press 2 to go to the hut.")
    choice = capture_input("Choose 1 or 2:",["1","2"])
    if choice == "1":
        return "house"
    elif choice == "2":
        return "hut"


def house():
    # this function represents the house
    global Villains, has_power, score
    print_pause("you enter the house.")
    print_pause(f"then comes the {Villain}.")
    print_pause("press 1 to attack the Villain.")
    print_pause("press 2 to escape.")
    choice = capture_input("choose 1 or 2: ", ["1", "2"])
    if choice == "1":
        if has_power == True:
            print_pause(f"you attack the {Villain} with your {power}.")
            print_pause(f"you defeated the {Villain} and saved the day!")
            score = score + 70
            print_pause("you got 70 points for your brave!.")
        else:
            print_pause("you attack the Villain with your bare hands.")
            print_pause(f"{Villain} is too strong for you.")
            print_pause("you are dead.")
            score = score - 100
            print_pause("you lost 100 points for your foolishness.")
        return None
    elif choice == "2":
        print_pause("you manage to escape and return to the field.")
        score = score - 10
        print_pause("you lost 10 points for your cowardness.")
        return "field"


def hut():
    # this function represents the hut
    global has_power, score
    print_pause("you enter the hut.")
    if has_power:
        print_pause("you got here before, nothing new to find.")
    else:
        print_pause("you recoginize something on the table.")
        print_pause(f"you find the legendary power of Ninga is {power}.")
        has_power = True
        score = score + 30
        print_pause("you got 30 points for your cleverful.")
    print_pause("you return to the field.")
    return "field"




if __name__ == "__main__":
    turns = 0
    max_turns = 10 #the maximum number of turns allowed

    print_pause("welcome to the mysterious land of Village (Konoha)!")
    print_pause(f"Rumors say that a {Villain} is frightening the villagers.")
    print_pause(f"but you are the {hero} who will save the day!")

    while True:
        if place == "field":
            place = field()
        elif place == "house":
            place = house()
        elif place == "hut":
            place = hut()

        turns += 1
        print_pause(f"Turn {turns} of {max_turns}")
        print_pause(f"Your current score is: {score}")

        # the game ends if the player wins, loses, or runs out of turns
        if score >= 100:
            print_pause(f"You won! You collected enough\
                         power and defeated {Villain}!")
            break
        elif score <= -100:
            print_pause("Game over! You lost too many points.")
            break
        elif turns >= max_turns:
            print_pause("Game over! You ran out of turns.")
            break

        if place is None:
            print_pause("Game Over!!")
            if score >= 100:
                print_pause("congratulations, you won!")
            elif score < 50:
                print_pause("you lost, but you did well!")
            elif score <= 0:
                print_pause("you lost")
            print_pause(f"your score is {score}.")
            game_over = capture_input(
                "do you want to play again? y/n :", ["y", "n"]
            )
            if game_over == "y":
                place = "field"
                has_power = False
                score = 0
                turns = 0
                continue
            elif game_over == "n":
                break

    print_pause("thank you for playing!")
    print_pause("goodbye!")
