"""
Juste un script python qui recharge le fichier Json créé auparavant,
mais il le charge et corrige déja les valeurs interne :
par exemple si la valeur n'existe pas ou que c'est par exemple '<5',
ce script retourne directement un 0 comme valeur.

On retourne évidemment un array contenant toutes les matrices journalière :)

VERSION 2-
J'ai enlevé les fioritures comme la couleur qui ne passait pas sur certains
pc.

De plus comme chaque matrice crée ici est liée à un jour, j'incorpore la
date en tant que clé d'un dico que je retourne... contrairement à un simple
array vu auparavant.

Delire Stéphane.
"""


def loadmatrice(path):

    def convert(x):
        """
        Methode interne qui tente de convertir les données en INT
        Et si c'est pas possible, on retourne un 0
        """
        try:
            int(x)
            return int(x)
        except:
            return 0
    # Print d'entrée
    print("\n==== rsc/ loadmatrix2.py ====")
    # Essais d'ouverture :
    try:
        file = open(path, 'r', encoding='utf8').read()
        print("► Fichier trouvé")
    except:
        return 0

    # Convertion de json vers array
    import json
    import datetime

    data = json.loads(file)
    # data est maintenant un dict dont les clé sont les dates journalière :)
    # Comme les clés sont des dates il faut s'assurer qu'elles soient triées dans l'ordre
    index = []
    # Extraction des clés :
    for key in data:
        index.append(key)
    # Modification du datetime object pour le tri :
    index = [datetime.datetime.strptime(ts, "%Y-%m-%d") for ts in index]
    index.sort()
    index = [datetime.datetime.strftime(ts, '%Y-%m-%d') for ts in index]

    print("► Clées extraites et triées")

    #On crée les matrices jour par jour:
    # Les try/except servent à retourner un 0 quand la clé (commune) n'existe pas dans le fichier
    rtn = {}
    for ind in index:
        try:
            bxl = convert(data[ind]['Bruxelles'])
        except:
            bxl = 0
        try:
            sch = convert(data[ind]['Schaerbeek'])
        except:
            sch = 0
        try:
            eve = convert(data[ind]['Evere'])
        except:
            eve = 0
        try:
            wsl = convert(data[ind]['Woluwe-Saint-Lambert'])
        except:
            wsl = 0
        try:
            ett = convert(data[ind]['Etterbeek'])
        except:
            ett = 0

        rtn[ind] = [bxl, sch, eve, wsl, ett]
    print("► " + str(len(rtn)) + " items")
    print("Matrices journalières créées")
    print("=============================\n")
    return rtn
