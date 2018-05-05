"""------------------------Affichage graphique du jeu------------------------"""

"""----------------------------------Imports---------------------------------"""
import os
from tkinter import *
from HowToHangman import *
from motspourpendu import *
from leaderboard import *

languages = ["Français", "English", "Deutsch", "Español", "Italiano"]

"""-------------------Definition de l'interface graphique--------------------"""
menu = Tk()
menu.title("Pendu")
# menu.geometry("720x480+100+0")

"""-------------------------------Frame du menu------------------------------"""

menu_Frame = Frame(menu, bg='#065a82', cursor='X_cursor')
# Canvas
pendu_Canvas = Canvas(menu_Frame, width=240, height=280, bg='#065a82', 
highlightbackground='#f5f0f6')
place_Hold1 = Canvas(menu_Frame, width=300, height=30, bg='#065a82', 
highlightbackground='#065a82')
place_Hold2 = Canvas(menu_Frame, width=300, height=30, bg='#065a82', 
highlightbackground='#065a82')
# Labels
language_Label = Label(menu_Frame, text=languages[0], fg='#f5f0f6', 
bg='#1e3231', font=('Comic Sans MS', 10), padx=5, pady=5)
# Buttons
play_Button1 = Button(menu_Frame, text='Jouer', height=2, width=15, 
fg='#f5f0f6', bg='#1e3231', font=('Comic Sans MS', 15, 'bold'), padx=5, pady=5,
command=lambda: play(menu_Frame,pseudo_Frame,return_Label,mot_Label,mot2_Label))
rules_Button = Button(menu_Frame, text='Règles', width=15, fg='#f5f0f6', 
bg='#1e3231', font=('Comic Sans MS', 15, 'bold'), padx=5, pady=5, 
command=lambda: changeGUI(menu_Frame, rules_Frame))
credits_Button = Button(menu_Frame, text='Crédits', width=15,  fg='#f5f0f6', 
bg='#1e3231', font=('Comic Sans MS', 15, 'bold'), padx=5, pady=5, 
command=lambda: changeGUI(menu_Frame, credits_Frame))
quit_Button = Button(menu_Frame, text='Quitter', fg='#f5f0f6', bg='#1e3231', 
font=('Comic Sans MS', 12), command=lambda: menu.destroy())
language_Button = Button(menu_Frame, text='Langue', fg='#f5f0f6', bg='#1e3231',
font=('Comic Sans MS',12),command=lambda: changeLang(language_Label, languages))
# Desssins de canvas, dessin du pendu statique
pendu_Canvas.create_line(20, 270, 220, 270, fill='black', width=5)
pendu_Canvas.create_line(50, 270, 50, 30, fill='black', width=5)
pendu_Canvas.create_line(48, 30, 180, 30, fill='black', width=5)
pendu_Canvas.create_line(50, 90, 110, 30, fill='black', width=5)
pendu_Canvas.create_line(180, 28, 180, 70, fill='black', width=5)
pendu_Canvas.create_oval(160, 68, 200, 108, fill='black', width=0)
pendu_Canvas.create_line(180, 108, 180, 170, fill='black', width=5)
pendu_Canvas.create_line(180, 168, 160, 230, fill='black', width=5)
pendu_Canvas.create_line(180, 168, 200, 230, fill='black', width=5)
pendu_Canvas.create_line(180, 140, 150, 120, fill='black', width=5)
pendu_Canvas.create_line(180, 140, 210, 120, fill='black', width=5)
# Tableau des scores
score_Frame = Frame(menu_Frame, bg='#065a82', highlightcolor='#f5f0f6',
highlightbackground='#f5f0f6', highlightthickness='1')
score_Frame.grid(row=3, rowspan=3, column=2, padx=10)
afficher_scores(score_Frame)
# Affichage des différents widgets
play_Button1.grid(row=3, column=3)
rules_Button.grid(row=4, column=3)
credits_Button.grid(row=5, column=3)
quit_Button.grid(row=8, column=6)
language_Button.grid(row=1, column=5, sticky=E)
pendu_Canvas.grid(row=3, rowspan=3, column=4, columnspan=2, padx=5)
language_Label.grid(row=1, column=6)
place_Hold1.grid(row=6, column=1, columnspan=6)
place_Hold2.grid(row=2, column=1, columnspan=6)
menu_Frame.pack()  # Affichage au lancement

"""------------------------------Frame des regles----------------------------"""
rules_Frame = Frame(menu, bg='#065a82', cursor='X_cursor')
# Importation des règles
rules_txt = open("rules.txt", "r", encoding="UTF8").read()
# Définition des widgets
rules_Label = Label(rules_Frame, text=rules_txt,  fg='#f5f0f6', bg='#065a82', 
font=('Comic Sans MS', 12), padx=5, pady=15)
play_Button2 = Button(rules_Frame, text='Jouer',  fg='#f5f0f6', bg='#1e3231', 
font=('Comic Sans MS', 12), command=lambda: play(rules_Frame, pseudo_Frame, 
return_Label, mot_Label, mot2_Label))
menu_Button1 = Button(rules_Frame, text='Menu ', fg='#f5f0f6', bg='#1e3231', 
font=('Comic Sans MS', 12), command=lambda: changeGUI(rules_Frame, menu_Frame))
# Affichage des widgets
rules_Label.grid(row=2, column=2)
play_Button2.grid(row=3, column=3)
menu_Button1.grid(row=4, column=3)

"""-----------------------------Frame des credits----------------------------"""
credits_Frame = Frame(menu, bg='#065a82', cursor='X_cursor')
# Importation des crédits
credits_txt = open("credits.txt", "r", encoding="UTF8").read()
# Définition des widgets
credits_Label = Label(credits_Frame, text=credits_txt, fg='#f5f0f6', 
bg='#065a82', font=('Comic Sans MS', 12), padx=5, pady=15)
menu_Button2 = Button(credits_Frame, text='Menu', fg='#f5f0f6', bg='#1e3231', 
font=('Comic Sans MS',12), command=lambda: changeGUI(credits_Frame, menu_Frame))
# Affichage des widgets
credits_Label.grid(row=2, column=2)
menu_Button2.grid(row=3, column=3)

"""------------------------------Frame du pseudo-----------------------------"""
pseudo_Frame = Frame(menu, bg='#065a82', cursor='X_cursor')
# Définition des widgets
pseudo_Label = Label(pseudo_Frame, text='Entrez votre pseudo:', 
font=('Comic Sans MS', 12), bg='#065a82', fg='#f5f0f6')
pseudo_Entry = Entry(pseudo_Frame, font=('Comic Sans MS', 12))
pseudo_Button = Button(pseudo_Frame, text='Soumettre', bg='#1e3231', 
fg='#f5f0f6', font=('Comic Sans MS', 12), command=lambda: 
get_Pseudo(pseudo_Entry, pseudo_Label, pseudo_Frame, game_Frame, game_Pseudo))
# Affichage des widgets
pseudo_Label.grid(row=1, column=1)
pseudo_Entry.grid(row=2, column=1, padx=5)
pseudo_Button.grid(row=2, column=2, pady=5)

"""-------------------------------Frame du jeu-------------------------------"""
game_Frame = Frame(menu, bg='#065a82', cursor='X_cursor')
# Canvas
place_Hold3 = Canvas(game_Frame, width=30, height=300, bg='#065a82', 
highlightbackground='#065a82')
pendu_Anime = Canvas(game_Frame, width=240, height=280, bg='#065a82', 
highlightbackground='#f5f0f6')
# Entry
input_Entry = Entry(game_Frame, font=('Comic Sans MS', 12))
# Label
game_Pseudo = Label(game_Frame, text='Pseudo: ', bg='#1e3231', fg='#f5f0f6', 
font=('Comic Sans MS', 12))
mot_Label = Label(game_Frame, text='Mot à deviner:', bg='#1e3231', fg='#f5f0f6',
font=('Comic Sans MS', 12))
input_Label = Label(game_Frame, text='Choisissez une lettre: ', bg='#065a82', 
fg='#f5f0f6', font=('Comic Sans MS', 12))
interdite_Label = Label(game_Frame, text='Lettres utilisées: ', bg='#1e3231',
fg='#f5f0f6', font=('Comic Sans MS', 12))
return_Label = Label(game_Frame, bg='#065a82', fg='#f5f0f6', 
font=('Comic Sans MS', 12))
# Button
leave_Button = Button(game_Frame, text="Retour au Menu", bg='#1e3231', 
fg='#f5f0f6', font=('Comic Sans MS', 12),command=lambda: 
changeGUI(game_Frame, quit_Frame))
input_Button = Button(game_Frame, text='Soumettre', bg='#1e3231', fg='#f5f0f6', 
font=('Comic Sans MS', 12), command=lambda: soumettre(input_Entry, return_Label,
mot_Label, interdite_Label, pendu_Anime, game_Frame, vicdef_Frame, 
resultat_Label, score_Label, erreur_Label, pseudo_Entry))
# Affichage des widgets
leave_Button.grid(row=8, column=6, sticky=E)
game_Pseudo.grid(row=1, column=1)
mot_Label.grid(row=3, column=2, columnspan=2)
input_Label.grid(row=4, column=2)
input_Entry.grid(row=4, column=3)
input_Button.grid(row=6, column=2, columnspan=2)
interdite_Label.grid(row=2, column=2, columnspan=3)
return_Label.grid(row=5, column=2, columnspan=2, pady=5)
place_Hold3.grid(row=2, rowspan=5, column=4)
pendu_Anime.grid(row=2, rowspan=3, column=5, columnspan=2)

"""-----------------------------Frame pour quitter---------------------------"""
quit_Frame = Frame(menu, bg='#065a82', cursor='X_cursor')
# Définition des widgets
quit_Label = Label(quit_Frame, text='Voulez vous vraiment quitter la partie?', 
font=('Comic Sans MS', 15), bg='#065a82', fg='#f5f0f6')
oui_Button = Button(quit_Frame, text="Oui", bg='#1e3231', fg='#f5f0f6', 
font=('Comic Sans MS', 15), command=lambda: quitGUI(quit_Frame, menu_Frame, 
pseudo_Entry, score_Frame, pendu_Anime, return_Label, interdite_Label))
non_Button = Button(quit_Frame, text="Non", bg='#1e3231', fg='#f5f0f6', 
font=('Comic Sans MS', 15), command=lambda: changeGUI(quit_Frame, game_Frame))
# Affichage des widgets
quit_Label.grid(row=1, column=1, columnspan=2)
oui_Button.grid(row=2, column=1)
non_Button.grid(row=2, column=2)

"""---------------------------Frame defaite victoire-------------------------"""
vicdef_Frame = Frame(menu, bg='#065a82', cursor='X_cursor')
# Definition des Widgets
score_Label = Label(vicdef_Frame, text='Score: ', font=('Comic Sans MS', 12), 
bg='#065a82', fg='#f5f0f6')
erreur_Label = Label(vicdef_Frame, text='Erreur(s): ', 
font=('Comic Sans MS', 12), bg='#065a82', fg='#f5f0f6')
resultat_Label = Label(vicdef_Frame, font=('Comic Sans MS', 25), bg='#065a82', 
fg='#f5f0f6')
quit1_Button = Button(vicdef_Frame, text="Retour au menu", bg='#1e3231', 
fg='#f5f0f6', font=('Comic Sans MS', 15), command=lambda: quitGUI(vicdef_Frame, 
menu_Frame, pseudo_Entry, score_Frame, pendu_Anime, return_Label, 
interdite_Label))
mot2_Label = Label(vicdef_Frame, text='Mot: ', font=('Comic Sans MS', 12), 
bg='#065a82', fg='#f5f0f6')
# Affichage des widgets
score_Label.grid(row=1, column=2)
erreur_Label.grid(row=3, column=2)
mot2_Label.grid(row=4, column=2)
resultat_Label.grid(row=5, column=2)
quit1_Button.grid(row=7, column=2)

#Mainloop
menu.mainloop()