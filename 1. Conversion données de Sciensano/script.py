"""
1. Conversion données de Sciensano

Bien regarder quel fichier prendre sur le site de sciensano
https://epistat.wiv-isp.be/covid/

2022.
"""

# Import (si fonctionne pas, executer le fichier 'requirement.bat' en racine (mode admin ?)
import json
from colorama import *

init(autoreset=True)
import datetime

import collections


def makehash():  # Pour les dict a plusieurs niveaux
    return collections.defaultdict(makehash)


###########################
# Début ###################

print("=====================================================")
print(Fore.YELLOW + "1. Conversion données de Sciensano")
print("=====================================================")


def jsonfilecreation():
    # DateTime pour enregistrer le temps que le fichier va mettre
    tempsDepart = datetime.datetime.now()

    # Ouverture du fichier
    try:
        file = open("COVID19BE_CASES_MUNI.json", "r", encoding='utf8').read()
    except:
        print(Fore.RED + "Erreur :")
        print("Impossible de trouver le fichier : " + Fore.CYAN + "COVID19BE_CASES_MUNI.json")
        input()
        quit()

    print("Fichier : " + Fore.CYAN + "COVID19BE_CASES_MUNI.json" + Fore.RESET + " trouvé.")
    print()

    # Conversion du fichier
    data = json.loads(file)
    print("Fichier converti")

    print("Il y a " + Fore.YELLOW + str(len(data)) + Fore.RESET + " entrées.")
    print('')

    """
    Data (fichier JSON) est constitué comme suit:
    C'est une list qui contient des dictionnaires.
    Dans ces dictionnaires on sait accèder aux valeurs grace à ces clés :
    
    NIS5
    DATE
    TX_DESCR_NL
    TX_DESCR_FR
    TX_ADM_DSTR_DESCR_NL
    TX_ADM_DSTR_DESCR_FR
    PROVINCE
    REGION
    CASES
    
    """
    """
    Bruxelles, Schaerbeek, Evere, Woluwe-Saint-Lambert, Etterbeek.
    """

    print("Creation du json pour les 5 communes suivantes : "
          + Fore.MAGENTA
          + "Bruxelles, Schaerbeek, Evere, Woluwe-Saint-Lambert, Etterbeek.")

    """
    On crée un dictionnaire (nested dict a plusieurs niveaux) dont la clé est la date, car c'est l'élement commun entre chaque noeuds.
    """
    dicoMatrix = makehash()
    for item in data:

        if item.get("TX_DESCR_FR") == "Bruxelles":
            dicoMatrix[item.get('DATE')]['Bruxelles'] = item.get('CASES')

        if item.get("TX_DESCR_FR") == "Schaerbeek":
            dicoMatrix[item.get('DATE')]['Schaerbeek'] = item.get('CASES')

        if item.get("TX_DESCR_FR") == "Evere":
            dicoMatrix[item.get('DATE')]['Evere'] = item.get('CASES')

        if item.get("TX_DESCR_FR") == "Woluwe-Saint-Lambert":
            dicoMatrix[item.get('DATE')]['Woluwe-Saint-Lambert'] = item.get('CASES')

        if item.get("TX_DESCR_FR") == "Etterbeek":
            dicoMatrix[item.get('DATE')]['Etterbeek'] = item.get('CASES')

    print()
    print("Enregistrement du fichier : " + Fore.CYAN + "'COVID_5BXL.JSON'")

    try:
        file = open('../2. Espérance de maximisation/COVID_5BXL.json', 'w', encoding='utf8')
        file.write(json.dumps(dicoMatrix))
        file.close()
    except:
        print(Fore.RED + "Erreur :")
        print(Fore.RED + "Impossible d'enregistrer le fichier...")
        input()
        quit()

    print("Fichier enregistré !")

    tempsFin = datetime.datetime.now()
    tempsTotal = tempsFin - tempsDepart
    print("Effectué en " + Fore.YELLOW + str(tempsTotal) + Fore.RESET + " millisecondes.")
