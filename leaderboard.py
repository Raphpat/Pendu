from tkinter import Label, Frame

leaderboard = open("F:/Pendu-master/leaderboard.txt", "a") #le mode d'ouverture 'a' permet de creer un fichier vide si il n'existe pas
leaderboard.close()

scores=[]

#Méthode permettant de stocker dans scores les scores dans le document leaderboard.txt
with open("F:/Pendu-master/leaderboard.txt","r") as document:
    for line in document:
        line = line.split()
        if not line:
            continue
        scores.append(line)
    for i in range(len(scores)):
        scores[i][1] = int(scores[i][1])

def score_Sort(): #Trie les scores  
    scores.sort(key=lambda x: x[1])
    scores.reverse()
    if len(scores)>10:
        for i in range(9,len(scores)-1):
            del scores[10]

def scoreAdd(score, pseudo): #Ajoute les scores au fichier des leaderboards
    file = open("F:/Pendu-master/leaderboard.txt", "a")
    score_str = pseudo + " " + str(score) + "\n"
    file.write(str(score_str))
    scores.append((pseudo, score))
    file.close()

def afficher_scores_first(frame): #Construit l'affichage des scores
    title_Label = Label(frame, text=' Tableau des scores ', bg='#065a82',  fg='#f5f0f6', font=('Comic Sans MS', 12))
    name_Label = Label(frame, text='Pseudo:', bg='#065a82', fg='#f5f0f6', font=('Comic Sans MS', 10))
    score_Label = Label(frame, text='Score:', bg='#065a82', fg='#f5f0f6', font=('Comic Sans MS', 10))
    title_Label.grid(row=1, column=1, columnspan=2)
    name_Label.grid(row=2, column=1)
    score_Label.grid(row=2, column=2)
    score_Sort()
    if len(scores) < 10:
        length = len(scores)
    else:
        length = 10
    for i in range(length):
        pseudo = Label(frame, text=scores[i][0], bg='#065a82', fg='#f5f0f6', font=('Comic Sans MS', 9))
        score = Label(frame, text=scores[i][1], bg='#065a82', fg='#f5f0f6', font=('Comic Sans MS', 9))
        pseudo.grid(row=i+3, column=1)
        score.grid(row=i+3, column=2)

def afficher_scores(frame, menu): #Réaffiche les scores
    frame.destroy()
    score_Frame = Frame(menu, bg='#065a82', highlightcolor='#f5f0f6',highlightbackground='#f5f0f6', highlightthickness='1')
    score_Frame.grid(row=3, rowspan=3, column=2, padx=10)
    afficher_scores_first(score_Frame)
