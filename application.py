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
    for t, i in enumerate(listeCommentaires):
        tag = 'not related'
        containsNomMarque = False
        containsYour = False
        containOtherMarque = False
        containsConjonction = False
        containisnt = False
        liste = i.split()
        #enlever le nombre au début
        if len(liste) > 2:
            liste[0] = liste[0].split(",")[1]
        #enlever les points
        #liste[len(liste)-1] = liste[len(liste)-1][:len(liste)-3]
        for j in liste:
            try:
                l = j.split('.')
                for y in l:
                    y.replace('.','')
                if len(l) != 1:
                    for k in l:
                        if k == "Ideji":
                            # filter ideji car pas dans le dico
                            containsNomMarque = True
                        else:
                            if k == "Your":
                                # filtrer your car pas dans le dico
                                containsYour = True
                            else:
                                if 'c' in listeDictionnaire[k]:
                                    containOtherMarque = True
                                if 'b' in listeDictionnaire[k]:
                                    if containOtherMarque:
                                        if tag == 'negative':
                                            tag = 'neutre'
                                        else:
                                            tag = 'positive'
                                    else:
                                        if tag == 'positive':
                                            tag = 'neutre'
                                        else:
                                            tag = 'negative'
                                elif 'g' in listeDictionnaire[k]:
                                    if containOtherMarque:
                                        if tag == 'positive':
                                            tag = 'neutre'
                                        else:
                                            tag = 'negative'
                                    else:
                                        if tag == 'negative':
                                            tag = 'neutre'
                                        else:
                                            tag = 'positive'
                                elif 's' in listeDictionnaire[k] and (containsYour or containsNomMarque):
                                    if tag == 'negative':
                                        tag = 'neutre'
                                    else:
                                        tag = 'positive'
                                elif k == "isn't":
                                    containisnt = True
                elif j == "Ideji":
                    #filter ideji car pas dans le dico
                    containsNomMarque = True
                else:
                    if j == "Your":
                        #filtrer your car pas dans le dico
                        containsYour = True
                    else:
                        if 'c' in listeDictionnaire[j]:
                            containOtherMarque = True
                        if 'b' in listeDictionnaire[j]:
                            if containOtherMarque:
                                if tag == 'negative':
                                    tag = 'neutre'
                                else:
                                    tag = 'positive'
                            else:
                                if tag == 'positive':
                                    tag = 'neutre'
                                else :
                                    tag = 'negative'
                        elif 'g' in listeDictionnaire[j]:
                            if containOtherMarque:
                                if tag == 'positive':
                                    tag = 'neutre'
                                else :
                                    tag = 'negative'
                            else:
                                if tag == 'negative':
                                    tag = 'neutre'
                                else:
                                    tag = 'positive'
                        elif 's' in listeDictionnaire[j] and (containsYour or containsNomMarque):
                                if tag == 'negative':
                                    tag = 'neutre'
                                else:
                                    tag = 'positive'
                        elif j == "isn't":
                            containisnt = True

            except (Exception):
                print('')
        if containisnt:
            if tag == "positive":
                tag = 'negative'
            elif tag == "negative":
                tag = "positive"
        print(f'{t+1} : {tag}')
if __name__ == '__main__':
    printVerdict('messages.csv')
    input()
