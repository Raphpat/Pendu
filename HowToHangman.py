##Module de fonctions
#11 erreurs pour perdre

##Variables locales
pseudoText = 'Pseudo: '

##Fonctions


def changeGUI(origin, target):
    origin.pack_forget()
    target.pack()

def quitGUI(origin, target, pseudo):
    pseudo.delete(0,len(pseudo.get()))
    changeGUI(origin, target)

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

def get_Pseudo(entry, label, origin, target, game_Pseudo): #Pour le GUY pseudo
    pseudo = entry.get()
    pseudoBar = pseudoText
    if len(pseudo) == 0:
        label.configure(text='Entrez votre pseudo!', fg='Red')
    else:
        changeGUI(origin, target)
        pseudoBar += pseudo
        game_Pseudo.configure(text = pseudoBar)