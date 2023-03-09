# Installation

## Créer un environnement virtuel

```bash
python3 -m venv envi
```

`envi` est le nom de l'environnement dans le gitignore. Par convention, conserver ce nom.

```bash
source envi/bin/activate

pip install --upgrade pip
pip install Flask
pip install rich
pip install python-dotenv
pip install flask-wtf
```

## installer tailwindcss

```bash
curl -sLO https://github.com/tailwindlabs/tailwindcss/releases/latest/download/tailwindcss-macos-arm64
chmod +x tailwindcss-macos-arm64
mv tailwindcss-macos-arm64 tailwindcss
```

## lancer le serveur tailwind

```bash
./tailwindcss -i paconsse/static/input.css -o paconsse/static/output.css --watch
```

## Lancer le serveur

```bash
flask --debug run
```

On peut également créer un fichier vide `tailwind.config.js` à la racine du projet pour permettre à vscode d'autocompléter.

## Comprendre la structure du projet

Les fichiers `run.py` et `wsgi.py` sont des fichiers de configuration pour le serveur. Ils sont à la racine du projet.

Le dossier `envi` est l'environnement virtuel. Il n'est pas inclus dans le dépôt GitHub mais devrait se trouver à la racine du projet une fois la procédure d'installation suivie.

Le dossier `paconsse` est le dossier principal du projet. Il contient tout le code du site.

### modules

Chaque dossier dans `paconsse` est un **blueprint**. Chaque **blueprint** correspond à une "branche" de fonctionnalités du site. Par exemple, le **blueprint** "default" contient toutes les pages d'accueils et les pages "statiques". Quand on rajoutera le jeu, on créera un **blueprint** dédié qui contiendra tout le code du jeu.

Un module contient un fichier `__init__.py` contenant le code d'initialisation du **blueprint**. Il charge les différentes pages que contient le **blueprint**. Chaque fichier supplémentaire correspond à une page / fonctionnalité différente.

Un module contient également un dossier `templates` qui contient toutes les templates HTML du **blueprint**. Ces templates contiennent également des `components` personalisables et réutilisables.

## utils

Le fichier utils contient des fonctions "indépendantes" utiles pour le projet, et qui peuvent être accédées n'importe où dans le projet. Par exemple, le print customisé `pprint()` est défini dans le fichier utils.
