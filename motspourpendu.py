##Imports
from random import choice

##Variables locales
langue = 0

##Fonctions

def changeLang(language_Label, languages):
    global langue 
    if langue == 4:
        langue = 0
    else:
        langue += 1
    language_Label.configure(text=languages[langue])

def getMot():
    if langue == 0:
        fichier = open("F:/Pendu-master/motsFrancais.txt")
    elif langue == 1:
        fichier = open("F:/Pendu-master/motsAnglais.txt")
    #Conditions pour autre langue
    mot = choice(fichier.readlines())
    fichier.close()
    return(mot)

#getMot()
