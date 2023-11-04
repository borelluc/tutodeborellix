import random

ENEMY_HEALTH = 50
PLAYER_HEALTH = 50
NUMBER_OF_POTIONS = 3
SKIP_TURN = False

print("       WELCOME BORELLIX Apprendre le jeux de guere pas a pas ☠️ ☠️ ☠️ ☠️ ☠️ ☠️ ☠️ ☠️  \n ","-" * 100)

print(" CHOISISSEZ L'OPTIONS 1🅰️ OU 2 🅱️ ")

while True:
    if SKIP_TURN:
        print("Vous passez votre tour..")
        SKIP_TURN = False
    else:
        user_choice = ""
        while user_choice not in ["1", "2"]:
            user_choice = input("Souhaiter vous Attaquer (1)⚔️ ⚔️⚔️⚔️⚔️⚔️⚔️⚔️ ou utiliser une potion (2)🧪 🧪🧪🧪🧪🧪? ")
            if user_choice == "1":
                your_attack = random.randint(5, 10)
                ENEMY_HEALTH -= your_attack
                print(f" Vous avez infliger{your_attack} pooint de degats de L'enemie ")
            elif user_choice == "2":
                if NUMBER_OF_POTIONS > 0:
                    potions_health = random.randint(15, 50)
                    PLAYER_HEALTH += potions_health
                    NUMBER_OF_POTIONS -= 1
                    SKIP_TURN = True
                    print(f" vous avez recuperez  {potions_health} potions de vie ({NUMBER_OF_POTIONS} restante) ")
                else:
                    print("vous n'avez plus de posion desole...")
                    continue

    if ENEMY_HEALTH <= 0:
        print("tu as gagne ")
        break

    enemy_attack = random.randint(5, 15)
    PLAYER_HEALTH -= enemy_attack
    print(f"L'ENEMY vous as infliger {enemy_attack} point de degats")

    if PLAYER_HEALTH <= 0:
        print("tu as perdu")
        break

    print(f"il vous reste {PLAYER_HEALTH} point de vie.")
    print(f"il te reste {ENEMY_HEALTH} point de vie a L'enemi.")
    print("-" * 100)

print("Fin du jue.")
