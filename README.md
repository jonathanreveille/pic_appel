# Exercice de développement

## Ceci est un programme qui permet de vérifier dans une 
liste d'appel, sous le format start:end, le pic d'appels
simultané (actif pendant la même seconde).

## Le programme vous retourne le plus grand nombre d'appel
qui sont simultanés.

Pour lancer le programme, utilisez ```git clone``` pour récupérer
le programme dans votre projet.

Activez l'environnement virtuel avec la commande ```pipenv shell```

Votre fichier avec la liste d'appels ('calls.txt') doit se situer 
au même niveau que votre fichier ***appel_pic.py*** .

Si vous voulez utilisez d'autres données entrantes, vous pouvez
modifier les données dans le fichier calls.txt sous la forme
**start:end**.  'Start' étant inférieur à 'End', et les appels
sont rangés dans l'ordre croissant sur le champ 'start'.

Une fois que l'environnement est activé, et que le script est
bien situé, vous pouvez lancer le programme avec la commande
suivante : ```python -m appel_pic ```

Si vous voulez faire passer les tests, la commande est la 
suivante : ```pytest -vvv```
