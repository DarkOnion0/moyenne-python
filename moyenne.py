#!/usr/bin/python3.8
#! -*- coding:Utf-8 -*
stop = False
tmp = []
tmpn = ""
tmpc = ""
flag1 = 0
while stop == False :
    while flag1 == 0 :
        # Note
        print("Entrer une note")
        tmpn = input(">>> ")
    
        # Coefficiant
        print("Entrer un coef")
        tmpc = input(">>>")
    
        # Merging
        try:
            tmpn = float(tmpn)
            tmpc = float(tmpc)
            tmp.append((tmpn, tmpc))
            print(tmp)
            flag1 == 1
        except ValueError :
            print("Veuillez Insérer un nombre")

    print("Voulez vous continuer (o/n) ?")
    stoptmp = input(">>> ")
    if stoptmp == "n" :
        stop = True
