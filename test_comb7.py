import pandas as pd
from subjects import Comb7Tools,do_comb7_with_fl_list,do_comb_7_tuple_list
from subjects import Deck,DeckTools
deck = DeckTools.do_full_deck()

comb7_tuple = ([8,9,10,11,14,2,11], [])
# comb7_tuple = ([10, 10, 10, 11, 12, 13, 14], [10, 11, 12, 13, 14])  
print(Comb7Tools.find_best_comb5(comb7_tuple))
print(Comb7Tools.do_str_key(comb7_tuple))

dict_am = Comb7Tools.count_amount_in_deck([8,9,10,7,14,2,11],deck)
print(f'{dict_am=}')
print(f'{sum(dict_am.values())=}')

comb7_str_list = Comb7Tools.do_comb7_str_list()
comb7_str_dict= {comb7_str: 0 for comb7_str in comb7_str_list}
print((comb7_str_dict))
combs_7_rank_only = do_comb_7_tuple_list()
for curr_main_comb7 in combs_7_rank_only:
    curr_amount_dict  = Comb7Tools.count_amount_in_deck(curr_main_comb7,deck)
    for str_key, amount in curr_amount_dict.items():
        comb7_str_dict[str_key] += amount


print(sum(comb7_str_dict.values()))
comb7_df = pd.DataFrame(comb7_str_dict.items(), columns=['comb7_str', 'amount'])
comb7_df.to_csv('comb7_df.csv')