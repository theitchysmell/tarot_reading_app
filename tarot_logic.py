import random

class TarotDeck:
    def __init__(self, data):
        self.data = data

    def draw_card(self):
        card_name = random.choice(list(self.data.keys()))
        return card_name, self.data[card_name]

    def interpret_card(self, card):
        return f"{card[0]}: {card[1][1]}"
