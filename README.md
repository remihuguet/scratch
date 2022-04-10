# Projet Todo list - Studi live Développement web avec Python

## Comment travailler avec le projet

1. Installer `pyenv` (documentation)[https://github.com/pyenv/pyenv#installation]
2. Installer Python `3.10`avec pyenv: `pyenv install 3.10.x` (choisissez la version la plus récente, `3.10.3`au moins)
3. Utiliser cette version dans le répertoire du projet `pyenv local 3.10.x`
4. Créer un environnement virtuel `python -m venv .venv`et l'activer avec `source .venv/bin/activate`(sur Linux / MacOS, dépend de votre système)
5. Mettre à jour pip `pip install -U pip setuptools`
6.  Installer les dépendances du projet: `pip install -r requirements.txt`
7.  Pour faire tourner l'application en local: `gunicorn application --reload`
