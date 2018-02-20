##Affichage graphique du menu

import os
from tkinter import *
from HowToHangman import *

languages = ["Français", "English", "Deutsch", "Español", "Italiano"]

##Definition de l'interface graphique
menu = Tk()
menu.title("Menu Pendu")
#menu.geometry("720x480+100+0")
menu.config(bg='Black',cursor='X_cursor')

##Canvas
pendu_Canvas = Canvas(menu, width=240, height=280, bg='Black', highlightbackground='Yellow')
score_Canvas = Canvas(menu, width=160, height=280, bg='Black', highlightbackground='Yellow')
place_Hold1 = Canvas(menu, width=30, height=300, bg='Black', highlightbackground='Black')
place_Hold2 = Canvas(menu, width=300, height=30, bg='Black', highlightbackground='Black')
place_Hold3 = Canvas(menu, width=300, height=30, bg='Black', highlightbackground='Black')

##Labels
language_Label = Label(menu, text = languages[0], bg='Yellow', font=('Comic Sans MS', 10), padx=5, pady=5)

##Buttons
play_Button = Button(menu,text='Jouer',height=2, width=15, bg='Yellow', font=('Comic Sans MS', 15, 'bold'), padx=5, pady=5)
rules_Button = Button(menu, text='Règles', width=15, bg='Yellow', font=('Comic Sans MS', 15, 'bold'), padx=5, pady=5)
credits_Button = Button(menu, text='Crédits', width=15, bg='Yellow', font=('Comic Sans MS', 15, 'bold'), padx=5, pady=5)
quit_Button = Button(menu, text='Quitter', bg='Yellow', font=('Comic Sans MS', 12), command= lambda: menu.destroy())
language_Button = Button(menu, text='Langue', bg='Yellow', font=('Comic Sans MS', 12), command = lambda: changeLang(language_Label, languages))

##Desssins de canvas
pendu_Canvas.create_line(20,270,220,270,fill='red',width=5)
pendu_Canvas.create_line(50,270,50,30,fill='red',width=5)
pendu_Canvas.create_line(48,30,180,30,fill='red',width=5)
pendu_Canvas.create_line(50,90,110,30,fill='red',width=5)
pendu_Canvas.create_line(180,28,180,70,fill='red',width=5)
pendu_Canvas.create_oval(160,68,200,108,fill='red',width=0)
pendu_Canvas.create_line(180,108,180,170,fill='red',width=5)
pendu_Canvas.create_line(180,168,160,230,fill='red',width=5)
pendu_Canvas.create_line(180,168,200,230,fill='red',width=5)
pendu_Canvas.create_line(180,140,150,120,fill='red',width=5)
pendu_Canvas.create_line(180,140,210,120,fill='red',width=5)

##Affichage des différents widgets
play_Button.grid(row=3,column=3)
rules_Button.grid(row=4,column=3)
credits_Button.grid(row=5,column=3)
quit_Button.grid(row=8,column=6)
language_Button.grid(row=1,column=5, sticky=E)
pendu_Canvas.grid(row= 3, rowspan=3, column=4, columnspan=2, padx=5) 
score_Canvas.grid(row=3, rowspan=3, column=2, padx=5)
language_Label.grid(row=1,column=6)
place_Hold1.grid(row=1, rowspan=6, column=1)
place_Hold2.grid(row=6, column=1, columnspan= 6)
place_Hold3.grid(row=2, column=1, columnspan= 6)


##Programme principal
