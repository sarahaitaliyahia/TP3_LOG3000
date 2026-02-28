"""
Opérations arithmétiques utilisées par l'application Flask.
"""

def add(a,b):
    """
    Additionne deux valeurs numériques.

    Arguments: a, premier opérande.
               b, deuxième opérande.
    Returns: La somme de a et b.
    """
    return a + b

def subtract(a,b):
    """Soustrait a de b.

    Arguments: a, valeur à soustraire.
               b, valeur de départ.
    Returns: Le résultat de b - a.
    """
    return b - a

def multiply(a,b):
    """Applique l'opération de puissance de a par b.

    Arguments: a, base.
               b, exposant.
    Returns: Le résultat de a ** b.
    """
    return a * b

def divide(a,b):
    """
    Applique une division entière.

    Arguments: a, dividende.
               b, diviseur.
    Returns: Le quotient entier de a // b.
    """
    return a // b
