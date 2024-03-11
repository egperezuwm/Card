from PlayingCard import Card
import unittest

class TestInit(unittest.TestCase):
  def test_default(self):
      card = Card()
      #there is NOT a default constructor as a card MUST be instantiated with Suit and Rank

  def test_oneArg(self):
      # there is NOT a default constructor as a card MUST be instantiated with Suit and Rank
      card = Card(10)
      card = Card(Card.Rank.ACE)
      card = Card(Card.Suit.SPADE)

  def test_oneArg(self):
      # the card should be constructed of from the Card class's ENUM class Rank and Suit.
      card = Card("ACE", 10)
      card = Card("SPADE", Card.Rank.ACE)
      card = Card(Card.Suit.SPADE)