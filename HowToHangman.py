##Module de fonctions
#11 erreurs pour perdre



##Fonctions
def changeGUI(origin, target):
    origin.pack_forget()
    target.pack()

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

def get_Pseudo(entry, origin, target): #Pour le GUY pseudo
    changeGUI(origin, target)
    return entry.get()

