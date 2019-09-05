from cells import *
from player import Player

class Game:
    def __init__(self):
        self.count_of_players = 3
        self.cell_positions = ['E', 'E', 'J', 'H', 'E', 'T', 'J', 'T', 'E', 'E', 'H', 'J', 'T', 'H', 'E',\
                                    'E', 'J', 'H', 'E', 'T', 'J', 'T', 'E', 'E', 'H', 'J', 'T', 'H', 'J',\
                                    'E', 'E', 'J', 'H', 'E', 'T', 'J', 'T', 'E', 'E', 'H', 'J', 'T', 'E', 'H', 'E']
        self.dice_output = [4, 4, 4, 6, 7, 8, 5, 11, 10, 12, 2, 3, 5, 6, 7, 8, 5, 11, 10, 12, 2, 3, 5, 6, 7, 8, 5, 11, 10, 12, 2, 3, 5, 6, 7, 8, 5, 11, 10, 12]
        self.game()

    def create_obj(self):
        self.players = []
        for i in range(self.count_of_players):
            self.players.append(Player())

        self.hotels = {}
        for num, item in enumerate(self.cell_positions):
            if item == "H":
                self.hotels.update({num: Hotel(num)})

        self.j1 = Jail()
        self.t1 = Treasure()


    def declare_winners(self):
        for player in self.players:
            print(player.remaining_amount)


    def calc_price(self, player, position):
        if position == 'J':
            self.j1.deduct_fine(player)
        elif position == 'T':
            self.t1.give_rewards(player)
        elif position == 'H':
            self.hotels[player.position].check_transaction


    def calc_position(self, player, item):
        player.position +=item
        player.position = player.position % len(self.cell_positions)
        position = self.cell_positions[player.position]
        self.calc_price(player, position)


    def game(self):
        self.create_obj()
        for num, item in enumerate(self.dice_output):
            self.calc_position(self.players[num%3], item)
        self.declare_winners()



game = Game()
