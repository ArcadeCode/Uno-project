'''
Project made by Dervaux Esteban (LA FRANCE)
It's a uno in python 3.10.0 (compatible 3.7.0)
necessary modules :
- random
'''

## Import
from motors.game import Game, Player
from motors.decks import motherClassDeck

## Consts :
const_win_WhenPlayerGet = None
const_win_MaxTurns = None
const_max_CharPlayerName = None 
const_max_Players = None
const_deck_nbCardsAtStart = None
const_deck_allCards = None
const_interface_exist = None
const_interface_path = None
const_ai_exist = None
const_const_ai_path = None
# Donne au variables leurs paramètres
with open("core\saves\global\setup.txt", "r") as file :
   for i in range(19) :
      exec(file.readline()) # Lecture du code python contenu dans setup.txt

## Creates Player
players = []
for x in range(const_max_Players) :
   players.append(Player(x, input("Choissisez un nom ou appuyer sur entrée\n>")))
   print(players[-1].get_name(), "a été créer !")
'''
# Debug version :
players = []
for x in range(const_max_Players) :
   players.append(Player(x, str(x)))
   print(players[-1].get_name(), "a été créer !")'''


## Creates Cards
#allCards = motherClassDeck(const_deck_nbCardsAtStart,const_deck_allCards)
pioche = motherClassDeck(const_deck_allCards)

for p in players :
   # Attribution d'un nombre de cartes au début de la partie à chaqu'un
   for x in range(const_deck_nbCardsAtStart) :
      p.setDeck(pioche.give_cards())

## Règles :
def get_uno(player) :
   '''Reste t-il des cartes au joueur ?'''
   if player.get_deck() == {} :
      return True
   else :
      return False

## Lancement
win = False
card_placed = []
card_pioche = []

card_placed.append(pioche.give_cards())
print(type(card_placed))
for x in range(107) :
   card_pioche.append(pioche.give_cards())

print(type(card_placed[0]))

## Boucle :
i = 0 # Pour éviter en cas de problème de générer une partie trop longue
while win == False and i < 10 : # Tant que aucun joueur à gagné
   # Pour chaque joueur
   for p in players :
      # Affiche ses cartes
      print("> Joueur :",p.get_name(), "joue")
      print("Voici vos cartes :")
      p.get_visualDeck()
      
      # Sélection de la carte par le user
      command = int(input("Choissisez l'index que vous voulez...\n>"))
      try : # Vérification de la présence de la carte dans le deck
         p.deck[command]
      except :
         print("Erreur, clé invalide veuillez choisir une clé existante dans votre deck")
         print("Votre tour est passé")
         continue
      else :
         print("Carte choissis !")
         # Vérification de la possibilité de placer la carte sur la carte
         # Précédemment placé, se référer à motors/game.py -> class Game()
         if Game.rules(card_placed[-1], p.deck[command]) == True :
            print("Votre carte a été posé")
         else :
            print("Erreur, carte impossible")
      
      win = get_uno(p) # Verif if the player have win
   i+=1