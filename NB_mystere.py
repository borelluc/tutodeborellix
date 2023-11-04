import sys
from random import randint

number_to_find= randint(0 , 200)
Tentative = 10
continuer = "o"
fin = "n"

print(" ******** LE JEUX DU NOMBRE MYSTERE HAHAHAHAH****")

while Tentative > 0:
    print(f" il te reste {Tentative} essai{'s' if Tentative>1 else ''}")
    user_choice= input(" DEVINE LE NOMBRE MYSTERE : ")
    if not user_choice.isdigit():
        print("veuillez entrer un nombre valide..")
        continue


    user_choice = int(user_choice)

    if number_to_find > user_choice:
        print(f"Le nombre mystere est plus grand que {user_choice}")
    elif number_to_find < user_choice:
        print(f" Le nombre mystere est plus petit que {user_choice} : ")
    else:
        break

    Tentative -= 1

if Tentative ==0:
     print(f" Domage ! le nombre etait {number_to_find}")
else:
    print(f"Bravo ! Le nombre mystere etait bien {number_to_find} !")
    print(f" Tu as trouver le nombre en {10 - Tentative} essai : ")

    print("Fin du jeux")

input( "Voulez-vous Reconmmncer le jeux  O/N :")

if user_choice == "n":
    sys.exit()

if user_choice == "o":
     continuer = True
     print(" C'est parti pour une Nouveau Round")

