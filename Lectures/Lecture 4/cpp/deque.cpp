#include "linked_list.cpp"
#include <iostream>

using namespace std;

class Deque : public LinkedList {
public:
    void add_first(char data) { LinkedList::prepend(data);}
    void add_last(char data) { LinkedList::append(data);}
    char remove_first() { return LinkedList::remove_first_node(); }
    char remove_last() { return LinkedList::remove_last_node();}
    char get_first() {return LinkedList::get_first_item();}
    char get_last() {return LinkedList::get_last_item();}
};

/**
 * Övn. 2: Implementera en Stack ovanpå en Deque
*/
class Stack : public Deque {
public:
    void push(char data) { Deque::add_first(data);}
    char pop() { return Deque::remove_first();}
    char peek() { return Deque::get_first();}
};

void deque_main() {
    Deque dq = Deque();
    cout << "Is empty? " << dq.is_empty() << endl;
    cout << "Size? " << dq.size() << endl;

    dq.add_first('a');
    dq.add_first('b');
    cout << dq << endl;
    cout << "Is empty?" << dq.is_empty();

    dq.add_last('c');
    dq.add_last('d');
    cout << dq << endl;
    cout << "Is empty?" << dq.is_empty() << endl;
    cout << "Size?" << dq.size() << endl;

    cout << dq.remove_first() << endl;
    cout << dq.remove_first() << endl;
    // cout << dq.remove_first() << endl;  // Ska ge ett fel
    cout << dq << endl;
    cout << "Is empty?" << dq.is_empty() << endl;

    cout << dq.remove_last() << endl;
    cout << dq.remove_last() << endl;
    cout << dq << endl;
    cout << "Is empty? " << dq.is_empty() << endl;
    cout << "Size? " << dq.size() << endl;
}

void stack_main() {
    Stack s = Stack();
    s.push('a');
    s.push('b');
    s.push('c');
    cout << s << endl;
    cout << s.size() << endl;
    cout << s.is_empty() << endl;

    cout << "peek: " << s.peek() << endl;

    cout << s.pop() << endl;
    cout << s.pop() << endl;
    cout << s.pop() << endl;
    cout << s.size() << endl;
    cout << s.is_empty() << endl;
}

// Avkommentera för att köra tester
/*
main () {
    deque_main();
    stack_main();
}
*/

