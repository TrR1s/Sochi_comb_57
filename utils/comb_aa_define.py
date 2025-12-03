from enum import Enum
from subjects import CombAAType,CombRanks,CombRanksTool,Rank, CombType,RankTools,Comb5shortTools,Comb5short
class AceCombRanks():
    a_ind_str = str(RankTools.rank_to_ind(Rank.ACE)+2)
    a = CombRanksTool.do_combrank_from_str_rank_key(a_ind_str)
    aa = CombRanksTool.do_combrank_from_str_rank_key(f'{a_ind_str},{a_ind_str}')
    aaa = CombRanksTool.do_combrank_from_str_rank_key(f'{a_ind_str},{a_ind_str},{a_ind_str}')
    aaaa = CombRanksTool.do_combrank_from_str_rank_key(f'{a_ind_str},{a_ind_str},{a_ind_str},{a_ind_str}')



def def_comb_ace(str_key:str) -> CombAAType:
    comb5_short = Comb5shortTools.do_combrank_from_str_key(str_key)
    match comb5_short.comb_name:
        
        
        case  CombType.ONE_PAIR.value: 
            if CombRanksTool.small_combrank_in_big(AceCombRanks.aa,comb5_short.comb_rank):
                return CombAAType.ONE_PAIR_AA
            return CombAAType.ONE_PAIR
             
        case  _ : return CombAAType(comb5_short.comb_name)