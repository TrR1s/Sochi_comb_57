import pandas as pd
from utils.comb_king_define import KingCombRanks,def_comb_king
from subjects import CombKingType,Deck,DeckTools,CombRanks,CombRanksTool,Rank,Suit,Card,Comb5short,Comb5shortTools,Comb5Dict
from core.config import CSV_FILES_PATH

# str_key = "8,9,10,11,12_fl"

# print(def_comb_king(str_key))


res_dict = dict((name.value,0) for name in CombKingType )
print(res_dict)
deck = DeckTools.do_full_deck()

for str_key in Comb5Dict.comb5_dict.keys():
    comb5_sh = Comb5shortTools.do_combrank_from_str_key(str_key)
    curr_amount = comb5_sh.count_amount_in_deck(deck)
    res_dict[def_comb_king(str_key)] += curr_amount
# print(res_dict)


df = pd.DataFrame(res_dict.items(),columns=['comb_name','amount'])
file_name='comb_kkk_fig.csv'
df.to_csv(f'{CSV_FILES_PATH}/{file_name}',index=False)
print(df)
