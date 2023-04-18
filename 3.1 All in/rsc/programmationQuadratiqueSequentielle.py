import numpy as np
from scipy.optimize import minimize

"""Pour tenir compte de la contrainte selon laquelle x1, x2 et x3 doivent être compris entre 0 et 1, nous pouvons 
utiliser une méthode différente appelée Programmation Quadratique Séquentielle (SQP). SQP est un algorithme 
d'optimisation qui peut gérer les contraintes. ....
######################################
F(x1, x2, x3) = 10x1 + 8x2 + 1*x3 - 14
######################################
"""


# fonction à minimiser
def F(x):
    return (10 * x[0] + 8 * x[1] + x[2] - 14) ** 2


# Les limites sont définies pour x1, x2 et x3 entre 0 et 1, garantissant ainsi que les contraintes sont satisfaites.
bounds = [(0, 1), (0, 1), (0, 1)]

# Estimation
x0 = np.array([0, 0, 0])

# Appliquer SQP
res = minimize(F, x0, bounds=bounds, method='SLSQP')

print("Solution:", res.x)

"""_______________________________________________________________________________ 
 SQP minimise l'équation et respecte les contraintes en même temps 
    
    
    
"""
