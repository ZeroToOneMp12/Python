import random
import time
import string
 
# Entrez le mot de passe a trouver
mot_de_passe = input("Entrez le mot de passe a trouver: ")

# Fonction qui genere un mot de passe aleatoire
def mot_aleatoire(longueur):
    lettres = string.ascii_letters
    mot_genere = ""
    for caract in range (0, longueur):
        mot_genere = mot_genere + lettres[random.randint(0, len(lettres) - 1)]
    return mot_genere


# Boucle qui genere des mots de passes aleatoires jusqu'a ce qu'il trouve le bon
debut = time.time()     
while True:
    mot_alea = mot_aleatoire(len(mot_de_passe))
    if mot_de_passe == mot_alea:
        print("Mot de passe trouve: " + mot_alea)
        fin = time.time() - debut
        print("Temps d'execution: " + str(fin) + " secondes")
        break