##Module de fonctions
#11 erreurs pour perdre

from leaderboard import afficher_scores

##Variables locales
pseudoText = 'Pseudo: '
fautes = 0
interdite = []
mot = 'allo' #fonction
motaffiche = 'Mot à deviner:'
##Fonctions


def changeGUI(origin, target):
    origin.pack_forget()
    target.pack()

def quitGUI(origin, target, pseudo, leader):
    pseudo.delete(0,len(pseudo.get()))
    changeGUI(origin, target)
    afficher_scores(leader, target)

def affichermot():
    vide = ['_' for lettre in mot]
    return(motaffiche)
    #nb caractères dans motaffiche = 13, puis ajouter par numero de caractere des _ et des espaces. Lors du 'devinement' du mot, on remplace la lettre à la position 13+2n (car espace) par la lettre deviné. 

def entre(input_Entry, input_Label):
    lettre = input_Entry.get()
    if len(lettre) == 1 and lettre.isalpha():
        statut = False
        return(lettre)
    else:
        input_Label.configure(text="Veuillez rentrer qu'une seule lettre!")
        return(0)

def traitement(lettre, mot, input_Label, mot_Label):
    global fautes
    erreur = True
    for i in range(len(mot)):
        if lettre in interdite:
            input_Label.configure(text="Vous avez déjà utiliser cette lettre!")
            break
        elif lettre == mot[i]:
            erreur = False
            vide[i] = mot[i]
    if erreur == True:
        interdite.append(lettre)
        fautes +=1

def soumettre(input_Entry, input_Label, mot, mot_Label):
    lettre = entre(input_Entry, input_Label)
    if lettre != 0:
        traitement(lettre, mot, input_Label, mot_Label)

def get_Pseudo(entry, label, origin, target, game_Pseudo): #Pour le GUY pseudo
    pseudo = entry.get()
    pseudoBar = pseudoText
    if len(pseudo) == 0:
        label.configure(text='Entrez votre pseudo!', fg='Red')
    else:
        changeGUI(origin, target)
        pseudoBar += pseudo
        game_Pseudo.configure(text = pseudoBar)
