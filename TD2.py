#!/usr/bin/env python
# coding: utf-8

# In[20]:


c = "qsdksdvdwcowkd452sdq5j23sqd" ###QST 1 - 2
c_num = ""
c_alpha = ""
for caracters in c: #Pour tt les caractères composant C
    if str.isdigit(caracters) == True: #Extraits les caractères numériques
        c_num += caracters #Les enregistres dans c_num
    else:
        c_alpha += caracters #Enregistre les autres dans c_alpha

print(c_num, c_alpha)

###QST 3

str_find = "j23"
c.find(str_find)
if c.find(str_find) != -1:
    new_c = c.replace(str_find, "j24")
    print(new_c)

###QST 4 pas réussi :)


# In[19]:


##cpts le nb de lettre
texte = "We introduce here the Python language." ##QST 1
i = 0
for lettre in texte:
    i = i+1
if i == len(texte):
    print("Il y a", i,"lettre dans ta phrase")
else:
    print("CA BUG") 


mots = len(texte) #Extrait le nombre de lettre et d'espace
espace = len(texte.split()) #Extrait le nombre d'espace --> split
print("Il y a", espace, "mots dans ta phrase")
print(int(mots)-int(espace),",c'est le nombre de lettres sans les espaces") #Nombre de lettre sans espace

#QST 2

texte2 = "We introduce here the Python language. To learn more about the language, consider going through the excellent tutorial https://docs.python.org/ tutorial. Dedicated books are also available, such as http://www.diveintopython.net/."

mots = len(texte2.split())
print(mots)


# In[21]:


a = input("Entrer des mots separes par un espace : ")
user_list = a.split() ##va séparé les caractères eux même séparés par des espaces
list_triee = sorted(user_list) ##créé une liste trié de c e que j'ai séparé lahaut là
print(list_triee) ##On imprime


# In[ ]:


a = input("Entrer des mots separes par un espace : ")
main_liste=[] #liste a remplir
while True : #Pour faire en sorte qu'on puisse écrire plein de mot jusqu'à FIN
    if a != "FIN":
        user_list = a.split() 
        list_triee = sorted(user_list)
        print(list_triee)
    else :
        break


# In[ ]:


import random from shuffle

couleurs=["Pique","Trèfle","Carreau","Coeur"]
valeurs =[2,3,4,5,6,7,8,9,10,"valet","dame","roi","as"]
for x in couleurs():
    for y in valeurs():
        listefinal=print (couleurs(x)+valeurs(y))
        y+1
    x+1
    

random.shuffle(listefinal)
print("Liste après le premier mélange",listefinale)


# In[12]:


with open("diamonds.csv", "r") as f:
    diamants=f.readlines()
    ping 8.8.8.8
    


# In[ ]:


a=input("NOM PRENOM MATRICULE")
list = values.split(" ")
tuple = tuple(list)
print(tuple)
while True:
    choix = input("Entrer prenom, nom et matricule étudiant séparés par un espace : (FIN pour finir) ")
    if choix == "FIN":
        break
    else:
        list = choix.split(" ")
        montuple = tuple(list)
        main_list.append(montuple)


# In[ ]:





# In[ ]:




