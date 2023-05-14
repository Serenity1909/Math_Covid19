import numpy as np

"""
En partant de l'équation simplifiée à 3 variables  !!
######################################
F(x1, x2, x3) = 10x1 + 8x2 + 1*x3 - 14
######################################

La méthode de Newton-Raphson est une technique d'optimisation pour trouver les racines d'une fonction réelle à une seule variable, alors que notre problème implique au moins trois variables !!

on peut utiliser une extension multivariée de la méthode de Newton-Raphson pour les systèmes d'équations non linéaires.

    => calculer la matrice jacobienne pour ce système, qui est la matrice des dérivées partielles du premier ordre. Comme nous n'avons qu'une seule équation, la matrice jacobienne sera une matrice 1x3 :

        [ dF/dx1, dF/dx2, dF/dx3 ] = [ 10, 8, 1 ]

    => Pour appliquer la méthode de Newton-Raphson multivariée, nous devons mettre à jour notre estimation de manière itérative en utilisant la formule suivante :

        x_new = x_old - J^(-1) * F(x_old)

Par contre, comme notre matrice jacobienne est une matrice 1x3, impossible de l'inverser directement. Apparemment on peut utiliser l'inverse pseudo de Moore-Penrose à la place :
"""


def F(x):
    # la fonction F(x) est la différence entre la somme pondérée des variables et la valeur cible (14)
    return 10 * x[0] + 8 * x[1] + x[2] - 14


def jacobian(x):
    # la matrice jacobienne contient les dérivées partielles de la fonction F(x) par rapport à chacune des variables
    # Dans notre cas, la matrice jacobienne est une matrice 1x3 contenant les coefficients
    return np.array([[10, 8, 1]])


def newton_raphson_multi_variable(x0, max_iter=100, tol=1e-6):
    x = np.array(x0)
    # À chaque itération, la méthode met à jour les valeurs des variables en soustrayant le produit de la matrice
    # pseudo-inverse de la jacobienne et de la fonction F(x) aux valeurs actuelles des variables
    for _ in range(max_iter):
        Fx = F(x)
        if np.linalg.norm(Fx) < tol:  # critère d'arret basé sur la variable
            return x
        J = jacobian(x)
        J_pseudo_inverse = np.linalg.pinv(J)
        x = x - np.dot(J_pseudo_inverse, Fx)

    raise Exception("La méthode de Newton-Raphson n'a pas convergé")


if __name__ == '__main__':
    x0 = [0, 0, 0]
    solution = newton_raphson_multi_variable(x0)
    print("Solution:\n", solution)

"""
Le problème est que la solution fournie par cette méthode peut ne pas satisfaire la contrainte de x1, 
x2 et x3 étant compris entre 0 et 1.

la méthode de Newton-Raphson ne prend pas en compte les contraintes sur les variables lors de la recherche d'une 
solution. Cette méthode cherche simplement à trouver un zéro (ou une racine) de la fonction F, sans considérer si les 
valeurs de x1, x2 et x3 respectent les contraintes données (ici, être compris entre 0 et 1).
"""
