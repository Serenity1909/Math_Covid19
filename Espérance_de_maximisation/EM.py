import json
import numpy as np
import matplotlib.pyplot as plt


def esperanceMaximisation():
    def parse_observations(file_path):
        dates = set()
        labels = set()
        observations = {}

        with open(file_path, 'r') as file:
            line_count = 0  # Add line counter
            for line in file:
                try:
                    date, label_value_dict = line.strip().split(':')
                    date = date.strip('"')
                    label_value_dict = eval(label_value_dict)
                    for label, value in label_value_dict.items():
                        if not value.isdigit():
                            raise ValueError(f"Invalid observation value at ({date}, {label}): {value}")
                        labels.add(label)
                        if date not in observations:
                            observations[date] = {}
                        observations[date][label] = int(value)
                    dates.add(date)
                except Exception as e:
                    print(f"Error parsing line: {line}")
                    print(f"Error message: {e}")

                line_count += 1  # Increment line counter
                if line_count == 5:  # Break out of loop after 5 lines
                    break

        return sorted(list(dates)), sorted(list(labels)), observations

    def forward_backward(obs, A, pi, n_states, n_labels):
        """
        Compute the alpha, beta, and gamma variables using the Forward-Backward algorithm.
        :param obs: matrix with shape (T, n_labels) containing the observations for one date
        :param A: transition matrix with shape (n_states, n_states)
        :param pi: initial state probabilities with shape (n_states,)
        :param n_states: number of hidden states
        :param n_labels: number of labels
        :return: alpha, beta, gamma
        """
        T = len(obs)

        # Forward algorithm
        alpha = np.zeros((T, n_states))
        alpha[0] = pi * obs[0]
        for t in range(1, T):
            alpha[t] = obs[t] * np.dot(alpha[t - 1], A)

        # Backward algorithm
        beta = np.zeros((T, n_states))
        beta[-1] = 1
        for t in range(T - 2, -1, -1):
            beta[t] = np.dot(A, obs[t + 1] * beta[t + 1])

        # Compute gamma
        gamma = alpha * beta
        gamma /= gamma.sum(axis=1, keepdims=True)

        return alpha, beta, gamma

    def estimate_parameters(observations, n_states, n_labels, n_iters=100, tol=1e-6):
        """
        Estimate the transition matrix A and initial state probabilities pi using the EM algorithm.
        :param observations: dictionary of matrices with shape (T_i, n_labels) containing the observations for each date
        :param n_states: number of hidden states
        :param n_labels: number of labels
        :param n_iters: maximum number of EM iterations
        :param tol: tolerance for the likelihood improvement between iterations
        :return: A, pi, likelihoods
        """
        dates = sorted(observations.keys())
        n_dates = len(dates)

        # Initialize A and pi randomly
        A = np.random.uniform(size=(n_states, n_states))
        A /= A.sum(axis=1, keepdims=True)
        pi = np.random.uniform(size=n_states)
        pi /= pi.sum()

        likelihoods = []
        for i in range(n_iters):
            new_likelihood = 0

            # E-step
            gammas = []
            for date in dates:
                obs = observations[date]
                alpha, beta, gamma = forward_backward(obs, A, pi, n_states, n_labels)
                gammas.append(gamma)
                new_likelihood += np.sum(np.log(np.dot(alpha[-1], pi)))

            # M-step
            A_num = np.zeros((n_states, n_states))
            A_den = np.zeros((n_states,))  # Fix: Changed shape to (n_states,)
            pi_num = np.zeros((n_states,))
            pi_den = 0
            for i in range(n_dates):
                date = dates[i]
                obs = observations[date]
                gamma = gammas[i]

                # Update A_num and A_den
                T = len(obs)
                for t in range(T - 1):
                    A_num += np.outer(gamma[t], gamma[t + 1])
                    A_den += gamma[t]  # Fix: Accumulate along the correct axis

                # Update pi_num and pi_den
                pi_num += gamma[0]
                pi_den += 1

            # Normalize A and pi
            A_den = np.sum(A_den)  # Fix: Sum over all states
            if np.isclose(A_den, 0):
                A = np.zeros((n_states, n_states))
            else:
                A = A_num / A_den[:, None]  # Fix: Normalize along the first dimension

            if np.isclose(pi_den, 0):
                pi = np.zeros((n_states,))
            else:
                pi = pi_num / pi_den

            likelihoods.append(new_likelihood)
            if i > 0 and likelihoods[-1] - likelihoods[-2] < tol:
                break

        return A, pi, likelihoods

    file_path = 'Espérance_de_maximisation/COVID_5BXL.json'
    n_states = 2
    n_labels = 19
    parsed_data = parse_observations(file_path)
    dates = parsed_data[0]
    labels = parsed_data[1]
    observations = parsed_data[2]
    A, pi, likelihoods = estimate_parameters(observations, n_states, n_labels)

    # Print the learned parameters
    print("Learned transition matrix A:")
    print(A)
    print("Learned initial state probabilities pi:")
    print(pi)

    # Plot the likelihoods
    # Plot the likelihoods
    plt.plot(range(len(likelihoods)), likelihoods)
    plt.xlabel('Iterations')
    plt.ylabel('Log-likelihood')
    plt.show()

    # Print the final estimated matrices
    print("Transition matrix A:")
    print(A)
    print("Initial state probabilities pi:")
    print(pi)
