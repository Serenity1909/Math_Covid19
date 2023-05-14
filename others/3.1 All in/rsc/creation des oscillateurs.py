import json
import itertools

"""
L'implémentation initiale utilisait des boucles imbriquées pour générer des combinaisons d'oscillateurs.
il n'était pas adapté pour appliquer la méthode de Newton-Raphson et trouver les racines d'une fonction à valeurs réelles.

Le module itertools permet de mieux gérer les ressources et ainsi accélérer le process. la fonction parcourt les 
combinaisons et génère celles qui sont valides, rendant le code plus rapide à exécuter

la complexité de base du problème reste la même. Le temps d'exécution
sera toujours relativement long en raison du grand nombre de combinaisons générées.

-> Itertool : https://www.youtube.com/watch?v=WR7mO_jYN9g
"""


def generate_combinations():
    """
    produit des combinaisons valides d'oscillateurs.
    parcourt le produit des plages et vérifie si la somme de la combinaison ajustée
    est égale à 0. Si la condition est remplie, la combinaison ajustée est générée.
    """
    for combination in itertools.product(range(0, 3), repeat=19):
        adjusted_combination = [x - 1 for x in combination]
        if sum(adjusted_combination) == 0:
            yield adjusted_combination


arr = list(generate_combinations())

print(arr)
print(len(arr))

# Enregistrer les oscillateurs dans un fichier
with open('oscillateurs', 'w', encoding='utf8') as file:
    json.dump(arr, file)

print("fin enregistrement")
