"""
4.0 Nouvelle idée de jordan sur les écarts-type.

Plutot que de sauvegarder chaque résultat dans un fichier jordan pousse la reflexion
un peu plus loin encore et compare les données obtenues par rapport au jours +1,
cette différence, l'écart type, est lui sauvegardé plutot que la matrice totale.


"""




""" Variable Globales ! """
Debut = 194
Fin = 387 #! nombre de jours -1 !
precision = 0.1




from rsc.loadmatrix2 import loadmatrice
from rsc.oscillateur import oscillation
from rsc.EcartType import EcartType
from rsc.log import log
from rsc.resolve import Resolve
import datetime
import json
import numpy
from multiprocessing import Process

numpy.seterr(invalid='ignore')





log(0)
log(1)

donnees = loadmatrice("COVID_5BXL.json")
oscillateurs = json.loads(open("rsc/oscillateurs", "r", encoding='utf8').read())
mtx_base = json.loads(open('mtx_base', 'r', encoding='utf8').read())
# Extraction des clées (jours) des données, pour pouvoir faire +1
keys = []
for key in donnees:
    keys.append(key)

print("=============================")
print("• " + str(len(oscillateurs)) + " oscillateurs chargés")
print("• " + str(len(mtx_base)) + " matrices de base")
print()
print("• Début : " + str(Debut) + " : " + str(keys[Debut]))
print("• Fin : " + str(Fin) + " : " + str(keys[Fin]))
print("=============================")
print()



"""
========================================================================================================================
Début première passe, cette passe sert à déterminer quelle matrice de base (les grossières) à choisir avant 
d'effectuer une oscillation dessus.
"""
print("=============================")
print("Première passe - " + datetime.datetime.now().strftime("%H:%M:%S"))
log(3)

# Verification si le fichier n'a pas déja été calculé pour gagner du temps:
exist = False
try:
    test = open("1 passe_P2.json", 'r').read()
    if test != "":
        exist = True
    else:
        exist = False
except:
    exist = False

if exist == False:
    # Fichier d'enregistrement de la premiere passe
    file = open("1 passe_P2.json", "w", encoding='utf8')
    file.write("{\n")
    for a in range(Debut, Fin, 1):
        threshold = 1000
        mtx_choix = []
        date = "error"

        for i in range(len(mtx_base)):
            r = EcartType(numpy.matrix(mtx_base[i]) * numpy.reshape(numpy.matrix(donnees[keys[a]]), (5, 1)), numpy.reshape(numpy.matrix(donnees[keys[a + 1]]), (5, 1)))
            r = r ** 0.5
            if r < threshold:
                threshold = r
                mtx_choix = mtx_base[i]
                date = keys[a]
        print("→ MTX : " + str(a) + "/" + str(Fin))
        # file.write(str(date) + ";" + str(threshold) + ";" + str(mtx_choix) + "\n")
        file.write('"' + str(date) + '": {"r":' + str(threshold) + ', "mtx":' + str(mtx_choix) + "}")
        if a < (Fin - 1):
            file.write(',\n')

    file.write("\n}")
    file.close()
print("Fin passe - " + datetime.datetime.now().strftime("%H:%M:%S"))
print("=============================\n")

"""
La première passe crée un fichier .json qui contient : 
clé : la date du jour
r : l'écart type
mtx : la matrice retenue
"""





"""
========================================================================================================================
Deuxieme passe, 
a partir d'ici il va falloir osciller sur les matrices trouvées aux passes précédentes.

Plutot que de faire des passes consécutives et de se risquer à avoir des écarts type très différents entre eux 
on va plutot boucler sur le calcul jusqu'à avoir un ecart-type en dessous d'une certaines valeur...

"""
print("=============================")
print("Deuxieme passe - " + datetime.datetime.now().strftime("%H:%M:%S"))
log(4, txt="Deuxieme passe - " + datetime.datetime.now().strftime("%H:%M:%S") + "\n")

# Chargement du fichier précédent
file = open("1 passe_P2.json", "r", encoding='utf8').read()
file = json.loads(file)
print("► Fichier '1 passe_P2.json' chargé")
print("• " + str(len(file)) + ' jour(s) à traiter')
print('• ' + str(precision) + ' précision\n')
log(4, txt="• " + str(len(file)) + ' jour(s) à traiter')
log(4, txt='• ' + str(precision) + ' précision\n')


sortie = open("result_MTX_P2.json", "w", encoding='utf8')
sortie.write("{\n")

compteur = 0
for jour in file:

    tps = datetime.datetime.now()

    r = file[jour]['r']
    mtx = file[jour]['mtx']

    date0 = datetime.datetime.strptime(jour, "%Y-%m-%d")
    date1 = date0 + datetime.timedelta(days=1)
    date0 = date0.strftime("%Y-%m-%d")
    date1 = date1.strftime("%Y-%m-%d")

    result = Resolve(mtx, oscillateurs, r, precision, donnees[date0], donnees[date1])
    result = result.split('||')

    sortie.write('"' + date0 + '": {"r":' + result[0] + ', "mtx": ' + str(result[1]) + "}")
    if compteur < (len(file) - 1):
        sortie.write(',')
    sortie.write("\n")

    compteur += 1
    temps = datetime.datetime.now() - tps
    print("→ " + str(date0) + " :: Ecart = " + result[0] + " :: " + str(temps))
    log(4, txt="→ " + str(date0) + " :: Ecart = " + result[0] + " :: " + str(temps))

sortie.write('}')
sortie.close()

print()
print("=============================")
print("Fini ☺ !")
print("=============================")
print("Par Stéphane Delire\nsous les conseils de :\nJordan Verstappen\nNicolas Debacq\nJeremy Alen\nGuy Gillain\nFrédéric Leloux\n")
input()


"""
========================================================================================================================
Par Stéphane Delire
sous les conseils de : 
Jordan Verstappen
Nicolas Debacq
Jeremy Alen
Guy Gillain
Frédéric Leloux
========================================================================================================================
"""
