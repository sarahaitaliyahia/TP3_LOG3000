"""
Simple Flask calculator application.

This module exposes a web interface that accepts an expression in the form
"number operator number" and delegates the operation to the operators module.
"""

from pathlib import Path

from flask import Flask, request, render_template
try:
    # Imported as a package: from backend.app import app
    from .operators import add, subtract, multiply, divide
except ImportError:
    # Executed directly: python backend/app.py
    from operators import add, subtract, multiply, divide

# UI resources remain at the project root even if Python code
# is grouped in the backend module.
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
    Evaluate an arithmetic expression with 2 operands.

    Argument: expr, user expression.
    Returns: Numeric result returned by the selected operator.
    Raises: ValueError, if format is invalid or operands are not numeric.
    """

    if not expr or not isinstance(expr, str):
        raise ValueError("empty expression")

    s = expr.replace(" ", "")

    op_pos = -1
    op_char = None

    # Parser intentionally supports only one binary operator.
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
    """
    Render the calculator and handle a submitted expression.

    Returns: HTML page with either computed result or an error message.
    """

    result = ""
    if request.method == 'POST':
        expression = request.form.get('display', '')
        try:
            result = calculate(expression)
        except Exception as e:
            # Return a UI-friendly error instead of exposing a server traceback.
            result = f"Error: {e}"
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
