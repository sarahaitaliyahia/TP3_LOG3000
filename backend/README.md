# Module backend

## Raison d'être
Ce module regroupe le code Python de l'application. Il centralise la logique
serveur (Flask) et les opérations de calcul pour simplifier la navigation dans
le projet.

## Fichiers principaux et responsabilités
- `app.py`: point d'entrée de l'application Flask, validation de l'expression,
  appel des opérations, rendu de `templates/index.html`.
- `operators.py`: fonctions arithmétiques utilisées par `app.py`.

## Dépendances et hypothèses
- Dépend de Flask pour le serveur HTTP et le rendu de templates.
- Les dossiers `templates/` et `static/` doivent rester à la racine du projet.
- L'évaluation supporte une expression binaire simple (un seul opérateur).