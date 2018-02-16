##Module de fonctions
#11 erreurs pour perdre
"""
mot = "hey"
interdite =[]
vide = ["_" for i in range(len(mot))]
fautes = 0
"""
langue = 0

def entre():
    statut = True
    while statut == True:
        lettre = str(input("Choisissez une lettre: "))
        if len(lettre) == 1 and lettre.isalpha():
            statut = False
        else:
            print("Veuillez rentrer qu'une seule lettre!")
    return(lettre)

#change input to take from the GUI

def traitement():
    global fautes
    lettre = entre()
    erreur = True
    for i in range(len(mot)):
        if lettre in interdite:
            print("Vous avez déjà utiliser cette lettre!")
            break
        elif lettre == mot[i]:
            erreur = False
            vide[i] = mot[i]
    if erreur == True:
        interdite.append(lettre)
        fautes +=1

def changeLang(language_Label, languages):
    global langue 
    if langue == 4:
        langue = 0
    else:
        langue += 1
    language_Label.configure(text=languages[langue])

"""
print(vide)

while True:
    traitement()
    if fautes == 11:
        print("C'est perdu!")
        break
    print("vide: ", vide)
    print("interdite: ", interdite)
    count = 0
    for i in range(len(mot)):
        if vide[i] != '_':
            count += 1
    if count == len(mot):
        print("Victory!")
        break
"""