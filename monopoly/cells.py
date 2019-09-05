
class Treasure:
    def __init__(self):
        self.award = 200

    def give_rewards(self, player):
        player.add_money(self.award)


class Jail:
    def __init__(self):
        self.fine = 200

    def deduct_fine(self, player):
        player.deduct_money(self.fine)


class Hotel:
    def __init__(self, position):
        self.rent = 50
        self.price = 200
        self.owner = None
        self.position = position

    def purchase_hotel(self, player):
        player.deduct_money(self.price)
        player.no_of_hotel +=1
        self.owner = player

    def pay_rent(self, player):
        player.deduct_money(self.rent)
        self.owner.add_money(self.rent)

    def check_transaction(self, player):
        if self.owner:
            self.pay_rent(player)
        else:
            self.purchase_hotel(player)

