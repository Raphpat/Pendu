##Variables locales

langue = 0

mots_pour_pendu = {'niveau1':{'français':["chat","lait","viande","lit","chaise","veste","boite","train","bonbon","sac"],
                              'anglais':["cat","milk","meat","bed","chair","coat","box","train","sweet","bag"]},
                               
                   'niveau2':{'français':["chapeau","cuisine","tiroire","avocat","crepe","lumiere","telephone","volets","magazine","plante"],
                              'anglais':["hat","kitchen","draw","avocado","pancake","light","telephone","shutters","magasine","plant"]},

                   'niveau3':{'français':["caramel","oreiller","","aviron","armoire","interieur","meuble","matelas","","plafond"],
                               'anglais':["caramel","pillow","","rowing","cupboard","inside","furniture","mattress","","ceiling"]},

                   'X-pert':{'français':["bibliotheque","dictionnaire","","orchestre","xylophone","zero","chuchotter","arrosoir","entonnoir","anticonstitutionnellement"],
                             'anglais':["library","dictionary","","orchestra","xylophone","zero","whisper","watering can","funnel","unconstitutionally"]}}

#print(mots_pour_pendu['niveau1']['anglais'][1])

##Fonctions

def changeLang(language_Label, languages):
    global langue 
    if langue == 4:
        langue = 0
    else:
        langue += 1
    language_Label.configure(text=languages[langue])
