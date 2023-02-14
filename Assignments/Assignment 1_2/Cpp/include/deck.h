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
    Clubs
};

class Card
{
public:
    int rank;
    Suit suit;

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

    static void insert(vector<Card> &cardlist, Card card);
};
#endif
