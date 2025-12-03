from subjects import Rank,Suit,Card,Comb5, Comb6

rank = Rank._10
suit = Suit.CLUBS
card1 = Card(
    rank=rank,
    suit=suit)

rank = Rank.JACK
suit = Suit.CLUBS
card2 = Card(
    rank=rank,
    suit=suit)

rank = Rank.QUEEN
suit = Suit.CLUBS
card3 = Card(
    rank=rank,
    suit=suit)

rank = Rank.KING
suit = Suit.DIAMONDS
card4 = Card(
    rank=rank,
    suit=suit)

rank = Rank.ACE
suit = Suit.CLUBS
card5 = Card(
    rank=rank,
    suit=suit)

rank = Rank.ACE
suit = Suit.DIAMONDS
card6 = Card(
    rank=rank,
    suit=suit)

card_set = {card1,card2,card3,card4,card5,card6}
comb6 = Comb6(card_set)
best_comb5 = comb6.best_comb5()
print(best_comb5.str_key)
print(best_comb5.comb_fig)


