from enum import Enum
"""
File:         PlayingCard.py
Author:       Enrique Perez
Date:         Date of creation/modification
Description:  A brief explanation of what this script does.
"""
class PlayingCard(object):

  class Suit(Enum):
    CLUB = "Club"
    DIAMOND = "Diamond"
    HEART = "Heart"
    SPADE = "Spade"
    @classmethod
    def __str__(self):
      return str(self.value)

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
    @classmethod
    def __str__(self):
      return str(self.value)

  def __init__(self, rank, suit):
    # precondition:   None
    # postcondition:  Card is assigned Suit and Rank (by the Deck)
    self.rank = rank
    self.suit = suit

  def equals(self, Card=None):
    if Card is None:
      False
    if self.rank == Card.rank:
      True


  def __str__(self):
    #precondition:  self is valid (should always be)
    #postcondition: return "self.rank of self.suit's'
    #example: King of Hearts, 10 of Hearts, Jack of Clubs, Ace of Spades
    assert isinstance(self, object) #shouldn't be possible
    print(self.rank.__str__(), 'of', self.suit.__str__(),'s')
