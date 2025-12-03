import numpy as np
import math
from itertools import combinations
import copy
from subjects.comb7.comb_7_list_wo_suit import do_comb7_with_fl_list, do_comb_7_tuple_list
from subjects.comb5.comb5_simple import Comb5Simple
from subjects import Deck

class Comb7Tools():
    
    def find_best_comb5(comb7_tuple:tuple[list[int], list[int]]) -> dict:
        all_comb7, fl_comb7 = comb7_tuple
        best_nn =-1
        best_name = ''
        best_str_key_5 = ''
        for curr_comb_5 in combinations(all_comb7,5):
            
            comb5 = Comb5Simple( rank_list = curr_comb_5,
                                flush_is = False)
            if comb5.comb_fig['nn'] > best_nn:
                    best_nn = comb5.comb_fig['nn']
                    best_name = comb5.comb_fig['name']
                    best_str_key_5 = comb5.str_key
        
        if fl_comb7 != []:
            for curr_comb_5 in combinations(fl_comb7,5):
                comb5 = Comb5Simple(rank_list = curr_comb_5,flush_is = True)
                if comb5.comb_fig['nn'] > best_nn:
                    best_nn = comb5.comb_fig['nn']
                    best_name = comb5.comb_fig['name']
                    best_str_key_5 = comb5.str_key
        return {
            'best_nn' :best_nn,
            'best_name': best_name,
            'str_key': best_str_key_5
        }             
    
    def do_str_key(comb7_tuple:tuple[list[int], list[int]]) -> str:
        rank_list, flush_list = comb7_tuple
        rank_list_str = ','.join(map(str, sorted(rank_list)))
        flush_str = 'unfl'
        if flush_list != []:
            flush_str = ','.join(map(str, sorted(flush_list)))
        
        return f'{rank_list_str}_{flush_str}'
    
    def count_amount_in_deck(rank_list:list[int],deck: Deck) -> dict[str,int]:
        
        def __count_amount(ranks, freq, deck_ranks_amount) -> int:
            total_amount = 1
            for i,cur_rank in enumerate(ranks):
                total_amount *= math.comb(deck_ranks_amount[cur_rank],freq[i])
            return total_amount     
        def __check_fl(flush_ranks:list[int],suit_nn: int, suits_0_1:list[list[int]] ) -> bool:
            fl_is = True
            for curr_fl_r in flush_ranks:
                if suits_0_1[suit_nn][curr_fl_r] ==0:
                    return False
            return fl_is            
            
        def __correct_r_amount_fl(all_ranks:list[int],suit_nn: int, suits_0_1:list[list[int]], rank_amount: list[int] ) -> list[int]:
            rank_amount_wo_fl_ranks = rank_amount[:]          
            for curr_r in all_ranks:
                if suits_0_1[suit_nn][curr_r] ==1:
                    rank_amount_wo_fl_ranks[curr_r] -=1
            return rank_amount_wo_fl_ranks 
    
        def __do_str_from_correct_lists(ranks:list[int],fl_ranks:list[int]) -> str:
            ranks_2 = list(map(lambda x: x+2,ranks ))
            if fl_ranks !=[]:
                fl_ranks_2 = list(map(lambda x: x+2,fl_ranks))
            else:
                fl_ranks_2=[]
            return Comb7Tools.do_str_key((ranks_2,fl_ranks_2))
        
        def __diff_wo_fl(all_ranks:list[int], fl_ranks:list[int]) -> list[int]:
            if not fl_ranks:
                return all_ranks[:]
            all_ranks_copy = all_ranks
            for curr_rank in fl_ranks:
                all_ranks_copy.remove(curr_rank)
            return all_ranks_copy
                
                
                
        rank_list_np = np.array(rank_list)
        rank_list_np -= 2
        ranks, freq = np.unique(rank_list_np, return_counts=True)
        if ranks.size < 5:
            amount = __count_amount(ranks,freq,deck.rank_amount)
            str_key = __do_str_from_correct_lists(rank_list_np,[]) 
            
            return {str_key:amount }
        
        
        #flush possible
        res_dist = {}
        for flushed_size in range(5,ranks.size+1):
            for cuur_fl_ranks in combinations(ranks,flushed_size):
                curr_amount= 0
                for suit_nn in range(4):
                    if __check_fl(cuur_fl_ranks,suit_nn,deck.suits_0_1):
                        rank_amount = deck.rank_amount[:]
                        rank_amount_corrected = __correct_r_amount_fl(ranks,suit_nn,deck.suits_0_1,rank_amount)
                        diff_list_wo_fl = __diff_wo_fl(list(rank_list_np),list(cuur_fl_ranks))
                        fl_free_ranks, fl_free_freq = np.unique(np.array(diff_list_wo_fl), return_counts= True)
                        curr_amount += __count_amount(fl_free_ranks, fl_free_freq,rank_amount_corrected)
                
                str_key = __do_str_from_correct_lists(rank_list_np,cuur_fl_ranks) 
                res_dist[str_key]  =  curr_amount
                  
                    
                
                
        # empty flush []
        empty_amount= __count_amount(ranks,freq,deck.rank_amount) - sum(res_dist.values())

        str_key = __do_str_from_correct_lists(rank_list_np,[]) 
        res_dist[str_key]  =  empty_amount        
                                
        return res_dist
    
    def do_comb7_str_list()-> list[str]:
        comb7_str_list = []
        combs7 = do_comb7_with_fl_list()
        for rank_tuple in combs7:
            comb7_str_list.append(Comb7Tools.do_str_key(rank_tuple))
        return comb7_str_list
            
        