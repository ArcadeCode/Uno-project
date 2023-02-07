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
'''players = []
for x in range(const_max_Players) :
   players.append(Player(x, input("Choissisez un nom ou appuyer sur entrée\n>")))
   print(players[-1].get_name(), "a été créer !")'''
players = []
for x in range(const_max_Players) :
   players.append(Player(x, str(x)))
   print(players[-1].get_name(), "a été créer !")


## Creates Cards
#allCards = motherClassDeck(const_deck_nbCardsAtStart,const_deck_allCards)
pioche = motherClassDeck(const_deck_nbCardsAtStart,const_deck_allCards)
#playerPioche = pioche.give_cards(4)
for p in players :
   p.setDeck(pioche.give_cards(7))

## Init a game
# Créer les 108 cartes
# Donner 7 cartes à chaque joueurs
# Placer les cartes restante dans la pioche
# Prendre une carte de la pioche est la posé sur la table

'''## Play game
win  = False
turn = 0
totalTurn = 0 # Cette varible sera stocké dans motors\turn plus tard
while win == False or turn > 1000 :
   
   turn += 1
   totalTurn += 1

   # Sécurités anti bouclage
   if turn > 1000 :
      if const.lanParty == False : # <-- Partie local
         print("Plus de", totalTurn,  "tours jouer voulez vous abandonner ?")
         if input("Write 'Confirm' to end the party\n") == "Confirm" :
            break
         else :
            turn = 0
      else : # <--- Partie LAN
         print("La partie a durée trop longtemps, la partie est terminé")
         # Si la partie dure trop longtemps (1K de tours) on la supprime
         break'''