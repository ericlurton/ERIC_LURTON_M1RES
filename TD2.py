#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Exo 1

c = "X44bf38j23jdjgfjh737nei47" ###QST 1 - 2
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

#4
i1 = c.find("f") #va chercher f et l'enregistrer dans i1
i2 = c.find("3") #idem 3
i3 = c.find("7") #7

if (i1 < i2) and (i2 < i3): #sachant que les caractères sont ordonné numériquement, si i1 < i2, veut dire si f arrive
                            #dans la chaine de caractère avant 3, et que i2 < i3, donc que 3 arrive avant 7
    print("Le pattern f37 existe dans la chaîne c") #cela répond au paterne voulu de F37 pas forcément consécutif
else:
    print("Le pattern f37 n'existe pas dans la chaîne c") #autrement


# In[19]:


#Exo 2
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


#Exercice 3

#1
liste_mots = [] #création d'une liste de mots, actuellement vide
m1 = input("Entrer un mot: ") #Demande un premier mot
liste_mots.append(m1) #rajoute a la fin de la liste le resultat de l'input
m2 = input("Entrer un mot: ")
liste_mots.append(m2) #toujours à la fin, donc après m
m3 = input("Entrer un mot: ")
liste_mots.append(m3)

liste_mots.sort() #.sort permet de trier par ordre alphabétique la liste

for m in liste_mots:#Pour chaque variable m contenu dans la liste ( sachant que tout nos mots ont une variable mX )
    print(m)#On affiche ces v ariables l'une après l'autre
    
liste_mots2 = []#Liste de mot vide
mot = input("Entrer un mot (taper FIN pour terminer la saisie): ")
while (mot != "FIN") and (mot != "fin"):#Tant que l'utilisateur n'as pas rentré le mot fin ou FIN ( au cas ou )
    liste_mots2.append(mot) #on ajoute le mot écrit dans l'input à la fin de la liste
    mot = input("Entrer un mot (taper FIN pour terminer la saisie): ") #permet de bouclé jusqu'à FIN ou fin

liste_mots2.sort() #Triage de la liste

for m in liste_mots2: #Même logique qu'au 1
    print(m)


# In[ ]:


#1
couleurs = ['Pique', 'Trefle', 'Carreau', 'Coeur']
valeurs = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'valet', 'dame', 'roi', 'as']

# Construction de la liste des 52 cartes :
cartes = []
for coul in couleurs:
	for val in valeurs:
		cartes.append(str(val) + " de " + coul)		
print(cartes)

#2
from random import shuffle

shuffle(cartes)
print(cartes)

#3
joueur1 = []
joueur2 = []
joueur3 = []
joueur4 = []

compteur = 0
for c in cartes:
	if compteur == 0:
		joueur1.append(c)
		compteur = (compteur + 1) % 4 
	elif compteur == 1:
		joueur2.append(c)
		compteur = (compteur + 1) % 4 
	elif compteur == 2:
		joueur3.append(c)
		compteur = (compteur + 1) % 4 
	elif compteur == 3:
		joueur4.append(c)
		compteur = (compteur + 1) % 4 

print(joueur1)
print(joueur2)
print(joueur3)
print(joueur4)


# In[12]:


#1
print('----1----')
dico_etudiants = {}

prenom = input("Entrer le prenom de l'etudiant: ")
nom = input("Entrer le nom de l'etudiant: ")
matricule = input("Entrer le matricule de l'etudiant: ")
dico_etudiants[nom] = (prenom, nom, matricule)
print(dico_etudiants)

#2
print('----2----')
dico_etudiants = {}
while True:
	prenom = input("Entrer le prenom de l'etudiant (entrer FIN pour terminer la saisie): ")
	if (prenom == "FIN") or (prenom == "fin"):
		break
	else:
		nom = input("Entrer le nom de l'etudiant: ")
		matricule = input("Entrer le matricule de l'etudiant: ")
		dico_etudiants[nom] = (prenom, nom, matricule)

#3
print('----3----')
for nom_etud in dico_etudiants:
	print("Prenom:", dico_etudiants[nom_etud][0] + ".", "Nom:", dico_etudiants[nom_etud][1]  + ".", "Matricule:", str(dico_etudiants[nom_etud][2]) + ".")

#4
print('----4----')
if "Obama" in dico_etudiants.keys():
	print("Prenom:", dico_etudiants["Obama"][0] + ".", "Nom:", dico_etudiants["Obama"][1]  + ".", "Matricule:", str(dico_etudiants["Obama"][2]) + ".")

#5
print('----5----')
for k, v in dico_etudiants.items():
	if v[2] == 12345678:
		print("Prenom:", dico_etudiants[k][0] + ".", "Nom:", dico_etudiants[k][1]  + ".", "Matricule:", str(dico_etudiants[k][2]) + ".")

#6
print('----6----')
dico_etudiants = {}
while True:
  prenom = input("Entrer le prenom de l'etudiant (entrer FIN pour terminer la saisie): ")
	if (prenom == "FIN") or (prenom == "fin"):
		break
	else:
		nom = input("Entrer le nom de l'etudiant: ")
		matricule = input("Entrer le matricule de l'etudiant: ")
		#ici, les clés deviennent des strings nom + matricule
		dico_etudiants[nom + str(matricule)] = (prenom, nom, matricule)

for nom_matricule in dico_etudiants:
	print("Prenom:", dico_etudiants[nom_matricule][0] + ".", "Nom:", dico_etudiants[nom_matricule][1]  + ".", "Matricule:", str(dico_etudiants[nom_matricule][2]) + ".")

