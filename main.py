import random
import hashlib
import re #ça va me permettre de verifier la presence de caractere spéciaux
import json



while True:
    password=str(input("Veuillez entrer votre mot de passe : ")) # variable password
    if len(password) < 8:
        print("Votre mot de passe doit contenir au moins 8 caracteres ! ")
    else:    
        if any(i.isupper() for i in password):
            if any(i.islower()for i in password):
                if any(i.isdigit() for i in password):
                    if re.search(r'[^\w\s]', password): #ça me permettre de verifier la presence de caractere spéciaux
                        print("Votres mot de passe a été enregistré avec succès !")
                        hashword = password.encode()
                        hashword_hashed=hashlib.sha256(hashword).hexdigest()
                        print(hashword_hashed)
                        break
                    else:
                        print("Votre mot de passe doit contenir au moins un caractere spécial !")    
                else:
                    print("Votre mot de passe doit contenir au moins un chiffre !")    
            else:
                print("Votre mot de passe doit contenir au moins une minuscule !")    
        else:
            print("Votre mot de passe doit contenir au moins une majuscule !") 