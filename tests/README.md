# Module tests

## Raison d'être
Ce module contient les tests de régression pour les 3 bogues logiques
identifiés et suivis dans les issues GitHub.

## Ce que les tests couvrent
- `test_operators.py`:
  - bug #1: ordre des opérandes de `subtract(a, b)`;
  - bug #2: opérateur utilisé par `multiply(a, b)`;
  - bug #3: type de division utilisée par `divide(a, b)`.

## Exécuter tous les tests
À partir de la racine du projet:

```bash
source .venv/bin/activate
python -m unittest discover -s tests -v
```