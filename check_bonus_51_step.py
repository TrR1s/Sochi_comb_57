import numpy as np
from itertools import combinations
from subjects import CombType,Deck,DeckTools,Comb6,BONUS_5_1_STEP

res_dict = dict((name.value,0) for name in CombType )
print(res_dict)
deck = DeckTools.do_full_deck()

deck_list = list(deck.cards_set)
bonus_res =  0
max_res =  0
min_res =  0
import pandas as pd
from core.config import CSV_FILES_PATH

for i in range(10_000_000):
    dealing_cards = np.random.choice(deck_list,6,replace = False)
    # print(f'{list(map(lambda card: card.short_name,dealing_cards))}')
    best_comb5 = Comb6(dealing_cards).best_comb5()
    # print(f'{best_comb5.str_key=}')
    comb_name = best_comb5.comb_fig['name']
    res_dict[comb_name] +=1
    bonus_res +=BONUS_5_1_STEP[comb_name]
    max_res = bonus_res if bonus_res> max_res else max_res
    min_res = bonus_res if bonus_res < min_res else min_res
    if i % 100_000 == 0 and i != 0 :
        print(f'{i=}') 
        print(f'{bonus_res= }, {max_res=}, {min_res= }')
        print(f'bonus_ev = {bonus_res/i }')
    
    # print(f'***************************')


df = pd.DataFrame(res_dict.items(),columns=['comb_name','amount'])
file_name='comb6_fig_gen.csv'
df.to_csv(f'{CSV_FILES_PATH}/{file_name}',index=False)
print(df)

