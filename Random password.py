import random
import time
import string
 
# Entrez le mot de passe a trouver
mot_de_passe = input("Entrez le mot de passe a trouver: ")

# Fonction qui genere un mot de passe aleatoire
def mot_aleatoire(longueur):
    lettres = string.ascii_letters
    suiv = ""
    resultat = ""
    for i in range (len(mot_de_passe)):
        while mot_de_passe[i] != suiv: 
            suiv = random.choice(lettres)
    resultat += suiv
    return resultat

# Boucle qui genere des mots de passes aleatoires jusqu'a ce qu'il trouve le bon
debut = time.time()     
while True:
    mot_alea = mot_aleatoire(len(mot_de_passe))
    if mot_de_passe == mot_alea:
        print("Mot de passe trouve: " + mot_alea)
        fin = time.time() - debut
        print("Temps d'execution: " + str(fin) + " secondes")
        break