from pydantic import BaseModel, computed_field,field_validator,Field
import numpy as np
from subjects.comb5.comb5 import Comb5Dict
from subjects.comb_shorts import CombRanks
from subjects import Deck

class Comb5short(BaseModel):
    comb_rank: CombRanks
    flush_is: bool
    
    @computed_field
    def str_key(self) -> str:
        fl_str = 'fl' if self.flush_is else 'unfl'
        return f"{self.comb_rank.str_rank_key}_{fl_str}"  
        
    @computed_field
    def comb_name(self) -> str:
        name, _ = Comb5Dict.comb5_dict[self.str_key]
        return name
    
    @computed_field
    def comb_nn(self) -> str:
        _,comb_nn = Comb5Dict.comb5_dict[self.str_key]
        return comb_nn    
        
    def count_amount_in_deck(self,deck: Deck) -> int|list[int]:
        total_amount, suit_am = self.comb_rank.count_amount_in_deck(deck)
        if self.flush_is:
            return sum(suit_am)
        else:
            return total_amount - sum(suit_am)
        
class Comb5shortTools():
    
    def do_combrank_from_str_key(str_key: str) -> Comb5short:
        str_key_split = str_key.split('_')
        ranks_str = str_key_split[0].split(',')
        ranks = np.array(ranks_str)
        unique_elements, counts = np.unique(ranks, return_counts=True)
        rank_dict = dict(zip(unique_elements,counts))
        comb_rank = CombRanks(rank_dict = rank_dict)
        flush_is = True if str_key_split[1] == 'fl' else False
        return Comb5short(
            comb_rank= comb_rank,
            flush_is = flush_is,
        )