#Verifions que le MDP est valide ou pas

mdp = input("Entrer votre mot de passe (8 caractere minimum) : ").title()
mdp_tro_court = ("votre mots de passe est trop court").upper()

if len(mdp) == 0:
    print(mdp_tro_court.upper())
elif len(mdp) < 8:
    print(mdp_tro_court.capitalize())
elif mdp.isdigit():
    print("votre mots de passe ne contient que des nombre.")
else:
    print("Inscription terminer !")
