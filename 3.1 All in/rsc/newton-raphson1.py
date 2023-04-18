import numpy as np

"""Il ne prend pas en compte les contraintes sur les variables (par exemple, si x1, x2, x3 etc doivent être entre 0 
et 1). 
ne prend pas en compte les contraintes.
ne vérifie pas si la solution obtenue est unique ou s'il existe plusieurs solutions pour l'équation
ne gère pas les situations où la méthode de Newton-Raphson ne converge pas
"""


# Fonction qui définit les équations

def F(x):
    return np.array(
        [10 * x[0] + 8 * x[1] + 1 * x[2] + 14 * x[3] + 8 * x[5] + 1 * x[6] + 1 * x[7] + 2 * x[8] + 1 * x[9] - 14])


def J(x):
    return np.array([[10, 8, 1, 14, 0, 8, 1, 1, 2, 1]])


# Méthode de Newton-Raphson pour résoudre le système d'équations
def newton_raphson(x0, tol=1e-6):
    delta = np.inf
    x = x0
    while delta > tol:
        f = F(x)
        j = J(x)
        delta_x = np.linalg.pinv(j) @ -f
        x_new = x + delta_x
        delta = np.max(np.abs(delta_x))
        x = x_new
    return x


if __name__ == '__main__':
    x0 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    solution = newton_raphson(x0)
    print("Solution:\n", solution)
