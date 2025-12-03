from pydantic import BaseModel, computed_field,model_validator,Field
from enum import StrEnum
import numpy as np

class Rank(StrEnum):
    ACE = 'A',
    KING = 'K',
    QUEEN = 'Q',
    JACK = 'J',
    _10 = '10',
    _9 = '9',
    _8 = '8',
    _7 = '7',
    _6 = '6',
    _5 = '5',
    _4 = '4',
    _3 = '3',
    _2 = '2',

class RankTools():
    # @staticmethod
    def rank_to_ind(rank:Rank)->int:
        match rank:
            case  Rank._2: return 0   
            case  Rank._3: return 1   
            case  Rank._4: return 2   
            case  Rank._5: return 3   
            case  Rank._6: return 4   
            case  Rank._7: return 5   
            case  Rank._8: return 6   
            case  Rank._9: return 7   
            case  Rank._10: return 8   
            case  Rank.JACK: return 9   
            case  Rank.QUEEN: return 10   
            case  Rank.KING: return 11   
            case  Rank.ACE: return 12  
    
    def ind_to_rank(rank:Rank)->int:
        match rank:
            case  0: return Rank._2   
            case  1: return Rank._3   
            case  2: return Rank._4   
            case  3: return Rank._5   
            case  4: return Rank._6   
            case  5: return Rank._7   
            case  6: return Rank._8   
            case  7: return Rank._9   
            case  8: return Rank._10   
            case  9: return Rank.JACK   
            case  10: return Rank.QUEEN   
            case  11: return Rank.KING   
            case  12: return Rank.ACE  

class Suit(StrEnum):
    HEARTS = 'h',
    CLUBS = 'c',
    DIAMONDS = 'd',
    SPADES = 's',

class SuitTools():
    def suit_to_ind(suit:Suit)->int:
        match suit:
            case  Suit.HEARTS: return 0   
            case  Suit.CLUBS: return 1   
            case  Suit.DIAMONDS: return 2   
            case  Suit.SPADES: return 3   
        

class Card(BaseModel):
    rank: Rank  
    suit: Suit
    
    @computed_field
    def short_name(self) -> str:
        return f'{self.rank}{self.suit}'
    
    def __hash__(self):
        return hash(self.short_name)
    
    
class Deck(BaseModel):
    cards_set: set[Card]
    
    @computed_field
    def short_view(self) -> dict[Suit,list[str]]:
        deck_view = {
            Suit.HEARTS:[],
            Suit.CLUBS:[],
            Suit.DIAMONDS:[],
            Suit.SPADES:[],
        }
        for curr_card in self.cards_set:
            deck_view[curr_card.suit].append(curr_card.short_name)
        return deck_view
    
    
    
    @computed_field 
    def rank_amount(self)-> list[int]:
        rank_amount = [0 for _ in range(13)]
        for curr_card in self.cards_set:
            rank_amount[RankTools.rank_to_ind(curr_card.rank)] +=1
        return rank_amount
    
    @computed_field 
    def suits_0_1(self)-> list[list[int]]:
        suit_0_1 = [[0 for _ in range(13)] for _ in range(4)]
        for curr_card in self.cards_set:
            suit_0_1[SuitTools.suit_to_ind(curr_card.suit)][RankTools.rank_to_ind(curr_card.rank)] =1
        return suit_0_1
         
    def remove_cards(self, card_list:list[Card]):
        self.cards_set -= set(card_list)
        
    def add_cards(self, card_list:list[Card]):
        self.cards_set |= set(card_list)
        

class DeckTools():
    
    def do_full_deck() -> Deck:
        cards_set = set()
        for curr_s in Suit:
            for curr_r in Rank:
                card = Card(
                            rank=curr_r,
                            suit=curr_s)
                cards_set.add(card) 
        return Deck(cards_set=cards_set)
    

        
if __name__ == "__main__":
    rank = Rank._10
    suit = Suit.CLUBS
    print( RankTools.rank_to_ind('2'))
    
    card = Card(
        rank=rank,
        suit=suit)
    print(card)
    full_deck = DeckTools.do_full_deck()
    remove_list = [card]
    full_deck.remove_cards([card])        
    print(full_deck.short_view)
    # full_deck.add_cards([card])        
    # print(full_deck.short_view)
    print(full_deck.suits_0_1)
    
    