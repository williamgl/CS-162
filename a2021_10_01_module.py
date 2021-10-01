# Author: Gan Li
# Date: 10/1/21 12:45 下午
# Description: Module 3 inheritance, composition, and polymorphism
class Card:
    """Represents a standard playing card."""

    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank

