#include "deck.h"
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <random>
#include <chrono>

using namespace std;
/**
 * Help function to convert Suit enum to string
 */
const string SuitToString(Suit s)
{
    switch (s)
    {
    case Suit::Hearts:
        return "H";
    case Suit::Diamonds:
        return "D";
    case Suit::Spades:
        return "S";
    case Suit::Clubs:
        return "C";
    case Suit::Joker:
        return "J";
    }
    return "";
}

Card::Card(int rank, Suit suit)
{
    this->rank = rank;
    this->suit = suit;
}

/**
 * Overload of << operator for Card class
 */
ostream &operator<<(ostream &out, const Card &c)
{
    string r;
    switch (c.rank)
    {
    case 1:
        r = 'A';
        break;
    case 11:
        r = 'J';
        break;
    case 12:
        r = 'Q';
        break;
    case 13:
        r = 'K';
        break;
    case 14:
        r = ' ';
        break;
    default:
        r = to_string(c.rank);
        break;
    }

    out << r << SuitToString(c.suit);

    return out;
}

/**
 * Create a deck of 55 cards
 */
Deck::Deck()
{
    srand(time(0));
    for (Suit s = Suit::Hearts; s <= Suit::Clubs; s = Suit(s + 1))
    {
        for (int r = 1; r < 14; r++)
        {
            cards.push_back(Card(r, s));
        }
    }
    for (int i = 0; i < 3; i++)
        cards.push_back(Card(14, Suit::Joker));
}

/**
 * Overload of << operator for Deck class
 */
ostream &operator<<(ostream &out, const Deck &d)
{
    string separator;
    for (auto i : d.cards)
    {
        out << separator << i;
        separator = ", ";
    }

    return out;
}

/**
 * Return number of cards in deck
 *
 */
int Deck::size()
{
    return this->cards.size();
}

/**
 * Shuffle all the cards in deck in ranom order.
 */
void Deck::shuffle()
{
    auto rng = std::default_random_engine(std::chrono::system_clock::now().time_since_epoch().count());
    std::shuffle(this->cards.begin(), this->cards.end(), rng);
}

/**
 * Sort the deck according to card rank. All aces, the all two's, then all threes, ...
 */
void Deck::sort()
{
    vector<Card> sorted_cards; // Empty temporary deck

    while (this->size() > 0)
    {
        // Go through the deck from left to right, insert the deck in the appropriate spot
        Deck::insert(sorted_cards, this->take()); // Take a card from the old deck, insert it into the new one
    }

    this->cards = sorted_cards;
}

/**
 * Take the top card from the deck
 */
Card Deck::take()
{
    Card c = this->cards.back();
    this->cards.pop_back();
    return c;
}

/**
 * Put a card on top of the deck
 */
void Deck::put(Card card)
{
    cards.push_back(card);
}

/**
 * Insert a card into a vector of cards
 */
void Deck::insert(vector<Card> &cardlist, Card card)
{

    std::vector<Card>::iterator it;

    for (it = cardlist.begin(); it < cardlist.end(); it++)
        if (card < *it)
            break;
    cardlist.insert(it, card);
}

/**
 * Insert a card into a vector of cards by suit.
 */
void Deck::insert_by_suit(vector<Card> &cardlist, Card card)
{

    std::vector<Card>::iterator it;

    for (it = cardlist.begin(); it < cardlist.end(); it++)
        if (card.getSuit() < (*it).getSuit())
            break;
        else if (card.getSuit() == (*it).getSuit())
            if (card < *it)
                break;
    cardlist.insert(it, card);
}

/**
 * Sort the deck according to card suit. All hearts, the all diamonds, then all spades, ...
 */
void Deck::sort_by_suit()
{
    vector<Card> sorted_cards; // Empty temporary deck

    while (this->size() > 0)
    {
        // Go through the deck from left to right, insert the deck in the appropriate spot
        Deck::insert_by_suit(sorted_cards, this->take()); // Take a card from the old deck, insert it into the new one
    }

    this->cards = sorted_cards;
}

/**
 * Insert a card into a vector of cards by suit.
 */
void Deck::insert_by_value(vector<Card> &cardlist, Card card)
{

    std::vector<Card>::iterator it;

    for (it = cardlist.begin(); it < cardlist.end(); it++)
        if (card < *it)
            break;
        else if (card == *it)
            if (card.getSuit() < (*it).getSuit())
                break;
    cardlist.insert(it, card);
}

/**
 * Sort the deck according to card value. All aces, the all two's, then all threes, ...,
 * each value sorted by suit.
 */
void Deck::sort_by_value()
{
    vector<Card> sorted_cards; // Empty temporary deck

    while (this->size() > 0)
    {
        // Go through the deck from left to right, insert the deck in the appropriate spot
        Deck::insert_by_value(sorted_cards, this->take()); // Take a card from the old deck, insert it into the new one
    }

    this->cards = sorted_cards;
}

/**
 * Pick and remove a random card from the deck
 */
Card Deck::pick_by_random()
{
    /*
    // Very messy, but correct so I'm going to read up on it more later
    auto rng = std::default_random_engine(std::chrono::system_clock::now().time_since_epoch().count());
    */
    // Short, but deprecated. Will suffice for now.
    int index = std::rand() % cards.size();
    Card card = cards[index];
    if (index == cards.size() - 1)
        cards.pop_back();
    else
        cards.erase(cards.begin() + index);
    return card;
}

/**
 * Deals the deck to n hands/piles
 */
vector<vector<Card>> Deck::deal(int n)
{
    vector<vector<Card>> piles;
    for (int i = 0; i < n; i++)
        piles.push_back(vector<Card>());

    int i = 0;
    while (cards.size() > 0)
    {
        piles[i].push_back(this->take());
        ++i %= n;
    }

    return piles;
}

/**
 * Removes duplicate cards from the deck
 */
void Deck::remove_duplicates()
{
    vector<Card> unique_cards;
    for (Card card : cards)
    {
        bool unique = true;
        for (Card unique_card : unique_cards)
        {
            if (card == unique_card && card.getSuit() == unique_card.getSuit())
                unique = false;
        }
        if (unique)
            unique_cards.push_back(card);
    }
    this->cards = unique_cards;
}

/**
 * Removes Jokers from the deck
 */
void Deck::remove_jokers()
{
    int index = 0;
    vector<int> index_list;

    for (Card card : cards)
    {
        if (card.getSuit() == Suit::Joker)
            index_list.push_back(index);
        index++;
    }
    int delta = 0;
    for (int i : index_list)
    {
        if (i == cards.size() - 1)
            cards.pop_back();
        else
            cards.erase(cards.begin() + i - delta++);
    }
}
