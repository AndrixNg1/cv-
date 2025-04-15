'''
import random

nombre = random.randint(1, 100)

i = 0

while True:
    essai = int(input("Entrez un nombre entre 1 et 100: "))
    i += 1
    
    if essai > nombre:
        print("Le nombre est plus grand.")
    elif essai < nombre:
        print("Le nombre est plus petit.")
    else:
        print("Bravo! Vous avez trouvé le nombre en", i, "tentatives.")
        break
print("Fin du programme.")

'''


nombre2 =100
nombre1=int(input("saisir un nombre: "))
nombre =3
if nombre  <= nombre2:
    i = 0
    while True:
        essai = nombre1
        i+=1

        if essai > nombre:
            print("Le nombre est plus grand.")
        elif essai < nombre:
            print("Le nombre est plus petit.")
        else:
            print("Bravo! Vous avez trouvé le nombre en", i, "tentatives.")
        break 
    print("fin programme ")
    

    ''''
    1/ declaration du premier variable qui garde la derniere ou la plus grande valeur a entrer
    2/ une deuxieme variable pour demander a l'utilisateur de saisir un nombre
    3/ une variable  pour stocker une valeur aleatoire 
    4/ une condition qui verfie si le nombre saisi par l'utilisateur est inferieur a la derniere valeur a choisir ex:100
    5/si True alors pn execute les conditions dans la conditions 
        a./ i comme compteur pour le nombre des fois qu'on peut faire l'essaie  
        b./ une boucle tanque qui s'ecute tanque la condition est vraie 
        c./on stocke dans la variable essaie le valeur saisi par l'utilisateur
        d./ on fait +  a notre compteur pour l'ajouter une nouvelle essai
        e./ une condition si essai > nombre on aficiche un message "le nombre est grand"
        f./ et un sinon si essai < nombre tempon on affiche un message dan sle print 
        g./ sinon on affiche juste le message bravo dan sle cas ou l'utilisateur a taper le bon nombre 
        h./ puis on fais un break pour sortir de la boucle : bon bref on sort de la boucle directement si l'une des instruction est True 
    6/ a la fin du programme on affiche juste un message 
    '''

import random

number = random.randint(1 ,100)
choice_number = number

while True:
    try:
        hum_choise=int(input("Entrez un nombre entre 1 et 100: "))