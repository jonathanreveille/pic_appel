# Exercice de développement

Ceci est un programme qui permet de vérifier dans une liste d'appel, sous le format start:end, le pic d'appels simultané (actif pendant la même seconde).
Le programme vous retourne le plus grand nombre d'appels qui sont simultanés.

### Installation
Pour récupérer le programme, utilisez la commande
 ```git clone https://github.com/jonathanreveille/pic_appel.git``` 
dans votre projet.

### Activer de l'environnement virtuel
Activez l'environnement virtuel en deux étapes à partir de la racine du projet : 
- avec la commande ```pipenv install```pour installer les dépendances
- avec la commande ```pipenv shell``` pour activer le shell

### Lancer le programme
Une fois que l'environnement est activé, vous pouvez lancer le programme avec la commande
suivante : ```python -m appel_pic ```

Votre fichier avec la liste d'appels ('calls.txt') est situé dans le dossier data.

### Les tests
Si vous voulez faire passer les tests, la commande est : ```pytest -vvv```

###  Modifier les données entrantes
Si vous voulez utiliser d'autres données entrantes, vous pouvez
modifier les données dans le fichier 'data/calls.txt' sous la forme
**start:end**.  'Start' étant inférieur à 'End', et les appels
sont rangés dans l'ordre croissant sur le champ 'Start'.
