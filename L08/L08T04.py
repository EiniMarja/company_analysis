# Tehdään ohjelma, joka tulostaa korttipakan kortit halutussa järjetyksessä sekä satunnaisessa järjestyksessä
import random

def create_card(suit: str, value: int) -> tuple[str, int]:
    return (suit, value)
#Luodaan korttipakka
def create_deck() -> list[tuple[str, int]]:
    suits = ["hertta", "ruutu", "risti", "pata"]
    values = list(range(2, 15))  # Korttien arvot 2–14
    deck = []
    for suit in suits:
        for value in values:
            deck.append(create_card(suit, value))
    return deck
#Korttien sekoittaminen
def shuffle_deck(deck: list[tuple[str, int]]) -> list[tuple[str, int]]:
    shuffled = deck.copy()
    random.shuffle(shuffled)
    return shuffled

def format_card(card: tuple[str, int]) -> str:
    suit, value = card
    suit_formatted = suit.capitalize()
    return f"{suit_formatted}, {value}" 

def print_deck(deck: list[tuple[str, int]]) -> None:
    for card in deck:
        print(format_card(card))

def main():
    original_deck = create_deck()
    print("Alkuperäinen pakka:")
    print_deck(original_deck)
    shuffled_deck = shuffle_deck(original_deck)
    print("Sekoitettu pakka:")
    print_deck(shuffled_deck)

if __name__ == "__main__":
    main()

