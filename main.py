import random
import hashlib
import re #ça va me permettre de verifier la presence de caractere spéciaux
import json
import string

#__init__
letters = string.ascii_letters
numbers = string.digits
special_charactere = string.punctuation
alphabet=letters+numbers+special_charactere


def add_pssword():
    with open("repertoire_mdp.json","w") as fichier:
        json.dump(list,fichier)

list=[]
while True:
    reponse=input("Voulez vous générer un mot de passe?(1=oui/2=non) : ")
    if reponse == "1":
        password=""
        lenght=12
        vrai=False
        while vrai == True:
            for i in range(12):
                password += random.choice(alphabet)
                print(password)
                if not any(i.isupper() for i in password):
                    vrai=True
                    if not any(i.islower()for i in password):
                        vrai=True
                        if not any(i.isdigit() for i in password):
                            vrai=True
                            if not re.search(r'[^\w\s]', password): #ça me permettre de verifier la presence de caractere spéciaux
                                vrai=False
    else:           
        password=str(input("Veuillez entrer votre mot de passe : ")) # variable password
    if len(password) < 8:
        print("Votre mot de passe doit contenir au moins 8 caracteres ! ")
    else:    
        if any(i.isupper() for i in password):
            if any(i.islower()for i in password):
                if any(i.isdigit() for i in password):
                    if re.search(r'[^\w\s]', password): #ça me permettre de verifier la presence de caractere spéciaux
                        print("Votres mot de passe a été enregistré avec succès !")
                        print(password)
                        hashword = password.encode()
                        hashword_hashed=hashlib.sha256(hashword).hexdigest()
                        if ("password : "+hashword_hashed) not in list:
                            list.append("password : "+hashword_hashed)     
                        print(list)                   
                        add_pssword()
                        rep=input("voulez vous voir l'historique des vos mot de passe ?(1=oui/2=non) : ")
                        if rep=="1":
                            with open("repertoire_mdp.json","r") as fichier:
                                for i in fichier:
                                    print(str(i))    
                        rep2=input("voulez vous arreter ?(1=oui/2=non) : ")
                        if rep2=="1": 
                            break                  
                    else:
                        print("Votre mot de passe doit contenir au moins un caractere spécial !")    
                else:
                    print("Votre mot de passe doit contenir au moins un chiffre !")    
            else:
                print("Votre mot de passe doit contenir au moins une minuscule !")    
        else:
            print("Votre mot de passe doit contenir au moins une majuscule !") 