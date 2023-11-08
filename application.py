#méthode mettant les mots du dictionnaire dans un dictionnaire
# key = le mot      value = son descriptif
def lireDico():
    fich = open('dictionary.txt', encoding="utf8")
    k = {}
    for i in fich.read().split("\n"):
        liste = i.split("\\")
        if len(liste) >= 2:
            k[liste[0]] = liste[1]
    return k


#fonction qui imprime si le commentaire est bon ou faux
def printVerdict(file):
    fich = open(file, encoding="utf8")
    listeCommentaires = fich.read().split("\n")
    listeDictionnaire = lireDico()
    #filtre chaque commentaire pour y atribuer un tag
    for k, i in enumerate(listeCommentaires):
        tag = 'neutral'
        containsNomMarque = False
        containsYour = False
        liste = i.split()
        #enlever le nombre au début
        liste[0] = liste[0].split(",")[1]
        #enlever les points
        liste[len(liste)-1] = liste[len(liste)-1][:len(liste)-3]
        for j in liste:
            if j == "Ideji":
                #filter ideji car pas dans le dico
                containsNomMarque = True
            else:
                if j == "Your":
                    #filtrer your car pas dans le dico
                    containsYour = True
                else:
                    if 'b' in listeDictionnaire[j]:
                        tag = 'negative'
        print(f'{k+1} : {tag}')

        
if __name__ == '__main__':
    printVerdict('messages.csv')
