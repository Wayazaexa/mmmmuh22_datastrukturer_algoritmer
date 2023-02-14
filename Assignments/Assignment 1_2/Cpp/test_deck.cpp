#include "deck.h"

#include "gtest/gtest.h"

/**
 * Initializes a card and then asserts that the rank and suite of the card was
 * set correctly.
 * 
 */
TEST(Card, init)
{
    Card c = Card(12, Suit::Hearts);
    EXPECT_EQ(c.getRank(), 12) << "card init (rank) failed";
    EXPECT_EQ(c.getSuit(), Suit::Hearts) << "card init (suit) failed";
}

/**
 * Initializes two of the same card and one different card and asserts
 * that the two cards that are the same are equal.
 * 
 */
TEST(Card, eq)
{
    Card c1 = Card(1, Suit::Clubs);
    Card c2 = Card(1, Suit::Clubs);
    EXPECT_EQ(c1, c2) << "eq failed";
}

/**
 * Initializes two cards of different rank and asserts that the one
 * with lower rank is less than the one with higher rank.
 * 
 */
TEST(Card, lt)
{
    Card c1 = Card(4, Suit::Hearts);
    Card c2 = Card(6, Suit::Clubs);
    EXPECT_LT(c1, c2) << "lt failed";
}

/**
 * Initializes two cards of different rank and asserts that the one
 * with higher rank is greater than the one with lower rank.
 * 
 */
TEST(Card, gt)
{
    Card c1 = Card(4, Suit::Hearts);
    Card c2 = Card(6, Suit::Clubs);
    EXPECT_GT(c2, c1) << "gt failed";
}

/**
 * Initializes a card and then asserts that the size of the cards in the deck
 * is 55.
 * 
 */
TEST(Deck, init)
{
    Deck d = Deck();
    EXPECT_EQ(d.getCards().size(), 52) << "deck init failed";
}

/**
 * Initializes a deck and asserts that the length of the deck is 55
 * (because we know that the constructor adds 55 cards to a newly
 * initialized deck), then removes 6 cards and asserts that the length of the
 * remaining deck is 49
 * 
 */
TEST(Deck, size)
{
    Deck d = Deck();
    EXPECT_EQ(d.size(), 52) << "deck size 1 failed";
    d.take();
    d.take();
    d.take();
    d.take();
    d.take();
    d.take();
    EXPECT_EQ(d.size(), 46) << "deck size 2 failed";
}

/**
 * Initializes a deck and asserts that the top card is a joker
 * (because we know that a joker is the last card that the constructor
 * adds to a newly initialized deck) """
 * 
 */
TEST(Deck, take)
{
    Deck d = Deck();
    Card c1 = d.take();
    Card c2 = Card(13, Suit::Clubs); // Check with joker later on
    EXPECT_EQ(c1, c2) << "deck take failed";
}

/**
 * Initializes a deck and sorts it. Then compares the first three cards
 * (the jokers) and then four cards at a time until the deck is empty,
 * that they are the same rank (because that's the only thing '==' compares
 * and sort() sorts by rank). """
 * 
 */
TEST(Deck, sort)
{
    Deck d = Deck();
    d.sort();
    Card c1(1, Suit::Clubs), c2(1, Suit::Clubs), c3(1, Suit::Clubs), c4(1, Suit::Clubs);
    // Remove/check the jokers first later on

    while (d.size() > 0)
    {
        c1 = d.take();
        c2 = d.take();
        c3 = d.take();
        c4 = d.take();
        EXPECT_EQ(c1, c2) << "deck sort failed";
        EXPECT_EQ(c1, c3) << "deck sort failed";
        EXPECT_EQ(c1, c4) << "deck sort failed";
    }
}

/**
 * Initializes a deck, adds a card to it, then takes that card from
 * the deck and asserts that the card is the same as the one we put into
 * the deck
 * 
 */
TEST(Deck, put)
{
    Deck d = Deck();
    Card c1 = Card(2, Suit::Hearts);
    d.put(c1);
    Card c2 = d.take();
    EXPECT_EQ(c1, c2) << "deck put failed";
}

/**
 * Initializes a deck, removes the jokers and takes a card from the deck
 * (which we know will be King of Clubs), inserts it into the deck and asserts
 * that the King of Clubs is now at index 12 in the deck because that's where
 * it should be inserted in a newly initialized deck
 * 
 */
TEST(Deck, insert)
{
    Deck d = Deck();
    // Remove jokers first later on
    Card c = d.take();
    vector<Card> cardlist = d.getCards();
    d.insert(cardlist, c);
    EXPECT_EQ(d.getCards()[12], Card(13, Suit::Clubs)) << "deck insert failed";
}
