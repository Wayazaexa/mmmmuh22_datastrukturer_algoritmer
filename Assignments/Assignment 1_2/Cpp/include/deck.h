#ifndef deck_kn3roiaipgb4ttyi2yaiogbaiugopi
#define deck_kn3roiaipgb4ttyi2yaiogbaiugopi

#include <iostream>
#include <vector>
#include <string>

using namespace std;

enum Suit {
    Hearts,
    Diamonds,
    Spades,
    Clubs,
    Joker
};

class Card
{
private:
    int rank;
    Suit suit;
public:
    Card(int rank, Suit suit);
    int getRank(){ return this->rank; }
    Suit getSuit(){ return this->suit; }
    
    friend bool operator== (const Card &lhs, const Card &rhs)
    {
        return lhs.rank == rhs.rank;
    }

    friend bool operator< (const Card &lhs, const Card &rhs)
    {
        return lhs.rank < rhs.rank;
    }

    friend bool operator> (const Card &lhs, const Card &rhs)
    {
        return lhs.rank > rhs.rank;
    }

    friend ostream & operator << (ostream &out, const Card &c);
};

class Deck
{
private:
    vector<Card> cards;
public:
    Deck();
    vector<Card> getCards(){ return this->cards; }
    friend ostream & operator << (ostream &out, const Deck &d);
    int size();
    void shuffle();
    void sort();
    Card take();
    void put(Card card);
    void sort_by_suit();
    void sort_by_value();
    Card pick_by_random();
    vector<vector<Card>> deal(int n);
    void remove_duplicates();
    void remove_jokers();

    static void insert(vector<Card> &cardlist, Card card);
    static void insert_by_suit(vector<Card> &cardlist, Card card);
    static void insert_by_value(vector<Card> &cardlist, Card card);
};
#endif
