import random # Module qui contient la fonction random.choice()
import time # Module qui contient la fonction time.time()
import string # Module qui contient les lettres de l'alphabet
import hashlib # Module qui contient la fonction hashlib.md5()
import sys # Module qui contient la fonction sys.exit()

mot_de_passe = input("Entrez le mot de passe a trouver: ")
mot_de_passe_mp5 = hashlib.md5(mot_de_passe.encode("utf8")).hexdigest() # Variable qui contient le mot de passe en md5
print("Mot de passe en md5: " + mot_de_passe_mp5) # Affiche le mot de passe en md5

def hash_crack():
    try:
        mot_fr = open("liste-francais.txt", "r") # Variable qui contient le fichier francais.txt
        for mot in mot_fr.readlines():
            mot = mot.strip("\n").encode("utf8") # Enleve les espaces
            print(hashlib.md5(mot).hexdigest()) # Affiche le mot de passe en md5
            
    except FileNotFoundError:
        print("Erreur: Le fichier n'existe pas")
        sys.exit(1)
    except Exception as err:
        print("Erreur : " + str(err))
        sys.exit(2)
        

deb = time.time() # Variable qui contient le temps de depart
hash_crack() # Appelle la fonction hash_crack()
#print("mot_aleatoire " + mot_aleatoire()) # Affiche le mot de passe aleatoire genere
print("Temps d'execution: " + str(time.time() - deb) + " secondes") # Affiche le temps d'execution



"""
# Boucle qui genere des mots de passes aleatoires jusqu'a ce qu'il trouve le bon
debut = time.time()     
while True:
    mot_alea = mot_aleatoire(len(mot_de_passe))
    if mot_de_passe == mot_alea:
        print("Mot de passe trouve: " + mot_alea)
        fin = time.time() - debut
        print("Temps d'execution: " + str(fin) + " secondes")
       break
# Fonction qui genere un mot de passe aleatoire
def mot_aleatoire(): 
    lettres = string.ascii_letters # string.ascii_letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    suiv = "" # Variable qui contient la lettre suivante
    resultat = "" # Variable qui contient le mot de passe
    for i in range (len(mot_de_passe)): # Boucle qui genere un mot de passe aleatoire de la meme longueur que le mot de passe a trouver
        while mot_de_passe[i] != suiv: 
            print(resultat + suiv)
            suiv = random.choice(lettres)
        resultat += suiv # Ajoute la lettre trouvee au mot de passe attention pense à mettre l'espace pour mettre au même niveau que ta boucle while sinon cela renvoi juste une lettre  
    return resultat
 
 """