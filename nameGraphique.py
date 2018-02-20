import os
from tkinter import *
from HowToHangman import *

##Definition de l'interface graphique
name = Tk()
name.title("Pseudo Pendu")
name.config(bg='Black',cursor='X_cursor')

##Définition des widgets
pseudo_Entry = Entry(name, font=('Comic Sans MS', 12))
pseudo_Button = Button(name, text='Soumettre', bg='Yellow', font=('Comic Sans MS', 12), command= lambda: get_Pseudo(pseudo_Entry))

##Affichage des widgets
pseudo_Entry.grid(row=1, column=2, padx=5)
pseudo_Button.grid(row=1, column=3)