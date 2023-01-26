#include "linked_list.cpp"

using namespace std;

class Queue : public LinkedList {
public:
    void enqueue(int data) {
        this->prepend(data);
    }

    int dequeue() {
        int data = this->tail->data;
        this->remove_last_node();
        return data;
    }

    bool is_empty() {
        return (this->head==NULL);
    }

    int peek() {
        if (this->tail == NULL) {
            throw std::out_of_range("Queue is empty");
        }

        return this->tail->data;
    }

    // Size is defined in base class, no need to redefine
};

main() {
    Queue my_queue = Queue();
    cout << "My queue: " << my_queue << endl;
    
    cout << boolalpha;   // Ensure we can print booleans as true/false instead of 1/0
    cout << "Empty?: " << my_queue.is_empty() << endl;
    cout << endl;
    
    my_queue.enqueue(1);
    cout << "My queue: " << my_queue << endl;
    my_queue.enqueue(2);
    cout << "My queue: " << my_queue << endl;

    cout << "Empty?: " << my_queue.is_empty() << endl;
    cout << "Size: " << my_queue.size() << endl;
    cout << "Peek: " << my_queue.peek() << endl;
    cout << endl;

    cout << "Dequeue: " << my_queue.dequeue() << endl;
    cout << "My queue: " << my_queue << endl;
    cout << "Dequeue: " << my_queue.dequeue() << endl;
    cout << "My queue: " << my_queue << endl;

     cout << "Peek: " << my_queue.peek() << endl;   
}