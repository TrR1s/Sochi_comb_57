# from pydantic import BaseModel
from subjects import Deck,DeckTools,CombRanks,CombRanksTool,Rank,Suit,Card,Comb5short,Comb5shortTools,Comb5Dict
deck = DeckTools.do_full_deck()

rank = Rank._9
suit = Suit.CLUBS

card = Card(
    rank=rank,
    suit=suit)
deck.remove_cards([card])

comb5_sh = Comb5shortTools.do_combrank_from_str_key('2,3,4,5,7_unfl')

print(comb5_sh.model_dump_json(indent=2))
print(comb5_sh)

