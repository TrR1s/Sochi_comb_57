from itertools import combinations
from subjects import CombType,Deck,DeckTools,Comb5,FixCards
import pandas as pd
from core.config import CSV_FILES_PATH
deck = DeckTools.do_full_deck()
set_3 = deck.deal_rnd_cards(2)
fix_card = FixCards(cards_set = set(set_3))
print(fix_card.str_key)
str_comb = "2,3,4,5,7_unfl"
amount = fix_card.count_amount_in_deck(str_comb,deck)
print(amount)