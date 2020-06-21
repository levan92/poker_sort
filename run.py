import time

from deck import PokerDeck
from hand import Hand

deck = PokerDeck()
deck.shuffle()

hand = Hand(init_draw=deck.draw(n=13), sort_algo='bubble')
print('initial hand ', hand)    

reps = 10000
dur = 0
for _ in range(reps):
    tic = time.perf_counter()
    hand.arrange()
    toc = time.perf_counter()
    dur += toc - tic
    hand.mix()

hand.arrange()
print('sorted hand', hand)
print('avrg time in {} reps: {:0.3e}s'.format(reps, dur/reps))