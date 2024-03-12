import Card

deck = Card.Deck() # empty deck (no cards)
card = Card.Card(Card.Rank.DEUCE, Card.Suit.CLUB)
for suit in Card.Suit:
    for rank in Card.Rank:
        deck.add(Card.Card(rank, suit))
deck.shuffle()

numPlayers = int(input("Enter Players (2-4): "))
players = []
for i in range(numPlayers):
    players.append(Card.Deck())

for i in range(deck.count):
    players[i%numPlayers-1].add(deck.remove())

for i in range(numPlayers):
    print("player ", i+1, ": ")
    players[i].show()
    print("\n")