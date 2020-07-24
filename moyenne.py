#!/usr/bin/python3.8
#! -*- coding:Utf-8 -*
stop = False
tmp = []
tmpn = ""
tmpc = ""
while stop != True :
    # Note
    print("Entrer une note")
    tmpn = input(">>> ")
    # Coefficiant
    print("Entrer un coef")
    tmpc = input(">>>")
    # Merging
    tmpn=str(tmpn)
    tmpc=int(tmpc)
    tmp.append((tmpn, tmpc))
    
    print(tmp)
    stop = True
