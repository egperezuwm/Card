import unittest
from unittest import TestCase

from card import Suit, Rank, Card, Deck

"""
File:         Test_Card.py
Author:       Enrique Perez
Date:         03/12/2024
Description:  Tests the "Card" and controlling "Deck" class.
"""
class TestCard(TestCase):
    def setUp(self):
        pass

class TestInit(unittest.TestCase):
    def setUp(self):
        # illegal suits
        self.suits = ["CLUB", "DIAMOND", "HEART", "SPADE", "Clubs", "Diamonds", "Hearts", "Spades"]
        # illegal ranks
        self.ranks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
                     "ACE", "DEUCE", "THREE", "FOUR", "FIVE", "SIX",
                     "SEVEN", "EIGHT", "NINE", "TEN", "JACK", "QUEEN", "king"]

    def test_zeroArg(self):
        # zero-argument Card calls are illegal
        with self.assertRaises(TypeError, msg="zero-argument failed"): Card()

    def test_oneArg(self):
        # one-argument Card calls are illegal.
        # test illegal ranks
        for rank in self.ranks:
            with self.assertRaises(TypeError, msg="one-arg (illegal rank) failed"): Card(rank)
        # test legal ranks
        for rank in Rank:
            with self.assertRaises(TypeError, msg="one-arg (rank) failed"): Card(rank)
        #test illegal suits
        for suit in self.suits:
            with self.assertRaises(TypeError, msg="one-arg (illegal suit) failed"): Card(rank)
        # test legal suits
        for suit in Suit:
            with self.assertRaises(TypeError, msg="one-arg (suit) failed"): Card(suit)


    def test_twoArg(self):
        # must use valid Rank and valid Suit in every Card call.
        # test illegal suits, illegal ranks
        for suit in self.suits:             #illegal
            for rank in self.ranks:         #illegal
                #print(f"{suit} - {rank}")
                with self.assertRaises(TypeError, msg="two-arg (illegal suit, illegal rank) failed"):
                    Card(suit, rank)

        # test illegal suits, legal ranks
        for suit in self.suits:             #illegal
            for rank in Rank:
                with self.assertRaises(TypeError, msg="two-arg (illegal suit) failed"):
                    Card(suit, rank)

        # test legal suits, illegal ranks
        for suit in Suit:
            for rank in self.ranks:         #illegal
                with self.assertRaises(TypeError, msg="two-arg (illegal rank) failed"):
                    Card(suit, rank)

        #test legal suits, legal ranks
        for suit in Suit:                   #legal
            for rank in Rank:               #legal
                Card(suit, rank)

