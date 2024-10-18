import random

shapes = ["Club", "Heart", "Diamond", "Spade"]
cards = ["A", "J", "K", "Q"] + [str(i) for i in range(2, 11)]
deck = []

def shuffle_cards(deck):
    for shape in shapes:
        for card in cards:
            deck.append(f"{card} {shape}")  
    random.shuffle(deck)
    return deck

shuffled_deck = shuffle_cards(deck)
print(shuffled_deck)
