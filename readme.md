# French readme file

Bonjour et voici le fichier de présentation du projet Uno en python. Ici vous retrouverez l'explication de comment faire fonctionner le projet et comment marche les moteurs.

Pour démarrer le projet il faut pour l'instant executer le fichier : **core\main.py**

## Sommaire :
- Pourquoi le dossier core ?
- motors\ ...
    - motors\deck.py
    - motors\game.py 
- système de sauvegarde

## Le gestionnaire de tours
Il est passer par beaucoup de changement celui là ^^
Le gestionnaire des tours : motors\turnSystem est un outil qui va gérer qui sera le prochain joueur en prenant en comptes 2 cartes pouvant altérer l'ordre :
- Carte "Stop", cette carte va sauter le tour du prochain pour l'empêcher de jouer
- Carte "Reverse" ou "Changement de sens", cette carte va changer le sens dans lequel vont jouer les jours, exemple : Nous avons A, B, C et D, 4 joueurs qui jouer ensembles, par défaut on joue dans l'ordre des aiguilles d'un montre si on considère que ABCD est équivalent, après que C posera sa carte se sera à D de jouer, mais C à poser une carte "Reverse" ainsi ce n'est plus à D de jouer mais à B, car le sens n'est plus ABCD mais DCBA.

Le gestionnaire des tours est une class nommer "TurnSystem"
Il possède plusieurs méthodes :
>- TurnSystem.turn({number of turn})
>- TurnSystem.played([reverse] or [stop])
>- TurnSystem.get_Turn()



### Pourquoi le dossier core ?
Le dossier core contient tout le code qui fait fonctionner le projet, ainsi on peut utiliser le core dans d'autres projets, il a simplement besoin d'être connecter à d'autres systèmes tel qu'une interface graphique ou une système de IA si la constante 'canSetAI' égal à True