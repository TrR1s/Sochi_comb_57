from itertools import combinations
import pandas as pd
import math
from subjects import CombType,Deck,DeckTools,Comb5,Card,Suit,Rank,RankTools
from core.config import CSV_FILES_PATH


RF_RANK_SET = {Rank._10,Rank.JACK, Rank.QUEEN,Rank.KING,Rank.ACE}

STREET_SETS = [set(list(range(i,i+5))) for i in range(12-3)]
def split_card_set_by_flash_and_rank(cards_set:set[Card]) -> list[set[Card]]:
    res_dict = {
        Suit.HEARTS:[],
        Suit.CLUBS:[],
        Suit.DIAMONDS:[],
        Suit.SPADES:[],
                }
    for curr_card in cards_set:
        if RankTools.rank_to_ind(curr_card.rank) < 10-2:
            continue
        
        res_dict[curr_card.suit].append(curr_card.rank)    

    res_list =[]
    for curr_set in res_dict.values():
        if curr_set:
           res_list.append(set(curr_set)) 
    return res_list

def check_draws(cards_set:set[Card]) -> tuple[bool,bool]:
    res_dict = {
        Suit.HEARTS:[],
        Suit.CLUBS:[],
        Suit.DIAMONDS:[],
        Suit.SPADES:[],
                }
    rank_list = []
    for curr_card in cards_set:
        res_dict[curr_card.suit].append(curr_card.rank)
        rank_list.append(RankTools.rank_to_ind(curr_card.rank))
    suit_max = 0
    for curr_suit_set in res_dict.values():
        if len(curr_suit_set) > suit_max:
            suit_max = len(curr_suit_set)
    flash_draw = True if suit_max == 4 else False
    rank_set = set(rank_list)
    if len(rank_set) <=3: return flash_draw, False
    street_draw = False
    for curr_street in STREET_SETS:
        if len(curr_street & rank_set) ==4:
            street_draw = True
            break
    
    return flash_draw, street_draw
    
    
            

def rf_draw_kind(clear_rf_rank_set: set[Rank]) -> int:
    return len(RF_RANK_SET.difference(clear_rf_rank_set)) 
    

PROB_BUY_DRAW ={
    0:float(1),
    1: 1/math.comb(47,1),
    2: 1/math.comb(47,2),
    3: 1/math.comb(47,3),
    4: 1/math.comb(47,4),
}

deck = DeckTools.do_full_deck()

def count_best_draw_for_one_comb5(comb5:Comb5) -> float:
    splitted_rank_sets = split_card_set_by_flash_and_rank(comb5.cards_set)
    if not splitted_rank_sets:
        return 5
    best_draw = 5
    for curr_set in splitted_rank_sets:
        curr_draw_int = rf_draw_kind(curr_set)
        if curr_draw_int < best_draw: 
            best_draw = curr_draw_int
            
    return best_draw

def to_buy_not_to_buy(best_draw:int,comb5:Comb5) -> float:
    match  best_draw:
        case 0: return PROB_BUY_DRAW[0]
        case 1: return PROB_BUY_DRAW[1]
        case 2: 
            if comb5.comb_fig["nn"] < 1277: # 2,2,2,3,4_unfl	THREE_OF_KIND	4995
                flash_draw, street_draw = check_draws(comb5.cards_set)
                if flash_draw or street_draw: return 0
                return PROB_BUY_DRAW[2]
            return 0
        case 3: 
            if comb5.comb_fig["nn"] < 1277: # 2,3,4,4,5_unfl	ONE_PAIR	1717
                                            #2,2,3,4,5_unfl	ONE_PAIR	1277
                                            #2,3,4,7,7_unfl	ONE_PAIR	2377
                flash_draw, street_draw = check_draws(comb5.cards_set)
                if flash_draw or street_draw: return 0

                return PROB_BUY_DRAW[3]
            return 0
        case _: return 0
        

def count_rf_after_buy()-> float:
    prob_res_sum = 0.
    deck = DeckTools.do_full_deck()
    for curr_set_5 in combinations(deck.cards_set,5):
        comb5= Comb5(cards_set=curr_set_5)
        best_draw= count_best_draw_for_one_comb5(comb5)
        curr_prob  =to_buy_not_to_buy(best_draw,comb5)
        # print(f'{type(curr_prob)=}, {curr_prob=}')
        prob_res_sum += curr_prob
    return prob_res_sum/math.comb(52,5)
           

if __name__ == "__main__":
    
    # card_1 = Card(
    #     rank=Rank._10,
    #     suit=Suit.CLUBS)
    
    # card_2 = Card(
    #     rank=Rank.KING,
    #     suit=Suit.HEARTS)
        
    # card_3 = Card(
    #     rank=Rank.QUEEN,
    #     suit=Suit.CLUBS)
    
    # card_4 = Card(
    #     rank=Rank.KING,
    #     suit=Suit.DIAMONDS)
    
    # card_5 = Card(
    #     rank=Rank.ACE,
    #     suit=Suit.CLUBS)
    
    # comb_5 =Comb5(cards_set= {card_1,card_2,card_3,card_4,card_5})
    # # print(f'{comb_5=}')
    # splitted_set =split_card_set_by_flash_and_rank(comb_5.cards_set)
    # print(splitted_set)
    
    # # rf_set = {Rank._10,Rank.JACK, Rank.QUEEN,Rank.KING,Rank.ACE}
    # for curr_set in splitted_set:
    #     # z = rf_set.difference(curr_set) 
    #     # print(f'{z=}, {len(z)=}')
    #     print(rf_draw_kind(curr_set))
    # print(PROB_BUY_DRAW)
    # best_draw= count_best_draw_for_one_comb5(comb_5)
    # print(to_buy_not_to_buy(best_draw,comb_5))
    # print(check_draws(comb_5.cards_set))
    
    # print(STREET_SETS)
    
    # curr_r_set =  {2, 3, 4, 10, 5}
    
    # for curr_street in STREET_SETS:
    #     print(curr_street & curr_r_set)
    
    prob_fr = count_rf_after_buy()
    print(f'{prob_fr=}')
    print(f'amount  = {1/prob_fr}')