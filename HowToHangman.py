##Module de fonctions
#11 erreurs pour perdre

from leaderboard import afficher_scores
from tkinter import Canvas

##Variables locales
pseudoText = 'Pseudo: '
couleur = 'Red'
fautes = 0
interdite = []
mot = 'allo' #transformer en fonction
vide = ['_' for lettre in mot]

##Fonctions

def changeGUI(origin, target): #pour chaque fenêtre
    origin.pack_forget()
    target.pack()

def affichermot(): #pour le jeu
    motaffiche = 'Mot à deviner:'
    for i in range(len(mot)):
        motaffiche += ' '
        motaffiche += vide[i]
    return(motaffiche)

def afficherinterdite(): #pour le jeu
    interditeaffiche = 'Lettres utilisées:'
    for i in range(len(interdite)):
        interditeaffiche+= ' '
        interditeaffiche+= interdite[i]
    return(interditeaffiche)

def quitGUI(origin, target, pseudo, leader, canvas, return_Label, input_Entry): #changeGUI special pour fin de jeu. Remise de tout à 0
    pseudo.delete(0,len(pseudo.get()))
    changeGUI(origin, target)
    afficher_scores(leader, target)
    canvas.delete('all')
    global fautes
    fautes = 0
    global interdite
    interdite = []
    mot = 'non' #fonction choisir mot
    global vide
    vide = ['_' for lettre in mot]
    return_Label.configure(text='')
    input_Entry.delete(0)
    affichermot()
    afficherinterdite()

def entre(input_Entry, return_Label): #pour le jeu
    lettre = input_Entry.get()
    lettre = lettre.lower()
    if len(lettre) == 1 and lettre.isalpha():
        statut = False
        return(lettre)
    else:
        return_Label.configure(text="Veuillez rentrer qu'une seule lettre!")
        return(0)

def drawHang(canvas): #Dessiner le pendu au fur et à mesur
    if fautes == 1:
        canvas.create_line(20, 270, 220, 270, fill='red', width=5)
    elif fautes == 2:
        canvas.create_line(50, 270, 50, 30, fill='red', width=5)
    elif fautes == 3:
        canvas.create_line(48, 30, 180, 30, fill='red', width=5)
    elif fautes == 4:
        canvas.create_line(50, 90, 110, 30, fill='red', width=5)
    elif fautes == 5:
        canvas.create_line(180, 28, 180, 70, fill='red', width=5)
    elif fautes == 6:
        canvas.create_oval(160, 68, 200, 108, fill='red', width=0)
    elif fautes == 7:
        canvas.create_line(180, 108, 180, 170, fill='red', width=5)
    elif fautes == 8:
        canvas.create_line(180, 168, 160, 230, fill='red', width=5)
    elif fautes == 9:
        canvas.create_line(180, 168, 200, 230, fill='red', width=5)
    elif fautes == 10:
        canvas.create_line(180, 140, 150, 120, fill='red', width=5)
    elif fautes == 11:
        canvas.create_line(180, 140, 210, 120, fill='red', width=5)
        #perdu() fonctionà définir

def traitement(lettre, mot, return_Label, mot_Label, interdite_Label, pendu_Anime): #pour le jeu
    global fautes
    erreur = True
    utilisation = False
    for i in range(len(mot)):
        if lettre in interdite:
            erreur = False
            break
        elif lettre == mot[i]:
            erreur = False
            vide[i] = mot[i]
            utilisation = True
    if erreur == True:
        fautes +=1
        utilisation = True
        return_Label.configure(text="Cette lettre n'est pas dans le mot!")
        drawHang(pendu_Anime)
    print(erreur, fautes) #debug
    mot_Label.configure(text=affichermot())
    if utilisation == False:
        global couleur
        if couleur == 'Red':
            couleur = 'White'
        else:
            couleur = 'Red'
        return_Label.configure(text="Vous avez déjà utilisé cette lettre!", fg=couleur)
    if lettre not in interdite:
        interdite.append(lettre)
    interdite_Label.configure(text=afficherinterdite())

def soumettre(input_Entry, return_Label, mot_Label, interdite_Label, pendu_Anime): #pour le jeu
    lettre = entre(input_Entry, return_Label)
    if lettre != 0:
        traitement(lettre, mot, return_Label, mot_Label, interdite_Label, pendu_Anime)

def get_Pseudo(entry, label, origin, target, game_Pseudo): #Pour le GUY pseudo
    pseudo = entry.get()
    pseudoBar = pseudoText
    if len(pseudo) == 0:
        label.configure(text='Entrez votre pseudo!', fg='Red')
    else:
        changeGUI(origin, target)
        pseudoBar += pseudo
        game_Pseudo.configure(text = pseudoBar)
