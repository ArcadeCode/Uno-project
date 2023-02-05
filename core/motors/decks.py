from random import randint

class motherClassDeck() :
    '''Deck "mère" contient toutes les cartes du jeu avant le commencement de la partie'''
    
    def __init__(self) -> None :
        self.deck = {}

        ## Code used for make all 108 cards
        def append_toDict(dict_obj, key, value):
        # Made by thispointer.com : https://thispointer.com/python-how-to-add-append-key-value-pairs-in-dictionary-using-dict-update/
        # Check if key exist in dict or not
            if key in dict_obj:
                # Key exist in dict.
                # Check if type of value of key is list or not
                if not isinstance(dict_obj[key], list):
                    # If type is not list then make it list
                    dict_obj[key] = [dict_obj[key]]
                # Append the value in list
                dict_obj[key].append(value)
            else:
                # As key is not in dict,
                # so, add key-value pair
                dict_obj[key] = value

        ## Creating 108 cards of the Uno game in self.deck
        # All cards have index in key
        # deck[i] = the proprieties of this : card, color, isPair or isImpair*, isSpecial
        # * = In the Uno all cards is in couple of 2 or 4 cards so you see A/B or A/B/C/D in the code for storage the differencie
        def init_deck() :
            i = 0
            for color in ["red", "blue", "yellow", "green"] :
                for nb in range(0, 10) : # Tout les chiffres de cette couleur
                    self.deck[i] = nb, color, "A", "number"
                    i += 1
                    # Il n'existe pas de pair de 0 par couleur, ainsi il n'y en a que 4 dans un jeu complet
                    # Nous vérifion avant de créer le second de la pair si la carte est un 0 :
                    if nb != 0 :
                        self.deck[i] = nb, color, "B", "number"
                        i += 1
                for specialPer2 in ["+2", "reverse", "skip"] : # Toutes les cartes spéciales de cette couleurs
                    self.deck[i] = specialPer2, color, "A", "specialPer2"
                    self.deck[i+1] = specialPer2, color, "B", "specialPer2"
                    i += 2
            color = None
            for specialPer4 in ["+4", "Joker"] : # Toutes les cartes spéciales en plus
                self.deck[i] = specialPer4, color, "A", "specialPer4"
                self.deck[i+1] = specialPer4, color, "B", "specialPer4"
                self.deck[i+2] = specialPer4, color, "C", "specialPer4"
                self.deck[i+3] = specialPer4, color, "D", "specialPer4"
                i += 4
        
        ## # Attribution des points pour chaque carte
        def init_deck_scorePoint() :
            for key, value in self.deck.items() :
                if value[3] == "number" : # Nombre sur la carte = pts
                    append_toDict(self.deck, key, value[0])
                elif value[3] == "specialPer2" : # +2, reverse, skip = +20 pts
                    append_toDict(self.deck, key, 20)
                elif value[3] == "specialPer4" : # +4, joker = +50 pts
                    append_toDict(self.deck, key, 50)

        init_deck() # Créer 108 cartes
        init_deck_scorePoint() # Attribution des points pour chaque carte

    def get_deck(self) :
        return self.deck

    def give_cards(self, nb=1) :
        '''Supprime une/plusieurs cartes du deck et les renvoit'''
        random = []
        for _ in range(nb) :
            random.append(self.deck[randint(0, len(self.deck)-1)])
        return random

