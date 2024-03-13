from card import Suit, Rank, Card, Deck

deck = Deck() # empty deck (no cards)
card = Card(Suit.CLUB, Rank.DEUCE)
for suit in Suit:
    for rank in Rank:
        deck.add(Card(suit, rank))
deck.shuffle()

numPlayers = int(input("Enter Players: "))
players = []
for i in range(numPlayers):
    players.append(Deck())

for i in range(deck.count):
    players[i%numPlayers-1].add(deck.remove())

for i in range(numPlayers):
    print("player ", i+1, ": ")
    players[i].show()
    print("Number of cards: ", players[i].count)
    print("\n")

deck.show()
print("cards in deck: ", deck.count)
