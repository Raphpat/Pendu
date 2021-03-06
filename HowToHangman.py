"""----------------------------Module de fonctions---------------------------"""

from leaderboard import afficher_scores, scoreAdd
from tkinter import *
from motspourpendu import getMot

"""-----------------------------Variables locales----------------------------"""
pseudoText = 'Pseudo: '
couleur = '#fca311' 
interdite = [] #lettres utilisées
mot = '' #mot à a deviner
vide = [] #liste avec les _ 
fautes = 0
score = 0

"""----------------------------Fonctions generales---------------------------"""

def start(return_Label, mot_Label, mot2_Label): 
    #initie le jeu, en choisissant un mot, créant le vide et affichant le mot
    global mot
    global vide
    mot = getMot()
    #print(mot) #debug
    vide = ['_' for lettre in mot]
    del vide[-1]
    return_Label.configure(text='')
    mot_Label.configure(text=affichermot())
    mot2_Label.configure(text = "Mot: " + mot)

def changeGUI(origin, target): #permet de changer de fenêtre
    origin.pack_forget()
    target.pack()

def play(origin, target, return_Label, mot_Label, mot2_Label): 
    #combine les fonctions start et changeGUI , utilisé parle bouton 'jouer'
    start(return_Label, mot_Label, mot2_Label)
    changeGUI(origin, target)
    
def quitGUI(origin, target, pseudo, leader, canvas, return_Label,
 interdite_Label): #changeGUI special pour fin de jeu. Remise de tout à 0
    global vide
    global fautes
    fautes = 0
    pseudo.delete(0,len(pseudo.get()))
    changeGUI(origin, target)
    afficher_scores(leader)
    canvas.delete('all')
    for i in range(len(vide)):
        del vide[0]
    for i in range(len(interdite)):
        del interdite[0]
    interdite_Label.configure(text=afficherinterdite())

"""-----------------------------Fonctions du jeu-----------------------------"""

def afficherinterdite(): 
    #renvoie la string avec un texte par defaut et les interdites
    interditeaffiche = 'Lettres utilisées:'
    for i in range(len(interdite)):
        interditeaffiche+= ' '
        interditeaffiche+= interdite[i]
    return(interditeaffiche)

def affichermot(): 
    #renvoie la string avec un texte par defaut et le mot à deviner
    motaffiche = 'Mot à deviner:'
    for i in range(len(vide)):
        motaffiche += ' '
        motaffiche += vide[i]
    return(motaffiche)

def entre(input_Entry, return_Label): #renvoi la lettre soumise par le joueur.
    lettre = input_Entry.get()
    lettre = lettre.lower()
    if len(lettre) == 1 and lettre.isalpha():
        input_Entry.delete(0,len(lettre))
        return(lettre)
    else:
        return_Label.configure(text="Veuillez rentrer qu'une seule lettre!")
        return(0)

def drawHang(canvas): #Dessine le pendu au fur et à mesure
    if fautes == 1:
        canvas.create_line(20, 270, 220, 270, fill='black', width=5)
    elif fautes == 2:
        canvas.create_line(50, 270, 50, 30, fill='black', width=5)
    elif fautes == 3:
        canvas.create_line(48, 30, 180, 30, fill='black', width=5)
    elif fautes == 4:
        canvas.create_line(50, 90, 110, 30, fill='black', width=5)
    elif fautes == 5:
        canvas.create_line(180, 28, 180, 70, fill='black', width=5)
    elif fautes == 6:
        canvas.create_oval(160, 68, 200, 108, fill='black', width=0)
    elif fautes == 7:
        canvas.create_line(180, 108, 180, 170, fill='black', width=5)
    elif fautes == 8:
        canvas.create_line(180, 168, 160, 230, fill='black', width=5)
    elif fautes == 9:
        canvas.create_line(180, 168, 200, 230, fill='black', width=5)
    elif fautes == 10:
        canvas.create_line(180, 140, 150, 120, fill='black', width=5)
    elif fautes == 11:
        canvas.create_line(180, 140, 210, 120, fill='black', width=5)

def vicdef(origin, target, resultat_Label, score_Label, erreur_Label, entry): 
    #Vérifie si le joueur a gagné ou perdu
    global score
    global fautes
    if '_' not in ''.join(vide): #gagné
        score -= fautes * 50
        score_Text = 'Score: '+ str(score)
        erreur_Text = 'Erreur(s): '+ str(fautes)
        scoreAdd(score, entry.get())
        changeGUI(origin, target)
        resultat_Label.configure(text='Victoire!')
        score_Label.configure(text=score_Text)
        erreur_Label.configure(text=erreur_Text)
        score = 0
        fautes = 0
    elif fautes == 11: #perdu
        score -= 11 * 50
        score_Text = 'Score: '+ str(score)
        erreur_Text = 'Erreur(s): '+ str(fautes)
        scoreAdd(score, entry.get())
        changeGUI(origin, target)
        resultat_Label.configure(text='Défaite :(')
        score_Label.configure(text=score_Text)
        erreur_Label.configure(text=erreur_Text)
        score = 0
        fautes = 0

def traitement(lettre, mot, return_Label, mot_Label, interdite_Label, 
pendu_Anime): #vérifie si une lettre est dans le mot
    global fautes
    global score
    erreur = True
    utilisation = False
    for i in range(len(vide)):
        if lettre in interdite: #si la lettre a été utilisé auparavent
            erreur = False
            break
        elif lettre == mot[i]: #si la lettre est juste
            erreur = False
            vide[i] = mot[i]
            utilisation = True
            score += 200
    if erreur == True: #si la lettre n'est ni dans interdite ou le mot
        fautes += 1
        utilisation = True
        return_Label.configure(text="Cette lettre n'est pas dans le mot!")
        drawHang(pendu_Anime)
    mot_Label.configure(text=affichermot())
    if utilisation == False:
        global couleur
        if couleur == '#fca311':
            couleur = '#1e3231'
        else:
            couleur = '#fca311'
        return_Label.configure(text="Vous avez déjà utilisé cette lettre!", 
        fg=couleur)
    if lettre not in interdite:
        interdite.append(lettre)
    interdite_Label.configure(text=afficherinterdite())

def soumettre(input_Entry, return_Label, mot_Label, interdite_Label, 
pendu_Anime, origin, target, resultat_Label, score_Label, erreur_Label, entry):
    #fonction qui appel traitement et vicdef 
    lettre = entre(input_Entry, return_Label)
    if lettre != 0:
        traitement(lettre, mot, return_Label, mot_Label, interdite_Label, 
        pendu_Anime)
    vicdef(origin, target, resultat_Label, score_Label, erreur_Label, entry)
    
"""-----------------------Fonctions de la frame pseudo-----------------------"""

def get_Pseudo(entry, label, origin, target, game_Pseudo):
    #prend le pseudo entré par le joueur et l'affiche.
    pseudo = entry.get()
    pseudoBar = pseudoText
    if len(pseudo) == 0:
        label.configure(text='Entrez votre pseudo!', fg='#fca311')
    else:
        changeGUI(origin, target)
        pseudoBar += pseudo
        game_Pseudo.configure(text = pseudoBar)
