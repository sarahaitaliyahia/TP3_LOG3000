# Module static

### Raison d'être
Ce module contient les ressources statiques de l'application web, soit
les styles CSS de l'interface.

### Fichiers principaux et responsabilités
- `style.css`: définit le formatage de la calculatrice dans la page.

### Dépendances et hypothèses
- Chargé par `templates/index.html` via `url_for('static', filename='style.css')`.
- Suppose une structure HTML qui contient les classes/ids: `calculator`, `buttons`, `btn`, `operator`, `display`.