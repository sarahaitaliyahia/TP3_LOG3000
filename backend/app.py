"""
Application Flask de calculatrice simple.

Ce module expose une interface web qui accepte une expression de la forme 
"nombre opérateur nombre" et délègue l'opération au module operators.
"""

from pathlib import Path

from flask import Flask, request, render_template
try:
    # Cas importé comme package: from backend.app import app
    from .operators import add, subtract, multiply, divide
except ImportError:
    # Cas exécuté directement: python backend/app.py
    from operators import add, subtract, multiply, divide

# Les ressources UI restent à la racine du projet même si le code Python
# est regroupé dans le module backend.
BASE_DIR = Path(__file__).resolve().parent.parent
app = Flask(
    __name__,
    template_folder=str(BASE_DIR / "templates"),
    static_folder=str(BASE_DIR / "static"),
)

OPS = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}

def calculate(expr: str):
    """
    Évalue une expression arithmétique avec 2 opérandes.

    Argument: expr, expression de l'utilisateur.
    Returns: Le résultat numérique retourné par l'opérateur sélectionné.
    Raises: ValueError, si le format est invalide ou si les opérandes ne sont pas numériques.
    """

    if not expr or not isinstance(expr, str):
        raise ValueError("empty expression")

    s = expr.replace(" ", "")

    op_pos = -1
    op_char = None

    # On limite volontairement le parser à une opération à 1 seul opérateur.
    for i, ch in enumerate(s):
        if ch in OPS:
            if op_pos != -1:
                raise ValueError("only one operator is allowed")
            op_pos = i
            op_char = ch

    if op_pos <= 0 or op_pos >= len(s) - 1:
        # operator at start/end or not found
        raise ValueError("invalid expression format")

    left = s[:op_pos]
    right = s[op_pos+1:]

    try:
        a = float(left)
        b = float(right)
    except ValueError:
        raise ValueError("operands must be numbers")

    return OPS[op_char](a, b)

@app.route('/', methods=['GET', 'POST'])
def index():
    """"
    Affiche la calculatrice et traite une soumission de calcul.

    Returns: La page HTML avec le résultat calculé ou un message d'erreur.
    """

    result = ""
    if request.method == 'POST':
        expression = request.form.get('display', '')
        try:
            result = calculate(expression)
        except Exception as e:
            # On renvoie une erreur lisible côté UI plutôt qu'une trace serveur.
            result = f"Error: {e}"
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
