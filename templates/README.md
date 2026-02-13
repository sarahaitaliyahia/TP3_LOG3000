# Module templates

## Raison d'être
Ce module contient les gabarits HTML rendus par Flask. Il définit la
structure de l'interface web que voit l'utilisateur.

## Fichiers principaux et responsabilités
- `index.html`: page unique de la calculatrice, il affiche le résultat renvoyé par
  Flask et contient les fonctions JavaScript minimales pour alimenter l'écran
  et effacer la saisie.

## Dépendances et hypothèses
- Dépend de Flask pour le rendu des variables/template tags `{{ url_for(...) }}` et `{{ result }}`.
- Dépend de `static/style.css` pour l'apparence visuelle.
- Le formulaire envoie la valeur de `display` en `POST` vers la route `/`.
- L'utilisateur veut résoudre des expressions à un seul opérateur et 2 opérandes.
