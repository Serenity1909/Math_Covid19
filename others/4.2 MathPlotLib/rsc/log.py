"""
Fichier de log.

Permet de simplement enregistrer dans un fichier texte ce qu'on veut sauvegarder comme
infos de log. Je passe par ici afin d'alléger le code principal au maximum...

Delire Stéphane.
"""

import datetime
path = "log.txt"


def log(x, txt=""):
    if x == 0:
        # Reset log
        file = open(path, "w")
        file.write("")
        file.close()
        return 0

    if x == 1:
        file = open(path, 'a', encoding='utf8')
        file.write("░░ Created by Delire Stéphane. ░░\n")
        file.write("Program start : " + datetime.datetime.now().strftime('%d/%m/%Y , %H:%M:%S') + "\n-----\n")
        file.close()
        return 0
    if x == 3:
        file = open(path, 'a', encoding='utf8')
        file.write("Première passe : " + str(datetime.datetime.now()) + "\n")
        file.close()
    if x == 4:
        file = open(path, 'a', encoding='utf8')
        file.write(txt + "\n")
        file.close()