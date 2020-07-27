#!/usr/bin/python3.8
#! -*- coding:Utf-8 -*
# Definition du modules
def moyenne(tmp):
    """
    Calcul de moyenne a partir d'une liste avec des tulpes avec en premiers: 
    les notes puis les coefs ; 
    Exemple : a = [(note, moyenne)]
    """
    tmpnotes = [tmpnote * tmpcoef for tmpnote, tmpcoef in tmp] # Extraction des notes fois les coefs
    #print(tmpfrno1) # Debug

    for index, note in enumerate(tmpnotes): # Combination des notes
        if index == 0:
            notes = tmpnotes[0]
        else:
            notes += tmpnotes[index]
    #print(frno1) # Debug

    # Coefficiants
    tmpcoef = [tmpcoef for note, tmpcoef in tmp] # Extraction des coefs
    #print(tmpfrco1) # Debug

    for index, note in enumerate(tmpcoef): # Combination des coefs
        if index == 0:
            coefs = tmpcoef[0]
        else:
            coefs += tmpcoef[index]
    #print(frco1) # Debug
    # Affichage final

    matiere = notes / coefs
    matiere = round(matiere, 2)
    return matiere

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

fr1 = moyenne(tmp)
print("Vous avez {} de moyenne en Francais".format(fr1))
