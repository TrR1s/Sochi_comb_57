from enum import Enum

class CombType(str, Enum):
    ROYAL_FLUSH = "ROYAL_FLUSH"
    STRAIGHT_FLUSH = 'STRAIGHT_FLUSH'
    FOUR_OF_KIND = 'FOUR_OF_KIND'
    FULL_HOUSE = 'FULL_HOUSE'
    FLUSH = 'FLUSH'
    STRAIGHT = 'STRAIGHT'
    THREE_OF_KIND = 'THREE_OF_KIND'
    TWO_PAIRS = 'TWO_PAIRS'
    ONE_PAIR = 'ONE_PAIR'
    ACE_KING = 'ACE_KING'
    HIGH_CARD = 'HIGH_CARD'
    
    
if __name__ == "__main__":
    print(CombType('ROYAL_FLUSH'))
    print(CombType.ACE_KING.value)
    