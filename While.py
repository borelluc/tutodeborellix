import sys

LISTE = []

MENU = """ Choisissez parmis les 5 options Suivantes :

1: Ajouter un element a la listes
2: Retirer un element de la liste
3: Afficher un elemet de la liste
4: vider la liste
5: Quittes la listes
👉Votre choix : """

MENU_CHOICES = ["1","2","3","4","5"]

while True:
    user_choice=""
    while user_choice not in MENU_CHOICES:
        user_choice = input(MENU)
        if user_choice not in MENU_CHOICES:
            print("veuillez choisir une options valide")

    if user_choice =="1":
        item = input("Entrer le nom d'un elements a Ajouter a la liste de sourses : ")
        LISTE.append(item)
        print(f" L' element {item} a bien ete Ajouter.")
    elif user_choice =="2":
        item = input("Entrer le nom de l'element a retirer dans la listes des courses : ")
        if item in LISTE:
            LISTE.remove(item)
            print(f"L'element {item} a ete bien supprimer de la liste...")
        else:
            print(f"L'element {item} n'est pas dans la liste.")
    elif user_choice == "3":
        if LISTE:
            print("voici le contenu de votre liste : ")
            for i, item in enumerate(LISTE, 1):
                print(f"{i}. {item}")
        else:
            print("votre liste contiens Aucun Element")
    elif user_choice == "4":
        LISTE.clear()
        print("la liste a ete videe de son contenu.")
    elif user_choice == "5":
        print("A bientot s'etais borellix")
        sys.exit()

    print("-"*50)


