##Variables locales

langue = 0
niveau = 0

mots_pour_pendu = {'Niveau 1':{'Français':["chat","lait","viande","lit","chaise","veste","boite","train","bonbon","sac"],
                              'English':["cat","milk","meat","bed","chair","coat","box","train","sweet","bag"]},
                               
                   'Niveau 2':{'Français':["chapeau","cuisine","tiroire","avocat","crepe","lumiere","telephone","volets","magazine","plante"],
                              'English':["hat","kitchen","draw","avocado","pancake","light","telephone","shutters","magasine","plant"]},

                   'Niveau 3':{'Français':["caramel","oreiller","","aviron","armoire","interieur","meuble","matelas","","plafond"],
                               'English':["caramel","pillow","","rowing","cupboard","inside","furniture","mattress","","ceiling"]},

                   'X-pert':{'Français':["bibliotheque","dictionnaire","","orchestre","xylophone","zero","chuchotter","arrosoir","entonnoir","anticonstitutionnellement"],
                             'English':["library","dictionary","","orchestra","xylophone","zero","whisper","watering can","funnel","unconstitutionally"]}}

#print(mots_pour_pendu['niveau1']['anglais'][1])

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
