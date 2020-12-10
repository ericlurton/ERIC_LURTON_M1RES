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


from random import *
def aleatoire():
    aleatoire1 = randint(1,100)
    correct = False
    while not correct:
        user = int(input("Un nombre entre 1e t 100 "))
        if aleatoire1 > user:
            print("trop bas")
        elif aleatoire1 < user:
            print("trop haut")
        elif aleatoire1 == user:
            break

    if aleatoire1 == user:
        rejoue = input ("Encore" (y or n) ")
        if rejoue == 'y':
            exo4()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




