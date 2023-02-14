
#include "deck.h"
#include <iostream>

using namespace std;

int main() {
    Deck deck = Deck();
    cout << "Fresh deck: " << deck << endl;
    deck.shuffle();
    cout << "Shuffled deck: " << deck << endl;
    deck.sort();
    cout << "Sorted deck: " << deck << endl;
    deck.shuffle();
    cout << "Shuffled deck: " << deck << endl;
    deck.sort_by_suit();
    cout << "Sorted deck by suit: " << deck << endl;
    deck.shuffle();
    cout << "Shuffled deck: " << deck << endl;
    deck.sort_by_value();
    cout << "Sorted deck by value: " << deck << endl << endl;

    int i = 5;
    while (i-- > 0)
        cout << "Random card: " << deck.pick_by_random() << endl;
    cout << endl;

    deck = Deck();
    deck.shuffle();
    vector<vector<Card>> piles = deck.deal(3);
    for (auto pile : piles)
    {
        std::cout << "Pile: " << endl;
        for (auto card : pile)
            cout << card << ", ";
        cout << endl;
    }
    cout << endl;

    deck = Deck();
    i = 5;
    while (i-- > 0)
        deck.put(Card(5, Suit::Hearts));
    deck.shuffle();
    std::cout << "Deck size (with 7 duplicates): " << deck.size() << endl;
    deck.remove_duplicates();
    std::cout << "Deck size (after duplicates removed): " << deck.size() << endl << endl;

    deck = Deck();
    deck.shuffle();
    deck.remove_jokers();
    std::cout << "Deck size (after jokers removed): " << deck.size() << endl << endl;

    return 0;
}