"""
2. Calcul de Matrices

Copier/coller le fichier "COVID_5BXL" depuis le premier dossier.

2022.
"""


# Import (si fonctionne pas, executer le fichier 'requirement.bat' en racine (mode admin ?)
import json
from colorama import *
init(autoreset=True)
import datetime

import collections
def makehash(): # Pour les dict a plusieurs niveaux
    return collections.defaultdict(makehash)





def convert(x):
    """
    Permet de convertir une chaine de caractère en un int
    Et si ce n'est pas possible comme par exemple avec les "<5",
    on retourne un 0
    """
    try:
        int(x)
        return x
    except:
        return 0








###########################
# Début ###################
tempsDepart = datetime.datetime.now()

print("=====================================================")
print(Fore.YELLOW + "2. Calcul de Matrices")
print("=====================================================")




# Ouverture du fichier
try:
    file = open("COVID_5BXL.json", "r", encoding='utf8').read()
except:
    print(Fore.RED + "Erreur :")
    print("Impossible de trouver le fichier : " + Fore.CYAN + "COVID_5BXL.json")
    input()
    quit()

print("Fichier : " + Fore.CYAN + "COVID_5BXL.json" + Fore.RESET + " trouvé.")



data = json.loads(file)

# Ouverture de la matrice de base:
try:
    matrice = open("squeletteMatrice.json", "r", encoding='utf8').read()
except:
    print(Fore.RED + "Erreur :")
    print("Impossible de trouver le fichier : " + Fore.CYAN + "squeletteMatrice.json")
    input()
    quit()

print("Fichier : " + Fore.CYAN + "squeletteMatrice.json" + Fore.RESET + " trouvé.")
print()

matrice = json.loads(matrice)
matrice = matrice['Matrice']


##################
# Calcul du nombre de constante
constA = 5
if matrice[0][0] != 'x':
    constA = constA - 1
if matrice[0][1] != 'x':
    constA = constA - 1
if matrice[0][2] != 'x':
    constA = constA - 1
if matrice[0][3] != 'x':
    constA = constA - 1
if matrice[0][4] != 'x':
    constA = constA - 1

constB = 5
if matrice[1][0] != 'x':
    constB = constB - 1
if matrice[1][1] != 'x':
    constB = constB - 1
if matrice[1][2] != 'x':
    constB = constB - 1
if matrice[1][3] != 'x':
    constB = constB - 1
if matrice[1][4] != 'x':
    constB = constB - 1

constC = 5
if matrice[2][0] != 'x':
    constC = constC - 1
if matrice[2][1] != 'x':
    constC = constC - 1
if matrice[2][2] != 'x':
    constC = constC - 1
if matrice[2][3] != 'x':
    constC = constC - 1
if matrice[2][4] != 'x':
    constC = constC - 1

constD = 5
if matrice[3][0] != 'x':
    constD = constD - 1
if matrice[3][1] != 'x':
    constD = constD - 1
if matrice[3][2] != 'x':
    constD = constD - 1
if matrice[3][3] != 'x':
    constD = constD - 1
if matrice[3][4] != 'x':
    constD = constD - 1

constE = 5
if matrice[4][0] != 'x':
    constE = constE - 1
if matrice[4][1] != 'x':
    constE = constE - 1
if matrice[4][2] != 'x':
    constE = constE - 1
if matrice[4][3] != 'x':
    constE = constE - 1
if matrice[4][4] != 'x':
    constE = constE - 1

if constA < 1 or constB < 1 or constC < 1 or constD < 1 or constE < 1:
    print(Fore.RED + "Erreur :")
    print("Il y a une erreur dans la matrice squelette.")
    print("Une ligne comporte trop de " + Fore.RED + "constantes" + Fore.RESET + ".")
    print("Il faut au minimum " + Fore.YELLOW + "1" + Fore.RESET + "variable...")
    print("Sinon le calcul ne sert à rien.")
    input()
    quit()
print(Fore.GREEN + "Matrice squelette vérifiée et valide.")


####################
# Debut calculs

# On s'assure que les clé soient dans le bon ordre, par date croissante
index = []
for key in data:
    index.append(key)
index = [datetime.datetime.strptime(ts, "%Y-%m-%d") for ts in index]
index.sort()
index = [datetime.datetime.strftime(ts, '%Y-%m-%d') for ts in index]
print("Index des matrices retrié par ordre croissant.")
print("Il y a " + Fore.YELLOW + str(len(index)) + Fore.RESET + " entrées, donc " + Fore.YELLOW + str(len(index)) + Fore.RESET + " matrice à calculer.")


# Suite à un bug python on remodifie la matrice en python pour faire des remplace dans la copie
matrice = json.dumps(matrice)

# Matrice des résultats :
goMatrice = []

for i in range(len(index)):

    # On est obligé de faire un try ici, car parfois les valeurs n'existent pas.Donc par défaut = 0
    try:
        bxlA = int(convert(data[index[i]]['Bruxelles']))
    except:
        bxlA = 0
    try:
        schA = int(convert(data[index[i]]['Schaerbeek']))
    except:
        schA = 0
    try:
        eveA = int(convert(data[index[i]]['Evere']))
    except:
        eveA = 0
    try:
        wslA = int(convert(data[index[i]]['Woluwe-Saint-Lambert']))
    except:
        wslA = 0

    try:
        ettA = int(convert(data[index[i]]['Etterbeek']))
    except:
        ettA = 0
    try:
        bxlB = int(convert(data[index[i+1]]['Bruxelles']))
    except:
        bxlB = 0
    try:
        schB = int(convert(data[index[i+1]]['Schaerbeek']))
    except:
        schB = 0
    try:
        eveB = int(convert(data[index[i+1]]['Evere']))
    except:
        eveB = 0
    try:
        wslB = int(convert(data[index[i+1]]['Woluwe-Saint-Lambert']))
    except:
        wslB = 0
    try:
        ettB = int(convert(data[index[i+1]]['Etterbeek']))
    except:
        ettB = 0

    # On copie la matrice de base, et on applique les modif dans cette copie
    # Et on passe en json suite bug python par rapport au copie de list entre elles.
    squeletteTmp = json.loads(matrice)

    # Faut empecher la division par 0
    if bxlA != 0:
        resultBxl = bxlB / bxlA / constA
    else:
        resultBxl = 0
    if squeletteTmp[0][0] == "x":
        squeletteTmp[0][0] = resultBxl
    if squeletteTmp[0][1] == "x":
        squeletteTmp[0][1] = resultBxl
    if squeletteTmp[0][2] == "x":
        squeletteTmp[0][2] = resultBxl
    if squeletteTmp[0][3] == "x":
        squeletteTmp[0][3] = resultBxl
    if squeletteTmp[0][4] == "x":
        squeletteTmp[0][4] = resultBxl

    if schA != 0:
        resultSch = schB / schA / constB
    else:
        resultSch = 0
    if squeletteTmp[1][0] == "x":
        squeletteTmp[1][0] = resultSch
    if squeletteTmp[1][1] == "x":
        squeletteTmp[1][1] = resultSch
    if squeletteTmp[1][2] == "x":
        squeletteTmp[1][2] = resultSch
    if squeletteTmp[1][3] == "x":
        squeletteTmp[1][3] = resultSch
    if squeletteTmp[1][4] == "x":
        squeletteTmp[1][4] = resultSch

    if eveA != 0:
        resultEve = eveB / eveA / constC
    else:
        resultEve = 0
    if squeletteTmp[2][0] == "x":
        squeletteTmp[2][0] = resultEve
    if squeletteTmp[2][1] == "x":
        squeletteTmp[2][1] = resultEve
    if squeletteTmp[2][2] == "x":
        squeletteTmp[2][2] = resultEve
    if squeletteTmp[2][3] == "x":
        squeletteTmp[2][3] = resultEve
    if squeletteTmp[2][4] == "x":
        squeletteTmp[2][4] = resultEve

    if wslA != 0:
        resultWsl = wslB / wslA / constD
    else:
        resultWsl = 0
    if squeletteTmp[3][0] == "x":
        squeletteTmp[3][0] = resultWsl
    if squeletteTmp[3][1] == "x":
        squeletteTmp[3][1] = resultWsl
    if squeletteTmp[3][2] == "x":
        squeletteTmp[3][2] = resultWsl
    if squeletteTmp[3][3] == "x":
        squeletteTmp[3][3] = resultWsl
    if squeletteTmp[3][4] == "x":
        squeletteTmp[3][4] = resultWsl

    if ettA != 0:
        resultEtt = ettB / ettA / constE
    else:
        resultEtt = 0
    if squeletteTmp[4][0] == "x":
        squeletteTmp[4][0] = resultEtt
    if squeletteTmp[4][1] == "x":
        squeletteTmp[4][1] = resultEtt
    if squeletteTmp[4][2] == "x":
        squeletteTmp[4][2] = resultEtt
    if squeletteTmp[4][3] == "x":
        squeletteTmp[4][3] = resultEtt
    if squeletteTmp[4][4] == "x":
        squeletteTmp[4][4] = resultEtt

    goMatrice.append(squeletteTmp)


# Enregistrement sous forme json
try:
    file = open('RESULT_MATRICES.json', "w", encoding='utf8')
    file.write(json.dumps(goMatrice))
    file.close()
    print("Fichier : " + Fore.CYAN + "RESULT_MATRICES.json" + Fore.RESET + " créé.")
except:
    print(Fore.RED + "Erreur : " + Fore.RESET + "impossible de créer le fichier de résultat.")
    input()
    quit()


# Calcul de temps :
tempsFin = datetime.datetime.now()
resultTemps = tempsFin - tempsDepart
print("Effectué en " + Fore.YELLOW + str(resultTemps) + Fore.RESET + " millisecondes.")
input()