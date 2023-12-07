import json
import random
import string

# fich=open("repertoire_mdp.json","r")
# data=fich.readlines()
# for ligne in data:
#     print(ligne)
# fich.close    
letters = string.ascii_letters
numbers = string.digits
special_charactere = string.punctuation
alphabet=letters+numbers+special_charactere
lenght=12
password=""
for i in range(lenght):
    password += random.choice(alphabet)

print(password)
