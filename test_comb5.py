from subjects import Rank,Suit,Card,Comb5

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

rank = Rank.ACE
suit = Suit.DIAMONDS
card3 = Card(
    rank=rank,
    suit=suit)

rank = Rank.KING
suit = Suit.CLUBS
card4 = Card(
    rank=rank,
    suit=suit)

rank = Rank.ACE
suit = Suit.CLUBS
card5 = Card(
    rank=rank,
    suit=suit)

card_set = {card1,card2,card3,card4,card5}
comb5 = Comb5(cards_set=card_set)

print(comb5.str_key)
print(comb5.comb_fig)
print(comb5.pair_rank)

