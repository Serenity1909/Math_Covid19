import matplotlib.pyplot as plt
import json
import numpy

paths = ["result_MTX_P1.json", "result_MTX_P2.json", "result_MTX_P3.json", "result_MTX_P4.json"]

# Synthèse des fichier result
data = []
compteur = 0
for path in paths:
    file = json.loads(open(path, 'r', encoding='utf8').read())
    for date in file:
        data.append(file[date]['r'])
        if compteur in [0, 100, 200, 300, 400, 500, 600, 700, 800]:
            print(str(compteur) + " : " + str(date))
        compteur += 1




# data = numpy.array(data)
# x = numpy.array(numpy.arange(len(data)))
# plt.scatter(x, data, alpha=0.5, color='orange')
# plt.show()

cpt = 0
for d in data:
    if d < 5:
        plt.scatter(cpt, d, color='green', alpha=0.5)
    elif d < 25:
        plt.scatter(cpt, d, color='orange', alpha=0.5)

    else:
        plt.scatter(cpt, d, color='red', alpha=0.7)
    cpt += 1

plt.title('Ecart-Type')
plt.show()