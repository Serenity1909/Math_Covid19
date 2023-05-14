import json
import numpy as np
import matplotlib.pyplot as plt

"""
1. correction des erreurs d'indexation de la liste dans la fonction `estimate_parameters`. ajout d'une condition pour vérifier si la longueur de la liste likelihoods est supérieure à 1 avant d'essayer d'accéder à l'indice -2

2. traitement des valeurs de probabilité ambiguës car on tentait de comparer une valeur unique à un tableau numpy. la fonction `np.all' permet d'appliquer la condition à tous les éléments du tableau numpy.

3. les probabilités initiales n'étaient pas normalisées. il a fallut ajouter une ligne de code pour le faire après leur calcul.

4. correction de l'emplacement du retour dans la boucle de la fonction `estimate_parameters`. Elle ne retournait qu'une seule itération car le retour était dans la boucle for. 
"""
def parse_observations(file_path):
    # Cette fonction parcourt le fichier JSON et crée une structure de données
    dates = set()
    labels = set()
    obs_dict = {}

    with open(file_path, 'r') as file:
        data = json.load(file)
        for date, label_value_dict in data.items():
            try:
                for label, value in label_value_dict.items():
                    if not isinstance(value, int):
                        raise ValueError(f"Invalid observation value at ({date}, {label}): {value}")
                    labels.add(label)
                    if date not in obs_dict:
                        obs_dict[date] = {}
                    obs_dict[date][label] = value
                dates.add(date)
            except Exception as e:
                print(f"Error parsing line: {date}, {label_value_dict}")
                print(f"Error message: {e}")

    return sorted(list(dates)), sorted(list(labels)), obs_dict


def forward_backward(obs, transition_matrix, initial_probs, num_states, num_labels):
    # Cette fonction implémente l'algorithme forward-backward, une étape importante dans l'EM
    num_obs = len(obs)
    alpha = np.zeros((num_obs, num_states))
    alpha[0] = initial_probs * obs[0]
    for t in range(1, num_obs):
        alpha[t] = obs[t] * np.dot(alpha[t - 1], transition_matrix)
    beta = np.zeros((num_obs, num_states))
    beta[-1] = 1
    for t in range(num_obs - 2, -1, -1):
        beta[t] = np.dot(transition_matrix, obs[t + 1] * beta[t + 1])
    gamma = alpha * beta
    gamma /= gamma.sum(axis=1, keepdims=True)
    return alpha, beta, gamma


def estimate_parameters(obs_dict, num_states, num_labels, num_iters=100, tol=1e-6):
    # Cette fonction implémente l'algorithme EM pour estimer les paramètres du modèle à partir des observations
    dates = sorted(obs_dict.keys())
    num_dates = len(dates)
    transition_matrix = np.random.uniform(size=(num_states, num_states))
    transition_matrix /= transition_matrix.sum(axis=1, keepdims=True)
    initial_probs = np.random.uniform(size=num_states)
    initial_probs /= initial_probs.sum()
    likelihoods = []

    for i in range(num_iters):
        new_likelihood = 0
        gammas = []
        for date in dates:
            obs = np.array(list(obs_dict[date].values()))
            alpha, beta, gamma = forward_backward(obs, transition_matrix, initial_probs, num_states, num_labels)
            gammas.append(gamma)
            new_likelihood += np.log(np.dot(alpha[-1], obs[-1]))
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
        initial_probs /= initial_probs.sum()  # Normalize initial probabilities
        likelihoods.append(new_likelihood)
        if i > 0 and len(likelihoods) > 1 and np.all(abs(likelihoods[-1] - likelihoods[-2]) < tol): break

    return transition_matrix, initial_probs, likelihoods  # This line is now outside the for loop


def execute_em_algorithm():
    # Fonction utilitaire qui va exécuter le script EM
    file_path = 'Espérance_de_maximisation/COVID_5BXL.json'
    num_states = 2
    num_labels = 19
    parsed_data = parse_observations(file_path)
    dates = parsed_data[0]
    labels = parsed_data[1]
    obs_dict = parsed_data[2]
    transition_matrix, initial_probs, likelihoods = estimate_parameters(obs_dict, num_states, num_labels)

    # Print the learned parameters
    print("Learned transition matrix A:")
    print(transition_matrix)
    print("Learned initial state probabilities pi:")
    print(initial_probs)

    # Plot the likelihoods
    plt.plot(range(len(likelihoods)), likelihoods)
    plt.xlabel('Iterations')
    plt.ylabel('Log-likelihood')
    plt.show()

    # Print the final estimated matrices
    print("Transition matrix A:")
    print(transition_matrix)
    print("Initial state probabilities pi:")
    print(initial_probs)


execute_em_algorithm()
