#!/usr/bin/python3.8
#! -*- coding:Utf-8 -*
# Definition du modules
from moyennemod import * 
import pickle

total = list()
globalstop = False # Boucle générale
moygeneraltmp = float()

while globalstop == False:
   
   # Déclaration de variable
    mastop = False # Boucle de la créaton de la matière
    nostop = False # Boucle de la création des notes

    mastopask = "o"
    stoptmp = "o"
    tmp = []
    tmpn = ""
    tmpc = ""
    nostop = False
    notetmp = 0.0

    while mastop == False: # Demande de la matière
        
        try:
            print("Quelle matière voulez vous créer ?")
            matmp = input(">>> ")
            print("Etes vous sur de créer une matière du nom de : {}".format(matmp))    
            mastopask = input("(o/n) \n>>> ")
            print(mastopask)  
            assert mastopask != "O" or "o" or "N" or "n"
        except AssertionError   :
            print("Veuillez ecrire la réponse en minuscule")
        
        if  mastopask == "o" or mastopask ==  "O" :
            print("\n")
            mastop = True
        
        else:
            mastop = False
    
    while nostop == False : # Demande de la note
        
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
            print("Voulez vous continuer (o/n) ?")
            stoptmp = input(">>> ")
            if stoptmp == "n" :
                nostop = True
            else:
                print('\n')
                nostop = False
        except ValueError :
            print("Veuillez inserer un nombre")
    
    # Calcul et fin du programme
    notetmp = moyenne(tmp)
    total.append((matmp, notetmp))

    print(total)
    try:
        globalstopask = input("Voulez vous recrez une matière (o/n) \n>>> ")
        assert globalstopask == "O" or "o" or "N" "n"
    except ValueError:
        print("Veuillez répondre avec (o) ou (n) ;")

    if globalstopask == "O" or globalstopask == "o": # Continuation du programme
        print('\n')
        globalstop = False
    if globalstopask == "N" or globalstopask == "n": # Arret du programme
        globalstop = True
        file = open('data.txt', 'w')
        file.write("Moyenne des matières")
        file.write("\n+----------")
        file.write('\n')
        for matiere, note in total:
            like = emoji(note)
            print("\nVous avez {} de moyennne en {} {}".format(note, matiere, like))
            # Ecriture dans un fichier lisible de la session actuelle
            file.write("\nVous avez {} de moyennne en {} {}".format(note, matiere, like))
        
        index = len(total)
        for flag, note in total:
            moygeneraltmp += note
        moygeneral = round(moygeneraltmp / index,  2)
        
        like = emoji(moygeneral)

        print('\n')
        print("Vous avez {} de moyenne générale {}".format(moygeneral, like))
        print("\n\U0001F4A1 Vos notes sont stocké dans un fichier data.txt dans le dossier actuelle")
        file.write("\n\nMoyenne Générale")
        file.write("\n+----------")
        file.write('\n')
        file.write("\nVous avez {} de moyenne générale {}".format(moygeneral, like))
        file.close()