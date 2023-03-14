"""
Oscillateur,
Ensemble de methodes pour les fonction d'oscillation du projet de math 2022.
Delire Stéphane.
"""


def oscillation(matriX, oscillateur, invert=False, multiply=1, divide=1):
    """
    Fonction d'oscillation,
    Spécifiez en entrée la matrice 5x1 (une seul ligne donc), et ensuite le tableau
    contenant les valeurs d'oscillation.
    Il est à noter que les valeurs de l'oscillateur sont scalaires et ordonnées :
    La première valeur de l'oscillateur s'additionnera à la plus haute valeur de la
    matrice et ainsi de suite...

    invert : mettre à true permet d'inverser les valeurs de l'oscillateur (concretement
    au lieu de faire une addition, c'est une soustraction).

    multiply : par défaut l'oscillateur ne s'applique qu'une fois, passez ce paramètre à
    plus pour que l'oscillateur s'applique plusieurs fois sur la matrice.

    Divide : par défaut sur un, ça divise les opérateurs de l'oscillateur. Ca permet de
    regler le pas. Par exemple on peut affiner la recherche en donnant un divide de 10,
    ce qui affinerait l'oscillateur de 10.
    """
    # Verification des types :
    if not isinstance(matriX, list) and not isinstance(oscillateur, list):
        return 0

    # Copie de la matrice de base :
    tmp = matriX.copy()
    mtx = matriX.copy()

    # Tri de la copie pour obtenir les chiffres dans l'ordre du plus grand au plus petit
    tmp.sort(reverse=True)

    # Formation de la list de sortie
    hsh = [0, 0, 0, 0, 0]

    # Calcul dans la boucle
    for i in range(0, len(mtx), 1):
        pop = tmp.pop(0)
        index = mtx.index(pop)
        mtx[index] = ""  # Pour éviter les doublons

        # Verification si on doit inverser ou pas & multiply
        # Le round, pour les float (voir err Python)
        if invert is False:
            hsh[index] = round(float(pop) + (oscillateur[i] / divide) * multiply, 5)
        else:
            hsh[index] = round(float(pop) - (oscillateur[i] / divide) * multiply, 5)

    # Return
    return hsh



# matrice = [0.1, 0.2, 0.3, 0.4, 0.5]
# osc = [0.1, 0.1, 0.1, 0.1, 0.1]
# print(oscillation(matrice, osc))

