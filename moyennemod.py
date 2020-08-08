#!/usr/bin/python3.8
#! -*- coding:Utf-8 -*

# moyenne
def moyenne(tmp):

    """
    Calcul de moyenne a partir d'une liste avec des tulpes avec en premiers: 
    les notes puis les coefs ; 
    Exemple : a = [(note, moyenne)]
    """
    tmpnotes = [tmpnote * tmpcoef for tmpnote, tmpcoef in tmp] # Extraction des notes fois les coefs
    #print(tmpnotes) # Debug

    for index, note in enumerate(tmpnotes): # Combination des notes
        if index == 0:
            notes = tmpnotes[0]
        else:
            notes += tmpnotes[index]
    #print(notes) # Debug
    
    # Coefficiants
    tmpcoef = [tmpcoef for note, tmpcoef in tmp] # Extraction des coefs
    #print(tmpcoef) # Debug

    for index, coef in enumerate(tmpcoef): # Combination des coefs
        if index == 0:
            coefs = tmpcoef[0]
        else:
            coefs += tmpcoef[index]
    #print(coefs) # Debug
    # Affichage final

    matiere = notes / coefs
    matiere = round(matiere, 2)
    return matiere

# emoji
def emoji(variable):
    if variable <= 0:
        like = "\U0001F92F"
    
    if variable > 0 and variable <= 10:
        like = " \U0001F915"
                
    if variable > 10 and variable <= 15:
        like =  "\U0001F914"
        
    if variable > 15 and variable < 18:
        like = "\U0001F920" 
                        
    if variable >= 18:
        like = "\U0001F973"
    return like