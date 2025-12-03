from itertools import combinations
from subjects import CombType,Deck,DeckTools,Comb5,Comb6
import pandas as pd
from core.config import CSV_FILES_PATH

res_dict = dict((name.value,0) for name in CombType )
print(res_dict)
deck = DeckTools.do_full_deck()


for curr_set_6 in combinations(deck.cards_set,6):
    best_comb5 = Comb6(curr_set_6).best_comb5()
    comb_name = best_comb5.comb_fig['name']
    res_dict[comb_name] +=1
print(res_dict)

df = pd.DataFrame(res_dict.items(),columns=['comb_name','amount'])
file_name='comb6_fig.csv'
df.to_csv(f'{CSV_FILES_PATH}/{file_name}',index=False)
print(df)