import random
monsters = ["dragon", "goblin", "troll" ,"vampire", "werewolf"]
monster = random.choice(monsters)

superheros = ["superman", "batman", "spiderman", "ironman", "wonderwoman"]
superhero = random.choice(superheros)


def print_pause(message, delay=4):
     import time
     print(message)
     time.sleep(delay)

print_pause("welcome to the mysterious land of Pythonia!")
print_pause(f"Rumors say that a {monster} is frightening the villagers.")
print_pause(f"but you are the {superhero} who will save the day!")
print_pause("you land in a very large field.")
print_pause("you see a castle in the distance.")
print_pause("and you see a cave nearby.")
print_pause("press 1 to go to the castle.")
print_pause("press 2 to go to the cave.")

def capture_choice():
    while True:
        choice = input("What do you want to do? (1 or 2): ")
        if choice in ["1", "2"]:
            return choice
        else:
            print("Invalid choice. Please enter 1 or 2.")

move = capture_choice()
print("you chose to go to the castle." 
      if move == "1"
       else "you chose to go to the cave.")              