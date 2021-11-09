class Player:
    """
    Class representing the players drafing

    Houses the current pool of cards, and
    the api for selecting a card from a given pack
    """
    
    def make_pick(self, pack):
        """
        API for making a pick from a given pack
        
        Params: pack - a list of indices indexing the list of cards
        Type: pack - list of ints

        Returns: Integer representing the index of the picked card
        within the pack
        
        """
        pass    
    def add_to_pool(self, card):
        pass

class BasicPlayer(Player):
   
    def __init__(self):
        self.pool = []

    def make_pick(self, pack):
        """
        API for making a pick from a given pack
        
        Params: pack - a list of indices indexing the list of cards
        Type: pack - list of ints

        Returns: Integer representing the index of the picked card
        within the pack
        
        """
        return 0

    def add_to_pool(self, card):
        self.pool.append(card)