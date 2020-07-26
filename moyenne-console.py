#!/usr/bin/python3.8
#! -*- coding:Utf-8 -*

# Importation des modules
from  moyenne import *

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

