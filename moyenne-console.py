#!/usr/bin/python3.8
#! -*- coding:Utf-8 -*
# Definition du modules
from moyennemod import * 
import pickle

total = list()
nobackupstop = False # Boucle générale
moygeneraltmp = float()
backupstop = False
yesbackupstop = True
backup = dict()

while backupstop == False:
    
    try:
        ask1 = input("Voulez vous restaurer un fichier (o/n)\n>>> ")
        assert ask1 != "O" or "o" or "N" or "n"
    except AssertionError   :
        print("Veuillez ecrire O ou N")
    
    if  ask1 == "o" or ask1 ==  "O" :
        print("\n")
        
        backupfile = open('data.bin', 'rb')
        backup = pickle.load(backupfile)
        backupfile.close()
        
        backupstop = True
        yesbackupstop = False
        
        print('\n')
    else:
        backupstop = True
        print('\n')

while yesbackupstop == False:
    
    # Déclaration de varibles
    stoptmp = "o"
    tmp = []
    tmpn = ""
    tmpc = ""
    nostop = False
    notetmp = 0.0
    ask2stop = False

    try:
        ask2 = input("Voulez vous \n1- Completer une matière \n2- Créer une nouvelle matière\n>>> ")
        assert ask2 == "1" or "2"
    except AssertionError:
        print("Veuillez répondre avec 1 ou 2")
    
    if ask2 == "1":
        while ask2stop == False:
            try:
                print("Quelle matière souhaitez vous modifier")
                for ma in backup.keys(): 
                    print("- ", ma)
                ask2_1 = input(">>> ")
                assert backup.get(ask2_1)
                ask2stop = True
            except AssertionError:
                print("Veuillez répondre avec le nom d'une des variables affichées")

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
                print("Veuillez insérer un nombre")
            
            notetmp = moyenne(tmp)
            total.append((ask2_1, notetmp))

            backuptmp = backup.get(ask2_1)
            backup[ask2_1] = backupobj(moyenne(tmp, mid=True), backuptmp)
            
            # Debug
            print(backuptmp)
            print(tmp)
            print(total)
            print(backup)

while nobackupstop == False:
   
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
            print("Veuillez ecrire la réponse avec O ou N")
        
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
            print("Veuillez insérer un nombre")
    
    # Calcul et fin du programme

    notetmp = moyenne(tmp)
    total.append((matmp, notetmp))
    backup[matmp] = moyenne(tmp, mid=True)

    print(total)
    try:
        nobackupstopask = input("Voulez vous re créer une matière (o/n) \n>>> ")
        assert nobackupstopask == "O" or "o" or "N" "n"
    except ValueError:
        print("Veuillez répondre avec (o) ou (n) ;")

    if nobackupstopask == "O" or nobackupstopask == "o": # Continuation du programme
        print('\n')
        nobackupstop = False
    
    # Ecriture

    if nobackupstopask == "N" or nobackupstopask == "n": # Arret du programme
        nobackupstop = True
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
        print("\n\U0001F4A1 Vos notes sont stockées dans un fichier data.txt dans le dossier actuelle")
        file.write("\n\nMoyenne Générale")
        file.write("\n+----------")
        file.write('\n')
        file.write("\nVous avez {} de moyenne générale {}".format(moygeneral, like))
        file.close()

        backupfile = open('data.bin', 'wb')
        pickle.dump(backup, backupfile)
        backupfile.close