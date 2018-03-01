from tkinter import Label, Frame

leaderboard = open("F:/Pendu-master/leaderboard.txt", "a")
leaderboard.close()

scores=[]

#Méthode permettant de stocker dans scores le meilleur score de chaque pseudo dans le document leaderboard.txt
with open("F:/Pendu-master/leaderboard.txt","r") as document:
    for line in document:
        line = line.split()
        if not line:
            continue
        scores.append(line)
    for i in range(len(scores)):
        scores[i][1] = int(scores[i][1])

def score_Sort():
    scores.sort(key=lambda x: x[1])
    scores.reverse()
    if len(scores)>10:
        for i in range(9,len(scores)-1):
            del scores[10]

def afficher_scores_first(frame):
    title_Label = Label(frame, text=' Tableau des scores ', bg='Black', fg='Yellow', font=('Comic Sans MS', 12))
    name_Label = Label(frame, text='Pseudo:', bg='Black', fg='Yellow', font=('Comic Sans MS', 10))
    score_Label = Label(frame, text='Score:', bg='Black', fg='Yellow', font=('Comic Sans MS', 10))
    title_Label.grid(row=1, column=1, columnspan=2)
    name_Label.grid(row=2, column=1)
    score_Label.grid(row=2, column=2)
    score_Sort()
    for i in range(10):
        pseudo = Label(frame, text=scores[i][0], bg='Black', fg='Yellow', font=('Comic Sans MS', 9))
        score = Label(frame, text=scores[i][1], bg='Black', fg='Yellow', font=('Comic Sans MS', 9))
        pseudo.grid(row=i+3, column=1)
        score.grid(row=i+3, column=2)

def afficher_scores(frame, menu):
    frame.destroy()
    score_Frame = Frame(menu, bg='Black', highlightcolor='Yellow',highlightbackground='Yellow', highlightthickness='1')
    score_Frame.grid(row=3, rowspan=3, column=2, padx=10)
    afficher_scores_first(score_Frame)

"""
leaderboard.write("Hi")
leaderboard.close()
leaderboard = open("leaderboard.txt", 'r')
print(leaderboard.read())
leaderboard.close()
"""
