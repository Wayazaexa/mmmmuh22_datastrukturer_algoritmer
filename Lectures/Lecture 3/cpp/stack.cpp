#include "linked_list.cpp"

using namespace std;

class Stack : public LinkedList {
public:
    void push(int data) {
        this->prepend(data);
    }

    /** 
     * Add item to start of the linked list
    */
    int pop() {
        int data = this->head->data;
        this->remove_first_node();
        return data;
    }

    bool is_empty() {
        return (this->size() == 0);
    }

    int peek() {
        if (this->head == NULL) {
            throw std::out_of_range("Stack is empty");
        }

        return this->head->data;
    }
    
    // Size is defined in base class, no need to redefine
};

main () {
    Stack my_stack = Stack();
    cout << "My stack: " << my_stack << endl;

    cout << boolalpha;   // Ensure we can print booleans as true/false instead of 1/0
    cout << "Empty?: " << my_stack.is_empty() << endl;
    cout << endl;

    my_stack.push(1);
    cout << "My stack: " << my_stack << endl;
    my_stack.push(2);
    cout << "My stack: " << my_stack << endl;
    cout << "Empty?: " << my_stack.is_empty() << endl;
    cout << "Size:" << my_stack.size() << endl;

    cout << "Peek: " << my_stack.peek() << endl;
    cout << endl;

    cout << "Pop: " << my_stack.pop() << endl;
    cout << "My stack: " << my_stack << endl;
    cout << "Pop: " << my_stack.pop() << endl;
    cout << "My stack: " << my_stack << endl;
    cout << "Peek:" << my_stack.peek() << endl;
}