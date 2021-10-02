# Author: Gan Li
# Date: 10/1/21 12:45 下午
# Description: Module 3 inheritance, composition, and polymorphism
import random


class Card:
    """Represents a standard playing card."""
    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank

    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7',
                  '8', '9', '10', 'Jack', 'Queen', 'King']

    def __str__(self):
        return '%s of %s' % (Card.rank_names[self.rank],
                             Card.suit_names[self.suit])

    def __lt__(self, other):
        card_1 = self.suit, self.rank
        card_2 = other.suit, other.rank
        return card_1 < card_2


class Deck:
    """Represents a standard deck of 52 cards."""
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                card = Card(suit, rank)
                self.cards.append(card)

    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)

    def pop_card(self):
        return self.cards.pop()

    def remove_card(self, card):
        for card_sample in self.cards:
            if str(card) == str(card_sample):
                self.cards.pop(self.cards.index(card_sample))

    def add_card(self, card):
        self.cards.append(card)

    def shuffle(self):
        random.shuffle(self.cards)

    def move_cards(self, hand, num):
        for i in range(num):
            hand.add_card(self.pop_card())


class Hand(Deck):
    """Represents a hand of playing cards."""
    def __init__(self, label=''):
        super().__init__()  # 没有也没关系
        self.cards = []
        self.label = label
