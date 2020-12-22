#!/usr/bin/env python
# coding: utf-8

# In[4]:


#Exercice 1

#1
def surf_circle(a): #On demande un "argument" une valeur qui prendra "a"
#On importe pi de la fonction math
    from math import pi
#On créé une variable "surface" avec le calcul de la surface du cercle en fonction de son rayon qu'on a définis plus haut
    surface=pi*(a**2)
#return == va retourner & concrétement print le résultat
    return surface

print(surf_circle(7.5))

#2
#Modification du prgrm pour faire ne sorte que l'argument est par défault la valeur 1
def surf_circle_2(b=1):
    from math import pi
    surface=pi*(b**2)
    return surface

print(surf_circle_2(8))

#3
def volboite(c,d,e):#On demande les 3 côtés de la boite puis calc volume
    calcul=(c*d*e)
    return calcul

print(volboite(1,3,9))

#4
def volboite(f,g,h):
    if g==None and h==None: #Si g ET h non remplis
        g==f and h==f #g et h prennent la valeur de f
        calcul=(f*g*h) #calcul classique
        print("La boite est cubique")
        return calcul
    elif h==None:#
        h==f #POUR FAIRE UN CARRE
        calcul=(f*g*h) #calcul classique
        print("La boite est un parallepipède a base carré")
        return calcul
    else:   
        calcul=(f*g*h)#autrement
        print("La boite est un parralepipède générale")
        return calcul

print(volboite(1,3,2))

#5
def remplacement(arg_1=3)
    arg_1 = c1
    arg_2 = c2
    arg_3 = ch
    c1=" "
    c2="*"
    ch = "Je fais un test juste pour voir en théorie, les espaces devraient être remplacé par des étoiles grâce à la fonction replace"

print ch.replace(c1,c2)

#6
def remplacement(*args)
    ch2 = "Test d'une autre manière"
    print(ch2.replace(" ","*"))


# In[14]:


#Exo 2

def nb_char(chaine):
    counter = 0 #Création d'une variable counter à 0
    for c in chaine: #Par caractère dans le texte, counter gagne 1
        counter += 1
    print(counter) #On affiche le nombre de caractère compté

print(nb_char(chaine="Décret n° 2020-1600 du 16 décembre 2020 relatif à la composition, à l'organisation et au fonctionnement du conseil de surveillance prévu à l'article L. 253-8 du code rural et de la pêche maritime"))


def nb_mots(chaine):
    mots = len(chaine.split())
    return mots

print(nb_mots(chaine="Décret n° 2020-1600 du 16 décembre 2020 relatif à la composition, à l'organisation et au fonctionnement du conseil de surveillance prévu à l'article L. 253-8 du code rural et de la pêche maritime"))


# In[22]:


#Exo 3

def multi(n, debut=1, fin=10): #On définis les 3 arguments début, fin et une variable n
    i=debut
    while i!=fin:
        print(n*i) #Afficher les multiplications de n commençant a "début=1" et finissant à fin
        i=i+1

multi(6)

def multi2(n, debut=1, fin=10):
    liste=[]
    if debut>fin:
        for i in range(fin, debut+1):
            liste.append(n*i)
        liste.reverse()
        print(liste)
    else:
        for i in range(debut,fin+1):
            liste.append(n*i)
        print(liste)
        
def multi3():
    ndébutfin=[]
    n = int(input("Entrer n"))
    début = int(input("Entrer le début"))
    fin = int(input("Entrer la fin"))
    ndébutfin.append(n,début,fin)
    
    liste = []
    if debut > fin:
        for i in range(fin, debut + 1):
            liste.append(n * i)
        liste.reverse()
        print(liste)
    else:
        for i in range(debut, fin + 1):
            liste.append(n * i)
        print(liste)


# In[ ]:


def motus(arg_1=10): #10 entrée possible
    from random import randint #On importe la fonction randint
    mots = ["arbre", "grave", "piece", "nuage", "crane", "sonne", "table", "herbe", "ecrou", "mulet"]
    choixmot=mots(randint(0,9)) #0-9 car la liste mots commence à 0
    motalpha=[] #On créé une liste dans laquel on récupérera le mot choisis aléatoirement
    motalpha[0]=choixmot #En caractère car dans une liste
    
#Le travail ci dessous est tolalement inspiré, par celui d'un camarade, je comprend ce qu'il a fait mais aurait été incapable de le faire par moi même

    for x in range(len(word)): #Tant que x < longueur du mot
        user.append("-") #On rajoute un - à la fin de la liste pour faire le fléchage ( herbe --> ----- )
    print(" ".join(user)) #Initialisation de "user"
    compteur = 0

    while True:
        compteur += 1
        if compteur == arg_1 + 1: #Si jamais le programme dépasse en nombre d'essaie la longueur du mots, il s'arrête
            break 
        else:
            print("Essai numéro : " + str(compteur)) 
            ask = input("Entrer une lettre : ") #On demande une lettre
            for i in range(len(word)):
                if ask == word[i]: #Si la lettre est dans le mot, on l'affiche et on remplace le - associé
                    user[i] = word[i]
                    if user == word: #Si l'user trouve le mot, il gagne
                        print(" ".join(user))
                        win = input("Bravo! Rejouer ? y/n ")
                        if win == "y":
                            motus()#Si il veut rejouer, on relance le programme
                        else:
                            exit()
                else:
                    pass
            print(" ".join(user)) #Si l'user n'a pas trouvé dans les essaies nécessaire, il perd, et le programme s'arrête sauf si l'user veut rejouer

    rejoue = input("Perdu... Rejoue y/n : ")
    if rejoue == "y":
        motus()
#motus()


# In[6]:





# In[ ]:


#Exo 5

#Pas réussi

