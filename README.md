# TP3 LOG3000 - Calculatrice Web

## But et portée du projet
Ce projet est une application web de calculatrice développée avec Flask.

Il a pour but :
- d'offrir une interface web pour calculer une expression arithmétique à 1 opérateur
- d'implémenter une architecture claire entre:
  - le serveur Flask (`backend/app.py`);
  - la logique d'opérations (`backend/operators.py`);
  - l'interface (`templates/` et `static/`).
    
## Guide d'installation
### Prérequis
- Python 3 installé
- Git installé localement
- pip installé

### Étapes
1. Cloner le dépôt:
   ```bash
   git clone https://github.com/sarahaitaliyahia/TP3_LOG3000.git
   cd TP3_LOG3000
   ```
2. Créer un environnement virtuel:
   ```bash
   python3 -m venv .venv
   ```
3. Activer l'environnement virtuel:
   ```bash
   source .venv/bin/activate
   ```
4. Installer les dépendances:
   ```bash
   pip install flask
   ```

## Utilisation
### Lancer l'application
1. Vérifier que l'environnement virtuel est actif.
2. Démarrer le serveur:
   ```bash
   python backend/app.py
   ```
3. Ouvrir le navigateur sur `http://127.0.0.1:5000`

### Utiliser les fonctionnalités
- Saisir une expression avec les boutons (ex.: `7+2`).
- Cliquer sur `=` pour envoyer le calcul au serveur et avoir le résultat (ou le message d'erreur).
- Cliquer sur `C` pour réinitialiser la saisie.

## Tests
La suite de tests se trouve dans le dossier `tests/`.

Commande standard:
```bash
pytest -q
```

Pour exécuter un fichier de test précis:
```bash
pytest tests/test_app.py -q
```

Pour exécuter un test précis:
```bash
pytest tests/test_app.py -k "nom_du_test" -q
```

Si `pytest` n'est pas installé dans l'environnement virtuel:
```bash
pip install pytest
```

## Flux de contribution
### 1. Créer une issue
- Créer une issue pour toute amélioration ou anomalie.
- Décrire le besoin, l'impact attendu et les critères d'acceptation.
- Utiliser les issues pour suivre l'avancement et prioriser le travail.

### 2. Créer une branche
Nommer les branches selon le type de travail:
- `feature/<court-nom-descriptif>` pour travailler sur une fonctionnalité
- `fix/<court-nom-descriptif>` pour régler un problème ou une erreur
- `docs/<court-nom-descriptif>` pour travailler sur la documentation

Exemple:
```bash
git checkout -b docs/readme-principal
```

### 3. Développer et valider localement
- Faire des commits atomiques avec un message clair.
- Vérifier que l'application démarre.
- Exécuter les tests (lorsqu'applicable).

### 4. Ouvrir une Pull Request
- Pousser la branche sur le dépôt distant.
- Créer une PR vers `main`.
- Décrire clairement:
  - le problème;
  - la solution proposée;
  - les validations effectuées.
- Référencer l'issue dans la PR (ex.: `Closes #12`).
