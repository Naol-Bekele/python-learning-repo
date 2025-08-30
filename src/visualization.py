import matplotlib.pyplot as plt
import numpy as np


def create_basic_plot(data, title="Basic Plot", xlabel="Index", ylabel="Value"):
    """Create a basic matplotlib plot"""
    plt.figure(figsize=(10, 6))
    plt.plot(data)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True, alpha=0.3)
    return plt


def customize_plot():
    """Demonstrate plot customization"""
    x = np.linspace(0, 10, 100)
    y = np.sin(x)

    plt.figure(figsize=(12, 6))
    plt.plot(x, y, "r-", linewidth=2, marker="o", markersize=4, label="sin(x)")
    plt.title("Customized Sine Wave", fontsize=14)
    plt.xlabel("X values", fontsize=12)
    plt.ylabel("sin(X)", fontsize=12)
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    return plt
