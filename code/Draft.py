from player import BasicPlayer

class Draft:
    """
    Main class operating the draft simulation.
    Maintains Player ordering, Moves Packs around
    """
    def __init__(self):
        self.players = [BasicPlayer() for i in range(8)]
        self.packs = None
        

    def simulate_round(self, direction):
        '''
        simulates a full round of picks for every player at the table

        Params: direction - if the pack is going to the left or right
        Type: direction - int (-1 or 1)

        Returns: None - modifies self.players in place updating the pools
        with the corresponding picks
        '''

        for i in range(len(self.players)):
            curr_pack = self.packs[i]
            curr_player = self.players[i]
            pick_ind = curr_player.make_pick(curr_pack)

            pick_card = curr_pack.pop(pick_ind)
            curr_player.add_to_pool(pick_card)

        self.packs = [self.packs[(i - direction) % len(self.packs)] for i in range(len(self.packs))]

    def simulate_draft(self):
        direction = 1
        for _ in range(3):
            self.packs = [Pack() for i in range(8)]

            for _ in range(13):
                self.simulate_round(direction)

            direction *= -1
        



            
        

