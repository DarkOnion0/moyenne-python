#!/usr/bin/python3.8
#! -*- coding:Utf-8 -*

# Déclaration de variable
stop = False
tmp = []
tmpn = ""
tmpc = ""
try1 = False

#Francais note / coef définitions
while stop == False :
    
    # Note
    print("Entrer une note")
    tmpn = input(">>> ")
    
    # Coefficiant
    print("Entrer un coef")
    tmpc = input(">>>")
    
    while try1 == False :
        try:
            tmpn = float(tmpn)
            tmpc = float(tmpc)
            tmp.append((tmpn, tmpc))
            print(tmp)
            try1 = True
        except ValueError :
            print("Veuillez inserer un nombre")
    
    print("Voulez vous continuer (o/n) ?")
    stoptmp = input(">>> ")
    if stoptmp == "n" :
        stop = True

# Convertion et calcul

