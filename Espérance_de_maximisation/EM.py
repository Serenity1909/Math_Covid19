import json
import numpy as np
import matplotlib.pyplot as plt

"""
L'algorithme Expectation-Maximization (EM) est un algorithme d'optimisation largement utilisé en statistiques pour estimer les paramètres dans les modèles statistiques, 
notamment lorsque le modèle dépend de certaines variables cachées. L'EM est un algorithme itératif qui commence par une estimation initiale des paramètres, puis 
optimise ces paramètres en utilisant une série d'étapes d'espérance (E) et de maximisation (M).

Dans ce cas particulier, l'EM est utilisé pour estimer les paramètres d'un modèle de Markov caché (HMM) qui modélise la propagation du COVID-19 à Bruxelles pendant la pandémie. 
Les HMM sont des modèles probabilistes utiles pour représenter les processus temporels où l'état réel du système est partiellement observé ou caché.

L'application de l'EM à ce problème peut aider à comprendre comment le virus se propage à travers la population de Bruxelles, en mettant en lumière les tendances cachées 
dans les données. Cela peut ensuite être utilisé pour informer les politiques de santé publique, par exemple en prévoyant les pics d'infection et en identifiant 
les zones à haut risque.
"""


def parse_observations(file_path):
    # Cette fonction parcourt le fichier JSON qui contient les données de contamination de COVID-19 à Bruxelles. Les
    # dates, labels (zones de la ville) et observations (nombre de cas) sont extraits et stockés dans des structures
    # de données appropriées.
    dates = set()
    labels = set()
    obs_dict = {}

    # Ouverture du fichier JSON en lecture
    with open(file_path, 'r') as file:
        data = json.load(file)
        # Parcours du fichier JSON
        for date, label_value_dict in data.items():
            try:
                for label, value in label_value_dict.items():
                    # Vérification que la valeur est bien un entier
                    if not isinstance(value, int):
                        raise ValueError(f"Invalid observation value at ({date}, {label}): {value}")
                    labels.add(label)
                    # Si la date n'existe pas encore dans obs_dict, on l'ajoute
                    if date not in obs_dict:
                        obs_dict[date] = {}
                    obs_dict[date][label] = value
                dates.add(date)
            except Exception as e:
                print(f"Error parsing line: {date}, {label_value_dict}")
                print(f"Error message: {e}")

    return sorted(list(dates)), sorted(list(labels)), obs_dict


def forward_backward(obs, transition_matrix, initial_probs, num_states, num_labels):
    # Cette fonction implémente l'algorithme forward-backward, qui est une étape essentielle de l'EM. L'algorithme
    # forward-backward est utilisé pour calculer les probabilités marginales de chaque état à chaque instant.
    num_obs = len(obs)
    alpha = np.zeros((num_obs, num_states))
    alpha[0] = initial_probs * obs[0]
    # Boucle forward
    for t in range(1, num_obs):
        alpha[t] = obs[t] * np.dot(alpha[t - 1], transition_matrix)
    beta = np.zeros((num_obs, num_states))
    beta[-1] = 1
    # Boucle backward
    for t in range(num_obs - 2, -1, -1):
        beta[t] = np.dot(transition_matrix, obs[t + 1] * beta[t + 1])
    # Calcul des probabilités marginales
    gamma = alpha * beta
    gamma /= gamma.sum(axis=1, keepdims=True)
    return alpha, beta, gamma


def estimate_parameters(obs_dict, num_states, num_labels, num_iters=100, tol=1e-6):
    # Cette fonction implémente l'algorithme EM pour estimer les paramètres du modèle à partir des observations.
    # Les paramètres du modèle sont la matrice de transition et les probabilités initiales.
    dates = sorted(obs_dict.keys())
    num_dates = len(dates)
    # Initialisation aléatoire des paramètres
    transition_matrix = np.random.uniform(size=(num_states, num_states))
    transition_matrix /= transition_matrix.sum(axis=1, keepdims=True)
    initial_probs = np.random.uniform(size=num_states)
    initial_probs /= initial_probs.sum()
    likelihoods = []

    # Boucle EM
    for i in range(num_iters):
        new_likelihood = 0
        gammas = []
        # Étape E : calcul des probabilités marginales avec l'algorithme forward-backward
        for date in dates:
            obs = np.array(list(obs_dict[date].values()))
            alpha, beta, gamma = forward_backward(obs, transition_matrix, initial_probs, num_states, num_labels)
            gammas.append(gamma)
            new_likelihood += np.log(np.dot(alpha[-1], obs[-1]))
        # Étape M : mise à jour des paramètres pour maximiser la vraisemblance
        a_num = np.zeros((num_states, num_states))
        a_den = np.zeros((num_states, num_states))
        pi_num = np.zeros((num_states,))
        for i in range(num_dates):
            date = dates[i]
            obs = np.array(list(obs_dict[date].values()))
            gamma = gammas[i]
            num_obs = len(obs)
            for t in range(num_obs - 1):
                a_num += np.outer(gamma[t], gamma[t + 1])
                a_den += np.outer(gamma[t], np.ones(num_states))
                pi_num += gamma[0]
        transition_matrix = a_num / a_den
        initial_probs = pi_num / num_dates
        initial_probs /= initial_probs.sum()  # Normaliser les résultats initiaux
        likelihoods.append(new_likelihood)
        # Vérification de la convergence
        if i > 0 and len(likelihoods) > 1 and np.all(abs(likelihoods[-1] - likelihoods[-2]) < tol): break

    return transition_matrix, initial_probs, likelihoods


def execute_em_algorithm(fileEM):
    # Fonction utilitaire qui va exécuter le script EM
    file_path = fileEM
    num_states = 2
    num_labels = 19
    parsed_data = parse_observations(file_path)
    dates = parsed_data[0]
    labels = parsed_data[1]
    obs_dict = parsed_data[2]
    transition_matrix, initial_probs, likelihoods = estimate_parameters(obs_dict, num_states, num_labels)

    # Affichage des paramètres appris
    print("Learned transition matrix A:")
    print(transition_matrix)
    print("Learned initial state probabilities pi:")
    print(initial_probs)

    # Tracé des vraisemblances
    plt.plot(range(len(likelihoods)), likelihoods)
    plt.xlabel('Iterations')
    plt.ylabel('Log-likelihood')
    plt.show()

    # Print du graphique
    print("Transition matrix A:")
    print(transition_matrix)
    print("Initial state probabilities pi:")
    print(initial_probs)


