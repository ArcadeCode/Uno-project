class Game() :
    def __init__(self) -> None:
        self.globalScoreBoard = {}

    def set_actuallyScoreBoard(self, playersScore) : ### IN BETA
        '''Return the scoreboard of the party'''
        actuallyScoreBoard = playersScore
        actuallyScoreBoard.sort(reversed)
        return actuallyScoreBoard
    def set_globalScoreBoard(self, playersVictory_inOneParty) : ### IN BETA
        '''Check if the global scoreboard can be refresh'''
        for i in playersVictory_inOneParty : # For every player in the last game
            i2 = 0 # If player is in the scoreboard 
            if i > self.globalScoreBoard[i2] :
                while i > self.globalScoreBoard[i2] :
                    i2 += 1 # Have more victory than i2
                self.globalScoreBoard[i2] = i # If i2 superior set at the bottom i
            return self.globalScoreBoard






from random import randint

class Player() :
    def __init__(self, id, name=None) -> None:
        # Vérification si le nom du joueur a été choisis
        if name == None or name == "" :
             # Si nom lui donner un nom aléatoire
            self.name = self.get_randomName()
        else :
            self.name = name

        self.deck = None
        self.id = id
        self.score = 0
        self.victory_all = 0
        self.victory_inOneParty = 0

    def get_name(self) :
        return self.name
    def get_id(self) :
        return self.id
    def get_score(self) :
        return self.score
    def get_deck(self) :
        return self.deck

    def get_randomName(self) :
        randomNameH = ["Adrien", "Benjamin", "Clovid", "David", "Esteban", "François", "Grégoire", "Jaque", "Richard"]
        randomNameF = ["Aline", "Céline", "Elsa", "Fadoua"]
        randomNames = randomNameH + randomNameF
        random = randomNames[randint(0, len(randomNames)-1)]
        randomNames[randomNames.index(random)] += "A"
        return random

    def setDeck(self, newDeck) :
        self.deck = newDeck