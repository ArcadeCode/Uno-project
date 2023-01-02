from random import randint

class TurnSystem() :
    def __init__(self) :
        self.isTurn = None
        self.isSkipped = False
        
    def __len__(self):
        ''' Me demande pas Esteban du futur jsp pourquoi j ai besoin d appeler len() comme ça
            Ouais bah finalement juste essaye pas de cap sa marche sans
        '''
        return len(self.list)
    
    def returnValueInIndex(self, players, nb=1, substractive=False) :
        ''' Permet l'ajout de passer au prochain joueur
        de manière sécuriser en passant du dernier de la
        liste au premier type 'roulette' '''
        indexMax = len(players)-1 # Stocke l'index maximun qu'on peut call avant error d'indexage 
        while nb+1 > indexMax : # Technique de la roulette
            nb = nb - indexMax
        return nb+1
    
    def setTurn(self, players) :
        ''' Passe au tour suivant '''
        if self.isTurn == None : # Si c'est le premier tour
            self.isTurn = randint(0, len(players)-1) # Choissir aléatoirement un premier joueur
            print("First turn,", players[self.isTurn], "have been choose")
        
        else : # Si c'est un tour parmi tand d'autres
            self.isTurn = self.returnValueInIndex(players, self.isTurn)
                    
        return f"C'est le tour de {players[self.isTurn]}" ### A changer par juste le player plus tard
    
    def skipTurn(self) : # Skip le tour suivant :
        self.isSkipped = True
    def reverse(self) :
        pass
    
turnSystem = TurnSystem()
for i in range(0, 10) :
    print(turnSystem.setTurn(["Esteban", "Michel", "Jaqueline", "Céléstin", "Micheline", "Jaque"]))
    #if i == 4 :
    #    turnSystem.skipTurn()