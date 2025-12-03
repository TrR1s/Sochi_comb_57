from pydantic import BaseModel, computed_field,field_validator,Field
import numpy as np
from subjects.comb5.comb5 import Comb5Dict
from subjects.comb_shorts import CombRanks,CombRanksTool
from subjects import Deck,Card,Suit,RankTools,SuitTools

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
        
class FixCards(BaseModel):
    cards_set: set[Card]|None= Field(default=None)
    
    @field_validator('cards_set')
    def check_card_amount(cls, value):
        if len(value) > 5:
            raise ValueError('Card amount must be 5 or less')
        return value
    
    @computed_field
    def suit(self)-> Suit|None:
        if self.cards_set is None or len(self.cards_set) ==0:
            return None
        suit_list = [card.suit for card in self.cards_set]
        if len(set(suit_list)) ==1:
            return suit_list[0]
        return None
    
    @computed_field
    def rank_list(self)-> list[int]|None:
        if self.cards_set is None or len(self.cards_set) ==0:
            return None
        rank_list = [card.rank for card in self.cards_set]
        return rank_list
    

    
    @computed_field
    def str_key(self) -> str|None:
        if self.cards_set is None or len(self.cards_set) ==0:
            return None
        rank_list = [RankTools.rank_to_ind(card.rank)+2 for card in self.cards_set]
        flush = 'fl' if self.suit is not None else 'unfl'
        return ','.join(map(str, sorted(rank_list))) + '_' + flush
    
    
    
    def count_amount_in_deck(self,comb_str_key: str,deck: Deck) -> int:
        if self.cards_set is None or len(self.cards_set) ==0:
            comb_5_short:Comb5short = Comb5shortTools.do_combrank_from_str_key(comb_str_key)
            return comb_5_short.count_amount_in_deck(deck)
        
        else:
            comb_5_short:Comb5short = Comb5shortTools.do_combrank_from_str_key(comb_str_key)
            fix_combrank:CombRanks= CombRanksTool.do_combrank_from_str_key(self.str_key)
            if not CombRanksTool.small_combrank_in_big(fix_combrank,comb_5_short.comb_rank):
                return 0
            

            rest_combrank_dict:CombRanks = CombRanksTool.rest_small_combrank_in_big(fix_combrank,comb_5_short.comb_rank)
            
            if rest_combrank_dict is None:
                if comb_5_short.flush_is and (self.suit is not None):
                    return 1
                if (not comb_5_short.flush_is) and (self.suit is None):
                    return 1
                return 0
            total_amount, suit_am =   rest_combrank_dict.count_amount_in_deck(deck)
            if comb_5_short.flush_is:   
                if self.suit is not None:
                    suit_ind = SuitTools.suit_to_ind(self.suit)
                    return suit_am[suit_ind]
                else:
                    return 0
            else:
                if self.suit is not None:
                    suit_ind = SuitTools.suit_to_ind(self.suit)
                    return total_amount -  suit_am[suit_ind]      
                else:
                    return total_amount

    
    