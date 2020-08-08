mastop = False

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
    if  mastopask == "o" :
        print("\U0001F4D7")
        print("\n")
        mastop = True
    else:
        mastop = False

print("Hello world \U0001F1EB\U0001F1F7")