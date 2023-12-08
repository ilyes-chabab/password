import random
import hashlib
import re #ça va me permettre de verifier la presence de caractere spéciaux
import json
import string
import os

#__init__
#pour la génération de mot de passe
letters = string.ascii_letters
numbers = string.digits
special_charactere = string.punctuation
alphabet=letters+numbers+special_charactere
password=""
minuscule= random.choice(string.ascii_lowercase)
majuscule= random.choice(string.ascii_uppercase)
chiffres= random.choice(string.digits)
caractere_spéciale=random.choice(string.punctuation)


def add_pssword(mdp):
    with open("repertoire_mdp.json","a") as fichier: 
        json.dump(mdp,fichier)#commande qui écrit ce que l'on veut dans un autre fichier.json

def verif_mdp(mdp):
    with open("repertoire_mdp.json","r") as fichier: 
        if mdp not in fichier.read():
            add_pssword(mdp)
def fichier_inexistant(mdp):
    with open("repertoire_mdp.json","w") as fichier: 
        json.dump(mdp,fichier)


list=[]#pour stocker les mdp
while True: #boucle pour pouvoir mettre plusieurs mdp
    reponse=input("Voulez vous générer un mot de passe?(1=oui/2=non) : ")#l'utilisateur choisis entre générer un mdp ou ecrire son mdp
    if reponse == "1":
        minimum= minuscule+majuscule+chiffres+caractere_spéciale #je crée cette fonction minimum pour que le mdp ait les prérequis
        password= minimum
        for i in range(12):
            password += random.choice(alphabet) #ensuite j'ajoute au mot de passe 12 caractere , chaque caractere sera piocher au hasard dans une selection de Lettre majuscule , minuscules , de nombres et de caractere speciaux               
    else:           
        password=str(input("Veuillez entrer votre mot de passe : ")) # variable password
    if len(password) < 8:  
        print("Votre mot de passe doit contenir au moins 8 caracteres réesseyez svp. ") #on revient au debut de la boucle si le mdp a moins de 8 caracteres , 
    else:    
        if any(i.isupper() for i in password):#on revient au debut de la boucle si le mdp n'a pas de majuscule.
            if any(i.islower()for i in password):#on revient au debut de la boucle si le mdp n'a pas de minuscule
                if any(i.isdigit() for i in password):#on revient au debut de la boucle si le mdp n'a pas de nombres
                    if re.search(r'[^\w\s]', password): #on revient au debut de la boucle si le mdp n'a pas de caractere spéciaux
                    #re;search permet de chercher quelque chose dans un mot et r'[^\w\s]' permet de chercher des caractere spéciaux
                        print(f"Votres mot de passe a été enregistré avec succès !")
                        print(f' Votre mot de passe est {password}')
                        hashword = password.encode() #ça permet de coder le message avant de la hasher en sha256
                        hashword_hashed=hashlib.sha256(hashword).hexdigest()
                        if ("password : "+hashword_hashed) not in list: #ca permet de d'ajouter seulement les mdp qui ne sont pas dans la liste, si le mdp est dans la liste , il ne sera pas ajouté
                            list.append("password : "+hashword_hashed) 
                        if os.path.exists("repertoire_mdp.json"):
                            verif_mdp(hashword_hashed)
                        else:
                            fichier_inexistant(hashword_hashed)    
                        rep=input("voulez vous voir l'historique des vos mot de passe ?(1=oui/2=non) : ")
                        if rep=="1": #historique des mdp
                            print("---HISTORIQUE DES MOT DE PASSE---")
                            with open("repertoire_mdp.json","r") as fichier: #commande qui écrit le contenu d'un fichier dans le terminal
                                for i in fichier:
                                    print(i)    
                        rep2=input("voulez vous arreter ?(1=oui/2=non) : ")
                        if rep2=="1":
                            break #si l'utilisateur souhaite arreter ca break la boucle 
                    else:#Tout les else qui renvoie les différentes erreurs
                        print("Votre mot de passe doit contenir au moins un caractere spécial réesseyez svp.")    
                else:
                    print("Votre mot de passe doit contenir au moins un chiffre réesseyez svp.")    
            else:
                print("Votre mot de passe doit contenir au moins une minuscule réesseyez svp.")    
        else:
            print("Votre mot de passe doit contenir au moins une majuscule réesseyez svp.") 