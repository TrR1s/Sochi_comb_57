from subjects import Deck,DeckTools,CombRanks,CombRanksTool,Rank,Suit,Card

deck = DeckTools.do_full_deck()

rank = Rank._9
suit = Suit.CLUBS

card = Card(
    rank=rank,
    suit=suit)
deck.remove_cards([card])
str_key = "3,8,9,14"

comb_rank = CombRanksTool.do_combrank_from_str_rank_key(str_key)
amount_comb,suit_am = comb_rank.count_amount_in_deck(deck)
print(amount_comb, suit_am)