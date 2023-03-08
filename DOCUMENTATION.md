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
```

## Lancer le serveur

```bash
flask --debug run
```

## Comprendre la structure du projet

Les fichiers `run.py` et `wsgi.py` sont des fichiers de configuration pour le serveur. Ils sont à la racine du projet.

Le dossier `envi` est l'environnement virtuel. Il n'est pas inclus dans le dépôt GitHub mais devrait se trouver à la racine du projet une fois la procédure d'installation suivie.

Le dossier `paconsse` est le dossier principal du projet. Il contient tout le code du site.

### modules

Chaque dossier dans `paconsse` est un **blueprint**. Chaque **blueprint** correspond à une "branche" de fonctionnalités du site. Par exemple, le **blueprint** "default" contient toutes les pages d'accueils et les pages "statiques". Quand on rajoutera le jeu, on créera un **blueprint** dédié qui contiendra tout le code du jeu.

Un module contient un fichier `__init__.py` contenant le code d'initialisation du **blueprint**. Il charge les différentes pages que contient le **blueprint**. Chaque fichier supplémentaire correspond à une page / fonctionnalité différente.

## utils

Le fichier utils contient des fonctions "indépendantes" utiles pour le projet, et qui peuvent être accédées n'importe où dans le projet. Par exemple, le print customisé `pprint()` est défini dans le fichier utils.