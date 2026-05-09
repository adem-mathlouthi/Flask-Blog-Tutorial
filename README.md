# Flask Blog - Projet DevOps

Projet réalisé dans le cadre du module DevOps.
On a pris une application Flask existante (Flask-Blog-Tutorial de TechWithTim)
et on a mis en place toute une chaîne DevOps dessus.


## C'est quoi ce projet ?

C'est un blog développé en Python/Flask qui permet de :
- Créer un compte et se connecter
- Publier des posts
- Commenter et liker des posts

On a ajouté dessus : des tests automatisés, un pipeline CI/CD avec GitHub Actions,
une containerisation avec Docker, et un monitoring avec Prometheus et Grafana.

## Comment lancer le projet ?

Il faut juste avoir Docker installé et lancer :

```bash
docker compose up --build
```

Ensuite :
- L'app est sur http://localhost:5000
- Prometheus sur http://localhost:9090
- Grafana sur http://localhost:3000 (login: admin / admin)

## Lancer les tests

```bash
pip install -r requirements.txt
pytest tests/ -v --cov=tutorial5
```

## Ce qu'on a mis en place

- Nettoyage du repo (gitignore, secrets dans .env)
- Tests unitaires et d'intégration avec pytest
- Pipeline CI : lint flake8 + tests automatiques sur chaque push
- Pipeline CD : build et push de l'image Docker sur ghcr.io
- Monitoring avec Prometheus qui scrape /metrics et Grafana pour visualiser
## Qualité de Code — Outils Pro

### Pre-commit Hooks
A chaque git commit, Black et flake8 tournent automatiquement :

```bash
pre-commit install
pre-commit run --all-files
```

### Dependabot
Chaque semaine, Dependabot vérifie automatiquement les nouvelles versions
des dépendances et ouvre des Pull Requests pour les mettre à jour.

### SonarCloud
Analyse automatique de la qualité du code à chaque push :
- Security, Reliability, Maintainability
- Couverture de code
- Duplications
- Security Hotspots

[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=adem-mathlouthi_Flask-Blog-Tutorial&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=adem-mathlouthi_Flask-Blog-Tutorial)

## Planification

On a utilisé GitHub Projects avec un board Kanban pour organiser le travail.
Chaque tâche était une issue qu'on déplaçait de Backlog vers Done
au fur et à mesure de l'avancement.

## Stack technique

Python, Flask, SQLite, Docker, GitHub Actions, Prometheus, Grafana
