# from pydantic import BaseModel
from subjects import Deck,DeckTools,CombRanks,CombRanksTool,Rank,Suit,Card,Comb5short,Comb5shortTools,Comb5Dict
import json

deck = DeckTools.do_full_deck()

comb5_list = []
for str_key in Comb5Dict.comb5_dict.keys():
    comb5_list.append(Comb5shortTools.do_combrank_from_str_key(str_key))
    

total_amount = 0

for curr_comb5 in comb5_list:
    total_amount += curr_comb5.count_amount_in_deck(deck)
    
print(total_amount)
print(comb5_list[0])