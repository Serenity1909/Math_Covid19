"""
Voir le diagram annexe pour voir le processus complet.

Ce script a plusieurs dépendances, essentiellement des méthodes qui ont été écrites dans des fichiers .py annexe.
Ces scripts ont été créés afin de simplifier ce script-ci... Il s'agit au final que du "squelette globale" du
diagram.

! Il faut quand même générer le fichier COVID_5BXL.json depuis les premiers dossiers

Delire Stéphane Math-22.
"""

# Import
from rsc.loadmatrix import loadmatrice
from rsc.formule import solve
from rsc.oscillateur import oscillation
from colorama import *
import datetime
import os.path
import json
from multiprocessing import Process

# Matrice probabiliste de base
mtx_prob = [
    [0.2, 0.2, 0.2, 0.2, 0.2],
    [0.2, 0.2, 0.2, 0.2, 0.2],
    [0.2, 0.2, 0.2, 0.2, 0.2],
    [0.2, 0.2, 0.2, 0.2, 0.2],
    [0.2, 0.2, 0.2, 0.2, 0.2]
]
# oscillateurs
oscillateurs = ''
# matrice journalière
mtx = []

def main():
    """ Debut du script """
    # Message début
    print("============================================================")
    print(Fore.CYAN + "3.1 Script All in" + Fore.RESET)
    print("============================================================")
    print()




    # Chargement des matrices journalières, du fichier COVID_5BXL precedement créé.
    if os.path.isfile('COVID_5BXL.json'):
        print("Fichier : " + Fore.CYAN + "COVID_5BXL.json " + Fore.RESET + "trouvé.")
    else:
        print(Fore.RED + "Erreur : " + Fore.RESET + "Le fichier " + Fore.CYAN + "COVID_5BXL.json " + Fore.RESET + "n'existe pas.")
        input()
        quit()
    global mtx
    mtx = loadmatrice('COVID_5BXL.json')
    # mtx est un array qui contient des arrays représentant les matrices [5x1] des cas journaliers.







    # Chargement de tout les oscillateurs créés précédement
    if os.path.isfile('rsc/oscillateurs'):
        print("Fichier des " + Fore.CYAN + "oscillateurs" + Fore.RESET + " trouvé.")
    else:
        print(Fore.RED + "Erreur : " + Fore.RESET + "Le fichier " + Fore.CYAN + "oscillateur " + Fore.RESET + "n'existe pas.")
        input()
        quit()

    global oscillateurs
    oscillateurs = open("rsc/oscillateurs", 'r', encoding='utf8').read()
    oscillateurs = json.loads(oscillateurs)
    print(Fore.CYAN + 'Oscillateurs' + Fore.RESET + ' chargés et convertis.')






    """ 
    Oscillation de toutes les matrices probabiliste possible d'après les paramètres de l'oscillateur depuis la matrice
    probabiliste de base. Celle que j'appelle médiane car elle distribue de façon équitable (la 0.2...)
    A partir d'ici on va commencer à calculer sévère... Attention que la méthode oscillation ne prend que ligne par ligne
    donc par 5 éléments.. 
    
    Il y a 101 oscillateurs par 5 lignes.. Ce qui fait 101^5 = 10 510 100 501 matrices à créér.
    NOTE : bon comme c'était encore trop énorme... J'ai réduit le nombre d'oscillateurs :(
    Faudra faire plus de passe... Y en a plus que 51
    
    J'ai utilisé le multiprocessing de Python afin d'accelérer les calculs d'oscillations, et dans le meme temps
    diviser les fichiers de sortie par process... J'espère que cette fois-ci ça passera..
    """
    mtxs_prob = []

    # Variable pour le processing (nombre d'oscillateurs!)
    debut_p1 = 0
    fin_p1 = 12
    debut_p2 = 12
    fin_p2 = 25
    debut_p3 = 25
    fin_p3 = 37
    debut_p4 = 37
    fin_p4 = 51

    print()
    print("Calcule sur 4 processeurs différents : ")
    print(Fore.RED + "Chaque processeur est bridé à 10 000 de calculs max !")
    print('pour des conditions de tests.. Ce qui ne laisse que **** millions de matrice probabiliste...' + Fore.RESET)
    print()

    p1 = Process(target=oscillation_processing, args=(debut_p1, fin_p1, oscillateurs, 'RESULT_PROB_P1.csv'))
    p1.start()
    print('Start ' + Fore.MAGENTA + 'Processus1' + Fore.RESET)

    p2 = Process(target=oscillation_processing, args=(debut_p2, fin_p2, oscillateurs, 'RESULT_PROB_P2.csv'))
    p2.start()
    print('Start ' + Fore.MAGENTA + 'Processus2' + Fore.RESET)

    p3 = Process(target=oscillation_processing, args=(debut_p3, fin_p3, oscillateurs, 'RESULT_PROB_P3.csv'))
    p3.start()
    print('Start ' + Fore.MAGENTA + 'Processus3' + Fore.RESET)

    p4 = Process(target=oscillation_processing, args=(debut_p4, fin_p4, oscillateurs, 'RESULT_PROB_P4.csv'))
    p4.start()
    print('Start ' + Fore.MAGENTA + 'Processus4' + Fore.RESET)
    print(Fore.MAGENTA + "Calcule..." + Fore.RESET)
    print()

    p1.join()
    p2.join()
    p3.join()
    p4.join()

    print("Matrices probabiliste de test créées!")
    print()





    print("Début de l'application de la formule pour déterminer toutes les matrices comportant les coéfficients de")
    print("contamination. Ces coéfficients ne représentent rien à ce stade, il faudra espérer voir une tendance se")
    print("créer pour repartir sur une oscillation de cette tendance, et ainsi affiner le pas...")
    print()
    print(Fore.BLUE + "Debut des calculs, par " + Fore.MAGENTA + "4 Processus." + Fore.RESET)
    print()

    print('Start'+ Fore.MAGENTA +' processus 1'+ Fore.RESET)
    p1 = Process(target=solving_math, args=('RESULT_PROB_P1.csv', 'RESULT_P1.csv', mtx))
    p1.start()

    print('Start' + Fore.MAGENTA +' processus 2'+ Fore.RESET)
    p2 = Process(target=solving_math, args=('RESULT_PROB_P2.csv', 'RESULT_P2.csv', mtx))
    p2.start()

    print('Start' + Fore.MAGENTA +' processus 3'+ Fore.RESET)
    p3 = Process(target=solving_math, args=('RESULT_PROB_P3.csv', 'RESULT_P3.csv', mtx))
    p3.start()

    print('Start'+ Fore.MAGENTA +' processus 4'+ Fore.RESET)
    p4 = Process(target=solving_math, args=('RESULT_PROB_P4.csv', 'RESULT_P4.csv', mtx))
    p4.start()


    p1.join()
    p2.join()
    p3.join()
    p4.join()



# Méthode à utiliser pour chaque process, ici 4 process différent...
def oscillation_processing(debut_p, fin_p, oscillateurs, path):
    count = 0

    file = open(path, 'w')
    file.write('')
    file.close()

    file = open(path, 'a', encoding='utf8')
    for a in range(debut_p, fin_p, 1):
        r1 = oscillation(mtx_prob[0], oscillateurs[a], divide=10)
        for b in range(0, len(oscillateurs), 1):
            r2 = oscillation(mtx_prob[1], oscillateurs[b], divide=10)
            for c in range(0, len(oscillateurs), 1):
                r3 = oscillation(mtx_prob[2], oscillateurs[c], divide=10)
                for d in range(0, len(oscillateurs), 1):
                    r4 = oscillation(mtx_prob[3], oscillateurs[d], divide=10)
                    for e in range(0, len(oscillateurs), 1):
                        r5 = oscillation(mtx_prob[4], oscillateurs[e], divide=10)
                        # mtxs_prob.append([r1, r2, r3, r4, r5])
                        # file.write(str(r1) + ';' + str(r2) + ';' + str(r3) + ';' + str(r4) + ';' + str(r5) + '\n')
                        file.write(str(r1[0]) + ";" + str(r1[1]) + ";" + str(r1[2]) + ";" + str(r1[3]) + ";" + str(r1[4]) + ";")
                        file.write(str(r2[0]) + ";" + str(r2[1]) + ";" + str(r2[2]) + ";" + str(r2[3]) + ";" + str(r2[4]) + ";")
                        file.write(str(r3[0]) + ";" + str(r3[1]) + ";" + str(r3[2]) + ";" + str(r3[3]) + ";" + str(r3[4]) + ";")
                        file.write(str(r4[0]) + ";" + str(r4[1]) + ";" + str(r4[2]) + ";" + str(r4[3]) + ";" + str(r4[4]) + ";")
                        file.write(str(r5[0]) + ";" + str(r5[1]) + ";" + str(r5[2]) + ";" + str(r5[3]) + ";" + str(r5[4]) + "\n")
                        count += 1
                        if count > 10000: #Bride
                            return 0

def solving_math(source, destination, mtx):
    count = 0
    # Chargement du csv precedement créé
    file = open(source, 'r').read()
    sortie = open(destination, 'w')
    sortie.write('')
    sortie.close()
    sortie = open(destination, 'a')

    lines = file.split('\n')
    lines.pop()
    prob = []
    for item in lines:
        i = list(item.split(';'))
        i = [float(x) for x in i]
        prob.append(i)

    for i in range(len(mtx) - 1):
        jour0 = mtx[i]
        jour1 = mtx[i + 1]
        for p in prob:
            result = solve(jour0, jour1, [
                [p[0], p[1], p[2], p[3], p[4]],
                [p[5], p[6], p[7], p[8], p[9]],
                [p[10], p[11], p[12], p[13], p[14]],
                [p[15], p[16], p[17], p[18], p[19]],
                [p[20], p[21], p[22], p[23], p[24]],
            ])
            sortie.write(json.dumps(result) + "\n")
            if count > 100000000: #Bride
                return 0
    sortie.close()

if __name__ == '__main__':
    main()