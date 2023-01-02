# Imports
from Engines import Player, Game

#Consts
const_version = "V.0.2"

def makePlayers(nbPlayers) :
    for x in range(0, nbPlayers) :
        input("Give a name for player",x,"\n>>>")

## Setup :
print("Welcome in Uno in python\n",const_version)
print("For starting...")

nbPlayers = input("Enter the nb of players\nmin = 2\nmax = 10\n>>>"),
makePlayers(nbPlayers)
