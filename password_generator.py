import string
import secrets
import math 
import os
# la préparation des caracteres 
minuscule = string.ascii_lowercase
majuscules = string.ascii_uppercase
chiffres = string.digits
symboles = string.punctuation
tous_les_caracteres = minuscule + majuscules + chiffres + symboles
# choix de la longueur 
while True :
    try:
        long = int(input("Entrez la longueur du mot de passe souhaitée : "))
        if long < 8 :
            print("Attention : un mot de passe de moins de 8 caractères n'est pas sécurisé ! Réessayez.")
        else :
            break # quand la valeur est correcte et >= 8 on sort de la boucle 
    except ValueError:
        print("Erreur : Veuillez entrer un nombre entier valide.")
# boucle de generation 
mot_de_passe_liste = []
for _ in range(long) :
    mot_de_passe_liste.append(secrets.choice(tous_les_caracteres))
# Assemblage et affichage 
mot_de_passe_final = ''.join(mot_de_passe_liste)
print("Voici ton mot de passe sécurisé :", mot_de_passe_final)
# le nbre total de caracteres dans notre reservoir 
n = len(tous_les_caracteres)
# calcul de l'entropie
entropie = long * math.log2(n)
# Détermination du niveau de force et de l'émoji
if entropie < 50:
    niveau = "Faible 🔴"
elif entropie <= 75:
    niveau = "Moyen 🟡"
else:
    niveau = "Fort 🟢"
# Affichage 
print(f"Force du mot de passe : {entropie:.2f} bits ({niveau})")

# Demande a l'utilisateur s'il souhite enregistrer 
choix = input("Voulez-vous sauvegarder ce mot de passe ? (o/n):").strip().lower()
if choix == 'o' :
    service = input("Pour quel service ou site (ex: Gmail, Facebook, GitHub) ? :")
# Ouverture du fichier en mode 'a' 
    dossier_actuel = os.path.dirname(os.path.abspath(__file__))
    chemin_fichier = os.path.join(dossier_actuel, "passwords.txt")

    with open(chemin_fichier, "a", encoding="utf-8") as fichier:
        fichier.write(f"Service : {service} | Mot de passe : {mot_de_passe_final} | Entropie : {entropie:.2f} bits ({niveau})\n")
        print("Mot de passe sauvegardé avec succès dans 'passwords.txt' !")
else:
    print("Mot de passe non sauvegardé.")