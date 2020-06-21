import random

class PokerDeck(object):
    def __init__(self, poker_numbers=13, suits=4):
        self.cards = [ num+1 for num in range(poker_numbers) for suit in range(suits) ]
        self.drawn = []

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self, n=1):
        this_draw = []
        for _ in range(n):
            this_draw.append(self.cards.pop())
        self.drawn.extend(this_draw)
        return this_draw

    def reset(self, shuffle=True):
        self.cards.extend(self.drawn[::-1])
        self.drawn = []
        if shuffle:
            self.shuffle()

if __name__ == '__main__':
    deck = PokerDeck()
    print(deck.cards)
    deck.shuffle()
    print(deck.cards)

    print(deck.draw())
    print(deck.cards)

    print(deck.draw(n=5))
    print(deck.cards)

    print(deck.reset(shuffle=False))
    print(deck.cards)

