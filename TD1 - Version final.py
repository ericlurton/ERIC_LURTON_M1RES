#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Exo 1

x=5
y=6
z=8

c=z-x #Soustraction
d=y+z #Additions
e=y**y #Exponantielli, je sais pas l'écrire mais vous avez compris
f=y*y #Multiplication classique
g=z/x #Division classique
h=z%x #Modulo ==> reste de la division, 8/5 == 1 fois 5 + 3 de reste

print(c)
print(d)
print(e)
print(f)
print(g)
print(h)


# In[8]:


#Exo 2

s = "test"
t = "encore un"

l=s[1] #Va mettre dans "l" le caractère n°1 de "S", sachant que la chaine commence à 0
k=len(s) #Affiche la longueur en caractère de S
m=s[0:6] #Va print les caractère de S allant de 0 à 6, si il y a - de 6 caractère, bah on s'arrête au dernier caractère

print(l,k,m)


# In[12]:


#Exo 3

a=5>6 #On sait bien que 6 est supérieur à 5, donc A devrait retourner "false"
b=5==5 #True
c=5>6 #False
e=5!=5 #!= veut dire "différent de", hors 5 ne peux pas être différent de 5, donc ça devrait nous sortir false
print(a)
print(b)
print(c)
print(e)


# In[16]:


#Exo 4

prenom="Eric"
nom="Lurton"
nom_complet=prenom+" "+nom
print(nom_complet*100)

initial=prenom[0]+nom[0]+''
print(initial*10)


# In[ ]:


#Exo 5

a=input("Quel est votre prénom") #Input va permettre de créé une "boite" ou l'utilisateur peut inscrire une donné
b=input("Quel est votre nom")
print(a+" "+b) #Ecrit prénom nom
print(a[0]+" "+b[0]) #Ecrit la première lettre du prénom et du nom, car pour rappel le premier caractère d'une variable est numéroté à 0


# In[ ]:


#Exo 6

temp = float(input("Quel est la température ?"))
degre = ((9/5) * temp) + 32
far = (temp - 32) * (5/9)
print(str(temp), "C = ", (degre), "F")
print(str(temp), "F = ", (far), "C")


# In[ ]:


#Exo 7 ne fonctionne pas malgré l'aide de camarade

A=input('Entrer une valeur de verite pour A (entrer False ou True): ')
B=input('Entrer une valeur de verite pour B (entrer False ou True): ')
C=input('Entrer une valeur de verite pour C (entrer False ou True): ')

expression_bol=input('Entrer une expression Bolenne avec des "non", "ou", "et", et des parentheses: ')
expression_bol.replace('non', 'not')
expression_bol.replace('et', 'and')
expression_bol.replace('ou', 'or')
print (bool(expression_bol))


# In[ ]:




