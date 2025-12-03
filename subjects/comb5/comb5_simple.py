from pydantic import BaseModel, computed_field,field_validator,Field
import numpy as np
from utils.read_json5 import read_json

class Comb5Dict():
    comb5_dict = read_json()


class Comb5Simple(BaseModel):
    rank_list: list[int]
    flush_is: bool
    
    
    @field_validator('rank_list')
    def check_card_amount(cls, value):
        if len(value) != 5:
            raise ValueError('Card amount must be 5')
        return value
    
    
    @computed_field
    def str_key(self) -> str:
        rank_list = sorted(self.rank_list)
        flush = 'fl' if self.flush_is else 'unfl'
        return ','.join(map(str, sorted(rank_list))) + '_' + flush
    
    @computed_field
    def comb_fig(self) -> dict[str,int]:
        name, nn = Comb5Dict.comb5_dict[self.str_key]
        return {'name':name, 
                'nn':nn
                }
    
    
    # @computed_field
    # def pair_rank(self)-> Rank|None:
    #     if self.comb_fig['name'] != CombType.ONE_PAIR.value:
    #         return None
    #     rank_np = np.array([RankTools.rank_to_ind(card.rank) for card in self.cards_set],dtype= int )   
    #     res, counts = np.unique(rank_np, return_counts=True)
    #     for i, freq in enumerate(counts):
    #         if freq == 2:
    #             return RankTools.ind_to_rank(res[i]).value
        
    #     raise ValueError('didnt find pair in pair')