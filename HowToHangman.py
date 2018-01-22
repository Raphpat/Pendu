mot = "hey"
interdite =[]
vide = ["_" for i in range(len(mot))]
erreur = True

def choixLettre(mot,vide,interdite,erreur):
    while True:
        try:
            while True:
                lettre = str(input("Choisissez une lettre: "))
                if len(lettre) == 1 and lettre.isalpha():
                    break
                print("Veuillez rentrer qu'une seule lettre!")
            break
        except:
            print("Veuillez rentrer une lettre!")
    for i in range(len(mot)):
        if lettre == mot[i] and lettre != vide[i]:
            vide[i] = lettre
            erreur = False
        elif lettre == vide[i] or lettre == interdite:
            print("Vous avez déjà utilisé cette lettre")
            break
        else:
            interdite.append(lettre)
    return(erreur, vide, interdite)

print(mot)
print(len(mot))
print(vide)
while True:
    tada = choixLettre(mot,vide,interdite,erreur)
    erreur = tada[0]
    vide = tada[1]
    interdite = tada[2]
    print(erreur)
    print(vide)
    print("Lettres utilisées: ",interdite)

"""
mot = "bonjour"
print(mot[3])
find = ["_" for i in range(len(mot))]
print(" ".join(find))
echec = 0
while echec < 11:
    lettre = str(input("Devinez une lettre: "))
    statut = False
    for i in range(len(mot)):
        if mot[i]== lettre:
            find[i] = lettre
            statut = True
    if statut == False:
        echec +=1
    print(" ".join(find))
    statut = False
    print(echec)
"""