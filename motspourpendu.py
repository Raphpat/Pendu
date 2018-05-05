"""----------------------------------Imports---------------------------------"""
from random import choice

"""-----------------------------Variables locales----------------------------"""
langue = 0

"""---------------------------------Fonctions--------------------------------"""

def changeLang(language_Label, languages): #Change la langue des mots du jeu
    global langue 
    if langue == 4:
        langue = 0
    else:
        langue += 1
    language_Label.configure(text=languages[langue])

def getMot():
    #Chosi un mot aleatoirement depuis le fichier texte de la langue specifiee
    if langue == 0:
        fichier = open("F:/Pendu-master/motsFrancais.txt")
    elif langue == 1:
        fichier = open("F:/Pendu-master/motsAnglais.txt")
    elif langue == 2:
        fichier = open("F:/Pendu-master/motsAllemand.txt")
    elif langue == 3:
        fichier = open("F:/Pendu-master/motsEspagnol.txt")
    elif langue == 4:
        fichier = open("F:/Pendu-master/motsItalien.txt")
    #Conditions pour autre langue
    mot = choice(fichier.readlines())
    fichier.close()
    return(mot)