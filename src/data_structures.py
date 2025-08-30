"""
Data structure utilities for tuples, lists, and dictionaries.
"""

from collections import namedtuple
import copy
import random


def create_named_tuple(type_name, fields):
    """
    Create a named tuple type with the given fields.

    Args:
        type_name (str): Name of the tuple type
        fields (list): List of field names

    Returns:
        type: Named tuple class
    """
    return namedtuple(type_name, fields)


def safe_list_operations():
    """
    Demonstrate safe list operations including copying.

    Returns:
        dict: Examples of different copy operations
    """
    original = [[1, 2], [3, 4]]

    # Shallow copy
    shallow_copy = original.copy()
    shallow_copy[0][0] = 99

    # Reset
    original = [[1, 2], [3, 4]]

    # Deep copy
    deep_copy = copy.deepcopy(original)
    deep_copy[0][0] = 99

    return {
        "original_after_shallow": original,
        "shallow_copy": shallow_copy,
        "original_after_deep": original,
        "deep_copy": deep_copy,
    }


def list_comprehension_examples():
    """
    Demonstrate various list comprehension patterns.

    Returns:
        dict: Examples of different comprehensions
    """
    # Basic comprehension
    squares = [x**2 for x in range(10)]

    # With condition
    even_squares = [x**2 for x in range(10) if x % 2 == 0]

    # Nested comprehensions
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    flattened = [num for row in matrix for num in row]

    # Transforming data
    str_numbers = ["1.5", "2.3", "5.25"]
    float_numbers = [float(num) for num in str_numbers]

    return {
        "squares": squares,
        "even_squares": even_squares,
        "flattened_matrix": flattened,
        "float_numbers": float_numbers,
    }


def sort_with_custom_key(data, key_func, reverse=False):
    """
    Sort data using a custom key function.

    Args:
        data (list): Data to sort
        key_func (callable): Function to extract sort key
        reverse (bool): Sort in descending order

    Returns:
        list: Sorted data
    """
    return sorted(data, key=key_func, reverse=reverse)


def nested_data_examples():
    """
    Demonstrate nested data structures.

    Returns:
        dict: Examples of nested structures
    """
    # 2D list (matrix)
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    # List of tuples
    student_grades = [("Alice", 85), ("Bob", 92), ("Charlie", 78)]

    return {"matrix": matrix, "student_grades": student_grades}


def dictionary_operations():
    """
    Demonstrate dictionary operations.

    Returns:
        dict: Examples of dictionary operations
    """
    capitals = {"California": "Sacramento", "New York": "Albany", "Texas": "Austin"}

    # Adding/updating values
    capitals["Colorado"] = "Denver"
    capitals["Texas"] = "Houston"

    # Removing values
    del capitals["Texas"]
    removed = capitals.pop("New York", "Not found")

    return {
        "capitals": capitals,
        "removed_value": removed,
        "keys": list(capitals.keys()),
        "values": list(capitals.values()),
        "items": list(capitals.items()),
    }


def nested_dictionary_example():
    """
    Create a nested dictionary example.

    Returns:
        dict: Nested dictionary of US states
    """
    states = {
        "California": {
            "capital": "Sacramento",
            "flower": "California Poppy",
            "population": 39500000,
        },
        "Texas": {"capital": "Austin", "flower": "Bluebonnet", "population": 29000000},
    }

    # Adding a new state
    states["New York"] = {"capital": "Albany", "flower": "Rose", "population": 19500000}

    # Updating nested values
    states["Texas"]["population"] = 30000000

    return states


def capital_quiz(capitals_dict):
    """
    Run a capital city quiz game.

    Args:
        capitals_dict (dict): Dictionary of state-capital pairs

    Returns:
        function: Quiz function
    """

    def quiz():
        states = list(capitals_dict.keys())
        state = random.choice(states)
        capital = capitals_dict[state]

        print(f"What is the capital of {state}?")

        while True:
            guess = input("Your answer (or 'exit' to quit): ").strip()

            if guess.lower() == "exit":
                print(f"The correct answer for {state} was {capital}. Goodbye!")
                break
            elif guess.title() == capital:
                print("Correct! 🎉")
                break
            else:
                print("That's not correct. Try again!")

    return quiz


def generate_poem():
    """
    Generate a random poem using predefined word lists.

    Returns:
        str: Generated poem
    """
    nouns = [
        "fossil",
        "horse",
        "aardvark",
        "judge",
        "chef",
        "mango",
        "extrovert",
        "gorilla",
    ]
    verbs = ["kicks", "jingles", "bounces", "slurps", "meows", "explodes", "curdles"]
    adjectives = [
        "furry",
        "balding",
        "incredulous",
        "fragrant",
        "exuberant",
        "glistening",
    ]
    prepositions = [
        "against",
        "after",
        "into",
        "beneath",
        "upon",
        "for",
        "in",
        "like",
        "over",
        "within",
    ]
    adverbs = ["curiously", "extravagantly", "tantalizingly", "furiously", "sensuously"]

    def select_random_words():
        return {
            "nouns": random.sample(nouns, 3),
            "verbs": random.sample(verbs, 3),
            "adjectives": random.sample(adjectives, 3),
            "prepositions": random.sample(prepositions, 2),
            "adverbs": random.sample(adverbs, 1),
        }

    words = select_random_words()

    # Get the words
    noun1, noun2, noun3 = words["nouns"]
    verb1, verb2, verb3 = words["verbs"]
    adj1, adj2, adj3 = words["adjectives"]
    prep1, prep2 = words["prepositions"]
    adverb1 = words["adverbs"][0]

    # Handle article for adjectives
    article = "An" if adj1[0].lower() in "aeiou" else "A"

    # Create the poem
    poem = f"{article} {adj1} {noun1}\n"
    poem += f"{article} {adj1} {noun1} {verb1} {prep1} the {adj2} {noun2}\n"
    poem += f"{adverb1}, the {noun1} {verb2}\n"
    poem += f"the {noun2} {verb3} {prep2} a {adj3} {noun3}"

    return poem


def enrollment_stats(universities):
    """
    Extract enrollment and tuition data from universities list.

    Args:
        universities (list): List of university data

    Returns:
        tuple: (enrollments, tuitions)
    """
    enrollments = [uni[1] for uni in universities]
    tuitions = [uni[2] for uni in universities]
    return enrollments, tuitions


def calculate_mean(values):
    """
    Calculate the mean of a list of values.

    Args:
        values (list): List of numerical values

    Returns:
        float: Mean value
    """
    return sum(values) / len(values)


def calculate_median(values):
    """
    Calculate the median of a list of values.

    Args:
        values (list): List of numerical values

    Returns:
        float: Median value
    """
    sorted_values = sorted(values)
    n = len(sorted_values)
    mid = n // 2

    if n % 2 == 0:
        return (sorted_values[mid - 1] + sorted_values[mid]) / 2
    else:
        return sorted_values[mid]


def cats_with_hats():
    """
    Solve the cats with hats problem.

    Returns:
        list: List of cats that have hats
    """
    # Create 100 cats without hats (False means no hat)
    cats = [False] * 100

    # Walk around 100 times
    for round_number in range(1, 101):
        # Visit every cat at the current step
        for cat_index in range(round_number - 1, 100, round_number):
            # Toggle hat status
            cats[cat_index] = not cats[cat_index]

    # Find which cats have hats
    cats_with_hats = []
    for i, has_hat in enumerate(cats):
        if has_hat:
            cats_with_hats.append(i + 1)  # +1 because cats are numbered from 1

    return cats_with_hats
