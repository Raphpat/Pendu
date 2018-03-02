##Variables locales

langue = 0
niveau = 0

mots_pour_pendu = {'Niveau 1':{'Français':["chat","lait","viande","lit","chaise","veste","boite","train","bonbon","sac"],
                              'English':["cat","milk","meat","bed","chair","coat","box","train","sweet","bag"]},
                               
                   'Niveau 2':{'Français':["chapeau","cuisine","tiroire","avocat","crepe","lumiere","telephone","volets","magazine","plante"],
                              'English':["hat","kitchen","draw","avocado","pancake","light","telephone","shutters","magasine","plant"]},

                   'Niveau 3':{'Français':["caramel","oreiller","adoption","aviron","armoire","interieur","meuble","matelas","parapluie","plafond"],
                               'English':["caramel","pillow","adoption","rowing","cupboard","inside","furniture","mattress","umbrella","ceiling"]},

                   'X-pert':{'Français':["bibliotheque","dictionnaire","mercantile","orchestre","xylophone","zero","chuchotter","","entonnoir","anticonstitutionnellement"],
                             'English':["library","dictionary","mercantile","orchestra","xylophone","zero","whisper","","funnel","unconstitutionally"]}}

#print(mots_pour_pendu['niveau1']['anglais'][1])
#Create function that is given level and language and that will chose randomly a word.
#Make it so that the word is show using "_" on the game_Frame
#Entry in game Frame so that user can add its letters
##Fonctions

def changeLang(language_Label, languages):
    global langue 
    if langue == 4:
        langue = 0
    else:
        langue += 1
    language_Label.configure(text=languages[langue])

def changeLevel(level_Label, levels):
    global niveau
    if niveau == 3:
        niveau = 0
    else:
        niveau += 1
    level_Label.configure(text=levels[niveau])
