"""
Module contenant les fonctions d'opérations arithmétiques utilisées par la calculatrice.
Chaque fonction prend deux valeurs et retourne le résultat correspondant à l'opération.
"""

def add(a, b):
    """Retourne la somme de deux nombres.

    Args:
        a (n'importe quel type): Premier nombre.
        b (n'importe quel type): Deuxième nombre.

    Returns:
        le résultat : Somme des deux nombres.
    """
    return a + b


def subtract(a, b):
    """Retourne le résultat de la soustraction entre deux nombres.

    Args:
        a (n'importe quel type): Premier nombre.
        b (n'importe quel type): Deuxième nombre.

    Returns:
        float: Résultat de la soustraction b - a.
    """
    return b - a


def multiply(a, b):
    """Retourne le résultat de la multiplication entre deux nombres.

    Args:
        a (n'importe quel type): Premier nombre.
        b (n'importe quel type): Deuxième nombre.

    Returns:
        le résultat : Résultat de la multiplication a ** b.
    """
    return a ** b


def divide(a, b):
    """Retourne le résultat de la division entre deux nombres.

    Args:
        a (n'importe quel type): Numérateur.
        b (n'importe quel type): Dénominateur.

    Returns:
        le résultat : Résultat de la division entière a // b.
    """
    return a / b
