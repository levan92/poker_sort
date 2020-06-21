import random 

from sorts import bubble_sort

class Hand(object):
    def __init__(self, init_draw = [], sort_algo='bubble'):
        self.cards = init_draw

        if sort_algo == 'bubble':
            self.sort = bubble_sort
        else:
            raise Exception('Sort algo {} not implemented yet'.format(sort_algo))

    def __repr__(self,):
        return ','.join( [ str(c) for c in self.cards ] )

    def draw(self, drawn_cards):
        self.cards.extend(drawn_cards)

    def mix(self):
        random.shuffle(self.cards)

    def arrange(self, reversed=False):
        self.cards = self.sort(self.cards, reversed=reversed)
