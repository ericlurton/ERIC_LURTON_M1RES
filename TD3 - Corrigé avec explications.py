#!/usr/bin/env python
# coding: utf-8

# In[3]:


# Exercice 1


n = input("Entrer un nombre: ") #Demande un nombre
for i in range(1,11): #Tant que i est inclus entre 1 et 11 --> on affiche n*i, donc n*1 à 10
    print(n*i)

print("# *** 1 *** #")

n = input("Entrer un nombre: ")
for i in range(1,11):
    print(n*i, end = ' ') #le end = ' ' permet d'écrire le tt en une ligne


print("\n")
print("# *** 3 *** #")

n = input("Entrer un nombre: ")
for i in range(n): 
    print("Table de", i+1, ":", end = ' ')
    for j in range(1,11):
        print((i+1)*j, end = ' ')
    print("\n")


print("\n")
print("# *** 4 *** #")

n = input("Entrer un nombre: ")
for i in range(n):
    print("*"*(i+1))


print("# *** 5 *** #")

n = input("Entrer un nombre: ")
for i in range(n):
    print(" "*((n-1)-i) + ("* "*(i+1))[:2*(i+1)-1] + " "*((n-1)-i))


# In[ ]:


# Exercice 2

print("# *** 1 *** #")
#Créations des listes
jours = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
mois = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

#Création de la liste dans laquel on lie les jours & moi
mj = []
for i in range(12): #Tant que i n'as pas fait 12 boucles ( car il y a 12 mots par listes, donc on à besoin de 12 boucles )
    mj.append((mois[i], jours[i]))#A la fin de la liste mj, on ajoute le mots numéroté "i" des listes mois puis jours
#Et i s'intialise à 1 prenant ainsi le 1er mots de chaque liste, puis 2, le 2e etc etc
print(mj)
#Afficher mj affichera donc les mois liés aux nombres de jours

print("# *** 2 *** #")
#Creation d'une liste annee
annee = []
for x in mj: #Initialasiation de x dans mj
	for y in range(x[1]): #Dans une liste, le compteur commence à 0, ici, tant que y est inférieur au jours
		annee.append(str(y+1) + " " + x[0]) #On ajoute a la fin de la liste anne, 0+1, un espace, et le mois de la liste
#y s'incrémente de 1 mais reste inférieur à 31, donc ça nous permet de boucler jusqu'à 31 pour ajouter dans la liste tout les jours / mois

print(annee)

print("# *** 3 *** #")
#création d'une liste année 2
annee2 = []
jours_semaine = ["Monday", "Tueday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
for x in range(365):#tant que x n'atteint pas 365 car il y a 365 jour dans l'année et en supposant que l'année commence un lundi
	annee2.append(jours_semaine[x%7] + " " + annee[x]) #On ajoute à la fin de année2 les jours de la semaine les uns après les autres
#suivis d'un espace, et de la liste année. X va s'incrémenter de 1 jusqu'à 365 permettant de faire tout les jours
#le x modulo 7 permet de faire boucler la liste jour semaine à 7 et de recommencer à monday à chaque fois
print(annee2)


print("# *** 4 *** #")
#création d'un dictionnaire
dico_annee = {}
#Tant que i n'a pas atteint 365
for i in range(365):
	dico_annee[annee[i]] = jours_semaine[i%7]
#on rajoute dans le dictionnaire la liste des jours de l'année comme précedemment je comprend pas trop la formule

print(dico_annee)


print("# *** 5 *** #")
#On peut rechercher dans le dico, c'est marrant je suis né le 28 octobre
print(dico_annee["28 October"])


# In[ ]:


# Exercice 3


print("# *** 1 *** #")
#initialisation d'une variable nb à 0 et d'une liste vide
nb = 0
liste_notes = []
#tant que nb < 3 ( 0 1 2 )
while nb < 3:
	note = input("Entrer une note: ") #Créé une input nommé note, demandant une note
	liste_notes.append(note) #on ajoute à la fin de la liste la note
	nb += 1 #on incrémente nb de 1
    
#Ainsi le prgm va demander 3 notes, et les mettres dans une liste
#Definissions des variable "mini" et "maxi" prenant grâce aux fonctions min & max les extrêmes de la liste
mini = min(liste_notes)
maxi = max(liste_notes)
#Initialisation d'une variable moy à 0
moy = 0
#Calcul de la moyenne je comprend mais pas trop
for n in liste_notes:
	moy += n
moy = float(moy)/len(liste_notes)

print("Note minimale:", mini)
print("Note maximale:", maxi)
print("Moyenne:", moy)



print("# *** 2 *** #")
#création d'une input demandant le nombre de note qu'il veut rentrer
#même programme qu'au dessus
nb_notes = input("Combien de notes voulez-vous entrer? ")
nb = 0
liste_notes = []
while nb < nb_notes:
	note = input("Entrer une note: ")
	liste_notes.append(note)
	nb += 1

mini = min(liste_notes)
maxi = max(liste_notes)
moy = 0
for n in liste_notes:
	moy += n
moy = float(moy)/len(liste_notes)

print("Note minimale:", mini)
print("Note maximale:", maxi)
print("Moyenne:", moy)



print("# *** 3 *** #")

#Même programme en spécifiant que l'utilisateur peut entrer autant de note qu'il veut jusqu'à ce qu'il écrive "fin" comme vu au TD2

liste_notes = []
note = input("Entrer une note (taper fin pour terminer la saisie): ")
while note != "fin":
	liste_notes.append(float(note))
	note = input("Entrer une note (taper fin pour terminer la saisie): ")

mini = min(liste_notes)
maxi = max(liste_notes)
moy = 0
for n in liste_notes:
	moy += n
moy = float(moy)/len(liste_notes)

print("Note minimale:", mini)
print("Note maximale:", maxi)
print("Moyenne:", moy)


# In[ ]:


# Exercice 4

#importation de la fonction random
from random import *
#on définis une variable n1 aléatoire inclus entre 0 et 100 et de n2 à -1 pour être sur que par hasard n1 ne soit pas égal à n2
n1 = randint(0,100)
n2 = -1

while n2 != n1: #tant que n2 est différent de n1
	n2 = input("Esssayer de deviner le nombre: ") #l'utilisateur fait une proposition qui sera sauvegardé en tant que n2
	if n2 < n1: #si
		print("plus haut...")
	elif n2 > n1: #sinon si
		print("plus bas...")
print("Correct!")

