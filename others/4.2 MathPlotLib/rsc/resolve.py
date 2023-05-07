def Resolve(mtx, oscillateurs, r, precision, mtx0, mtx1):
    """
    Resolve est la fonction qui regroupe l'oscillation des matrices afin de les faire varier et d'effectuer un zoom,
    et de calculer dans la foulée l'écart-type entre le produit de la matrice calculée et celle du jour 0 par rapport
    a la matrice du jour +1.
    Plus le paramètre r est petit, et plus la matrice calculée est proche de la réalité.

    :param mtx: Matrice connue que l'on souhaite améliorer
    :param oscillateurs: Liste des oscillateurs qui vont faire varier la matrice connue
    :param r: Ecart-Type connu;
    :param precision: Précision de l'écart type minimal à obtenir par la fonction.
    :param mtx0: correspond à la matrice journalière du jour 0
    :param mtx1: correspond à la matrice journalière du jour 1
    :return: Retourne une liste comprenant la matrice calculée ainsi que l'écart type.
    """
    # import de la methode oscillation
    from rsc.oscillateur import oscillation
    from rsc.EcartType import EcartType
    import numpy
    numpy.seterr(invalid='ignore')
    # Variable de fonction
    tentative = 0
    # boucle tant que l'on est pas arrivé à la précision voulue :
    while (r > precision):
        # gestion du nombre de tentative qui va influencer la précision des oscillateurs
        if tentative in [0, 1, 2, 3, 4]:
            div = 1
        elif tentative in [5, 6, 7, 8]:
            div = 10
        elif tentative in [9, 10, 11, 12]:
            div = 50
        else:
            div = 100
        # oscillation de la matrice recue, et retour dans la liste mtx_R
        mtx_R = []
        for a in range(len(oscillateurs)):
            r1 = oscillation(mtx[0], oscillateurs[a], divide=div)
            for b in range(len(oscillateurs)):
                r2 = oscillation(mtx[1], oscillateurs[b], divide=div)
                for c in range(len(oscillateurs)):
                    r3 = oscillation(mtx[2], oscillateurs[c], divide=div)
                    for d in range(len(oscillateurs)):
                        r4 = oscillation(mtx[3], oscillateurs[d], divide=div)
                        for e in range(len(oscillateurs)):
                            r5 = oscillation(mtx[4], oscillateurs[e], divide=div)
                            # Rajout de la condition Not Neg, il ne faut pas de retour d'osc négatif
                            if checkNeg(r1) == True and checkNeg(r2) == True and checkNeg(r3) == True and checkNeg(r4) == True and checkNeg(r5) == True:
                                mtx_R.append([r1, r2, r3, r4, r5])

        # Calcul d'écart-type
        for i in range(len(mtx_R)):
            ec = EcartType(numpy.matrix(mtx_R[i]) * numpy.reshape(numpy.matrix(mtx0), (5, 1)), numpy.reshape(numpy.matrix(mtx1), (5, 1)))
            ec = ec ** 0.5
            if (ec < r):
                r = ec
                mtx = mtx_R[i]
        tentative += 1
        print("↕ Oscillation : " + str(tentative))

        if tentative >= 10:
            break
        if r < precision:
            break

    ss = str(r) + "||" + str(mtx)
    return ss

def checkNeg(list):
    """
    Méthode interne qui renvoit True si aucun nombre négatif trouvé dans la liste recue
    """
    for number in list:
        if number < 0:
            return False
    return True