import numpy as np
from scipy.optimize import minimize

"""
Pour tenir compte de la contrainte selon laquelle x1, x2 et x3 doivent être compris entre 0 et 1, nous pouvons utiliser une méthode différente appelée Programmation Quadratique Séquentielle (SQP). SQP est un algorithme d'optimisation qui peut gérer les contraintes.
....
"""

# fonction à minimiser
def F(x):
    return (10 * x[0] + 8 * x[1] + x[2] - 14) ** 2

#Les limites sont définies pour x1, x2 et x3 entre 0 et 1, garantissant ainsi que les contraintes sont satisfaites.
bounds = [(0, 1), (0, 1), (0, 1)]

# Estimation
x0 = [0, 0, 0]

# Appliquer SQP
res = minimize(F, x0, bounds=bounds, method='SLSQP')


print("Solution:", res.x)

""" _______________________________________________________________________________
    NB :la solution n'est pas unique, parceque le problème n'a qu'une seule équation linéaire avec trois variables. il pourrait y avoir une infinité de solutions qui marchent avec l'équation et les contraintes données. L'optimiseur trouve lui même une de ces solutions qui minimise la fonction F(x).
    
    
    
"""