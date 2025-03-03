#!/usr/bin/env python
# coding: utf-8

# In[6]:


def multi():
    a = int(input("Entrer un nombre à multiplier : "))
    for b in range(1,11):
        print(a*b)  #Va afficher tout les calculs a*b avec b[1-10]

multi()


# In[8]:


def multi2():
    a = int(input("Entrer un nombre à multiplier : "))
    for b in range(1, 11):
        print(a*b, end=" ") #End ="" permet de tout écrire sur une ligne
        
multi2()


# In[3]:


def multiplat():
    a = int(input("Entrer un nombre pour trouver les tables de ce nombre et celle inférieur : "))
    for b in range(a):
        print("Table de", int(b) + 1, ":")
        for i in range(1, 11):
            print(b+1)*i,)
            
multiplat()


# In[11]:


def multi4():
    a = int(input("Entrer un nombre à afficher en asterisk : "))
    for b in range(a):
        print("*" * (b+1))
        
multi4()


# In[12]:


def multi5():
    a = int(input("Entrer un nombre à afficher en pyramide d'asterisk : "))
    for b in range(a):
        print(" " * ((user-1)-b) + ("* " * (b+1)))
multi5()


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


# In[18]:


def note():
    user_nb = int(input("Combien de note"))
    liste_notes = []
    while len(liste_notes) < user_nb:
        user = int(input("Entrer une note : "))
        liste_notes.append(user)
    mini = min(liste_notes)
    maxi = max(liste_notes)
    som = 0

    for notes in liste_notes:
        som += int(notes)
    moy = float(som) / len(liste_notes)

    print("moyenne " + str(moy), "minimum " + str(mini), "maximum " + str(maxi))

note()


# In[ ]:


def note2():
    user_nb = int(input("Entrer le nombre de notes que vous voulez entrer ? "))
    liste_notes = []
    while len(liste_notes) < user_nb:
        user = int(input("Entrer une note : "))
        liste_notes.append(user)
    mini = min(liste_notes)
    maxi = max(liste_notes)
    som = 0

    for notes in liste_notes:
        som += int(notes)
    moy = float(som) / len(liste_notes)

    print("moyenne " + str(moy), "minimum " + str(mini), "maximum " + str(maxi))
    
    
note2()


# In[19]:


def note3():
    liste_notes = []
    while True:
        user = input("Entrer une note : (fin pour finir) ")
        if user == "fin":
                break
        else:
            liste_notes.append(float(user))
            mini = min(liste_notes)
            maxi = max(liste_notes)
            som = 0
            for notes in liste_notes:
                som += int(notes)
            moy = float(som) / len(liste_notes)

    print("moyenne " + str(moy), "minimum " + str(mini), "maximum " + str(maxi))


note3()


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

