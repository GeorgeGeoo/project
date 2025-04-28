def prtint_pause(message, delay=2):
    import time
    print(message)
    time.sleep(delay)

import random
monsters = ["dragon", "goblin", "troll" ,"vampire", "werewolf"]
monster = random.choice(monsters)

heros = ["superman", "batman", "spiderman", "ironman", "wonderwoman"]
hero = random.choice(heros)

prtint_pause("welcome to the mysterious land of Pythonia!")
prtint_pause(f"Rumors say that a {monster} is frightening the villagers.")
prtint_pause(f"but you are the {hero} who will save the day!")    
prtint_pause("you land in a very large field.")
prtint_pause("you see a castle in the distance.")
prtint_pause("you see a cave nearby.")
prtint_pause(f"press 1 to go to the castle():.")
prtint_pause("press 2 to go to the cave.")

def capture_choice():
    while True:
        choice = input("What do you want to do? (1 or 2): ")
        if choice in ["1", "2"]:
            return choice
        else:
            print("Invalid choice. Please enter 1 or 2.")
move = capture_choice()
print("you chose to go to the castle." if move == "1" else "you chose to go to the cave.")

def castle():
    prtint_pause("you enter the castle.")
    prtint_pause("you see a treasure chest.")
    prtint_pause("you see a dragon guarding the treasure.")
    prtint_pause("you can either fight the dragon or sneak past it.")
    prtint_pause("press 1 to fight the dragon.")
    prtint_pause("press 2 to sneak past the dragon.")


    if __name__ == "__main__":
        castle()
        move = capture_choice()
        if move == "1":
            prtint_pause("you chose to fight the dragon.")
            prtint_pause("you defeat the dragon and take the treasure.")
        else:
            prtint_pause("you chose to sneak past the dragon.")
            prtint_pause("you successfully sneak past the dragon and take the treasure.")