
from tarot_logic import TarotDeck
from data_loader import load_tarot_dict


def main():
    data = load_tarot_dict()
    deck = TarotDeck(data)

    print("Welcome to the Tarot Reading App!")
    input("Press Enter to draw a card...")

    card_name, card_info = deck.draw_card()
    interpretation = deck.interpret_card((card_name, card_info))

    print(f"\nYou drew: {card_name}")
    print(f"Interpretation: {interpretation}")


if __name__ == "__main__":
    main()
