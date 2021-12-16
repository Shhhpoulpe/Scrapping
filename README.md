# Scrapping

Ce projet github contient trois projets de scrapping

# El futbol.ipynb

El futbol.ipynb est un playbook d'introduction au scrapping avec la bibliothèque BeautifulSoup, il permet de voir des informations qui sont dans la page wikipédia du Championnat de France de football 2019-2020.

# bs4

Le dossier BS4 contient un début de code pour pouvoir regarder quand une chaine Youtube sort une nouvelle vidéo.

Le programme envoie dans les cookies qu'il a accepté les cookies afin de passer cette page, mais une fois arrivé sur la chaine Youtube, Beautiful Soup n'est pas capable de lire les scripts JavaScript de Youtube, le projet n'a donc pas pu être fini.

# selenium

Le dossier Selenium contient le même projet que bs4, mais codé avec Selenium.
Il permet de pouvoir lire le contenue de la chaine Youtube car il est capable de lire le Javascript.

Il contient aussi un ChromeDriver pour windows.

Pour le faire fonctionner il faut:

- Si vous n'êtes pas sur Windows, installer un nouveau ChromeDriver
- Changer la route absolue vers le ChromeDriver dans le code
- Créer un fichier 'discord_param.py' avec à l'intérieur :
  ```python
    discord_token = 'VOTRE TOKEN DISCORD'
  ```
- installer le requirements.txt pour python