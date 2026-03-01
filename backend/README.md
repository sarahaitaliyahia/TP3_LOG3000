# Module backend

## Purpose
This module groups the Python code of the application. It centralizes server
logic (Flask) and calculation operations to simplify navigation in the
project.

## Main files and responsibilities
- `app.py`: Flask application entry point, expression validation,
  operation calls, and rendering of `templates/index.html`.
- `operators.py`: arithmetic functions used by `app.py`.

## Dependencies and assumptions
- Depends on Flask for the HTTP server and template rendering.
- The `templates/` and `static/` folders must remain at the project root.
- Evaluation supports a simple binary expression (a single operator).
