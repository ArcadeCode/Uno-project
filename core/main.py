'''
Project made by Dervaux Esteban (LA FRANCE)
It's a uno in python 3.10.0 (compatible 3.7.0)
necessary modules :
- random
'''

## Import
from motors.game import Game, Player
from motors.decks import motherClassDeck

## Create consts :
class Const : # On les stock dans un objet
    def __init__(self) -> None:
        self.version = "V.0.1"
        self.acceptAI = False
        self.lanParty = True
const = Const()

## Creates Player
playerA = Player(0)
playerB = Player(1)
playerC = Player(2)
playerD = Player(3)
playerE = Player(4)
playerF = Player(5)
playerG = Player(6)
playerH = Player(7)
# 8 players because it's the max accept by Uno rules

test = motherClassDeck()


## Init salon
if const.lanParty == True :
   class network() :
      def __init__(self) -> None:
         pass
      def post() :
         pass
      def get() :
         pass
      def broadcast() :
         pass

      def waitOK(self) :
         print("Êtes-vous prêt ?")
         input("press enter to continue")
         self.post()


## Init a game
# Créer les 108 cartes
# Donner 7 cartes à chaque joueurs
# Placer les cartes restante dans la pioche
# Prendre une carte de la pioche est la posé sur la table

## Play game
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
         break