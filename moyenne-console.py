#!/usr/bin/python3.8
#! -*- coding:Utf-8 -*
# Definition du modules
from moyennemod import *

from rich.console import Console
from rich.table import Table

from os import path as os_path

import json, os, glob

# Var
total = list()
nobackup = True
moygeneraltmp = float()
backup = False
yesbackup = True
backup = dict()
justcount = True
home = False
console = Console(record="True")
no_dir = False

# Data
PATH = os_path.abspath(os_path.split(__file__)[0])
data_dir = os.path.join(PATH, "data")

data_json = os.path.join(data_dir, "data.json")
data_txt = os.path.join(data_dir, "data.txt")
data_html = os.path.join(data_dir, "data.html")
data_html = os.path.join(data_dir, "data.html")

print(data_html, data_json, data_txt)

listdir = os.listdir(PATH)
index_dir = len(listdir)
#print(type(listdir), listdir, index_dir)

try:
    assert glob.glob(os.path.join(PATH, "data"))
except AssertionError:
    os.mkdir(os.path.join(PATH, "data"))
    console.print("Data Folder create \U0001F642 \n")

# Table
moyenne_table = Table(title="\U0001F3EB Moyenne des Matières \U0001F3EB", )
moyenne_table.add_column("Matières", justify="center", style="red")
moyenne_table.add_column("note", justify="center", style="blue")
moyenne_table.add_column("Moyennes", justify="right", style="cyan")
moyenne_table.add_column("Like", justify="center", style="green")

while home  == False:
    
    try:
        ask1 = input("Voulez vous :\n1- Créer un nouveaux fichier\n2- Réstaurer un fichier\n3- Lire un fichier data.json\n>>> ")
        assert ask1 != "1" or "2" or "3"
    except AssertionError   :
        print("Veuillez choisire soit : 1, 2 ou 3")
    
    if  ask1 == "2":
        print("\n")
        
        backupfile = open(data_json, 'r')
        backup = json.load(backupfile)
        backupfile.close()
        
        home = True
        yesbackup = False
        
        print('\n')

    if ask1 == "1":
        home = True
        nobackup = False
        print('\n')

    if ask1 == "3":
        home = True
        justcount = False
        print('\n')

while yesbackup == False:
    
    # Déclaration de varibles
    stoptmp = "o"
    tmp = []
    tmpn = ""
    tmpc = ""
    nostop = False
    notetmp = 0.0
    ask2stop = False

    try:
        ask2 = input("Voulez vous :\n1- Compléter une matière \n2- Créer une nouvelle matière \n3- Arréter le programme\n>>> ")
        assert ask2 == "1" or "2" or "3"
    except AssertionError:
        print("Veuillez répondre avec 1, 2 ou 3")
    
    if ask2 == "1": # Completer une matière
        while ask2stop == False:
            try:
                print("Quelle matière souhaitez vous modifier :")
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
            
            note = backup[ma].get('note')
            coef = backup[ma].get('coef')

            #print(type(note), note)
            #print(type(coef), coef)

            index = len(note)
            flag = 0
            tot = list()
            tmp_tmp = list()

            #print(index)

            while flag != index:
                tottmp = (note[flag], coef[flag])
                tmp.append(tottmp)
                flag += 1
                #print(tottmp)

            notetmp = moyenne(tmp)
            #total.append((ask2_1, notetmp))
            indextmp = 0

            backup[ask2_1] = {'note': separate(tmp), 'coef': separate(tmp, noteask=False), 'last': tmp[indextmp],'moyenne': notetmp}
            
            backupfile = open(data_json, 'w')
            json.dump(backup, backupfile, ensure_ascii=False, indent = 4)
            backupfile.close()

            # Debug
            #print(backuptmp)
            #print(tmp)
            #print(total)
            #print(backup)
    if ask2 == "2": # Créer une nouvelle matière
        
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
                #print(mastopask)  
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

        notetmp = moyenne(tmp) # moyenne
        #total.append((matmp, notetmp)) # liste finale
        
        indextmp = len(tmp) - 1 # Index de la dernière note
        backup[matmp] = {'note': separate(tmp), 'coef': separate(tmp, noteask=False), 'last': tmp[indextmp],'moyenne': notetmp} # Mise a jour de la variable du fichier JSON
        
        #print(backup)
        
        # Ecriture du fichier JSON
        backupfile = open(data_json, 'w')
        json.dump(backup, backupfile, ensure_ascii=False, indent = 4)
        backupfile.close()
        
    if ask2 == "3": # Fin
        
        # Recupération des vielles moyennes
        for matiere_backup in list(backup):
            note_backup = backup[matiere_backup].get('moyenne')
            total.append((matiere_backup, note_backup))
        
        yesbackup = True
        file = open(data_txt, 'w')
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

while nobackup == False:
   
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
            #print(mastopask)  
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
    indextmp = len(tmp) - 1
    backup[matmp] = {'note': separate(tmp), 'coef': separate(tmp, noteask=False), 'last': tmp[indextmp],'moyenne': notetmp}

    print(total)
    try:
        nobackupask = input("Voulez vous re créer une matière (o/n) \n>>> ")
        assert nobackupask == "O" or "o" or "N" "n"
    except ValueError:
        print("Veuillez répondre avec (o) ou (n) ;")

    if nobackupask == "O" or nobackupask == "o": # Continuation du programme
        print('\n')
        nobackup = False
    
    # Ecriture

    if nobackupask == "N" or nobackupask == "n": # Arret du programme
        nobackup = True
        file = open(data_txt, 'w')
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

        backupfile = open(data_json, 'w')
        json.dump(backup, backupfile, ensure_ascii=False, indent = 4)
        backupfile.close()

        #print(backup)

while justcount == False:
    #print("\U0001F44D")

    # Note en tulpe
    backupfile = open(data_json, 'r')
    backup = json.load(backupfile)
    backupfile.close()

    
    flag1 = 0
    flag2 = 0
    malist = list(backup)
    index1 = len(malist)
    
    while flag2 != index1:
        matmp = malist[flag2]

        note = backup[matmp].get('note')
        coef = backup[matmp].get('coef')

        index = len(note)
        flag = 0
        tot = list()

        #print(type(note), note)
        #print(type(coef), coef)

        # Recovery de toute les notes
        #while flag1 != index1:

            #print(index)

        while flag != index:
            tottmp = (note[flag], coef[flag])
            tot.append(tottmp)
            flag += 1
            #print(tottmp)
        
        #print(tot)
        total.append((matmp, moyenne(tot)))
        #print(total)
        #flag1 += 1
        flag2 += 1

    # Ecriture / Affichage

    file = open(data_txt, 'w')
    file.write("Moyenne des matières")
    file.write("\n+----------")
    file.write('\n')
    
    for matiere, note in total:
        like = emoji(note)
        note = str(note)
        #console.print("\nVous avez [green]{}[/] de moyennne en [bold cyan]{}[/] {}".format(note, matiere, like); style="")
        moyenne_table.add_row(matiere, " ", note, like)
        # Ecriture dans un fichier lisible de la session actuelle
        file.write("\nVous avez {} de moyennne en {} {}".format(note, matiere, like))
    console.print(moyenne_table)
    console.save_text(data_txt)
    console.save_html(data_html)

    index = len(total)
    for flag, note in total:
        moygeneraltmp += note
    moygeneral = round(moygeneraltmp / index,  2)
    
    like = emoji(moygeneral)
    
    #console.print('\n')
    #console.print("Vous avez [purple]{}[/] de moyenne générale {}".format(moygeneral, like), style="bold")
    #console.print("\n\U0001F4A1 Vos notes sont stockées dans un fichier data.txt dans le dossier actuelle")
    #file.write("\n\nMoyenne Générale")
    #file.write("\n+----------")
    #file.write('\n')
    #file.write("\nVous avez {} de moyenne générale {}".format(moygeneral, like))
    #file.close()

    #backup[matmp]['note'].append((separate(tmp)))
    #backup[matmp]['coef'].append((separate(tmp, noteask=False)))
    
    backupfile = open(data_json, 'w')
    json.dump(backup, backupfile, ensure_ascii=False, indent = 4)
    backupfile.close()
    

    #print(backup)
    justcount = True