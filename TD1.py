#!/usr/bin/env python
# coding: utf-8

# In[27]:


x=5
y=6
z=8

c=z-x
d=y+z
e=y**y

print(c)
print(d)
print(e)


# In[26]:


s = "test "
t = "encore un"

print (s + t)


# In[25]:


a=5>6
b=5==5
c=5>6
print(a)
print(b)
print(c)


# In[31]:


prenom="Eric"
nom="Lurton"
nom_complet=prenom+" "+nom
print(nom_complet*100)

initial=prenom[0]+nom[0]+''
print(initial*10)


# In[34]:


a=input("Quel est votre prénom")
b=input("Quel est votre nom")
print(a+" "+b)
print(a[0]+" "+b[0])


# In[ ]:


Temperature = float(input("Y meule là non ?"))

Fahrenheit = 9.0/5.0 * Temp + 32
print (Temperature, "C = ", Fahrenheit, " F")

Celsius = (Temperature - 32) * 5.0/9.0
print (Temperature, "F = ", Celsius, " C")


# In[ ]:


A=input('Entrer une valeur de verite pour A (entrer False ou True): ')
B=input('Entrer une valeur de verite pour B (entrer False ou True): ')
C=input('Entrer une valeur de verite pour C (entrer False ou True): ')

expression_bol=input('Entrer une expression Bolenne avec des "non", "ou", "et", et des parentheses: ')
expression_bol.replace('non', 'not')
expression_bol.replace('et', 'and')
expression_bol.replace('ou', 'or')
print (bool(expression_bol))

