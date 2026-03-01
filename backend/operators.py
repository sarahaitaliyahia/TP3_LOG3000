"""
Arithmetic operations used by the Flask application.
"""

def add(a,b):
    """
    Add two numeric values.

    Arguments: a (float), first operand, b (float), second operand.
    Returns: float, sum of a and b.
    """
    return a + b

def subtract(a,b):
    """Subtract b from a.

    Arguments: a (float), first operand, b (float), second operand.
    Returns: float, result of a - b.
    """
    return a - b

def multiply(a,b):
    """Multiply two numeric values.

    Arguments: a (float), first operand, b (float), second operand.
    Returns: float, result of a * b.
    """
    return a * b

def divide(a,b):
    """
    Apply real division.

    Arguments: a (float), dividend, b (float), divisor.
    Returns: float, quotient of a / b.
    """
    return a / b
