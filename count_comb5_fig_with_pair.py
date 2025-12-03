from itertools import combinations
from subjects import CombType,Deck,DeckTools,Comb5
import pandas as pd
from core.config import CSV_FILES_PATH

res_dict = dict((name.value,0) for name in CombType )
print(res_dict)
deck = DeckTools.do_full_deck()


for curr_set_5 in combinations(deck.cards_set,5):
    
    curr_comb5 = Comb5(cards_set =curr_set_5)
    comb_name = curr_comb5.comb_fig['name']
    
    if comb_name == CombType.ONE_PAIR.value:
       comb_name = f'{comb_name}_{curr_comb5.pair_rank}{curr_comb5.pair_rank}' 
       
    if comb_name not in res_dict:
        res_dict[comb_name] = 1 
    else:
        res_dict[comb_name] +=1
print(res_dict)

df = pd.DataFrame(res_dict.items(),columns=['comb_name','amount'])
file_name='comb5_fig_with_pairs.csv'
df.to_csv(f'{CSV_FILES_PATH}/{file_name}',index=False)
print(df)