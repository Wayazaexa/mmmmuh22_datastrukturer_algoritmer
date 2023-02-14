
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
    return 0;
}