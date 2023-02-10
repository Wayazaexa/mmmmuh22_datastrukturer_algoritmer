#include "deque.cpp"

using namespace std;

/**
 * Är strängen "word" ett palindrom
*/
bool is_palindrome(string word) {
    Deque dq = Deque();

    // Fyll vår deque med tecken
    for (int i=0; i<word.length(); i++) {
        dq.add_last(word[i]);
    }

    while (dq.size()>1) {
        // Ta första och sista tecknet från vår deque
        char first = dq.remove_first();
        char last = dq.remove_last();
        if (first != last) {
            return false;
        }
    }

    return true;
}

int main() {
    cout << std::boolalpha;
    cout << "radar:" << is_palindrome("radar") << endl; // True
    cout << "racecar:" << is_palindrome("racecar") << endl; // True
    cout << "tacocat:" << is_palindrome("tacocat") << endl; // True
    cout << "palindrome:" << is_palindrome("palindrome") << endl; // False
}