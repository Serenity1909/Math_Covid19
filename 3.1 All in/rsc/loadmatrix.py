"""
Juste un script python qui recharge le fichier Json créé auparavant,
mais il le charge et corrige déja les valeurs interne :
par exemple si la valeur n'existe pas ou que c'est par exemple '<5',
ce script retourne directement un 0 comme valeur.

On retourne évidemment un array contenant toutes les matrices journalière :)
"""
from colorama import *

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

    # Essais d'ouverture :
    try:
        file = open(path, 'r', encoding='utf8').read()
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
    print(Fore.GREEN + "Clés du fichier " + Fore.CYAN + "COVID_19BXL.json" + Fore.GREEN +" extraites et triées.")

    #On crée les matrices jour par jour:
    # Les try/except servent à retourner un 0 quand la clé (commune) n'existe pas dans le fichier
    rtn = []
    for ind in index:
        try:
            ander = convert(data[ind]['Anderlecht'])
        except:
            ander = 0
        try:
            aud = convert(data[ind]['Auderghem'])
        except:
            aud = 0
        try:
            ber = convert(data[ind]['Berchem-Sinte-Agathe'])
        except:
            ber = 0
        try:
            bxl = convert(data[ind]['Bruxelles'])
        except:
            bxl = 0
        try:
            ett = convert(data[ind]['Etterbeek'])
        except:
            ett = 0
        try:
            eve = convert(data[ind]['Evere'])
        except:
            eve = 0
        try:
            fore = convert(data[ind]['Forest'])
        except:
            fore = 0
        try:
            gan = convert(data[ind]['Ganshoren'])
        except:
            gan = 0
        try:
            ixe = convert(data[ind]['Ixelles'])
        except:
            ixe = 0
        try:
            jet = convert(data[ind]['Jette'])
        except:
            jet = 0
        try:
            koe = convert(data[ind]['Koekelberg'])
        except:
            koe = 0
        try:
            mol = convert(data[ind]['Molenbeek-Saint-Jean'])
        except:
            mol = 0
        try:
            sai = convert(data[ind]['Saint-Gilles'])
        except:
            sai = 0
        try:
            saijo = convert(data[ind]['Saint-Josse-ten-Noode'])
        except:
            saijo = 0
        try:
            sch = convert(data[ind]['Schaerbeek'])
        except:
            sch = 0
        try:
            ucc = convert(data[ind]['Uccle'])
        except:
            ucc = 0
        try:
            wat = convert(data[ind]['Watermael-Boitsfort'])
        except:
            wat = 0
        try:
            wsl = convert(data[ind]['Woluwe-Saint-Lambert'])
        except:
            wsl = 0
        try:
            wsp = convert(data[ind]['Woluwe-Saint-Pierre'])
        except:
            wsp = 0

        rtn.append([ander, aud, ber, bxl, ett, eve, fore, gan, ixe, jet, koe, mol, sai, saijo, sch, ucc, wat, wsl, wsp])

    print(Fore.RESET + "Matrices journalières créées.")
    print()
    return rtn
