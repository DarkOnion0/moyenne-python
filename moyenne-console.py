#!/usr/bin/python3.8
#! -*- coding:Utf-8 -*

# Importation des modules
import os 
# Definition du modules
def moyenne(tmp):
    """
    Calcul de moyenne a partir d'une liste avec des tulpes avec en premiers: 
    les notes puis les coefs ; 
    Exemple : a = [(note, moyenne)]
    """
    tmpfrno1 = [note * coef for note, coef in tmp] # Extraction des notes fois les coefs
    #print(tmpfrno1) # Debug

    for index, note in enumerate(tmpfrno1): # Combination des notes
        if index == 0:
            frno1 = tmpfrno1[0]
        else:
            frno1 += tmpfrno1[index]
    #print(frno1) # Debug

    # Coefficiants
    tmpfrco1 = [coef for note, coef in tmp] # Extraction des coefs
    #print(tmpfrco1) # Debug

    for index, note in enumerate(tmpfrco1): # Combination des coefs
        if index == 0:
            frco1 = tmpfrco1[0]
        else:
            frco1 += tmpfrco1[index]
    print(frco1) # Debug
    # Affichage final

    fr1 = frno1 / frco1
    fr1 = round(fr1, 2)
    print("Vous avez {} de moyenne en Francais".format(fr1))

# Déclaration de variable
stop = False
tmp = []
tmpn = ""
tmpc = ""
try1 = False
frno1 = 0.0

#Francais note / coef définitions
while stop == False :
    
    while try1 == False :
        try:
           # Note
            print("Entrer une note")
            tmpn = input(">>> ")
    
            # Coefficiant
            print("Entrer un coef")
            tmpc = input(">>> ") 
            tmpn = float(tmpn)
            tmpc = float(tmpc)
            
            # La ligne en dessous sert a debugger
            tmp.append((tmpn, tmpc))
            print(tmp)
            try1 = True 
        except ValueError :
            print("Veuillez inserer un nombre")
    
    print("Voulez vous continuer (o/n) ?")
    stoptmp = input(">>> ")
    if stoptmp == "n" :
        stop = True
    else:
        print('\n')
        try1 = False

print(moyenne(tmp))
