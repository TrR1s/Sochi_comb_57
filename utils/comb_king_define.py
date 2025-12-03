from enum import Enum
from subjects import CombKingType,CombRanks,CombRanksTool,Rank, CombType,RankTools,Comb5shortTools,Comb5short
class KingCombRanks():
    k_ind_str = str(RankTools.rank_to_ind(Rank.KING)+2)
    k = CombRanksTool.do_combrank_from_str_rank_key(k_ind_str)
    kk = CombRanksTool.do_combrank_from_str_rank_key(f'{k_ind_str},{k_ind_str}')
    kkk = CombRanksTool.do_combrank_from_str_rank_key(f'{k_ind_str},{k_ind_str},{k_ind_str}')
    kkkk = CombRanksTool.do_combrank_from_str_rank_key(f'{k_ind_str},{k_ind_str},{k_ind_str},{k_ind_str}')



def def_comb_king(str_key:str) -> CombKingType:
    comb5_short = Comb5shortTools.do_combrank_from_str_key(str_key)
    match comb5_short.comb_name:
        case  CombType.STRAIGHT_FLUSH.value: 
            if CombRanksTool.small_combrank_in_big(KingCombRanks.k,comb5_short.comb_rank):
                return CombKingType.STRAIGHT_FLUSH_K
            return CombKingType.STRAIGHT_FLUSH
        
        case  CombType.FOUR_OF_KIND.value: 
            if CombRanksTool.small_combrank_in_big(KingCombRanks.kkkk,comb5_short.comb_rank):
                return CombKingType.FOUR_OF_KIND_KKKK
            return CombKingType.FOUR_OF_KIND
        
        case  CombType.FULL_HOUSE.value: 
            if CombRanksTool.small_combrank_in_big(KingCombRanks.kkk,comb5_short.comb_rank):
                return CombKingType.FULL_HOUSE_KKK
            if CombRanksTool.small_combrank_in_big(KingCombRanks.kk,comb5_short.comb_rank):
                return CombKingType.FULL_HOUSE_KK
            return CombKingType.FULL_HOUSE
        
        case  CombType.FLUSH.value: 
            if CombRanksTool.small_combrank_in_big(KingCombRanks.k,comb5_short.comb_rank):
                return CombKingType.FLUSH_K
            return CombKingType.FLUSH
        
        case  CombType.STRAIGHT.value: 
            if CombRanksTool.small_combrank_in_big(KingCombRanks.k,comb5_short.comb_rank):
                return CombKingType.STRAIGHT_K
            return CombKingType.STRAIGHT
        
        case  CombType.THREE_OF_KIND.value: 
            if CombRanksTool.small_combrank_in_big(KingCombRanks.kkk,comb5_short.comb_rank):
                return CombKingType.THREE_OF_KIND_KKK
            return CombKingType.THREE_OF_KIND
        
        case  CombType.TWO_PAIRS.value: 
            if CombRanksTool.small_combrank_in_big(KingCombRanks.kk,comb5_short.comb_rank):
                return CombKingType.TWO_PAIRS_KK
            return CombKingType.TWO_PAIRS
        
        case  CombType.ONE_PAIR.value: 
            if CombRanksTool.small_combrank_in_big(KingCombRanks.kk,comb5_short.comb_rank):
                return CombKingType.ONE_PAIR_KK
            return CombKingType.ONE_PAIR
             
        case  _ : return CombKingType(comb5_short.comb_name)