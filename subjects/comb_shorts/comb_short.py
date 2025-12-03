from pydantic import BaseModel, computed_field,field_validator,Field
import numpy as np
import math
from subjects import Deck,RankTools

class CombRanks(BaseModel):
    rank_dict: dict[str,int] # {rank: amount_rank}
    
    @computed_field
    def str_rank_key(self) -> str:
        rank_list = []
        for rank, amount in self.rank_dict.items():
            rank_list.extend([int(rank) for _ in range(amount)])
        return ','.join(map(str, sorted(rank_list)))

    def count_amount_in_deck(self,deck: Deck) -> tuple[int,list[int]]:
        total_amount = 1
        suit_am = [0,0,0,0]
        for curr_rank_str, amount in self.rank_dict.items():
            rank_ind = int(curr_rank_str)-2
            total_amount *= math.comb(deck.rank_amount[rank_ind],amount)
        if max(self.rank_dict.values()) <= 1:
            for curr_suit in range(4):
                curr_suit_am = 1
                for curr_rank_str in self.rank_dict.keys():
                    rank_ind = int(curr_rank_str)-2
                    curr_suit_am *= deck.suits_0_1[curr_suit][rank_ind]
                suit_am[curr_suit] = curr_suit_am
            
        return total_amount, suit_am


class CombRanksTool():
    
    def do_combrank_from_str_key(str_key: str) -> CombRanks:
        str_key_split = str_key.split('_')
        ranks_str = str_key_split[0].split(',')
        ranks = np.array(ranks_str)
        unique_elements, counts = np.unique(ranks, return_counts=True)
        rank_dict = dict(zip(unique_elements,counts))
        return CombRanks(
            rank_dict = rank_dict,
        )
        
    def do_combrank_from_str_rank_key( str_rank_key: str) -> CombRanks:
        ranks_str = str_rank_key.split(',')
        ranks = np.array(ranks_str)
        unique_elements, counts = np.unique(ranks, return_counts=True)
        rank_dict = dict(zip(unique_elements,counts))
        return CombRanks(
            rank_dict = rank_dict,
        )
        
    # def do_combrank_from_list_rank( list_rank: str) -> CombRanks:
    #     ranks = np.array(list_rank)
    #     unique_elements, counts = np.unique(ranks, return_counts=True)
    #     rank_dict = dict(zip(unique_elements,counts))
    #     return CombRanks(
    #         rank_dict = rank_dict,
    #     )
    
    def small_combrank_in_big(small_cr: CombRanks,big_small: CombRanks ) -> bool:
        for small_r, small_am_r in small_cr.rank_dict.items():
            if small_r not in big_small.rank_dict:
                return False
            if big_small.rank_dict[small_r] < small_am_r:
                return False
        return True
    


if __name__ =="__main__":
    str_key = "3,8,9,9,14"
    
    comb5_sh = CombRanksTool.do_combrank_from_str_rank_key(str_key)
    print(comb5_sh)
    str_key_small = "9,9,7"
    comb5_sh_small = CombRanksTool.do_combrank_from_str_rank_key(str_key_small)
    print(comb5_sh_small)
    print(CombRanksTool.small_combrank_in_big(comb5_sh_small,comb5_sh))
    # ranks_str = str_key.split('_')[0].split(',')
    # ranks = np.array(list(map(lambda x: int(x),ranks_str)))
    # unique_elements, counts = np.unique(ranks, return_counts=True)
    # # print(ranks_str.split(',').map(lambda x: int(x)))
    # print( unique_elements, counts)
    # res_dict = dict(zip(unique_elements,counts))
    # print(res_dict)