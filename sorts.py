
def bubble_sort(in_list, reversed=False):
    out_list = in_list.copy()
    run_to = len(in_list) - 1

    if reversed:
        comparator = lambda a,b: a < b 
    else:
        comparator = lambda a,b: a > b 

    while run_to > 1:
        for j in range(run_to):
            a = out_list[j]
            b = out_list[j+1]

            if comparator(a,b):
                out_list[j] = b
                out_list[j+1] = a
        
        run_to -= 1

    return out_list

if __name__ == '__main__':
    from deck import PokerDeck
    deck = PokerDeck()
    deck.shuffle()
    hand = deck.draw(n=13)
    sorted_hand = bubble_sort(hand, reversed=True)

    print('initial hand ', hand)    

    print('sorted hand', sorted_hand)