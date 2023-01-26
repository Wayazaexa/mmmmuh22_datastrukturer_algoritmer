#include <iostream>
#include <vector>

using namespace std;

class Stack
{
private:
    vector<string> stack;

public:
    Stack() {
    }

    friend ostream & operator << (ostream &out, const Stack &stack);
    void push(string text);
    string pop();
    string peek();
    bool is_empty() const {
        return (stack.size() == 0);
    }
    int size() {
        return stack.size();
    }
};

ostream & operator << (ostream &out, const Stack &stack) 
{
    out << "[";

    string separator;
    for (auto i: stack.stack) {
        out << separator << "'" << i << "'";
        separator = ", ";
    }
    out << "]";
    return out;
}

void Stack::push(string text) {
    this->stack.push_back(text);
}

string Stack::pop() {
    string text = this->stack.back();
    this->stack.pop_back();
    return text;
}

string Stack::peek() {
    if (this->size()==0) {
        // Todo: Better way of handling empty stack?
        return "";
    }
    return this->stack.back();
}

main () {
    Stack my_stack = Stack();
    cout << "My stack: " << my_stack << endl;

    cout << boolalpha;   // Ensure we can print booleans as true/false instead of 1/0
    cout << "Empty?: " << my_stack.is_empty() << endl;
    cout << endl;

    my_stack.push("hello");
    cout << "My stack: " << my_stack << endl;
    my_stack.push("world");
    cout << "My stack: " << my_stack << endl;
    cout << "Empty?: " << my_stack.is_empty() << endl;

    cout << "Peek: " << my_stack.peek() << endl;
    cout << endl;

    cout << "Pop: " << my_stack.pop() << endl;
    cout << "My stack: " << my_stack << endl;
    cout << "Pop: " << my_stack.pop() << endl;
    cout << "My stack: " << my_stack << endl;
    cout << "Peek:" << my_stack.peek() << endl;
}