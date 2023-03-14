"""
Machine Learning -
Suite au script que j'ai créé pour MathPlotLib afin de générer des graphiques je m'aperçois que la
librairie scikit permet de faire du machine learning et donc de pouvoir générer des prédictions concernant
les probabilités de contamination gràce aux datas trouvées juste avant...

Ce script devrait permettre un input d'une date et générer la matrice probabiliste voulue...

Delire Stéphane.
"""


import numpy
from sklearn.linear_model import LinearRegression
import json
import datetime

# Chargement des données contenues dans les .json calculés
path = ["result_MTX_P1.json", "result_MTX_P2.json", "result_MTX_P3.json", "result_MTX_P4.json"]
# Synthèse sur un seul dico :
data = {}
for dir in path:
    file = open(dir, "r", encoding='utf8').read()
    file = json.loads(file)
    for jour in file:
        data[jour] = file[jour]['mtx']

# Extraction des clés :
keys = []
for key in data:
    keys.append(key)


# Message d'entrée :
print("=========================================")
print("Machine Learning - COVID5BXL - Math2022")
print("=========================================")
print()
print("Veuillez introduire une date au format")
print("YYYY-MM-DD : ")
date = input()

# Tentative de conversion de la date fournie
try:
    date = datetime.datetime.strptime(date, "%Y-%m-%d")
except:
    print("mauvais encodage...")
    input()
    quit()


# On recupère le premier jour pour en déterminer le delta
jour0 = keys[0]
jour0 = datetime.datetime.strptime(jour0, "%Y-%m-%d")

delta = date - jour0
delta = int(delta.days)
# delta ici servira à la méthode de prediction de scikit learn.



# Instanciation du model et learning

res = []

for a in range(5):
    for b in range(5):

        x = []
        y = []
        cpt = 0
        for key in data:
            y.append(data[key][a][b])
            x.append(cpt)
            cpt += 1

        y = numpy.array(y).reshape(-1, 1)
        x = numpy.array(x).reshape(-1, 1)

        model = LinearRegression()
        model.fit(x, y)

        res.append(model.predict(numpy.array(delta).reshape(1, -1)))

print()
print("La matrice probabiliste trouvée est :")
for i in range(len(res)):
    res[i] = float(res[i])
print(
    "[" + str(res[0]) + ", " + str(res[1]) + ", " + str(res[2]) + ", " + str(res[3]) + ", " + str(res[4]) + "]\n"
    "[" + str(res[5]) + ", " + str(res[6]) + ", " + str(res[7]) + ", " + str(res[8]) + ", " + str(res[9]) + "]\n"
    "[" + str(res[10]) + ", " + str(res[11]) + ", " + str(res[12]) + ", " + str(res[13]) + ", " + str(res[14]) + "]\n"
    "[" + str(res[15]) + ", " + str(res[16]) + ", " + str(res[17]) + ", " + str(res[18]) + ", " + str(res[19]) + "]\n"
    "[" + str(res[20]) + ", " + str(res[21]) + ", " + str(res[22]) + ", " + str(res[23]) + ", " + str(res[24]) + "]\n"
)

print()
print("==========================================")
print("Par \nStéphane Delire\nJordan Verstappen\nNicolas Debacq\nJeremy Alen\nGuy Gillain\nFrédéric Leloux")
print("==========================================")
input()