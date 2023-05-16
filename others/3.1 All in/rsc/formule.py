
"""
Formule,
Script à part du programme principal pour y améliorer la lecture.
Acceptera en entrée 3 matrices :
Les deux matrices journalière composée du jour[0] et du jour[1], matrices [1x5]
et de la matrices probabiliste que l'on test [5x5]
Le retour de la fonction est une matrice [5x5] qui correspond aux coefficient biaisé par la matrice de probabilité
de contamination...
Il faut espérer pouvoir dégager une tendance entre les matrices de test probabiliste
Delire Stéphane.
"""


def solve(jour0, jour1, prob):

    # Verification des entrées :
    if not isinstance(jour0, list) and not isinstance(jour1, list) and not isinstance(prob, list):
        return 0

    """ 
    jour0 et jour1 doivent être sous la forme [a, b, c, d, e]
    et prob : [[0.2, 0.2, 0.2, 0.2, 0.2], [0.2,0.2,0.2,0.2.....
    """

    # Matrice de sortie :
    rtn = []

    for i in range(len(jour1)):
        # jour1[1] = BXL[1], jour1[2] = SCH[1]...
        # prob[1] = 1ere ligne = [0.2,0.2,0.2...] Il faut encore un indice pour accéder aux valeurs..

        # r1 = prob[i][0] * jour1[i] / jour0[0] if jour0[0] != 0 else prob[i][0]
        # r2 = prob[i][1] * jour1[i] / jour0[1] if jour0[1] != 0 else prob[i][1]
        # r3 = prob[i][2] * jour1[i] / jour0[2] if jour0[2] != 0 else prob[i][2]
        # r4 = prob[i][3] * jour1[i] / jour0[3] if jour0[3] != 0 else prob[i][3]
        # r5 = prob[i][4] * jour1[i] / jour0[4] if jour0[4] != 0 else prob[i][4]

        r1 = prob[i][0] * jour1[i] / jour0[0] if jour0[0] != 0 else 0
        r2 = prob[i][1] * jour1[i] / jour0[1] if jour0[1] != 0 else 0
        r3 = prob[i][2] * jour1[i] / jour0[2] if jour0[2] != 0 else 0
        r4 = prob[i][3] * jour1[i] / jour0[3] if jour0[3] != 0 else 0
        r5 = prob[i][4] * jour1[i] / jour0[4] if jour0[4] != 0 else 0
        r6 = prob[i][5] * jour1[i] / jour0[5] if jour0[5] != 0 else 0
        r7 = prob[i][6] * jour1[i] / jour0[6] if jour0[6] != 0 else 0
        r8 = prob[i][7] * jour1[i] / jour0[7] if jour0[7] != 0 else 0
        r9 = prob[i][8] * jour1[i] / jour0[8] if jour0[8] != 0 else 0
        r10 = prob[i][9] * jour1[i] / jour0[9] if jour0[9] != 0 else 0
        r11 = prob[i][10] * jour1[i] / jour0[10] if jour0[10] != 0 else 0
        r12 = prob[i][11] * jour1[i] / jour0[11] if jour0[11] != 0 else 0
        r13 = prob[i][12] * jour1[i] / jour0[12] if jour0[12] != 0 else 0
        r14 = prob[i][13] * jour1[i] / jour0[13] if jour0[13] != 0 else 0
        r15 = prob[i][14] * jour1[i] / jour0[14] if jour0[14] != 0 else 0
        r16 = prob[i][15] * jour1[i] / jour0[15] if jour0[15] != 0 else 0
        r17 = prob[i][16] * jour1[i] / jour0[16] if jour0[16] != 0 else 0
        r18 = prob[i][17] * jour1[i] / jour0[17] if jour0[17] != 0 else 0
        r19 = prob[i][18] * jour1[i] / jour0[18] if jour0[18] != 0 else 0

        tt = [r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, r11, r12, r13, r14, r15, r16, r17, r18, r19]
        rtn.append(tt)

    return rtn




# jour0 = [46, 29, 15, 21, 19] #01.02.22
# jour1 = [32, 27, 15, 8, 8] #02.02.22
# prop = [
#     [0.2, 0.2, 0.2, 0.2, 0.2],
#     [0.2, 0.2, 0.2, 0.2, 0.2],
#     [0.2, 0.2, 0.2, 0.2, 0.2],
#     [0.2, 0.2, 0.2, 0.2, 0.2],
#     [0.2, 0.2, 0.2, 0.2, 0.2]
# ]
#
# print(solve(jour0, jour1, prop))