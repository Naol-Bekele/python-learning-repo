import pytest
from src.probability_utils import (
    simulate_coin_flips,
    simulate_election,
    run_election_simulation,
    run_coin_toss_simulation,
)


def test_simulate_coin_flips():
    """Test coin flip simulation."""
    results = simulate_coin_flips(1000)

    # Should have exactly 1000 flips
    assert results["heads"] + results["tails"] == 1000

    # With fair coin, should be roughly 50/50
    ratio = results["heads"] / 1000
    assert 0.45 <= ratio <= 0.55


def test_simulate_election():
    """Test election simulation."""
    # Test with high probability of winning
    high_prob = [0.9, 0.9, 0.9]
    wins = sum(simulate_election(high_prob) for _ in range(100))
    assert wins > 90  # Should win most elections

    # Test with low probability of winning
    low_prob = [0.1, 0.1, 0.1]
    wins = sum(simulate_election(low_prob) for _ in range(100))
    assert wins < 20  # Should lose most elections


def test_run_election_simulation():
    """Test running multiple election simulations."""
    probabilities = [0.87, 0.65, 0.17]
    win_percentage = run_election_simulation(probabilities, 1000)

    # Should be a valid percentage
    assert 0 <= win_percentage <= 100


def test_run_coin_toss_simulation():
    """Test coin toss simulation."""
    avg_flips = run_coin_toss_simulation(1000)

    # Theoretical average is 3, but allow some variance
    assert 2.5 <= avg_flips <= 3.5
