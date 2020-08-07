#!/usr/bin/python3.8
#! -*- coding:Utf-8 -*
def moyenne(tmp):
    """
    Calcul de moyenne a partir d'une liste avec des tulpes avec en premiers: 
    les notes puis les coefs ; 
    Exemple : a = [(note, moyenne)]
    """
    tmpnotes = [tmpnote * tmpcoef for tmpnote, tmpcoef in tmp] # Extraction des notes fois les coefs
    #print(tmpfrno1) # Debug

    for index, notes in enumerate(tmpnotes): # Combination des notes
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