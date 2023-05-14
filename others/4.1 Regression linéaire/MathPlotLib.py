"""
Regression linéaire -
A partir des dernier fichiers issu de la partie 4.0 (calculé en commun par tout le monde)

On charge les données contenues dans le fichier qui correspond à chaque matrices probabiliste trouvées.
Ce script se charge de faire la regression linéaire sur chacunes des valeurs afin d'en sortir
la matrice recherchée...

lien en fr, sur l'utilisation de la regression linéaire simple et multiple sur python:
https://www.cours-gratuit.com/tutoriel-python/tutoriel-python-matriser-la-rgression-linaire-avec-scikit-learn

autre lien :
https://www.activestate.com/resources/quick-reads/how-to-run-linear-regressions-in-python-scikit-learn/


Delire Stéphane.
"""


import numpy
from sklearn.linear_model import LinearRegression
import json
import matplotlib.pyplot as plt
from matplotlib import ticker

# Chargement des données contenues dans les .json calculés
path = ["result_MTX_P1.json", "result_MTX_P2.json", "result_MTX_P3.json", "result_MTX_P4.json"]
# Synthèse sur un seul dico :
data = {}
for dir in path:
    file = open(dir, "r", encoding='utf8').read()
    file = json.loads(file)
    for jour in file:
        # Condition si écart type pas trop grand (defaut 1000):
        if file[jour]['r'] < 1000:
            data[jour] = file[jour]['mtx']

print(len(data))


# Extraction des clés :
keys = []
for key in data:
    keys.append(key)



# mathplotlib param et instance :
fig, axs = plt.subplots(5, 5)
fig.suptitle('Résultat de régression linéaire')




# Conversion des données pour la regression lineaire multiple :

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

        # Ligne qui représente la regression linéaire
        xfit = numpy.linspace(0, cpt)
        yfit = model.predict(xfit[:, numpy.newaxis])

        # math plot lib
        # plt.scatter(x, y)
        # plt.plot(xfit, yfit, color='red')
        # plt.show()

        props = dict(boxstyle='round', facecolor='green', alpha=0.4)
        axs[a, b].text(0.5, 0.1, 'R²=' + str(round(model.score(x, y), 6)), horizontalalignment='center', verticalalignment='center', transform=axs[a, b].transAxes, bbox=props)

        axs[a, b].scatter(x, y, alpha=0.2, label='data')
        axs[a, b].plot(xfit, yfit, color='red', alpha=0.7)
        axs[a, b].set_ylabel(None)
        axs[a, b].set_xlabel("[" + str(a) + ", " + str(b) + "]")
        axs[a, b].set_xticks([])
        # axs[a, b].set_yticks([])
        # axs[a, b].legend(loc='upper right')


        # Prédiction du model :
        # g = numpy.array(700).reshape(1, -1)
        # prediction = model.predict(g)
        #
        #
        # axs[a, b].scatter(g, prediction)

plt.show()
