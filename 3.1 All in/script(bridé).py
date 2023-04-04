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
    [0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.10],
    [0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.10],
    [0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.10],
    [0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.10],
    [0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.10],
    [0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.10],
    [0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.10],
    [0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.10],
    [0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.10],
    [0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.10],
    [0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.10],
    [0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.10],
    [0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.10],
    [0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.10],
    [0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.10],
    [0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.10],
    [0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.10],
    [0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.10],
    [0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.10]
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
    if os.path.isfile('COVID_19BXL.json'):
        print("Fichier : " + Fore.CYAN + "COVID_19BXL.json " + Fore.RESET + "trouvé.")
    else:
        print(Fore.RED + "Erreur : " + Fore.RESET + "Le fichier " + Fore.CYAN + "COVID_19BXL.json " + Fore.RESET + "n'existe pas.")
        input()
        quit()
    global mtx
    mtx = loadmatrice('COVID_19BXL.json')
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
    fin_p1 = 5
    debut_p2 = 6
    fin_p2 = 11
    debut_p3 = 12
    fin_p3 = 15
    debut_p4 = 16
    fin_p4 = 19

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
                        for f in range(0, len(oscillateurs), 1):
                            r6 = oscillation(mtx_prob[5], oscillateurs[e], divide=10)
                            for g in range(0, len(oscillateurs), 1):
                                r7 = oscillation(mtx_prob[6], oscillateurs[e], divide=10)
                                for h in range(0, len(oscillateurs), 1):
                                    r8 = oscillation(mtx_prob[7], oscillateurs[e], divide=10)
                                    for i in range(0, len(oscillateurs), 1):
                                        r9 = oscillation(mtx_prob[8], oscillateurs[e], divide=10)
                                        for j in range(0, len(oscillateurs), 1):
                                            r10 = oscillation(mtx_prob[9], oscillateurs[e], divide=10)
                                            for k in range(0, len(oscillateurs), 1):
                                                r11 = oscillation(mtx_prob[10], oscillateurs[e], divide=10)
                                                for l in range(0, len(oscillateurs), 1):
                                                    r12 = oscillation(mtx_prob[11], oscillateurs[e], divide=10)
                                                    for m in range(0, len(oscillateurs), 1):
                                                        r13 = oscillation(mtx_prob[12], oscillateurs[e], divide=10)
                                                        for n in range(0, len(oscillateurs), 1):
                                                            r14 = oscillation(mtx_prob[13], oscillateurs[e], divide=10)
                                                            for o in range(0, len(oscillateurs), 1):
                                                                r15 = oscillation(mtx_prob[14], oscillateurs[e],divide=10)
                                                                for p in range(0, len(oscillateurs), 1):
                                                                    r16 = oscillation(mtx_prob[15], oscillateurs[e],divide=10)
                                                                    for q in range(0, len(oscillateurs), 1):
                                                                        r17 = oscillation(mtx_prob[16], oscillateurs[e],divide=10)
                                                                        for r in range(0, len(oscillateurs), 1):
                                                                            r18 = oscillation(mtx_prob[17],oscillateurs[e], divide=10)
                                                                            for s in range(0, len(oscillateurs), 1):
                                                                                r19 = oscillation(mtx_prob[18],oscillateurs[e],divide=10)
                                                                                # mtxs_prob.append([r1, r2, r3, r4, r5])
                                                                                # file.write(str(r1) + ';' + str(r2) + ';' + str(r3) + ';' + str(r4) + ';' + str(r5) + '\n')
                                                                                file.write(str(r1[0]) + ";" + str(
                                                                                    r1[1]) + ";" + str(
                                                                                    r1[2]) + ";" + str(
                                                                                    r1[3]) + ";" + str(
                                                                                    r1[4]) + ";" + str(
                                                                                    r1[5]) + ";" + str(
                                                                                    r1[6]) + ";" + str(
                                                                                    r1[7]) + ";" + str(
                                                                                    r1[8]) + ";" + str(
                                                                                    r1[9]) + ";" + str(
                                                                                    r1[10]) + ";" + str(
                                                                                    r1[11]) + ";" + str(
                                                                                    r1[12]) + ";" + str(
                                                                                    r1[13]) + ";" + str(
                                                                                    r1[14]) + ";" + str(
                                                                                    r1[15]) + ";" + str(
                                                                                    r1[16]) + ";" + str(
                                                                                    r1[17]) + ";" + str(r1[18]) + ";")
                                                                                file.write(str(r2[0]) + ";" + str(
                                                                                    r2[1]) + ";" + str(
                                                                                    r2[2]) + ";" + str(
                                                                                    r2[3]) + ";" + str(
                                                                                    r2[4]) + ";" + str(
                                                                                    r2[5]) + ";" + str(
                                                                                    r2[6]) + ";" + str(
                                                                                    r2[7]) + ";" + str(
                                                                                    r2[8]) + ";" + str(
                                                                                    r2[9]) + ";" + str(
                                                                                    r2[10]) + ";" + str(
                                                                                    r2[11]) + ";" + str(
                                                                                    r2[12]) + ";" + str(
                                                                                    r2[13]) + ";" + str(
                                                                                    r2[14]) + ";" + str(
                                                                                    r2[15]) + ";" + str(
                                                                                    r2[16]) + ";" + str(
                                                                                    r2[17]) + ";" + str(r2[18]) + ";")
                                                                                file.write(str(r3[0]) + ";" + str(
                                                                                    r3[1]) + ";" + str(
                                                                                    r3[2]) + ";" + str(
                                                                                    r3[3]) + ";" + str(
                                                                                    r3[4]) + ";" + str(
                                                                                    r3[5]) + ";" + str(
                                                                                    r3[6]) + ";" + str(
                                                                                    r3[7]) + ";" + str(
                                                                                    r3[8]) + ";" + str(
                                                                                    r3[9]) + ";" + str(
                                                                                    r3[10]) + ";" + str(
                                                                                    r3[11]) + ";" + str(
                                                                                    r3[12]) + ";" + str(
                                                                                    r3[13]) + ";" + str(
                                                                                    r3[14]) + ";" + str(
                                                                                    r3[15]) + ";" + str(
                                                                                    r3[16]) + ";" + str(
                                                                                    r3[17]) + ";" + str(r3[18]) + ";")
                                                                                file.write(str(r4[0]) + ";" + str(
                                                                                    r4[1]) + ";" + str(
                                                                                    r4[2]) + ";" + str(
                                                                                    r4[3]) + ";" + str(
                                                                                    r4[4]) + ";" + str(
                                                                                    r4[5]) + ";" + str(
                                                                                    r4[6]) + ";" + str(
                                                                                    r4[7]) + ";" + str(
                                                                                    r4[8]) + ";" + str(
                                                                                    r4[9]) + ";" + str(
                                                                                    r4[10]) + ";" + str(
                                                                                    r4[11]) + ";" + str(
                                                                                    r4[12]) + ";" + str(
                                                                                    r4[13]) + ";" + str(
                                                                                    r4[14]) + ";" + str(
                                                                                    r4[15]) + ";" + str(
                                                                                    r4[16]) + ";" + str(
                                                                                    r4[17]) + ";" + str(r4[18]) + ";")
                                                                                file.write(str(r5[0]) + ";" + str(
                                                                                    r5[1]) + ";" + str(
                                                                                    r5[2]) + ";" + str(
                                                                                    r5[3]) + ";" + str(
                                                                                    r5[4]) + ";" + str(
                                                                                    r5[5]) + ";" + str(
                                                                                    r5[6]) + ";" + str(
                                                                                    r5[7]) + ";" + str(
                                                                                    r5[8]) + ";" + str(
                                                                                    r5[9]) + ";" + str(
                                                                                    r5[10]) + ";" + str(
                                                                                    r5[11]) + ";" + str(
                                                                                    r5[12]) + ";" + str(
                                                                                    r5[13]) + ";" + str(
                                                                                    r5[14]) + ";" + str(
                                                                                    r5[15]) + ";" + str(
                                                                                    r5[16]) + ";" + str(
                                                                                    r5[17]) + ";" + str(r5[18]) + ";")
                                                                                file.write(str(r6[0]) + ";" + str(
                                                                                    r6[1]) + ";" + str(
                                                                                    r6[2]) + ";" + str(
                                                                                    r6[3]) + ";" + str(
                                                                                    r6[4]) + ";" + str(
                                                                                    r6[5]) + ";" + str(
                                                                                    r6[6]) + ";" + str(
                                                                                    r6[7]) + ";" + str(
                                                                                    r6[8]) + ";" + str(
                                                                                    r6[9]) + ";" + str(
                                                                                    r6[10]) + ";" + str(
                                                                                    r6[11]) + ";" + str(
                                                                                    r6[12]) + ";" + str(
                                                                                    r6[13]) + ";" + str(
                                                                                    r6[14]) + ";" + str(
                                                                                    r6[15]) + ";" + str(
                                                                                    r6[16]) + ";" + str(
                                                                                    r6[17]) + ";" + str(r6[18]) + ";")
                                                                                file.write(str(r7[0]) + ";" + str(
                                                                                    r7[1]) + ";" + str(
                                                                                    r7[2]) + ";" + str(
                                                                                    r7[3]) + ";" + str(
                                                                                    r7[4]) + ";" + str(
                                                                                    r7[5]) + ";" + str(
                                                                                    r7[6]) + ";" + str(
                                                                                    r7[7]) + ";" + str(
                                                                                    r7[8]) + ";" + str(
                                                                                    r7[9]) + ";" + str(
                                                                                    r7[10]) + ";" + str(
                                                                                    r7[11]) + ";" + str(
                                                                                    r7[12]) + ";" + str(
                                                                                    r7[13]) + ";" + str(
                                                                                    r7[14]) + ";" + str(
                                                                                    r7[15]) + ";" + str(
                                                                                    r7[16]) + ";" + str(
                                                                                    r7[17]) + ";" + str(r7[18]) + ";")
                                                                                file.write(str(r8[0]) + ";" + str(
                                                                                    r8[1]) + ";" + str(
                                                                                    r8[2]) + ";" + str(
                                                                                    r8[3]) + ";" + str(
                                                                                    r8[4]) + ";" + str(
                                                                                    r8[5]) + ";" + str(
                                                                                    r8[6]) + ";" + str(
                                                                                    r8[7]) + ";" + str(
                                                                                    r8[8]) + ";" + str(
                                                                                    r8[9]) + ";" + str(
                                                                                    r8[10]) + ";" + str(
                                                                                    r8[11]) + ";" + str(
                                                                                    r8[12]) + ";" + str(
                                                                                    r8[13]) + ";" + str(
                                                                                    r8[14]) + ";" + str(
                                                                                    r8[15]) + ";" + str(
                                                                                    r8[16]) + ";" + str(
                                                                                    r8[17]) + ";" + str(r8[18]) + ";")
                                                                                file.write(str(r9[0]) + ";" + str(
                                                                                    r9[1]) + ";" + str(
                                                                                    r9[2]) + ";" + str(
                                                                                    r9[3]) + ";" + str(
                                                                                    r9[4]) + ";" + str(
                                                                                    r9[5]) + ";" + str(
                                                                                    r9[6]) + ";" + str(
                                                                                    r9[7]) + ";" + str(
                                                                                    r9[8]) + ";" + str(
                                                                                    r9[9]) + ";" + str(
                                                                                    r9[10]) + ";" + str(
                                                                                    r9[11]) + ";" + str(
                                                                                    r9[12]) + ";" + str(
                                                                                    r9[13]) + ";" + str(
                                                                                    r9[14]) + ";" + str(
                                                                                    r9[15]) + ";" + str(
                                                                                    r9[16]) + ";" + str(
                                                                                    r9[17]) + ";" + str(r9[18]) + ";")
                                                                                file.write(str(r10[0]) + ";" + str(
                                                                                    r10[1]) + ";" + str(
                                                                                    r10[2]) + ";" + str(
                                                                                    r10[3]) + ";" + str(
                                                                                    r10[4]) + ";" + str(
                                                                                    r10[5]) + ";" + str(
                                                                                    r10[6]) + ";" + str(
                                                                                    r10[7]) + ";" + str(
                                                                                    r10[8]) + ";" + str(
                                                                                    r10[9]) + ";" + str(
                                                                                    r10[10]) + ";" + str(
                                                                                    r10[11]) + ";" + str(
                                                                                    r10[12]) + ";" + str(
                                                                                    r10[13]) + ";" + str(
                                                                                    r10[14]) + ";" + str(
                                                                                    r10[15]) + ";" + str(
                                                                                    r10[16]) + ";" + str(
                                                                                    r10[17]) + ";" + str(r10[18]) + ";")
                                                                                file.write(str(r11[0]) + ";" + str(
                                                                                    r11[1]) + ";" + str(
                                                                                    r11[2]) + ";" + str(
                                                                                    r11[3]) + ";" + str(
                                                                                    r11[4]) + ";" + str(
                                                                                    r11[5]) + ";" + str(
                                                                                    r11[6]) + ";" + str(
                                                                                    r11[7]) + ";" + str(
                                                                                    r11[8]) + ";" + str(
                                                                                    r11[9]) + ";" + str(
                                                                                    r11[10]) + ";" + str(
                                                                                    r11[11]) + ";" + str(
                                                                                    r11[12]) + ";" + str(
                                                                                    r11[13]) + ";" + str(
                                                                                    r11[14]) + ";" + str(
                                                                                    r11[15]) + ";" + str(
                                                                                    r11[16]) + ";" + str(
                                                                                    r11[17]) + ";" + str(r11[18]) + ";")
                                                                                file.write(str(r12[0]) + ";" + str(
                                                                                    r12[1]) + ";" + str(
                                                                                    r12[2]) + ";" + str(
                                                                                    r12[3]) + ";" + str(
                                                                                    r12[4]) + ";" + str(
                                                                                    r12[5]) + ";" + str(
                                                                                    r12[6]) + ";" + str(
                                                                                    r12[7]) + ";" + str(
                                                                                    r12[8]) + ";" + str(
                                                                                    r12[9]) + ";" + str(
                                                                                    r12[10]) + ";" + str(
                                                                                    r12[11]) + ";" + str(
                                                                                    r12[12]) + ";" + str(
                                                                                    r12[13]) + ";" + str(
                                                                                    r12[14]) + ";" + str(
                                                                                    r12[15]) + ";" + str(
                                                                                    r12[16]) + ";" + str(
                                                                                    r12[17]) + ";" + str(r12[18]) + ";")
                                                                                file.write(str(r13[0]) + ";" + str(
                                                                                    r13[1]) + ";" + str(
                                                                                    r13[2]) + ";" + str(
                                                                                    r13[3]) + ";" + str(
                                                                                    r13[4]) + ";" + str(
                                                                                    r13[5]) + ";" + str(
                                                                                    r13[6]) + ";" + str(
                                                                                    r13[7]) + ";" + str(
                                                                                    r13[8]) + ";" + str(
                                                                                    r13[9]) + ";" + str(
                                                                                    r13[10]) + ";" + str(
                                                                                    r13[11]) + ";" + str(
                                                                                    r13[12]) + ";" + str(
                                                                                    r13[13]) + ";" + str(
                                                                                    r13[14]) + ";" + str(
                                                                                    r13[15]) + ";" + str(
                                                                                    r13[16]) + ";" + str(
                                                                                    r13[17]) + ";" + str(r13[18]) + ";")
                                                                                file.write(str(r14[0]) + ";" + str(
                                                                                    r14[1]) + ";" + str(
                                                                                    r14[2]) + ";" + str(
                                                                                    r14[3]) + ";" + str(
                                                                                    r14[4]) + ";" + str(
                                                                                    r14[5]) + ";" + str(
                                                                                    r14[6]) + ";" + str(
                                                                                    r14[7]) + ";" + str(
                                                                                    r14[8]) + ";" + str(
                                                                                    r14[9]) + ";" + str(
                                                                                    r14[10]) + ";" + str(
                                                                                    r14[11]) + ";" + str(
                                                                                    r14[12]) + ";" + str(
                                                                                    r14[13]) + ";" + str(
                                                                                    r14[14]) + ";" + str(
                                                                                    r14[15]) + ";" + str(
                                                                                    r14[16]) + ";" + str(
                                                                                    r14[17]) + ";" + str(r14[18]) + ";")
                                                                                file.write(str(r15[0]) + ";" + str(
                                                                                    r15[1]) + ";" + str(
                                                                                    r15[2]) + ";" + str(
                                                                                    r15[3]) + ";" + str(
                                                                                    r15[4]) + ";" + str(
                                                                                    r15[5]) + ";" + str(
                                                                                    r15[6]) + ";" + str(
                                                                                    r15[7]) + ";" + str(
                                                                                    r15[8]) + ";" + str(
                                                                                    r15[9]) + ";" + str(
                                                                                    r15[10]) + ";" + str(
                                                                                    r15[11]) + ";" + str(
                                                                                    r15[12]) + ";" + str(
                                                                                    r15[13]) + ";" + str(
                                                                                    r15[14]) + ";" + str(
                                                                                    r15[15]) + ";" + str(
                                                                                    r15[16]) + ";" + str(
                                                                                    r15[17]) + ";" + str(r15[18]) + ";")
                                                                                file.write(str(r16[0]) + ";" + str(
                                                                                    r16[1]) + ";" + str(
                                                                                    r16[2]) + ";" + str(
                                                                                    r16[3]) + ";" + str(
                                                                                    r16[4]) + ";" + str(
                                                                                    r16[5]) + ";" + str(
                                                                                    r16[6]) + ";" + str(
                                                                                    r16[7]) + ";" + str(
                                                                                    r16[8]) + ";" + str(
                                                                                    r16[9]) + ";" + str(
                                                                                    r16[10]) + ";" + str(
                                                                                    r16[11]) + ";" + str(
                                                                                    r16[12]) + ";" + str(
                                                                                    r16[13]) + ";" + str(
                                                                                    r16[14]) + ";" + str(
                                                                                    r16[15]) + ";" + str(
                                                                                    r16[16]) + ";" + str(
                                                                                    r16[17]) + ";" + str(r16[18]) + ";")
                                                                                file.write(str(r17[0]) + ";" + str(
                                                                                    r17[1]) + ";" + str(
                                                                                    r17[2]) + ";" + str(
                                                                                    r17[3]) + ";" + str(
                                                                                    r17[4]) + ";" + str(
                                                                                    r17[5]) + ";" + str(
                                                                                    r17[6]) + ";" + str(
                                                                                    r17[7]) + ";" + str(
                                                                                    r17[8]) + ";" + str(
                                                                                    r17[9]) + ";" + str(
                                                                                    r17[10]) + ";" + str(
                                                                                    r17[11]) + ";" + str(
                                                                                    r17[12]) + ";" + str(
                                                                                    r17[13]) + ";" + str(
                                                                                    r17[14]) + ";" + str(
                                                                                    r17[15]) + ";" + str(
                                                                                    r17[16]) + ";" + str(
                                                                                    r17[17]) + ";" + str(r17[18]) + ";")
                                                                                file.write(str(r18[0]) + ";" + str(
                                                                                    r18[1]) + ";" + str(
                                                                                    r18[2]) + ";" + str(
                                                                                    r18[3]) + ";" + str(
                                                                                    r18[4]) + ";" + str(
                                                                                    r18[5]) + ";" + str(
                                                                                    r18[6]) + ";" + str(
                                                                                    r18[7]) + ";" + str(
                                                                                    r18[8]) + ";" + str(
                                                                                    r18[9]) + ";" + str(
                                                                                    r18[10]) + ";" + str(
                                                                                    r18[11]) + ";" + str(
                                                                                    r18[12]) + ";" + str(
                                                                                    r18[13]) + ";" + str(
                                                                                    r18[14]) + ";" + str(
                                                                                    r18[15]) + ";" + str(
                                                                                    r18[16]) + ";" + str(
                                                                                    r18[17]) + ";" + str(r18[18]) + ";")
                                                                                file.write(str(r19[0]) + ";" + str(
                                                                                    r19[1]) + ";" + str(
                                                                                    r19[2]) + ";" + str(
                                                                                    r19[3]) + ";" + str(
                                                                                    r19[4]) + ";" + str(
                                                                                    r19[5]) + ";" + str(
                                                                                    r19[6]) + ";" + str(
                                                                                    r19[7]) + ";" + str(
                                                                                    r19[8]) + ";" + str(
                                                                                    r19[9]) + ";" + str(
                                                                                    r19[10]) + ";" + str(
                                                                                    r19[11]) + ";" + str(
                                                                                    r19[12]) + ";" + str(
                                                                                    r19[13]) + ";" + str(
                                                                                    r19[14]) + ";" + str(
                                                                                    r19[15]) + ";" + str(
                                                                                    r19[16]) + ";" + str(
                                                                                    r19[17]) + ";" + str(r19[18]) + ";")

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
                [p[0], p[1], p[2], p[3], p[4], p[5], p[6], p[7], p[8], p[9], p[10], p[11], p[12], p[13], p[14], p[15],
                 p[16], p[17], p[18]],
                [p[19], p[20], p[21], p[22], p[23], p[24], p[25], p[26], p[27], p[28], p[29], p[30], p[31], p[32], p[33], p[34],
                 p[35], p[36], p[37]],
                [p[38], p[39], p[40], p[41], p[42], p[43], p[44], p[45], p[46], p[47], p[48], p[49], p[50], p[51], p[52], p[53],
                 p[54], p[55], p[56]],
                [p[57], p[58], p[59], p[60], p[61], p[62], p[63], p[64], p[65], p[66], p[67], p[68], p[69], p[70], p[71], p[72],
                 p[73], p[74], p[75]],
                [p[76], p[77], p[78], p[79], p[80], p[81], p[82], p[83], p[84], p[85], p[86], p[87], p[88], p[89], p[90], p[91],
                 p[92], p[93], p[94]],
                [p[95], p[96], p[97], p[98], p[99], p[100], p[101], p[102], p[103], p[104], p[105], p[106], p[107], p[108], p[109], p[110],
                 p[111], p[112], p[113]],
                [p[114], p[115], p[116], p[117], p[118], p[119], p[120], p[121], p[122], p[123], p[124], p[125], p[126], p[127], p[128], p[129],
                 p[130], p[131], p[132]],
                [p[133], p[134], p[135], p[136], p[137], p[138], p[139], p[140], p[141], p[142], p[143], p[144], p[145], p[146], p[147], p[148],
                 p[149], p[150], p[151]],
                [p[152], p[153], p[154], p[155], p[156], p[157], p[158], p[159], p[160], p[161], p[162], p[163], p[164], p[165], p[166], p[167],
                 p[168], p[169], p[170]],
                [p[171], p[172], p[173], p[174], p[175], p[176], p[177], p[178], p[179], p[180], p[181], p[182], p[183], p[184], p[185], p[186],
                 p[187], p[188], p[189]],
                [p[190], p[191], p[192], p[193], p[194], p[195], p[196], p[197], p[198], p[199], p[200], p[201], p[202], p[203], p[204], p[205],
                 p[206], p[207], p[208]],
                [p[209], p[210], p[211], p[212], p[213], p[214], p[215], p[216], p[217], p[218], p[219], p[220], p[221], p[222], p[223], p[224],
                 p[225], p[226], p[227]],
                [p[228], p[229], p[230], p[231], p[232], p[233], p[234], p[235], p[236], p[237], p[238], p[239], p[240], p[241], p[242], p[243],
                 p[244], p[245], p[246]],
                [p[247], p[248], p[249], p[250], p[251], p[252], p[253], p[254], p[255], p[256], p[257], p[258], p[259], p[260], p[261], p[262],
                 p[263], p[264], p[265]],
                [p[266], p[267], p[268], p[269], p[270], p[271], p[272], p[273], p[274], p[275], p[276], p[277], p[278], p[279], p[280], p[281],
                 p[282], p[283], p[284]],
                [p[285], p[286], p[287], p[288], p[289], p[290], p[291], p[292], p[293], p[294], p[295], p[296], p[297], p[298], p[299], p[300],
                 p[301], p[302], p[303]],
                [p[304], p[305], p[306], p[307], p[308], p[309], p[310], p[311], p[312], p[313], p[314], p[315], p[316], p[317], p[318], p[319],
                 p[320], p[321], p[322]],
                [p[323], p[324], p[325], p[326], p[327], p[328], p[329], p[330], p[331], p[332], p[333], p[334], p[335], p[336], p[337], p[338],
                 p[339], p[340], p[341]],
                [p[342], p[343], p[344], p[345], p[346], p[347], p[348], p[349], p[350], p[351], p[352], p[353], p[354], p[355], p[356], p[357],
                 p[358], p[359], p[360]]
            ])
            sortie.write(json.dumps(result) + "\n")
            if count > 100000000: #Bride
                return 0
    sortie.close()

if __name__ == '__main__':
    main()