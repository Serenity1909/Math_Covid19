from rsc.loadmatrix2 import loadmatrice
import matplotlib.pyplot as plt
import json
import numpy

donnees = loadmatrice('COVID_5BXL.json')

"""
0 - BXL
1 - Sch
2 - Eve
3 - Wsl
4 - Ett
"""

cpt = 0
bxl = []
sch = []
eve = []
wsl = []
ett = []
for key in donnees:
    # plt.scatter(cpt, donnees[key][0], color="blue", alpha=0.2)
    # plt.scatter(cpt, donnees[key][1], color="gray", alpha=0.2)
    # plt.scatter(cpt, donnees[key][2], color="orange", alpha=0.2)
    # plt.scatter(cpt, donnees[key][3], color="green", alpha=0.2)
    # plt.scatter(cpt, donnees[key][4], color="fuchsia", alpha=0.2)
    bxl.append(donnees[key][0])
    sch.append(donnees[key][1])
    eve.append(donnees[key][2])
    wsl.append(donnees[key][3])
    ett.append(donnees[key][4])
    cpt += 1

plt.scatter(numpy.array(numpy.arange(len(bxl))), bxl, color="blue", alpha=0.7, label="Bxl")
plt.scatter(numpy.array(numpy.arange(len(sch))), sch, color="gray", alpha=0.7, label="Sch")
plt.scatter(numpy.array(numpy.arange(len(eve))), eve, color="orange", alpha=0.7, label="Eve")
plt.scatter(numpy.array(numpy.arange(len(wsl))), wsl, color="green", alpha=0.7, label="Wsl")
plt.scatter(numpy.array(numpy.arange(len(ett))), ett, color="fuchsia", alpha=0.7, label="Ett")


plt.title('Nombres de cas COVID - pour les 5 communes de BXL')
plt.legend()
plt.show()