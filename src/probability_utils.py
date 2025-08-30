"""
Probability and simulation utilities.
"""

import random


def simulate_coin_flips(num_flips, bias=0.5):
    """
    Simulate multiple coin flips.

    Args:
        num_flips: Number of flips to simulate
        bias: Probability of heads (0.0 to 1.0)

    Returns:
        Dictionary with heads and tails counts
    """
    heads = 0
    tails = 0

    for _ in range(num_flips):
        if random.random() < bias:
            heads += 1
        else:
            tails += 1

    return {"heads": heads, "tails": tails}


def simulate_election(region_probabilities):
    """
    Simulate an election based on regional probabilities.

    Args:
        region_probabilities: List of probabilities for each region

    Returns:
        True if candidate wins, False otherwise
    """
    wins = 0
    for probability in region_probabilities:
        if random.random() < probability:
            wins += 1

    # Candidate wins if they win at least half the regions
    return wins >= len(region_probabilities) / 2


def run_election_simulation(probabilities, num_trials=10000):
    """
    Run multiple election simulations.

    Args:
        probabilities: List of regional probabilities
        num_trials: Number of simulations to run

    Returns:
        Win percentage
    """
    wins = 0
    for _ in range(num_trials):
        if simulate_election(probabilities):
            wins += 1

    return wins / num_trials * 100


def coin_toss_experiment():
    """
    Simulate flipping a coin until both heads and tails appear.

    Returns:
        Number of flips needed
    """
    flips = 0
    has_head = False
    has_tail = False

    while not (has_head and has_tail):
        result = "heads" if random.random() < 0.5 else "tails"
        flips += 1

        if result == "heads":
            has_head = True
        else:
            has_tail = True

    return flips


def run_coin_toss_simulation(num_trials=10000):
    """
    Run multiple coin toss experiments.

    Args:
        num_trials: Number of experiments to run

    Returns:
        Average number of flips needed
    """
    total_flips = 0
    for _ in range(num_trials):
        total_flips += coin_toss_experiment()

    return total_flips / num_trials
