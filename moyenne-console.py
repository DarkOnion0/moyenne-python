#!/usr/bin/python3.8
#! -*- coding:Utf-8 -*
# Definition du modules
from moyennemod import *

# Déclaration de variable
mastop = False
nostop = False
globalstop = False

mastopask = "o"
tmp = []
tmpn = ""
tmpc = ""
nostop = False
frno1 = 0.0

while globalstop == False:
   
    while mastop == False:
        # Demande de la matière
        try:
            print("Quelle matière voulez vous créer ?")
            matmp = input(">>> ")
            print("Etes vous sur de créer une matière du nom de : {}".format(matmp))    
            mastopask = input("(O/n) \n>>> ")
            print(mastopask)  
            assert mastopask != "O" or "o" or "N" or "n"
        except AssertionError   :
            print("Veuillez ecrire la réponse en minuscule")
        if  mastopask == "o" or mastopask ==  "O" :
            print("\n")
            mastop = True
        else:
            mastop = False
    
    # Demande de note
    while nostop == False :
        try:
            #Note
            print("Entrer une note")
            tmpn = input(">>> ")
    
            # Coefficiant
            print("Entrer un coef")
            tmpc = input(">>> ") 
            tmpn = float(tmpn)
            tmpc = float(tmpc)
            
            tmp.append((tmpn, tmpc))
            print(tmp)
            nostop = True 
        except ValueError :
            print("Veuillez inserer un nombre")
    
        print("Voulez vous continuer (o/n) ?")
        stoptmp = input(">>> ")
        if stoptmp == "n" :
            nostop = True
        else:
            print('\n')
            nostop = False
    fr1 = moyenne(tmp)
    print("Vous avez {} de moyenne en Francais".format(fr1))
