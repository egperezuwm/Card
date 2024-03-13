import random
from enum import Enum
"""
File:         card.py
Author:       Enrique Perez
Date:         03/11/2024
Description:  Contains a "Card" and controlling "Deck" class.
              A card should be treated as a unique object to a Deck, 
              no two cards should be equal to each other.
"""


class Suit(Enum):
  CLUB = "Clubs"
  DIAMOND = "Diamonds"
  HEART = "Hearts"
  SPADE = "Spades"

  def show(self):
    return self.value

class Rank(Enum):
  ACE = 1
  DEUCE = 2
  THREE = 3
  FOUR = 4
  FIVE = 5
  SIX = 6
  SEVEN = 7
  EIGHT = 8
  NINE = 9
  TEN = 10
  JACK = 11
  QUEEN = 12
  KING = 13

  def show(self):
    match self.value:
      case 1:
        return "Ace"
      case 11:
        return "Jack"
      case 12:
        return "Queen"
      case 13:
        return "King"
      case _:
        return self.value

class Card(object):
  def __init__(self, suit=None, rank=None):
    # precondition:   suit and rank must be valid (Enum)
    # postcondition:  Card is assigned Suit and Rank (by the Deck)
    #if suit is None: raise ValueError("suit cannot be None")
    #if suit is not isinstance(suit, Suit.name): raise ValueError("suit is invalid")
    #if rank is None: raise ValueError("rank cannot be None")
    #if rank is not isinstance(rank, Rank.name): raise ValueError("rank is invalid")
    if not isinstance(suit, Suit): raise TypeError
    if not isinstance(rank, Rank): raise TypeError
    self.suit = suit;
    self.rank = rank;


  def __eq__(self, card=None):
    #used to detect duplicates in tests
    if card is None:
      return False
    elif self.suit == card.suit and self.rank == card.rank:
      return True
    else:
      return False

  def show(self):
    #precondition:  self is valid (should always be)
    #postcondition: return "self.rank of self.suit's'
    #example: King of Hearts, 10 of Hearts, Jack of Clubs, Ace of Spades
    assert isinstance(self, object) #shouldn't be possible
    print(self.rank.show(), 'of', self.suit.show())

class Deck:
  def __init__(self):
    self.cards = []
    self.count = 0

  def shuffle(self):
    random.shuffle(self.cards)

  def add(self, card):
    self.cards.append(card)
    self.count += 1

  def remove(self, c=None):
    if c == None:
      card = self.cards[0]
      self.remove(self.cards[0])
      return card
    for card in self.cards:
      if card.__eq__(c):
        self.cards.remove(card)
        self.count -= 1
        return card

  def contains(self, c):
    for card in self.cards:
      if card.__eq__(c):
        return True
    return False

  def show(self):
    for card in self.cards:
      card.show()





