class Game() :
    def __init__(self) -> None:
        pass

    def rules(cardPlaced, cardPlayer) :
        
        print(cardPlaced)
        print(cardPlayer)
        print(type(cardPlaced))
        print(type(cardPlayer))
        '''Vérifie si le joueur peut jouer cette carte'''
        if cardPlayer[0] == "Joker" :
            # Carte joker
            print("Joker")
            return True
        elif cardPlayer[0] == "+4" :
            # Carte +4
            print("Joker")
            return True
        elif cardPlaced[0][1][0] == cardPlayer[0] :
            # Même symbole
            return True
        elif cardPlaced[0][1][1] == cardPlayer[1] :
            # Même couleur
            return True
        else :
            # La carte ne peut pas être poser
            return False
        





from random import randint

class Player() :
    def __init__(self, id, name=None) -> None:
        # Vérification si le nom du joueur a été choisis
        if name == None or name == "" :
             # Si nom lui donner un nom aléatoire
            self.name = self.get_randomName()
        else :
            self.name = name

        self.deck = {}
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

    def get_visualDeck(self) :
        '''Permet un affichage type tableau de toutes les cartes du joueur'''
        print("index :\a informations :")
        for cle, valeur in self.deck.items() :
            if valeur[0][1] != None : # Evite de print la valeur de la couleur de la carte c'est une "None"
                print(cle, "\a\t=", valeur[0][0], valeur[0][1])
            else :
                print(cle, "\a\t=", valeur[0][0])

    def get_randomName(self) :
        '''Ajoute un nom à un joueur qui n'en a pas'''
        randomNameH = ["Adrien", "Benjamin", "Clovid", "David", "Esteban", "François", "Grégoire", "Jaque", "Richard"]
        randomNameF = ["Aline", "Céline", "Elsa", "Fadoua"]
        randomNames = randomNameH + randomNameF
        random = randomNames[randint(0, len(randomNames)-1)]
        randomNames[randomNames.index(random)] += "A"
        return random

    def setDeck(self, newDeck, ecrase=False) :
        '''Ajoute une carte au deck, ou écrase le deck par une carte'''
        if ecrase == False :
            self.deck.update(newDeck)
        elif ecrase == True :
            self.deck = newDeck