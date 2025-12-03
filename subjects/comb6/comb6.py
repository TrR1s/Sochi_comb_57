from itertools import combinations
from utils.read_json5 import read_json
from subjects import Card,Comb5

class Comb6():
    def __init__(self,card_set:set[Card]):
        if len(card_set) != 6:
            raise ValueError('Card amount must be 6') 
        self.card_set = card_set
    
    def best_comb5(self) -> Comb5:
        comb5_list =[]
        for curr_comb5_set in combinations(self.card_set,5):
            comb5_list.append(Comb5(cards_set=curr_comb5_set))
        best_ind =0
        for index, comb5 in enumerate(comb5_list):
            if comb5_list[best_ind].comb_fig['nn'] < comb5.comb_fig['nn']:
                best_ind = index
        return comb5_list[best_ind]

            