"""
Conversion_Sciensano

Bien regarder quel fichier prendre sur le site de sciensano
https://epistat.wiv-isp.be/covid/  'Confirmed case by date and municipality' format: json

2022.
"""

# Import (si fonctionne pas, executer le fichier 'requirement.bat' en racine (mode admin ?)
import json
import datetime
from colorama import *

# coloration de l'output
init(autoreset=True)


def jsonConversion(filename):
    MUNICIPALITIES = ["Bruxelles", "Schaerbeek", "Evere", "Woluwe-Saint-Lambert", "Etterbeek"]

    print("=====================================================")
    print(Fore.YELLOW + "Conversion_Sciensano")
    print("=====================================================")

    tempsDepart = datetime.datetime.now()

    try:
        # Ouverture et lecture du fichier de données
        with open(filename, "r", encoding='utf8') as f:
            data = json.loads(f.read())
    except FileNotFoundError:
        # Gestion de l'erreur si le fichier n'est pas trouvé
        print(Fore.RED + "Erreur :")
        print("Impossible de trouver le fichier : " + Fore.CYAN + filename)
        return

    print("Fichier : " + Fore.CYAN + filename + Fore.RESET + " trouvé.")
    print("Fichier converti")

    print("Il y a " + Fore.YELLOW + str(len(data)) + Fore.RESET + " entrées.")
    print('')

    # Initialisation du dictionnaire qui stockera les données converties
    dicoMatrix = {}
    for item in data:
        # Vérification si la municipalité est dans la liste des municipalités d'intérêt
        if item.get("TX_DESCR_FR") in MUNICIPALITIES:
            # Conversion des cas "<5" en 1 pour permettre l'analyse statistique
            cases = item.get('CASES')
            if cases == "<5":
                cases = 1
            else:
                # Ajout d'une règle pour convertir la valeur en entier
                cases = int(cases)

            # Stockage des cas par date et par municipalité dans le dictionnaire
            dicoMatrix.setdefault(item.get('DATE'), {})[item.get("TX_DESCR_FR")] = cases

    print()
    print("Enregistrement du fichier : " + Fore.CYAN + "'COVID_5BXL.JSON'")

    try:
        # Enregistrement des données converties dans un nouveau fichier JSON
        with open('../dataEM.json', 'w', encoding='utf8') as f:
            f.write(json.dumps(dicoMatrix))
    except Exception as e:
        # Gestion de l'erreur si l'enregistrement du fichier échoue
        print(Fore.RED + "Erreur :")
        print(Fore.RED + "Impossible d'enregistrer le fichier...")
        print(f"Error details: {e}")
        return

    print("Fichier enregistré !")

    # Calcul et affichage du temps d'exécution
    tempsFin = datetime.datetime.now()
    tempsTotal = tempsFin - tempsDepart
    print("Effectué en " + Fore.YELLOW + str(tempsTotal) + Fore.RESET + " millisecondes.")
