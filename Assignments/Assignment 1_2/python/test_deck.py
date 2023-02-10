import pytest
from deck import Deck, Card

# Implementera tester ni anser lämpliga här. Motivera gärna varför de behövs (vad de testar och varför).


def test_card_init():
    """ Initializes a card and then asserts that the rank and suite
    of the card was set correctly """
    c = Card(12, 'Hearts')
    assert c.rank == 12
    assert c.suite == 'Hearts'

def test_card_eq():
    """ Initializes two of the same card and one different card and asserts
    that the two cards that are the same compare to True and that the
    one that is different compares to False """
    c1 = Card(1, 'Clubs')
    c2 = Card(1, 'Clubs')
    c3 = Card(2, 'Clubs')
    assert c1 == c2
    assert not c1 == c3

def test_card_lt():
    """ Initializes two cards of different rank and asserts that the one
    with lower rank < the one with higher rank returns True """
    c1 = Card(4, 'Hearts')
    c2 = Card(6, 'Clubs')
    assert c1 < c2

def test_card_gt():
    """ Initializes two cards of different rank and asserts that the one
    with higher rank > the one with lower rank returns True """
    c1 = Card(4, 'Hearts')
    c2 = Card(6, 'Clubs')
    assert c2 > c1

def test_deck_len():
    """ Initializes a deck and asserts that the length of the deck is 55
    (because we know that the constructor adds 55 cards to a newly
    initialized deck), then removes 6 cards and asserts that the length of the
    remaining deck is 49 """
    d = Deck()
    assert len(d) == 55
    d.take()
    d.take()
    d.take()
    d.take()
    d.take()
    d.take()
    assert len(d) == 49

def test_deck_take():
    """ Initializes a deck and asserts that the top card is a joker
    (because we know that a joker is the last card that the constructor
    adds to a newly initialized deck) """
    d = Deck()
    c1 = d.take()
    c2 = Card(14, 'Joker')
    assert c1 == c2

def test_deck_sort():
    """ Initializes a deck and sorts it. Then compares the first three cards
    (the jokers) and then four cards at a time until the deck is empty,
    that they are the same rank (because that's the only thing '==' compares
    and sort() sorts by rank). """
    d = Deck()
    d.sort()

    c1 = d.take()
    c2 = d.take()
    c3 = d.take()
    assert c1 == c2 == c3
    while len(d.cards) > 0:
        c1 = d.take()
        c2 = d.take()
        c3 = d.take()
        c4 = d.take()
        assert c1 == c2 == c3 == c4

def test_deck_put():
    """ Initializes a deck, adds a card to it, then takes that card from
    the deck and asserts that the card is the same as the one we put into
    the deck """
    d = Deck()
    c1 = Card(2, 'Hearts')
    d.put(c1)
    c2 = d.take()
    assert c1 == c2

def test_deck_insert():
    """ Initializes a deck, removes the jokers and takes a card from the deck
    (which we know will be King of Clubs), inserts it into the deck and asserts
    that the King of Clubs is now at index 12 in the deck because that's where
    it should be inserted in a newly initialized deck """
    d = Deck()
    d.take()
    d.take()
    d.take()
    c = d.take()
    d.insert(d.cards, c)
    assert d.cards[12] == Card(13, 'Clubs')

if __name__ == '__main__':
    pytest.main()
