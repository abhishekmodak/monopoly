
class Player:
    def __init__(self):
        self.remaining_amount = 1000
        self.no_of_hotel = 0
        self.position = 0

    def calc_money_remaining(self):
        self.total_money = self.remaining_amount + 200*no_of_hotel

    def deduct_money(self, amount):
        self.remaining_amount -= amount

    def add_money(self, amount):
        self.remaining_amount += amount