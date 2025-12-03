import pandas as pd
from utils.comb_aa_define import def_comb_ace
from subjects import CombAAType,Deck,DeckTools,CombRanks,CombRanksTool,Rank,Suit,Card,Comb5short,Comb5shortTools,Comb5Dict
from core.config import CSV_FILES_PATH




res_dict = dict((name.value,0) for name in CombAAType )
print(res_dict)
deck = DeckTools.do_full_deck()

for str_key in Comb5Dict.comb5_dict.keys():
    comb5_sh = Comb5shortTools.do_combrank_from_str_key(str_key)
    curr_amount = comb5_sh.count_amount_in_deck(deck)
    res_dict[def_comb_ace(str_key)] += curr_amount
# print(res_dict)


df = pd.DataFrame(res_dict.items(),columns=['comb_name','amount'])
file_name='comb_aa_fig.csv'
df.to_csv(f'{CSV_FILES_PATH}/{file_name}',index=False)
print(df)
